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
    app.run(host='0.0.0.0', port=3000)