> **March 15th, 2025**  **19:11:06** 
> **Topics:** [[TypeScript L2]] 
> **Tags:** #CS 
---

**TypeScript Level 1: Introduction to TypeScript Programming**

  

**Introduction**

  

TypeScript is a **strongly typed superset of JavaScript** that compiles to plain JavaScript. It enhances JavaScript by **adding static types, interfaces, and modern ES features**, making it ideal for **large-scale applications and frontend development with Angular, React, and Node.js**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Setting Up TypeScript & Compiling Code**

✅ **Basic Syntax (Variables, Data Types, Operators)**

✅ **Functions & Type Annotations**

✅ **Interfaces & Type Aliases**

✅ **Control Flow (If-Else, Loops, Switch)**

✅ **Classes & Object-Oriented Programming**

✅ **Error Handling & Debugging**

✅ **Building a Simple TypeScript Web App**

  

By the end of this lesson, you will be able to **write TypeScript programs with type safety and object-oriented features**.

---

**1. Setting Up TypeScript**

  

**1.1. Installing TypeScript**

  

Install TypeScript globally:

```
npm install -g typescript
```

Verify installation:

```
tsc --version
```

**1.2. Compiling TypeScript Code**

1. Create a file hello.ts:

```
let message: string = "Hello, TypeScript!";
console.log(message);
```

  

1. Compile and run:

```
tsc hello.ts
node hello.js
```

  

---

**2. TypeScript Basics: Variables, Data Types & Operators**

  

**2.1. Declaring Variables**

```
let username: string = "Alice";
let age: number = 25;
let isDeveloper: boolean = true;
```

**2.2. Basic Data Types**

```
let x: number = 10;
let y: string = "Hello";
let isActive: boolean = true;
let numbers: number[] = [1, 2, 3, 4];
let anything: any = "Can be anything"; // Avoid using `any`
```

**2.3. Operators**

```
let a = 10, b = 3;
console.log(a + b);  // Addition
console.log(a - b);  // Subtraction
console.log(a * b);  // Multiplication
console.log(a / b);  // Division
console.log(a % b);  // Modulus
```

  

---

**3. Functions & Type Annotations**

  

**3.1. Defining Functions**

```
function greet(name: string): string {
    return `Hello, ${name}!`;
}
console.log(greet("Alice"));
```

**3.2. Default & Optional Parameters**

```
function sayHello(name: string = "Guest", age?: number) {
    console.log(`Hello, ${name}, Age: ${age || "Unknown"}`);
}
sayHello("Bob");
```

**3.3. Arrow Functions**

```
const add = (a: number, b: number): number => a + b;
console.log(add(5, 3));
```

  

---

**4. Interfaces & Type Aliases**

  

**4.1. Using Interfaces**

```
interface User {
    name: string;
    age: number;
}

let user: User = { name: "Alice", age: 30 };
console.log(user.name);
```

**4.2. Type Aliases**

```
type Point = { x: number; y: number };

let p: Point = { x: 10, y: 20 };
console.log(p);
```

  

---

**5. Control Flow (If-Else, Loops, Switch)**

  

**5.1. If-Else Statement**

```
let num: number = 10;
if (num > 5) {
    console.log("Greater than 5");
} else {
    console.log("Less than or equal to 5");
}
```

**5.2. For Loop**

```
for (let i = 1; i <= 5; i++) {
    console.log(`Iteration ${i}`);
}
```

**5.3. While Loop**

```
let count = 0;
while (count < 3) {
    console.log(`Count: ${count}`);
    count++;
}
```

**5.4. Switch Case**

```
let fruit: string = "apple";
switch (fruit) {
    case "apple":
        console.log("You chose an apple!");
        break;
    case "banana":
        console.log("Bananas are great!");
        break;
    default:
        console.log("Nice choice!");
}
```

  

---

**6. Classes & Object-Oriented Programming**

  

**6.1. Creating a Class**

```
class Car {
    brand: string;
    speed: number;

    constructor(brand: string, speed: number) {
        this.brand = brand;
        this.speed = speed;
    }

    drive(): void {
        console.log(`${this.brand} is moving at ${this.speed} km/h`);
    }
}

let myCar = new Car("Tesla", 120);
myCar.drive();
```

**6.2. Inheritance**

```
class ElectricCar extends Car {
    batteryLife: number;

    constructor(brand: string, speed: number, batteryLife: number) {
        super(brand, speed);
        this.batteryLife = batteryLife;
    }

    charge(): void {
        console.log(`${this.brand} is charging with ${this.batteryLife}% battery left.`);
    }
}

let myTesla = new ElectricCar("Tesla", 150, 80);
myTesla.charge();
```

  

---

**7. Error Handling & Debugging**

  

**7.1. Try-Catch Block**

```
try {
    throw new Error("Something went wrong!");
} catch (error) {
    console.log("Error:", error.message);
}
```

**7.2. Debugging TypeScript**

1. Compile with source maps:

```
tsc --sourceMap script.ts
```

  

1. Debug in Chrome or VS Code.

---

**8. Building a Simple TypeScript Web App**

  

**8.1. Setting Up a TypeScript HTML Project**

1. Create **index.html**:

```
<html>
<head><script src="script.js"></script></head>
<body>
    <button onclick="sayHello()">Click Me</button>
</body>
</html>
```

  

1. Create **script.ts**:

```
function sayHello(): void {
    alert("Hello from TypeScript!");
}
```

  

1. Compile and run:

```
tsc script.ts
```

  

---

**9. Conclusion**

  

**What You Learned in TypeScript Level 1:**

  

✅ **Setting Up TypeScript & Compiling Code**

✅ **Basic Syntax (Variables, Data Types, Operators)**

✅ **Functions & Type Annotations**

✅ **Interfaces & Type Aliases**

✅ **Control Flow (If-Else, Loops, Switch)**

✅ **Classes & Object-Oriented Programming**

✅ **Error Handling & Debugging**

✅ **Built a Simple TypeScript Web App**

  

Now, you’re ready for **TypeScript Level 2**, where we explore **Generics, Modules, Advanced Types, Web APIs, and Full-Stack TypeScript Development!** 🚀