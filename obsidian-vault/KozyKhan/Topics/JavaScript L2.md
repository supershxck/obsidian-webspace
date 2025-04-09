> **March 14th, 2025**  **18:18:47** 
> **Topics:** [[JavaScript L3]] 
> **Tags:** #
---

**JavaScript Level 2: Intermediate to Advanced JavaScript**

  

**Introduction**

  

Now that you understand the **basics of JavaScript**, it’s time to explore **advanced topics** such as:

• **Advanced DOM Manipulation**

• **Events & Delegation**

• **Web APIs (Fetch, Local Storage, Geolocation, etc.)**

• **AJAX & JSON**

• **Asynchronous JavaScript (Advanced Promises, Async/Await)**

• **Modules & ES6+ Features**

• **Object-Oriented Programming (OOP) in JavaScript**

• **Error Handling & Debugging**

• **Introduction to Node.js & Express.js**

• **Building a To-Do List Web App**

  

By the end of this lesson, you will be able to **write efficient JavaScript code for web applications, handle APIs, and work with Node.js**.

---

**1. Advanced DOM Manipulation**

  

**1.1. Selecting Multiple Elements**

```
document.querySelectorAll(".item").forEach(item => {
  item.style.color = "red";
});
```

**1.2. Creating and Appending Elements**

```
let newElement = document.createElement("p");
newElement.textContent = "New Paragraph";
document.body.appendChild(newElement);
```

**1.3. Removing Elements**

```
let element = document.getElementById("removeMe");
element.remove();
```

  

---

**2. Events & Delegation**

  

**2.1. Event Bubbling & Capturing**

```
document.getElementById("parent").addEventListener("click", () => {
  console.log("Parent Clicked!");
}, true);  // 'true' enables capturing phase
```

**2.2. Event Delegation**

```
document.getElementById("list").addEventListener("click", (event) => {
  if (event.target.tagName === "LI") {
    console.log("Item Clicked:", event.target.textContent);
  }
});
```

  

---

**3. Web APIs (Fetch, Local Storage, Geolocation, etc.)**

  

**3.1. Local Storage (Saving User Data)**

```
localStorage.setItem("username", "Alice");
console.log(localStorage.getItem("username"));  // "Alice"
localStorage.removeItem("username");
```

**3.2. Geolocation API (Getting User Location)**

```
navigator.geolocation.getCurrentPosition(position => {
  console.log(position.coords.latitude, position.coords.longitude);
});
```

**3.3. Fetch API (Getting Data from an API)**

```
fetch("https://jsonplaceholder.typicode.com/users")
  .then(response => response.json())
  .then(data => console.log(data));
```

  

---

**4. AJAX & JSON**

  

AJAX allows asynchronous requests without reloading the page.

  

**4.1. Fetching JSON Data**

```
fetch("https://jsonplaceholder.typicode.com/posts")
  .then(response => response.json())
  .then(posts => console.log(posts));
```

**4.2. Sending Data with Fetch (POST Request)**

```
fetch("https://jsonplaceholder.typicode.com/posts", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ title: "New Post", body: "This is a post" })
})
.then(response => response.json())
.then(data => console.log(data));
```

  

---

**5. Advanced Asynchronous JavaScript**

  

**5.1. Chaining Promises**

```
fetch("https://jsonplaceholder.typicode.com/users")
  .then(response => response.json())
  .then(users => users[0])
  .then(user => console.log(user.name));
```

**5.2. Async/Await with Error Handling**

```
async function getUser() {
  try {
    let response = await fetch("https://jsonplaceholder.typicode.com/users/1");
    let user = await response.json();
    console.log(user.name);
  } catch (error) {
    console.error("Error:", error);
  }
}
getUser();
```

  

---

**6. JavaScript Modules (ES6+)**

  

**6.1. Exporting Functions**

```
// module.js
export function greet(name) {
  return `Hello, ${name}`;
}
```

**6.2. Importing Functions**

```
// main.js
import { greet } from "./module.js";
console.log(greet("Alice"));
```

  

---

**7. Object-Oriented Programming (OOP) in JavaScript**

  

**7.1. Creating a Class**

```
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  greet() {
    return `Hello, I'm ${this.name}`;
  }
}
let alice = new Person("Alice", 25);
console.log(alice.greet());
```

**7.2. Inheritance**

```
class Student extends Person {
  constructor(name, age, grade) {
    super(name, age);
    this.grade = grade;
  }
}
let student = new Student("Bob", 20, "A");
console.log(student.greet());
```

  

---

**8. Error Handling & Debugging**

  

**8.1. Try-Catch for Error Handling**

```
try {
  let x = undefinedVariable;
} catch (error) {
  console.error("Caught an error:", error);
}
```

**8.2. Using throw for Custom Errors**

```
function checkAge(age) {
  if (age < 18) throw "Underage!";
  return "Allowed";
}
try {
  console.log(checkAge(16));
} catch (error) {
  console.error(error);
}
```

  

---

**9. Introduction to Node.js & Express.js**

  

**9.1. Setting Up a Node.js Server**

```
npm init -y
npm install express
```

**9.2. Creating a Simple Express.js Server**

```
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("Hello from Node.js!");
});

app.listen(3000, () => console.log("Server running on port 3000"));
```

  

---

**10. Building a To-Do List Web App**

  

**10.1. HTML**

```
<!DOCTYPE html>
<html>
<head>
  <title>To-Do List</title>
</head>
<body>
  <h1>To-Do List</h1>
  <input id="taskInput" type="text">
  <button id="addTask">Add Task</button>
  <ul id="taskList"></ul>
  <script src="script.js"></script>
</body>
</html>
```

**10.2. JavaScript (script.js)**

```
document.getElementById("addTask").addEventListener("click", () => {
  let task = document.getElementById("taskInput").value;
  if (task) {
    let li = document.createElement("li");
    li.textContent = task;
    document.getElementById("taskList").appendChild(li);
    document.getElementById("taskInput").value = "";
  }
});
```

  

---

**Conclusion**

  

**What You Learned in JavaScript Level 2:**

  

✅ **Advanced DOM Manipulation**

✅ **Events, Delegation & Event Bubbling**

✅ **Web APIs (Local Storage, Geolocation, Fetch API)**

✅ **AJAX & JSON Data Handling**

✅ **Advanced Asynchronous JavaScript (Promises, Async/Await)**

✅ **JavaScript Modules (ES6 Imports/Exports)**

✅ **Object-Oriented Programming (Classes, Inheritance)**

✅ **Error Handling & Debugging**

✅ **Introduction to Node.js & Express.js**

✅ **Built a To-Do List Web App**

  

Now, you’re ready for **JavaScript Level 3**, where we dive into **Full-Stack Development, WebSockets, Advanced Node.js, and React.js**! 🚀