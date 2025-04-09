> **March 14th, 2025**  **18:21:43** 
> **Topics:** [[Java L1]] 
> **Tags:** #
---

**JavaScript Level 3: Advanced JavaScript & Full-Stack Development**

  

**Introduction**

  

Now that you’ve mastered **JavaScript fundamentals and intermediate concepts**, it’s time to explore **advanced techniques** that will help you build **scalable, full-stack applications**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Advanced JavaScript Concepts (Closures, Prototypes, Higher-Order Functions)**

✅ **Functional Programming (Pure Functions, Currying, Composition)**

✅ **WebSockets & Real-Time Communication**

✅ **Full-Stack Development with Node.js & Express.js**

✅ **Database Integration (MongoDB, PostgreSQL)**

✅ **Authentication & Security (JWT, OAuth, Encryption)**

✅ **Introduction to React.js (Component-Based UI)**

✅ **Deployment & Performance Optimization**

  

By the end of this lesson, you will be able to **build and deploy full-stack JavaScript applications**.

---

**1. Advanced JavaScript Concepts**

  

**1.1. Closures**

  

A **closure** is a function that remembers the variables from its outer scope, even after that scope has closed.

```
function outerFunction(x) {
  return function innerFunction(y) {
    return x + y;
  };
}

const add10 = outerFunction(10);
console.log(add10(5)); // 15
```

**1.2. Prototypes & Prototype Inheritance**

  

JavaScript uses **prototypes** instead of classes for object inheritance.

```
function Person(name) {
  this.name = name;
}

Person.prototype.greet = function () {
  console.log(`Hello, my name is ${this.name}`);
};

const alice = new Person("Alice");
alice.greet(); // "Hello, my name is Alice"
```

**1.3. Higher-Order Functions**

  

Functions that **accept functions as arguments** or **return functions**.

```
function multiplyBy(factor) {
  return function (num) {
    return num * factor;
  };
}

const double = multiplyBy(2);
console.log(double(5)); // 10
```

  

---

**2. Functional Programming**

  

**2.1. Pure Functions**

  

Pure functions have **no side effects** and always return the same output for the same input.

```
const add = (a, b) => a + b;
```

**2.2. Currying**

  

Converts a function with multiple arguments into a sequence of functions.

```
const curriedAdd = (a) => (b) => a + b;
console.log(curriedAdd(5)(10)); // 15
```

**2.3. Function Composition**

  

Combining multiple functions into one.

```
const toUpperCase = (str) => str.toUpperCase();
const addExclamation = (str) => str + "!";
const excitedGreeting = (str) => addExclamation(toUpperCase(str));

console.log(excitedGreeting("hello")); // "HELLO!"
```

  

---

**3. WebSockets & Real-Time Communication**

  

**3.1. Setting Up a WebSocket Server**

```
const WebSocket = require("ws");
const server = new WebSocket.Server({ port: 8080 });

server.on("connection", (socket) => {
  socket.send("Welcome to the WebSocket Server!");
  socket.on("message", (message) => console.log("Received:", message));
});
```

**3.2. Connecting WebSocket on the Client**

```
const socket = new WebSocket("ws://localhost:8080");
socket.onmessage = (event) => console.log("Message:", event.data);
socket.send("Hello Server!");
```

  

---

**4. Full-Stack Development with Node.js & Express.js**

  

**4.1. Creating a Simple Express Server**

```
const express = require("express");
const app = express();

app.get("/", (req, res) => res.send("Hello, Full-Stack JavaScript!"));

app.listen(3000, () => console.log("Server running on port 3000"));
```

**4.2. REST API with Express**

```
const express = require("express");
const app = express();
app.use(express.json());

let users = [{ id: 1, name: "Alice" }];

app.get("/users", (req, res) => res.json(users));

app.post("/users", (req, res) => {
  users.push(req.body);
  res.status(201).json(req.body);
});

app.listen(3000, () => console.log("API running on port 3000"));
```

  

---

**5. Database Integration (MongoDB, PostgreSQL)**

  

**5.1. Connecting to MongoDB with Mongoose**

```
const mongoose = require("mongoose");
mongoose.connect("mongodb://localhost:27017/mydb", { useNewUrlParser: true });

const UserSchema = new mongoose.Schema({ name: String });
const User = mongoose.model("User", UserSchema);

const user = new User({ name: "Alice" });
user.save();
```

**5.2. PostgreSQL with Node.js**

```
const { Client } = require("pg");
const client = new Client({ connectionString: "postgres://user:pass@localhost:5432/mydb" });

client.connect();
client.query("SELECT * FROM users", (err, res) => {
  console.log(res.rows);
  client.end();
});
```

  

---

**6. Authentication & Security**

  

**6.1. JSON Web Tokens (JWT)**

```
const jwt = require("jsonwebtoken");
const token = jwt.sign({ user: "Alice" }, "secret_key", { expiresIn: "1h" });
console.log(token);
```

**6.2. Hashing Passwords with bcrypt**

```
const bcrypt = require("bcrypt");
const hashedPassword = bcrypt.hashSync("mypassword", 10);
console.log(hashedPassword);
```

  

---

**7. Introduction to React.js**

  

React is a front-end framework for **building interactive UIs**.

  

**7.1. Creating a React Component**

```
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}
export default Greeting;
```

**7.2. Rendering Components**

```
import React from "react";
import ReactDOM from "react-dom";
import Greeting from "./Greeting";

ReactDOM.render(<Greeting name="Alice" />, document.getElementById("root"));
```

  

---

**8. Deployment & Performance Optimization**

  

**8.1. Minify JavaScript for Faster Load Times**

```
npm install terser -g
terser script.js -o script.min.js
```

**8.2. Deploying a Node.js App to Heroku**

```
heroku login
heroku create my-app
git push heroku main
```

  

---

**9. Final Project: Real-Time Chat App**

  

**9.1. Backend (Node.js + WebSockets)**

```
const express = require("express");
const http = require("http");
const WebSocket = require("ws");

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

wss.on("connection", (ws) => {
  ws.on("message", (message) => {
    wss.clients.forEach(client => client.send(message));
  });
});

server.listen(3000, () => console.log("Chat server running on port 3000"));
```

**9.2. Frontend (HTML + JavaScript)**

```
<!DOCTYPE html>
<html>
<body>
  <input id="message" type="text">
  <button onclick="sendMessage()">Send</button>
  <ul id="chat"></ul>

  <script>
    const socket = new WebSocket("ws://localhost:3000");
    socket.onmessage = event => {
      let li = document.createElement("li");
      li.textContent = event.data;
      document.getElementById("chat").appendChild(li);
    };

    function sendMessage() {
      let msg = document.getElementById("message").value;
      socket.send(msg);
    }
  </script>
</body>
</html>
```

  

---

**Conclusion**

  

**What You Learned in JavaScript Level 3:**

  

✅ **Advanced JavaScript (Closures, Prototypes, Higher-Order Functions)**

✅ **Functional Programming (Currying, Composition)**

✅ **Real-Time WebSockets**

✅ **Full-Stack API with Node.js & Express.js**

✅ **MongoDB & PostgreSQL Integration**

✅ **Authentication (JWT, bcrypt)**

✅ **Introduction to React.js**

✅ **Deployment & Optimization**

✅ **Built a Real-Time Chat App**

  

Now, you’re ready for **JavaScript Level 4**, where we explore **Advanced React.js, GraphQL, Microservices, and AI with JavaScript**! 🚀