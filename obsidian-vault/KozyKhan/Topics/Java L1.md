> **March 14th, 2025**  **18:24:18** 
> **Topics:** [[Java L2]] 
> **Tags:** #CS 
---

**Java Level 1: From Beginner to Intermediate in One Lesson**

  

**Introduction**

  

Java is one of the most widely used **object-oriented programming (OOP) languages**, powering **web applications, enterprise software, Android apps, and backend systems**. In this lesson, you’ll learn:

✅ **Java Basics** (Syntax, Variables, Data Types, Operators)

✅ **Control Flow (If-Else, Loops)**

✅ **Methods & Functions**

✅ **Object-Oriented Programming (Classes, Objects, Inheritance)**

✅ **Exception Handling & Debugging**

✅ **File Handling (Reading/Writing Files)**

✅ **Basic Data Structures (Arrays, Lists, Maps)**

✅ **Introduction to Multi-threading**

✅ **Building a Simple Java Application**

  

By the end of this lesson, you will be able to **write Java programs confidently**.

---

**1. Setting Up Java**

  

**1.1. Installing Java (JDK)**

  

Download and install **Java Development Kit (JDK)** from [Oracle JDK](https://www.oracle.com/java/technologies/javase-jdk17-downloads.html) or use [OpenJDK](https://openjdk.org/).

  

**1.2. Writing Your First Java Program**

  

Create a file **HelloWorld.java** and write:

```
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Compile and run:

```
javac HelloWorld.java
java HelloWorld
```

  

---

**2. Java Basics: Variables, Data Types & Operators**

  

**2.1. Variables & Data Types**

```
int age = 25;          // Integer
double pi = 3.14;      // Floating point number
char grade = 'A';      // Character
boolean isStudent = true;  // Boolean
String name = "Alice"; // String
```

**2.2. Operators**

```
int a = 10, b = 3;
System.out.println(a + b); // Addition
System.out.println(a - b); // Subtraction
System.out.println(a * b); // Multiplication
System.out.println(a / b); // Division
System.out.println(a % b); // Modulus (Remainder)
```

  

---

**3. Control Flow (If-Else, Loops)**

  

**3.1. If-Else Statement**

```
int age = 18;
if (age >= 18) {
    System.out.println("You are an adult.");
} else {
    System.out.println("You are a minor.");
}
```

**3.2. Loops**

  

**For Loop**

```
for (int i = 0; i < 5; i++) {
    System.out.println("Iteration: " + i);
}
```

**While Loop**

```
int count = 0;
while (count < 5) {
    System.out.println(count);
    count++;
}
```

**Do-While Loop**

```
int num = 0;
do {
    System.out.println("Number: " + num);
    num++;
} while (num < 5);
```

  

---

**4. Methods & Functions**

  

**4.1. Defining a Method**

```
public class Main {
    public static void greet(String name) {
        System.out.println("Hello, " + name);
    }

    public static void main(String[] args) {
        greet("Alice");
    }
}
```

**4.2. Returning Values**

```
public class Calculator {
    public static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int result = add(5, 7);
        System.out.println("Sum: " + result);
    }
}
```

  

---

**5. Object-Oriented Programming (OOP)**

  

Java is **object-oriented**, meaning everything revolves around **classes and objects**.

  

**5.1. Defining a Class & Creating an Object**

```
class Car {
    String brand;
    int speed;

    void drive() {
        System.out.println(brand + " is driving at " + speed + " km/h");
    }
}

public class Main {
    public static void main(String[] args) {
        Car myCar = new Car();
        myCar.brand = "Toyota";
        myCar.speed = 120;
        myCar.drive();
    }
}
```

**5.2. Constructor & Destructor**

```
class Person {
    String name;

    // Constructor
    public Person(String name) {
        this.name = name;
    }

    // Method
    public void greet() {
        System.out.println("Hello, my name is " + name);
    }
}

public class Main {
    public static void main(String[] args) {
        Person p = new Person("Alice");
        p.greet();
    }
}
```

**5.3. Inheritance**

```
class Animal {
    void speak() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    void speak() {
        System.out.println("Woof!");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.speak();
    }
}
```

  

---

**6. Exception Handling & Debugging**

  

**6.1. Try-Catch for Handling Errors**

```
public class Main {
    public static void main(String[] args) {
        try {
            int result = 10 / 0; // Division by zero error
        } catch (ArithmeticException e) {
            System.out.println("Error: Cannot divide by zero");
        }
    }
}
```

  

---

**7. File Handling (Reading/Writing Files)**

  

**7.1. Writing to a File**

```
import java.io.FileWriter;
import java.io.IOException;

public class FileExample {
    public static void main(String[] args) {
        try {
            FileWriter file = new FileWriter("example.txt");
            file.write("Hello, file!");
            file.close();
        } catch (IOException e) {
            System.out.println("An error occurred.");
        }
    }
}
```

**7.2. Reading from a File**

```
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FileExample {
    public static void main(String[] args) {
        try {
            File file = new File("example.txt");
            Scanner reader = new Scanner(file);
            while (reader.hasNextLine()) {
                System.out.println(reader.nextLine());
            }
            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        }
    }
}
```

  

---

**8. Basic Data Structures**

  

**8.1. Arrays**

```
int[] numbers = {10, 20, 30, 40};
System.out.println(numbers[2]); // 30
```

**8.2. ArrayList (Dynamic Array)**

```
import java.util.ArrayList;
ArrayList<String> names = new ArrayList<>();
names.add("Alice");
names.add("Bob");
System.out.println(names.get(0)); // Alice
```

**8.3. HashMap (Key-Value Pairs)**

```
import java.util.HashMap;
HashMap<String, Integer> scores = new HashMap<>();
scores.put("Alice", 90);
System.out.println(scores.get("Alice")); // 90
```

  

---

**9. Introduction to Multi-threading**

  

**9.1. Creating a Thread**

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

  

---

**Final Project: Simple Calculator**

```
import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number: ");
        double num1 = scanner.nextDouble();

        System.out.print("Enter operator (+, -, *, /): ");
        char op = scanner.next().charAt(0);

        System.out.print("Enter second number: ");
        double num2 = scanner.nextDouble();

        switch (op) {
            case '+': System.out.println("Result: " + (num1 + num2)); break;
            case '-': System.out.println("Result: " + (num1 - num2)); break;
            case '*': System.out.println("Result: " + (num1 * num2)); break;
            case '/': System.out.println("Result: " + (num1 / num2)); break;
            default: System.out.println("Invalid operator!");
        }
    }
}
```

  

---

**Next Steps**

  

✅ **Mastered Java Basics**

✅ **Learned Object-Oriented Programming (OOP)**

✅ **Worked with File Handling & Data Structures**

✅ **Built a Simple Java Application**

  

Now, you’re ready for **Java Level 2**, where we explore **Advanced OOP, Concurrency, Database Integration, and Web Development with Spring Boot!** 🚀