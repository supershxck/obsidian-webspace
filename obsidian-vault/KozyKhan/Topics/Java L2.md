> **March 14th, 2025**  **18:24:32** 
> **Topics:** [[
> **Tags:** #CS 
---

**Java Level 2: Intermediate to Advanced Java Programming**

  

**Introduction**

  

In **Java Level 2**, we dive into **advanced programming techniques** to help you build **robust, scalable applications**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Advanced OOP (Encapsulation, Polymorphism, Abstraction)**

✅ **Multithreading & Concurrency**

✅ **Java Collections Framework (Lists, Maps, Sets, Queues)**

✅ **Lambda Expressions & Streams API**

✅ **Database Connectivity with JDBC**

✅ **Networking & APIs (HTTP Requests, WebSockets)**

✅ **Unit Testing with JUnit**

✅ **Introduction to Spring Boot for Web Development**

✅ **Building a Full-Stack Java Application**

  

By the end of this lesson, you will be able to **write efficient Java applications, interact with databases, and develop backend services**.

---

**1. Advanced Object-Oriented Programming (OOP)**

  

**1.1. Encapsulation (Data Hiding)**

```
class Person {
    private String name; // Private field

    public void setName(String name) {
        this.name = name;
    }
    public String getName() {
        return name;
    }
}
```

**1.2. Abstraction (Hiding Implementation Details)**

```
abstract class Animal {
    abstract void makeSound();
}

class Dog extends Animal {
    void makeSound() {
        System.out.println("Woof!");
    }
}
```

**1.3. Polymorphism (Method Overriding)**

```
class Shape {
    void draw() {
        System.out.println("Drawing a shape");
    }
}

class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a circle");
    }
}
```

  

---

**2. Multithreading & Concurrency**

  

**2.1. Creating Threads**

```
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running...");
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread t = new MyThread();
        t.start();
    }
}
```

**2.2. Using Runnable Interface**

```
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Thread is running...");
    }
}

public class Main {
    public static void main(String[] args) {
        Thread t = new Thread(new MyRunnable());
        t.start();
    }
}
```

**2.3. Synchronization to Avoid Race Conditions**

```
class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }
}
```

  

---

**3. Java Collections Framework**

  

**3.1. ArrayList (Dynamic Arrays)**

```
import java.util.ArrayList;
ArrayList<String> names = new ArrayList<>();
names.add("Alice");
names.add("Bob");
```

**3.2. HashMap (Key-Value Storage)**

```
import java.util.HashMap;
HashMap<String, Integer> scores = new HashMap<>();
scores.put("Alice", 90);
System.out.println(scores.get("Alice")); // 90
```

**3.3. HashSet (Unique Elements)**

```
import java.util.HashSet;
HashSet<Integer> numbers = new HashSet<>();
numbers.add(10);
numbers.add(20);
```

**3.4. PriorityQueue (Queue with Priority Order)**

```
import java.util.PriorityQueue;
PriorityQueue<Integer> queue = new PriorityQueue<>();
queue.add(5);
queue.add(1);
queue.add(10);
System.out.println(queue.poll()); // 1 (Lowest Priority)
```

  

---

**4. Lambda Expressions & Streams API**

  

**4.1. Lambda Functions**

```
interface MathOperation {
    int operate(int a, int b);
}

public class Main {
    public static void main(String[] args) {
        MathOperation add = (a, b) -> a + b;
        System.out.println(add.operate(5, 3)); // 8
    }
}
```

**4.2. Streams API for Functional Programming**

```
import java.util.Arrays;
import java.util.List;

List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
numbers.stream().filter(n -> n % 2 == 0).forEach(System.out::println);
```

  

---

**5. Database Connectivity with JDBC**

  

**5.1. Connecting to a MySQL Database**

```
import java.sql.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "root", "password");
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT * FROM users");

        while (rs.next()) {
            System.out.println(rs.getString("name"));
        }

        conn.close();
    }
}
```

  

---

**6. Networking & APIs**

  

**6.1. Making HTTP Requests with HttpURLConnection**

```
import java.net.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://jsonplaceholder.typicode.com/posts/1");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");

        BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
        reader.close();
    }
}
```

  

---

**7. Unit Testing with JUnit**

  

**7.1. Writing a JUnit Test**

```
import static org.junit.Assert.*;
import org.junit.Test;

public class CalculatorTest {
    @Test
    public void testAddition() {
        assertEquals(5, Calculator.add(2, 3));
    }
}
```

  

---

**8. Introduction to Spring Boot (Java Web Framework)**

  

**8.1. Creating a Spring Boot API**

```
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class HelloController {
    @GetMapping("/hello")
    public String sayHello() {
        return "Hello, Spring Boot!";
    }
}
```

  

---

**9. Final Project: Building a CRUD API with Spring Boot**

  

**9.1. Define a Model**

```
import javax.persistence.*;

@Entity
public class User {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
}
```

**9.2. Create a Repository**

```
import org.springframework.data.jpa.repository.JpaRepository;
public interface UserRepository extends JpaRepository<User, Long> {}
```

**9.3. Create a REST Controller**

```
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
public class UserController {
    private final UserRepository repository;
    
    public UserController(UserRepository repository) {
        this.repository = repository;
    }

    @GetMapping
    public List<User> getUsers() {
        return repository.findAll();
    }

    @PostMapping
    public User createUser(@RequestBody User user) {
        return repository.save(user);
    }
}
```

  

---

**Conclusion**

  

**What You Learned in Java Level 2:**

  

✅ **Advanced OOP (Encapsulation, Polymorphism, Abstraction)**

✅ **Multithreading & Concurrency (Threads, Synchronization)**

✅ **Java Collections Framework (Lists, Maps, Sets, Queues)**

✅ **Functional Programming (Lambda, Streams API)**

✅ **Database Connectivity with JDBC & MySQL**

✅ **Networking & APIs (Making HTTP Requests)**

✅ **Unit Testing with JUnit**

✅ **Introduction to Spring Boot (Building Web APIs)**

✅ **Built a Full-Stack Java Application**

  

Now, you’re ready for **Java Level 3**, where we explore **Microservices, Cloud Deployment, Advanced Security, and Spring Boot in Depth!** 🚀