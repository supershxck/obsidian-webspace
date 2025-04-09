> **March 14th, 2025**  **18:17:30** 
> **Topics:** [[JavaScript L2]] 
> **Tags:** #
---

**JavaScript Level 1: From Beginner to Intermediate in One Lesson**

  

**Introduction**

  

JavaScript is the **core language of the web**, used for **front-end development, back-end (Node.js), game development, and even AI**. In this lesson, you will learn:

1. **JavaScript Basics** (Syntax, Variables, Data Types, Operators)

2. **Functions & Scope**

3. **Control Flow (If-Else, Loops)**

4. **Arrays & Objects**

5. **DOM Manipulation (Basic Web Interaction)**

6. **Events & Callbacks**

7. **Asynchronous JavaScript (Promises & Async/Await)**

8. **Basic Error Handling**

9. **Introduction to ES6+ Features**

10. **Building a Simple Web App**

  

By the end of this lesson, you will be able to **write functional JavaScript code and interact with the browser**.

---

**1. JavaScript Basics**

  

JavaScript runs **inside the browser** and **on servers with Node.js**.

  

**1.1. Running JavaScript**

• In a browser, open the **Console (F12 > Console)**.

• Create a **.js file** and include it in an HTML file:

```
<script src="script.js"></script>
```

  

  

**1.2. Hello World**

```
console.log("Hello, World!");
```

**1.3. Variables (var, let, const)**

```
let name = "Alice";   // Can be reassigned
const age = 25;       // Cannot be changed
var city = "New York"; // Older, avoid using
```

**1.4. Data Types**

```
let num = 10;       // Number
let pi = 3.14;      // Float
let isStudent = true; // Boolean
let message = "Hello"; // String
let items = ["apple", "banana"]; // Array
let person = { name: "Alice", age: 25 }; // Object
let notDefined;      // Undefined
let emptyValue = null; // Null
```

**1.5. Operators**

```
let x = 10 + 5;  // Addition
let y = 10 / 2;  // Division
let z = 10 % 3;  // Modulus
let isEqual = (10 === "10"); // false (strict comparison)
```

  

---

**2. Functions & Scope**

  

Functions let you **reuse code**.

  

**2.1. Function Declaration**

```
function greet(name) {
  return "Hello, " + name;
}
console.log(greet("Alice"));
```

**2.2. Arrow Functions (ES6)**

```
const greet = (name) => `Hello, ${name}`;
console.log(greet("Bob"));
```

**2.3. Function Scope (Global vs Local)**

```
let globalVar = "I'm global";

function testScope() {
  let localVar = "I'm local";
  console.log(globalVar); // Accessible
}
console.log(localVar); // Error (local variable)
```

  

---

**3. Control Flow (If-Else, Loops)**

  

**3.1. If-Else Statement**

```
let age = 18;
if (age >= 18) {
  console.log("You are an adult.");
} else {
  console.log("You are a minor.");
}
```

**3.2. For Loop**

```
for (let i = 0; i < 5; i++) {
  console.log("Iteration: " + i);
}
```

**3.3. While Loop**

```
let count = 0;
while (count < 5) {
  console.log(count);
  count++;
}
```

  

---

**4. Arrays & Objects**

  

**4.1. Arrays**

```
let fruits = ["apple", "banana", "cherry"];
console.log(fruits[1]); // banana
fruits.push("orange");  // Add item
console.log(fruits.length); // Get array length
```

**4.2. Objects**

```
let person = {
  name: "Alice",
  age: 25,
  greet: function() {
    return "Hello, " + this.name;
  }
};
console.log(person.greet());
```

  

---

**5. DOM Manipulation (Basic Web Interaction)**

  

JavaScript interacts with the **Document Object Model (DOM)** to modify web pages.

  

**5.1. Selecting Elements**

```
document.getElementById("myElement").textContent = "Changed text!";
```

**5.2. Modifying HTML & CSS**

```
document.querySelector(".myClass").style.color = "blue";
```

  

---

**6. Events & Callbacks**

  

**6.1. Handling Events**

```
document.getElementById("myButton").addEventListener("click", () => {
  alert("Button Clicked!");
});
```

  

---

**7. Asynchronous JavaScript (Promises & Async/Await)**

  

JavaScript is **non-blocking**, meaning code can run **asynchronously**.

  

**7.1. Using Promises**

```
fetch("https://jsonplaceholder.typicode.com/posts")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

**7.2. Async/Await (ES8)**

```
async function fetchData() {
  try {
    let response = await fetch("https://jsonplaceholder.typicode.com/posts");
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Error:", error);
  }
}
fetchData();
```

  

---

**8. Basic Error Handling**

```
try {
  let x = 10 / 0;
} catch (error) {
  console.log("Error:", error.message);
}
```

  

---

**9. Introduction to ES6+ Features**

  

**9.1. Template Literals**

```
let name = "Alice";
console.log(`Hello, ${name}!`);
```

**9.2. Destructuring**

```
let person = { name: "Bob", age: 30 };
let { name, age } = person;
console.log(name, age);
```

**9.3. Spread Operator**

```
let numbers = [1, 2, 3];
let newNumbers = [...numbers, 4, 5];
console.log(newNumbers);
```

  

---

**10. Building a Simple Web App**

  

**HTML**

```
<!DOCTYPE html>
<html>
<head>
  <title>Counter App</title>
</head>
<body>
  <h1 id="counter">0</h1>
  <button id="increment">Increment</button>
  <script src="script.js"></script>
</body>
</html>
```

**JavaScript (script.js)**

```
let count = 0;
document.getElementById("increment").addEventListener("click", () => {
  count++;
  document.getElementById("counter").textContent = count;
});
```

  

---

**Conclusion**

  

**What You Learned in JavaScript Level 1:**

  

✅ **Basic Syntax & Variables**

✅ **Functions & Scope**

✅ **Control Flow (If-Else, Loops)**

✅ **Arrays & Objects**

✅ **DOM Manipulation (Web Interaction)**

✅ **Events & Callbacks**

✅ **Asynchronous JavaScript (Promises & Async/Await)**

✅ **Basic Error Handling**

✅ **Modern JavaScript (ES6+ Features)**

✅ **Built a Simple Counter App**

  

Now, you are ready for **JavaScript Level 2**, where we explore **Advanced DOM Manipulation, Web APIs, Local Storage, AJAX, and Node.js**! 🚀