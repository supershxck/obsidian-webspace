> **March 16th, 2025**  **15:31:46** 
> **Topics:** [[Linux L1]] 
> **Tags:** #
---

**TypeScript Level 3: Advanced TypeScript Development & Full-Stack Applications**

  

**Introduction**

  

Now that you’ve learned **advanced TypeScript features, REST APIs, and frontend integration**, it’s time to explore **GraphQL, microservices, authentication, advanced testing, and cloud deployment**.

  

**What You’ll Learn in This Lesson:**

  

✅ **GraphQL with TypeScript (Apollo Server & Client)**

✅ **Microservices & Event-Driven Architecture**

✅ **Authentication (JWT, OAuth 2.0, Role-Based Access Control)**

✅ **Testing (Jest, Cypress, Supertest)**

✅ **Advanced TypeScript with Decorators & Metadata**

✅ **Cloud Deployment (Docker, Kubernetes, AWS, Firebase, Vercel)**

✅ **Building & Deploying a Full-Stack TypeScript App**

  

By the end of this lesson, you will be able to **develop scalable, production-ready TypeScript applications using modern web technologies**.

---

**1. GraphQL with TypeScript**

  

**1.1. Setting Up Apollo Server**

1. Install dependencies:

```
npm install apollo-server graphql typescript ts-node @types/node
```

  

1. Create server.ts:

```
import { ApolloServer, gql } from "apollo-server";

const typeDefs = gql`
    type Query {
        hello: String
    }
`;

const resolvers = {
    Query: {
        hello: () => "Hello, GraphQL!",
    },
};

const server = new ApolloServer({ typeDefs, resolvers });

server.listen(4000).then(({ url }) => console.log(`Server running at ${url}`));
```

  

1. Start the server:

```
ts-node server.ts
```

  

1. Open **http://localhost:4000** in a browser to test queries.

  

**1.2. Adding a GraphQL Mutation**

```
const typeDefs = gql`
    type User {
        id: ID!
        name: String!
    }
    type Query {
        users: [User]
    }
    type Mutation {
        createUser(name: String!): User
    }
`;

let users = [];

const resolvers = {
    Query: {
        users: () => users,
    },
    Mutation: {
        createUser: (_, { name }) => {
            const user = { id: users.length + 1, name };
            users.push(user);
            return user;
        },
    },
};
```

  

---

**2. Microservices & Event-Driven Architecture**

  

**2.1. Setting Up a Microservice with TypeScript**

1. Install dependencies:

```
npm install express amqplib axios typescript ts-node
```

  

1. Create user-service.ts:

```
import express from "express";

const app = express();
app.use(express.json());

let users: any[] = [];

app.post("/users", (req, res) => {
    const user = { id: users.length + 1, ...req.body };
    users.push(user);
    res.status(201).json(user);
});

app.listen(3001, () => console.log("User service running on port 3001"));
```

  

1. Create order-service.ts:

```
import express from "express";
import axios from "axios";

const app = express();
app.use(express.json());

app.get("/orders", async (req, res) => {
    const users = await axios.get("http://localhost:3001/users");
    res.json({ message: "Orders", users: users.data });
});

app.listen(3002, () => console.log("Order service running on port 3002"));
```

  

---

**3. Authentication (JWT, OAuth 2.0, Role-Based Access Control)**

  

**3.1. Implementing JWT Authentication**

1. Install dependencies:

```
npm install express jsonwebtoken bcryptjs @types/jsonwebtoken @types/bcryptjs
```

  

1. Create auth.ts:

```
import express from "express";
import jwt from "jsonwebtoken";
import bcrypt from "bcryptjs";

const app = express();
app.use(express.json());

const users: any[] = [];

app.post("/register", async (req, res) => {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = { id: users.length + 1, email: req.body.email, password: hashedPassword };
    users.push(user);
    res.status(201).json({ message: "User registered" });
});

app.post("/login", async (req, res) => {
    const user = users.find(u => u.email === req.body.email);
    if (!user || !(await bcrypt.compare(req.body.password, user.password))) {
        return res.status(401).json({ message: "Invalid credentials" });
    }
    const token = jwt.sign({ id: user.id }, "secret", { expiresIn: "1h" });
    res.json({ token });
});

app.listen(4000, () => console.log("Auth service running on port 4000"));
```

  

---

**4. Testing (Jest, Cypress, Supertest)**

  

**4.1. Unit Testing with Jest**

```
npm install jest ts-jest @types/jest
```

```
function add(a: number, b: number): number {
    return a + b;
}

test("adds 2 + 3 to equal 5", () => {
    expect(add(2, 3)).toBe(5);
});
```

**4.2. API Testing with Supertest**

```
npm install supertest @types/supertest
```

```
import request from "supertest";
import app from "./server"; // Import Express server

test("GET /users should return an array", async () => {
    const response = await request(app).get("/users");
    expect(response.status).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);
});
```

  

---

**5. Advanced TypeScript with Decorators & Metadata**

  

**5.1. Using Decorators**

```
function Logger(target: Function) {
    console.log("Logging...");
}

@Logger
class Person {
    constructor(public name: string) {
        console.log(`Person ${name} created`);
    }
}

new Person("Alice");
```

  

---

**6. Cloud Deployment (Docker, Kubernetes, AWS, Firebase, Vercel)**

  

**6.1. Dockerizing a TypeScript App**

1. Create a Dockerfile:

```
FROM node:14
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "dist/server.js"]
```

  

1. Build and run:

```
docker build -t my-typescript-app .
docker run -p 3000:3000 my-typescript-app
```

  

  

**6.2. Deploying to AWS Lambda**

1. Install:

```
npm install -g serverless
```

  

1. Deploy:

```
serverless deploy
```

  

  

**6.3. Deploying to Vercel**

```
npm install -g vercel
vercel deploy
```

  

---

**7. Building & Deploying a Full-Stack TypeScript App**

  

**7.1. Creating a React Frontend**

```
npx create-react-app my-app --template typescript
cd my-app
npm start
```

**7.2. Connecting Frontend to GraphQL**

```
import { gql, useQuery } from "@apollo/client";

const GET_USERS = gql`
    query {
        users {
            id
            name
        }
    }
`;

const Users = () => {
    const { loading, error, data } = useQuery(GET_USERS);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error</p>;

    return <ul>{data.users.map(user => <li key={user.id}>{user.name}</li>)}</ul>;
};
```

  

---

**8. Conclusion**

  

**What You Learned in TypeScript Level 3:**

  

✅ **GraphQL with TypeScript (Apollo Server & Client)**

✅ **Microservices & Event-Driven Architecture**

✅ **Authentication (JWT, OAuth 2.0, Role-Based Access Control)**

✅ **Testing (Jest, Cypress, Supertest)**

✅ **Advanced TypeScript with Decorators & Metadata**

✅ **Cloud Deployment (Docker, Kubernetes, AWS, Firebase, Vercel)**

✅ **Built & Deployed a Full-Stack TypeScript App**

  

Now, you’re ready for **TypeScript Level 4**, where we explore **Blockchain, AI, WebAssembly, and Advanced CI/CD Pipelines!** 🚀