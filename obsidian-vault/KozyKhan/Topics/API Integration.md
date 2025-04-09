> **March 16th, 2025**  **22:19:33** 
> **Topics:** [[Net L1]] 
> **Tags:** #CS 
---

**API Implementation Level 1: Introduction to Building and Consuming APIs**

  

**Introduction**

  

An **API (Application Programming Interface)** allows different applications to communicate with each other. In this lesson, you’ll learn how to **build a basic REST API, consume APIs, and work with JSON data**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Understanding RESTful APIs & HTTP Methods**

✅ **Building a Simple API with Express.js (Node.js)**

✅ **Consuming APIs with Fetch (JavaScript) & HttpClient (VB.NET)**

✅ **Handling JSON Data**

✅ **Testing APIs with Postman & Curl**

✅ **Securing API Requests with Basic Authentication**

✅ **Building a Simple API-Connected Web App**

  

By the end of this lesson, you will be able to **create and consume REST APIs, handle API requests, and integrate them into applications**.

---

**1. Understanding RESTful APIs & HTTP Methods**

  

**1.1. What is a REST API?**

• **REST (Representational State Transfer)** is a standard for designing **web APIs**.

• It uses **HTTP methods** to communicate between a **client** (frontend, mobile app) and a **server** (backend API).

  

**1.2. Common HTTP Methods in APIs**

|**HTTP Method**|**Purpose**|
|---|---|
|GET|Retrieve data from the server|
|POST|Send data to the server (create)|
|PUT|Update existing data|
|DELETE|Remove data from the server|

Example API Endpoint:

```
GET https://api.example.com/users
```

  

---

**2. Building a Simple API with Express.js (Node.js)**

  

**2.1. Setting Up Express.js**

1. **Install Node.js** from [Node.js official website](https://nodejs.org/).

2. Create a new project:

```
mkdir api-project && cd api-project
npm init -y
npm install express
```

  

  

**2.2. Creating a Simple API**

  

Create a file **server.js**:

```
const express = require("express");
const app = express();
const PORT = 3000;

app.use(express.json()); // Enable JSON parsing

const users = [{ id: 1, name: "Alice" }, { id: 2, name: "Bob" }];

// GET: Fetch all users
app.get("/users", (req, res) => {
    res.json(users);
});

// POST: Add a new user
app.post("/users", (req, res) => {
    const newUser = { id: users.length + 1, name: req.body.name };
    users.push(newUser);
    res.status(201).json(newUser);
});

// DELETE: Remove a user
app.delete("/users/:id", (req, res) => {
    const userId = parseInt(req.params.id);
    const index = users.findIndex(user => user.id === userId);
    if (index !== -1) {
        users.splice(index, 1);
        res.json({ message: "User deleted" });
    } else {
        res.status(404).json({ error: "User not found" });
    }
});

// Start the server
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
```

**2.3. Running the API**

```
node server.js
```

Open your browser and visit:

```
http://localhost:3000/users
```

  

---

**3. Consuming APIs in JavaScript**

  

**3.1. Fetching Data from an API**

```
fetch("http://localhost:3000/users")
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error("Error:", error));
```

**3.2. Sending Data to an API**

```
fetch("http://localhost:3000/users", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name: "Charlie" })
})
.then(response => response.json())
.then(data => console.log("New user added:", data));
```

  

---

**4. Consuming APIs in VB.NET**

  

**4.1. Installing HttpClient**

  

Ensure **System.Net.Http** is referenced in your project.

  

**4.2. Fetching Data from an API**

```
Imports System.Net.Http
Imports System.Threading.Tasks

Module Program
    Async Function GetUsers() As Task
        Dim client As New HttpClient()
        Dim response As String = Await client.GetStringAsync("http://localhost:3000/users")
        Console.WriteLine(response)
    End Function

    Sub Main()
        GetUsers().Wait()
    End Sub
End Module
```

**4.3. Sending Data to an API**

```
Imports System.Net.Http
Imports System.Text
Imports System.Threading.Tasks

Module Program
    Async Function AddUser() As Task
        Dim client As New HttpClient()
        Dim content As New StringContent("{""name"":""Eve""}", Encoding.UTF8, "application/json")
        Dim response As HttpResponseMessage = Await client.PostAsync("http://localhost:3000/users", content)
        Dim result As String = Await response.Content.ReadAsStringAsync()
        Console.WriteLine(result)
    End Function

    Sub Main()
        AddUser().Wait()
    End Sub
End Module
```

  

---

**5. Testing APIs with Postman & Curl**

  

**5.1. Using Postman**

1. Open **Postman**.

2. **Make a GET request** to:

```
http://localhost:3000/users
```

  

1. **Make a POST request**:

• Select **POST**.

• Go to **Body** → **Raw** → **JSON**.

• Enter:

```
{
  "name": "David"
}
```

  

• Click **Send**.

  

**5.2. Using Curl**

```
curl -X GET http://localhost:3000/users
```

```
curl -X POST -H "Content-Type: application/json" -d '{"name": "Eve"}' http://localhost:3000/users
```

  

---

**6. Securing API Requests with Basic Authentication**

  

**6.1. Adding Basic Authentication**

  

Modify **server.js**:

```
const users = [{ username: "admin", password: "1234" }];

app.use((req, res, next) => {
    const authHeader = req.headers["authorization"];
    if (!authHeader) return res.status(401).json({ error: "Unauthorized" });

    const credentials = Buffer.from(authHeader.split(" ")[1], "base64").toString().split(":");
    const user = users.find(u => u.username === credentials[0] && u.password === credentials[1]);

    if (!user) return res.status(401).json({ error: "Invalid credentials" });
    
    next();
});
```

**6.2. Making Authenticated API Requests**

```
curl -u admin:1234 -X GET http://localhost:3000/users
```

  

---

**7. Building a Simple API-Connected Web App**

  

**7.1. HTML & JavaScript API Integration**

  

Create **index.html**:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <title>API Test</title>
</head>
<body>
    <h1>Users</h1>
    <button onclick="fetchUsers()">Load Users</button>
    <ul id="userList"></ul>

    <script>
        function fetchUsers() {
            fetch("http://localhost:3000/users")
                .then(response => response.json())
                .then(data => {
                    document.getElementById("userList").innerHTML = data.map(user => `<li>${user.name}</li>`).join("");
                });
        }
    </script>
</body>
</html>
```

Run:

```
http://localhost:3000/index.html
```

  

---

**8. Conclusion**

  

**What You Learned in API Level 1:**

  

✅ **Understanding RESTful APIs & HTTP Methods**

✅ **Building a Simple API with Express.js (Node.js)**

✅ **Consuming APIs with Fetch (JavaScript) & HttpClient (VB.NET)**

✅ **Handling JSON Data**

✅ **Testing APIs with Postman & Curl**

✅ **Securing API Requests with Basic Authentication**

✅ **Built a Simple API-Connected Web App**

  

Now, you’re ready for **API Level 2**, where we explore **GraphQL, Authentication (JWT, OAuth), WebSockets, and Advanced API Security!** 🚀