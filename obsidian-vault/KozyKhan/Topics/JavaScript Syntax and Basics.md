> **February 8th, 2025**  **03:26:30** 
> **Topics:** [[
> **Tags:** #
---

JavaScript Syntax and Basics

  

JavaScript is a high-level, interpreted programming language used primarily for web development. It allows developers to add interactivity, manipulate the DOM, and create dynamic web applications.

1. JavaScript Syntax

  

The syntax of JavaScript follows rules similar to other C-like languages (such as Java and C++). Here are the key syntax rules:

â€¢ Case-Sensitive: var and Var are different identifiers.

â€¢ Statements End with a Semicolon (;): Though optional, itâ€™s a good practice.

â€¢ Comments:

â€¢ Single-line: // This is a comment

â€¢ Multi-line:

/* This is a

   multi-line comment */

2. Variables and Data Types

  

JavaScript has three main ways to declare variables:

  

Variable Declarations

var x = 10;    // Function-scoped (older syntax)

let y = 20;    // Block-scoped (ES6)

const z = 30;  // Block-scoped and constant

Data Types

  

JavaScript is dynamically typed, meaning variables do not have fixed types.

1. Primitive Data Types

let str = "Hello";   // String

let num = 42;        // Number

let isTrue = true;   // Boolean

let nothing = null;  // Null

let notDefined;      // Undefined

let unique = Symbol("id"); // Symbol (ES6)

  

2. Complex Data Type

let obj = { name: "John", age: 25 }; // Object

let arr = [1, 2, 3];                 // Array (special object)

let func = function() { return "Hi"; }; // Function (also an object)

1. Operators

  

JavaScript supports a variety of operators:

â€¢ Arithmetic Operators

let sum = 10 + 5;   // Addition

let diff = 10 - 5;  // Subtraction

let prod = 10 * 5;  // Multiplication

let div = 10 / 5;   // Division

let mod = 10 % 3;   // Modulus

let exp = 2 ** 3;   // Exponentiation

  

â€¢ Comparison Operators

console.log(10 > 5);  // true

console.log(10 == "10"); // true (loose equality)

console.log(10 === "10"); // false (strict equality)

console.log(10 !== "10"); // true (strict inequality)

  

â€¢ Logical Operators

console.log(true && false); // false (AND)

console.log(true || false); // true (OR)

console.log(!true);         // false (NOT)

  

â€¢ Assignment Operators

let x = 10;

x += 5; // Equivalent to x = x + 5

x *= 2; // Equivalent to x = x * 2

2. Control Flow

  

Control flow structures help manage program execution.

  

Conditional Statements

let age = 20;

if (age >= 18) {

    console.log("You are an adult.");

} else {

    console.log("You are a minor.");

}

Switch Statement

let day = "Monday";

switch (day) {

    case "Monday":

        console.log("Start of the week!");

        break;

    case "Friday":

        console.log("Weekend is near!");

        break;

    default:

        console.log("Just another day.");

}

Loops

  

Loops execute code repeatedly.

â€¢ For Loop

for (let i = 0; i < 5; i++) {

    console.log(i);

}

  

â€¢ While Loop

let j = 0;

while (j < 5) {

    console.log(j);

    j++;

}

  

â€¢ Do-While Loop

let k = 0;

do {

    console.log(k);

    k++;

} while (k < 5);

3. Functions

  

Functions encapsulate reusable logic.

  

Function Declaration

function greet(name) {

    return "Hello, " + name + "!";

}

console.log(greet("Alice"));

Arrow Functions (ES6)

const greet = (name) => `Hello, ${name}!`;

console.log(greet("Bob"));

4. Objects and Arrays

  

Objects

let person = {

    name: "John",

    age: 30,

    greet: function() {

        console.log("Hello!");

    }

};

console.log(person.name);  // Access property

person.greet();  // Call method

Arrays

let fruits = ["Apple", "Banana", "Cherry"];

console.log(fruits[1]); // Access index (Banana)

fruits.push("Orange");  // Add element

fruits.pop();           // Remove last element

5. DOM Manipulation

  

JavaScript interacts with HTML and CSS via the Document Object Model (DOM).

  

Selecting Elements

let heading = document.getElementById("title");

let paragraphs = document.querySelectorAll("p");

Modifying Content

heading.textContent = "New Title";

Event Listeners

button.addEventListener("click", function() {

    alert("Button clicked!");

});

6. Asynchronous JavaScript

  

JavaScript can handle asynchronous operations using callbacks, promises, and async/await.

  

Using setTimeout (Callback)

setTimeout(() => {

    console.log("This runs after 2 seconds.");

}, 2000);

Using Promises

let promise = new Promise((resolve, reject) => {

    setTimeout(() => resolve("Success!"), 3000);

});

  

promise.then(response => console.log(response));

Using Async/Await

async function fetchData() {

    let response = await fetch("https://api.example.com/data");

    let data = await response.json();

    console.log(data);

}

fetchData();

7. ES6+ Features

  

Modern JavaScript includes features like:

â€¢ Template Literals:

let name = "Alice";

console.log(`Hello, ${name}!`);

  

â€¢ Destructuring:

let { name, age } = { name: "Bob", age: 25 };

console.log(name, age);

  

â€¢ Spread Operator:

let arr1 = [1, 2, 3];

let arr2 = [...arr1, 4, 5];

console.log(arr2); // [1, 2, 3, 4, 5]

Conclusion

  

JavaScript is a powerful language for web development. Understanding its syntax, control flow, functions, objects, DOM manipulation, and asynchronous programming is crucial for building modern applications. Start by practicing basic syntax, and gradually explore advanced topics like ES6+ features and API integrations.