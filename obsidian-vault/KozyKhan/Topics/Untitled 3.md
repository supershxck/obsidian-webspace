> **April 9th, 2025**  **12:29:39** 
> **Topics:** [[
> **Tags:** #
---

Great to hear you got the website hosted! Now, let’s extend your setup to integrate your Obsidian vault and enable searching through it using a large language model (LLM) or transformer within Docker. We’ll modify the existing setup to include a search functionality powered by a transformer model (e.g., using Hugging Face’s `transformers` library) and connect it to your Obsidian vault.

### Plan
1. **Mount Obsidian Vault**: Ensure your markdown files are accessible to the Python container.
2. **Add an LLM/Transformer**: Use a lightweight transformer model (e.g., `sentence-transformers`) to create embeddings of your notes for semantic search.
3. **Search Interface**: Extend the Node.js app to provide a simple web interface for querying your notes.
4. **Docker Adjustments**: Update the `docker-compose.yml` and Python environment to include the necessary dependencies.

### Step-by-Step Implementation

#### 1. Ensure Obsidian Vault is Mounted
Your `docker-compose.yml` already mounts `./obsidian-vault:/app/vault` in the `python-app` service. Copy your Obsidian markdown files into the `obsidian-webspace/obsidian-vault/` directory on your host machine. The Python container will see them at `/app/vault`.

#### 2. Update Python Environment for LLM/Transformer
We’ll use `sentence-transformers` to generate embeddings and perform semantic search. Update the Python-related files:

- **`python/requirements.txt`**:
```
markdown
sentence-transformers
torch
numpy
```

- **`python/Dockerfile`** (unchanged, but ensure it builds with new dependencies):
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "process_markdown.py"]
```

- **`python/process_markdown.py`** (updated for embeddings and search):
```python
import os
import markdown
from sentence_transformers import SentenceTransformer, util
import numpy as np

# Load transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight and fast

# Paths
vault_dir = "/app/vault"
output_dir = "/usr/share/nginx/html"
embeddings_file = "/app/embeddings.npy"
metadata_file = "/app/metadata.txt"

# Function to load and process markdown files
def process_vault():
    notes = []
    filenames = []
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(vault_dir):
        for file in files:
            if file.endswith(".md"):
                input_path = os.path.join(root, file)
                output_file = os.path.join(output_dir, file.replace(".md", ".html"))
                with open(input_path, "r") as f:
                    text = f.read()
                    html = markdown.markdown(text)
                    notes.append(text)
                    filenames.append(file)
                with open(output_file, "w") as f:
                    f.write(f"<html><body>{html}</body></html>")

    # Generate embeddings
    embeddings = model.encode(notes, convert_to_tensor=False)
    np.save(embeddings_file, embeddings)
    with open(metadata_file, "w") as f:
        f.write("\n".join(filenames))
    return notes, embeddings, filenames

# Search function
def search_notes(query, embeddings, filenames):
    query_embedding = model.encode(query, convert_to_tensor=False)
    cos_scores = util.cos_sim(query_embedding, embeddings)[0]
    top_results = np.argpartition(-cos_scores, range(5))[:5]  # Top 5 results
    return [(filenames[idx], cos_scores[idx]) for idx in top_results]

# Initial processing
if not os.path.exists(embeddings_file):
    notes, embeddings, filenames = process_vault()
else:
    embeddings = np.load(embeddings_file)
    with open(metadata_file, "r") as f:
        filenames = f.read().splitlines()

# Simple CLI for testing (replace with API later)
if __name__ == "__main__":
    while True:
        query = input("Enter search query (or 'exit' to quit): ")
        if query.lower() == "exit":
            break
        results = search_notes(query, embeddings, filenames)
        for filename, score in results:
            print(f"{filename}: {score:.4f}")
```

This script:
- Converts markdown to HTML (as before).
- Generates embeddings for all notes using `sentence-transformers`.
- Saves embeddings and metadata to files for reuse.
- Provides a basic search function using cosine similarity.

#### 3. Update Node.js for Search Interface
Let’s extend the Node.js app to serve a web interface and connect to the Python search functionality via an API. We’ll use a simple Python Flask server for the API.

- **Add Flask to `python/requirements.txt`**:
```
markdown
sentence-transformers
torch
numpy
flask
```

- **Update `python/process_markdown.py` to include a Flask API**:
```python
import os
import markdown
from sentence_transformers import SentenceTransformer, util
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

vault_dir = "/app/vault"
output_dir = "/usr/share/nginx/html"
embeddings_file = "/app/embeddings.npy"
metadata_file = "/app/metadata.txt"

def process_vault():
    notes = []
    filenames = []
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(vault_dir):
        for file in files:
            if file.endswith(".md"):
                input_path = os.path.join(root, file)
                output_file = os.path.join(output_dir, file.replace(".md", ".html"))
                with open(input_path, "r") as f:
                    text = f.read()
                    html = markdown.markdown(text)
                    notes.append(text)
                    filenames.append(file)
                with open(output_file, "w") as f:
                    f.write(f"<html><body>{html}</body></html>")

    embeddings = model.encode(notes, convert_to_tensor=False)
    np.save(embeddings_file, embeddings)
    with open(metadata_file, "w") as f:
        f.write("\n".join(filenames))
    return notes, embeddings, filenames

def search_notes(query, embeddings, filenames):
    query_embedding = model.encode(query, convert_to_tensor=False)
    cos_scores = util.cos_sim(query_embedding, embeddings)[0]
    top_results = np.argpartition(-cos_scores, range(5))[:5]
    return [(filenames[idx], float(cos_scores[idx])) for idx in top_results]

# Load or process vault
if not os.path.exists(embeddings_file):
    notes, embeddings, filenames = process_vault()
else:
    embeddings = np.load(embeddings_file)
    with open(metadata_file, "r") as f:
        filenames = f.read().splitlines()

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '')
    results = search_notes(query, embeddings, filenames)
    return jsonify({'results': [{'file': f, 'score': s} for f, s in results]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```

- **Update `docker-compose.yml`** to expose the Flask port:
```yaml
version: '3.8'

services:
  nginx:
    image: nginx:latest
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - python-app

  python-app:
    build:
      context: ./python
      dockerfile: Dockerfile
    volumes:
      - ./obsidian-vault:/app/vault
      - ./html:/usr/share/nginx/html  # Share output with Nginx
    ports:
      - "5000:5000"  # Expose Flask API
    command: python process_markdown.py

  nodejs:
    image: node:18
    volumes:
      - ./js:/app
    working_dir: /app
    command: npm start
    ports:
      - "3000:3000"

  ruby:
    image: ruby:3.2
    volumes:
      - ./ruby:/app
    working_dir: /app
    command: ruby app.rb
```

- **Update `js/app.js` for a search interface**:
```javascript
const express = require('express');
const fetch = require('node-fetch');  // Add this dependency
const app = express();
const port = 3000;

app.use(express.static('public'));  // Serve static files from 'public' folder
app.use(express.json());

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.post('/search', async (req, res) => {
  const query = req.body.query;
  const response = await fetch('http://python-app:5000/search', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query })
  });
  const data = await response.json();
  res.json(data);
});

app.listen(port, () => {
  console.log(`App running at http://localhost:${port}`);
});
```

- **Add `js/package.json` dependency**:
```bash
npm install node-fetch
```

- **Create `js/public/index.html`**:
```html
<!DOCTYPE html>
<html>
<head>
  <title>Obsidian Search</title>
</head>
<body>
  <h1>Search Your Obsidian Vault</h1>
  <input type="text" id="query" placeholder="Enter search query">
  <button onclick="search()">Search</button>
  <div id="results"></div>

  <script>
    async function search() {
      const query = document.getElementById('query').value;
      const response = await fetch('/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
      });
      const data = await response.json();
      const resultsDiv = document.getElementById('results');
      resultsDiv.innerHTML = data.results.map(r => 
        `<p><a href="/${r.file.replace('.md', '.html')}">${r.file}</a> (Score: ${r.score.toFixed(4)})</p>`
      ).join('');
    }
  </script>
</body>
</html>
```

- **Create `js/public/` directory**:
```bash
mkdir js/public
```

#### 4. Rebuild and Run
```bash
docker-compose down
docker-compose up --build
```

### How It Works
1. **Obsidian Vault**: Your markdown files in `./obsidian-vault/` are processed by the Python container, converted to HTML, and served by Nginx at `http://localhost:8080`.
2. **Embeddings**: The Python app generates embeddings for your notes and exposes a `/search` endpoint via Flask at `http://localhost:5000/search`.
3. **Search Interface**: The Node.js app at `http://localhost:3000` provides a simple webpage where you can enter a query, hit "Search," and see the top 5 matching notes with links to their HTML versions.

### Accessing Your Setup
- **Static HTML Notes**: `http://localhost:8080/<filename>.html`
- **Search Interface**: `http://localhost:3000`

### Enhancements
- **Better Link Handling**: Extend `process_markdown.py` to resolve `[[double bracket]]` links into clickable HTML links.
- **Model Choice**: Swap `all-MiniLM-L6-v2` for a different transformer if you need more accuracy (e.g., `all-mpnet-base-v2`), though it’ll use more resources.
- **UI Polish**: Add CSS to `index.html` for a nicer look.

Let me know if you hit any snags or want to tweak this further!