> **March 15th, 2025**  **19:17:58** 
> **Topics:** [[TypeScript L3]] 
> **Tags:** #CS 
---

**TypeScript Level 2: Intermediate to Advanced TypeScript Programming**

  

**Introduction**

  

Now that you’ve mastered **TypeScript basics**, it’s time to explore **advanced topics like generics, modules, web APIs, and full-stack development with TypeScript**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Advanced TypeScript Features (Enums, Generics, Union & Intersection Types)**

✅ **Modules & Namespaces**

✅ **Working with Web APIs & Fetching Data**

✅ **TypeScript with Node.js (Express.js, REST APIs)**

✅ **Asynchronous Programming (Async/Await, Promises)**

✅ **Error Handling & Debugging Best Practices**

✅ **Deploying a Full-Stack TypeScript Web App**

  

By the end of this lesson, you will be able to **develop scalable applications using TypeScript with frontend and backend integration**.

---

**1. Advanced TypeScript Features**

  

**1.1. Enums**

```
enum Status {
    Pending,
    InProgress,
    Completed
}
let taskStatus: Status = Status.InProgress;
console.log(taskStatus);  // Output: 1 (Enums are zero-based by default)
```

**1.2. Generics (Reusable Components)**

```
function identity<T>(arg: T): T {
    return arg;
}
console.log(identity<number>(42));  // Output: 42
console.log(identity<string>("Hello"));  // Output: Hello
```

**1.3. Union & Intersection Types**

```
type ID = string | number;  // Union Type
let userID: ID = 123;
userID = "ABC123";  // Valid

type Employee = { name: string; age: number };
type Developer = { language: string };
type SoftwareEngineer = Employee & Developer;  // Intersection Type

const dev: SoftwareEngineer = { name: "Alice", age: 30, language: "TypeScript" };
```

  

---

**2. Modules & Namespaces**

  

**2.1. Creating & Importing Modules**

1. **Create math.ts**:

```
export function add(a: number, b: number): number {
    return a + b;
}
```

  

1. **Use it in app.ts**:

```
import { add } from "./math";
console.log(add(5, 3));  // Output: 8
```

  

1. **Compile with:**

```
tsc --module commonjs app.ts
```

  

---

**3. Working with Web APIs & Fetching Data**

  

**3.1. Fetching JSON Data**

```
async function fetchData(): Promise<void> {
    const response = await fetch("https://jsonplaceholder.typicode.com/todos/1");
    const data = await response.json();
    console.log(data);
}
fetchData();
```

**3.2. Handling API Errors**

```
async function fetchUser(userId: number) {
    try {
        let response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
        if (!response.ok) throw new Error("User not found");
        let data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Error:", error.message);
    }
}
fetchUser(1);
```

  

---

**4. TypeScript with Node.js (Express.js, REST APIs)**

  

**4.1. Setting Up Express with TypeScript**

1. Install dependencies:

```
npm init -y
npm install express @types/express typescript ts-node nodemon
```

  

1. **Create server.ts**:

```
import express from "express";

const app = express();
app.use(express.json());

app.get("/", (req, res) => {
    res.send("Hello from TypeScript Express!");
});

app.listen(3000, () => console.log("Server running on port 3000"));
```

  

1. Run the server:

```
ts-node server.ts
```

  

  

**4.2. Creating a REST API with Express**

```
import express from "express";

const app = express();
app.use(express.json());

type User = { id: number; name: string };
const users: User[] = [{ id: 1, name: "Alice" }];

app.get("/users", (req, res) => {
    res.json(users);
});

app.post("/users", (req, res) => {
    const newUser: User = { id: users.length + 1, name: req.body.name };
    users.push(newUser);
    res.status(201).json(newUser);
});

app.listen(3000, () => console.log("Server running on port 3000"));
```

Test it with:

```
curl http://localhost:3000/users
```

  

---

**5. Asynchronous Programming (Async/Await, Promises)**

  

**5.1. Using Promises**

```
const getData = (): Promise<string> => {
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve("Data loaded"), 2000);
    });
};

getData().then(console.log).catch(console.error);
```

**5.2. Async/Await with Error Handling**

```
async function loadData() {
    try {
        let data = await getData();
        console.log(data);
    } catch (error) {
        console.error("Error:", error);
    }
}
loadData();
```

  

---

**6. Error Handling & Debugging Best Practices**

  

**6.1. Using try-catch for API Calls**

```
async function fetchData() {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/posts");
        if (!response.ok) throw new Error("Failed to fetch data");
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
}
fetchData();
```

**6.2. TypeScript Logging with Winston**

```
npm install winston
```

```
import winston from "winston";

const logger = winston.createLogger({
    level: "info",
    format: winston.format.json(),
    transports: [new winston.transports.Console()],
});

logger.info("Application started");
logger.error("Something went wrong!");
```

  

---

**7. Deploying a Full-Stack TypeScript Web App**

  

**7.1. Setting Up a Frontend (React with TypeScript)**

```
npx create-react-app my-app --template typescript
cd my-app
npm start
```

**7.2. Connecting Frontend to Backend**

  

Fetch data in React:

```
useEffect(() => {
    fetch("http://localhost:3000/users")
        .then(response => response.json())
        .then(data => console.log(data));
}, []);
```

**7.3. Deploying the Backend to Vercel**

```
npm install -g vercel
vercel deploy
```

  

---

**8. Conclusion**

  

**What You Learned in TypeScript Level 2:**

  

✅ **Advanced TypeScript Features (Enums, Generics, Union & Intersection Types)**

✅ **Modules & Namespaces**

✅ **Working with Web APIs & Fetching Data**

✅ **TypeScript with Node.js (Express.js, REST APIs)**

✅ **Asynchronous Programming (Async/Await, Promises)**

✅ **Error Handling & Debugging Best Practices**

✅ **Deploying a Full-Stack TypeScript Web App**

  

Now, you’re ready for **TypeScript Level 3**, where we explore **GraphQL, Microservices, Authentication (JWT, OAuth), and Cloud Deployment!** 🚀