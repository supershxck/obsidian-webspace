> **February 8th, 2025**  **14:50:18** 
> **Topics:** [[
> **Tags:** #
---

**Java Basics: Introduction to Java Programming**

  

**1. What is Java?**

  

Java is a **high-level, object-oriented, platform-independent programming language** developed by **Sun Microsystems (now owned by Oracle)**. It follows the **“Write Once, Run Anywhere” (WORA)** principle, meaning Java programs can run on any platform that supports Java **without modification**.

  

**Why Use Java?**

  

✔ **Platform-independent** – Runs on any OS with Java Virtual Machine (JVM).

✔ **Object-Oriented** – Uses classes and objects for modular programming.

✔ **Secure and Reliable** – Provides strong memory management and security.

✔ **Multi-threaded** – Supports concurrent execution of multiple tasks.

✔ **Rich API & Libraries** – Includes built-in support for data structures, networking, and more.

**2. Java Program Structure**

  

A basic Java program consists of:

1. **Class Declaration** – Java programs are organized into **classes**.

2. **Main Method (main())** – The **entry point** of a Java program.

3. **Statements** – Instructions inside the main method.

  

✔ **Example: Hello World Program in Java**

```
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

✔ **Explanation:**

• public class HelloWorld – Declares a class named HelloWorld.

• public static void main(String[] args) – Main method, where execution starts.

• System.out.println("Hello, World!"); – Prints text to the console.

**3. Java Data Types**

  

Java has **two categories** of data types:

  

**1. Primitive Data Types (Built-in)**

|**Data Type**|**Size**|**Example**|
|---|---|---|
|byte|1 byte|byte age = 25;|
|short|2 bytes|short year = 2024;|
|int|4 bytes|int salary = 50000;|
|long|8 bytes|long distance = 1000000L;|
|float|4 bytes|float price = 19.99f;|
|double|8 bytes|double pi = 3.14159;|
|char|2 bytes|char grade = 'A';|
|boolean|1 bit|boolean isJavaFun = true;|

✔ **Example: Declaring Variables**

```
int age = 25;
double price = 99.99;
boolean isAvailable = true;
```

**2. Non-Primitive Data Types (Reference Types)**

• **Strings** – String message = "Hello";

• **Arrays** – int[] numbers = {1, 2, 3};

• **Classes & Objects** – Custom types created using classes.

  

✔ **Example: Using Strings**

```
String name = "Java";
System.out.println("Welcome to " + name);
```

**4. Java Operators**

  

Java provides **arithmetic, logical, and relational operators**.

  

✔ **Example: Arithmetic Operators**

```
int a = 10, b = 5;
System.out.println(a + b); // Addition
System.out.println(a - b); // Subtraction
System.out.println(a * b); // Multiplication
System.out.println(a / b); // Division
System.out.println(a % b); // Modulus
```

✔ **Example: Relational Operators**

```
System.out.println(a > b);  // true
System.out.println(a == b); // false
System.out.println(a != b); // true
```

✔ **Example: Logical Operators**

```
boolean x = true, y = false;
System.out.println(x && y); // false
System.out.println(x || y); // true
System.out.println(!x);     // false
```

**5. Control Statements in Java**

  

Java supports **decision-making (if-else, switch)** and **loops (for, while, do-while)**.

  

✔ **Example: If-Else Statement**

```
int num = 10;
if (num > 0) {
    System.out.println("Positive number");
} else {
    System.out.println("Negative number");
}
```

✔ **Example: Switch Statement**

```
int day = 3;
switch(day) {
    case 1: System.out.println("Monday"); break;
    case 2: System.out.println("Tuesday"); break;
    default: System.out.println("Other day");
}
```

✔ **Example: For Loop**

```
for (int i = 1; i <= 5; i++) {
    System.out.println("Iteration " + i);
}
```

✔ **Example: While Loop**

```
int i = 1;
while (i <= 5) {
    System.out.println(i);
    i++;
}
```

✔ **Example: Do-While Loop**

```
int i = 1;
do {
    System.out.println(i);
    i++;
} while (i <= 5);
```

**6. Functions (Methods) in Java**

  

Methods **encapsulate reusable logic**.

  

✔ **Example: Method Declaration and Calling**

```
public class MathOperations {
    static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int sum = add(10, 5);
        System.out.println("Sum: " + sum);
    }
}
```

✔ **Explanation:**

• static int add(int a, int b) – Defines a method named add.

• return a + b; – Returns the sum.

• add(10, 5); – Calls the method.

**7. Object-Oriented Programming (OOP) in Java**

  

Java follows **OOP principles**:

• **Encapsulation** – Data hiding using private modifiers.

• **Inheritance** – Reusing parent class properties (extends keyword).

• **Polymorphism** – Using methods in multiple ways.

• **Abstraction** – Hiding implementation details using abstract classes or interfaces.

  

✔ **Example: Creating a Class and Object**

```
class Car {
    String brand;
    
    Car(String brand) {
        this.brand = brand;
    }

    void showBrand() {
        System.out.println("Car Brand: " + brand);
    }
}

public class Main {
    public static void main(String[] args) {
        Car myCar = new Car("Tesla");
        myCar.showBrand();
    }
}
```

✔ **Explanation:**

• Car is a **class**.

• brand is an **instance variable**.

• Car("Tesla") initializes the object.

• showBrand() prints the brand.

**8. Exception Handling in Java**

  

Java provides **try-catch blocks** for handling errors.

  

✔ **Example: Handling Exceptions**

```
try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero!");
}
```

✔ **Explanation:**

• Code inside try block may cause an exception.

• catch block handles the error.

**9. Java File Handling**

  

Java supports **reading and writing files**.

  

✔ **Example: Writing to a File**

```
import java.io.FileWriter;
import java.io.IOException;

public class FileExample {
    public static void main(String[] args) {
        try {
            FileWriter writer = new FileWriter("output.txt");
            writer.write("Hello, Java!");
            writer.close();
            System.out.println("File written successfully.");
        } catch (IOException e) {
            System.out.println("An error occurred.");
        }
    }
}
```

**10. Conclusion**

  

Java is a **powerful, object-oriented, and platform-independent** language used in **web, mobile, and enterprise applications**. Understanding **data types, control structures, OOP concepts, and file handling** provides a strong foundation for **building scalable Java applications**. 🚀