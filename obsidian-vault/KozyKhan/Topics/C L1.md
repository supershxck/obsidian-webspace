> **March 15th, 2025**  **18:58:32** 
> **Topics:** [[C L2]] 
> **Tags:** #CS 
---

**C# Level 1: Introduction to C# Programming**

  

**Introduction**

  

C# is a **modern, object-oriented programming language** developed by Microsoft. It is widely used for **desktop applications, web development (ASP.NET), game development (Unity), and cloud applications**.

  

**What You’ll Learn in This Lesson:**

  

✅ **C# Basics (Syntax, Variables, Data Types, Operators)**

✅ **Control Flow (If-Else, Loops, Switch Statements)**

✅ **Methods & Parameters**

✅ **Object-Oriented Programming (Classes, Structs, Inheritance)**

✅ **Collections (Lists, Dictionaries, Arrays)**

✅ **Exception Handling**

✅ **File Handling (Reading & Writing Files)**

✅ **Building a Simple Console Application**

  

By the end of this lesson, you will be able to **write basic C# programs, understand OOP, and interact with files**.

---

**1. Setting Up C#**

  

**1.1. Installing C# & .NET SDK**

• Download and install **.NET SDK** from [dotnet.microsoft.com](https://dotnet.microsoft.com/download).

• Verify installation:

```
dotnet --version
```

  

  

**1.2. Running C# Code**

• **Run a C# script**:

```
dotnet run Program.cs
```

  

• **Compile & Execute**:

```
dotnet build
dotnet run
```

  

---

**2. C# Basics: Variables, Data Types & Operators**

  

**2.1. Variables & Constants**

```
using System;

class Program {
    static void Main() {
        int age = 25;
        string name = "Alice";
        const double PI = 3.1415; // Constant (Immutable)
        Console.WriteLine($"{name} is {age} years old.");
    }
}
```

**2.2. Data Types**

```
class Program {
    static void Main() {
        int number = 42;       // Integer
        double pi = 3.14;       // Floating-point number
        bool isCSharpAwesome = true; // Boolean
        char letter = 'C';      // Character
        string message = "Hello, C#!"; // String
        Console.WriteLine($"{number}, {pi}, {isCSharpAwesome}, {letter}, {message}");
    }
}
```

**2.3. Operators**

```
class Program {
    static void Main() {
        int a = 10, b = 3;
        Console.WriteLine("Sum: " + (a + b));
        Console.WriteLine("Diff: " + (a - b));
        Console.WriteLine("Product: " + (a * b));
        Console.WriteLine("Quotient: " + (a / b));
        Console.WriteLine("Remainder: " + (a % b));
    }
}
```

  

---

**3. Control Flow (If-Else, Loops, Switch)**

  

**3.1. If-Else Statement**

```
class Program {
    static void Main() {
        int temp = 30;
        if (temp > 25) {
            Console.WriteLine("It's hot outside!");
        } else {
            Console.WriteLine("It's cool outside.");
        }
    }
}
```

**3.2. For Loop**

```
class Program {
    static void Main() {
        for (int i = 1; i <= 5; i++) {
            Console.WriteLine("Iteration " + i);
        }
    }
}
```

**3.3. While Loop**

```
class Program {
    static void Main() {
        int count = 0;
        while (count < 3) {
            Console.WriteLine("Count: " + count);
            count++;
        }
    }
}
```

**3.4. Switch Statement**

```
class Program {
    static void Main() {
        string day = "Monday";
        switch (day) {
            case "Monday":
                Console.WriteLine("Start of the week!");
                break;
            case "Friday":
                Console.WriteLine("Weekend is coming!");
                break;
            default:
                Console.WriteLine("A regular day.");
                break;
        }
    }
}
```

  

---

**4. Methods & Parameters**

  

**4.1. Defining a Method**

```
class Program {
    static string Greet(string name) {
        return "Hello, " + name + "!";
    }

    static void Main() {
        Console.WriteLine(Greet("Alice"));
    }
}
```

**4.2. Method with Multiple Parameters**

```
class Program {
    static int Add(int a, int b) {
        return a + b;
    }

    static void Main() {
        Console.WriteLine(Add(5, 3)); // Output: 8
    }
}
```

  

---

**5. Object-Oriented Programming (OOP)**

  

**5.1. Creating a Class & Object**

```
class Car {
    public string Brand;
    public int Speed;

    public void Drive() {
        Console.WriteLine(Brand + " is driving at " + Speed + " km/h");
    }
}

class Program {
    static void Main() {
        Car myCar = new Car { Brand = "Tesla", Speed = 120 };
        myCar.Drive();
    }
}
```

**5.2. Inheritance**

```
class Animal {
    public virtual void Speak() {
        Console.WriteLine("Animal makes a sound");
    }
}

class Dog : Animal {
    public override void Speak() {
        Console.WriteLine("Woof!");
    }
}

class Program {
    static void Main() {
        Dog myDog = new Dog();
        myDog.Speak();
    }
}
```

  

---

**6. Collections (Lists, Dictionaries, Arrays)**

  

**6.1. Arrays**

```
class Program {
    static void Main() {
        string[] fruits = { "Apple", "Banana", "Cherry" };
        Console.WriteLine(fruits[1]); // Banana
    }
}
```

**6.2. Lists**

```
using System;
using System.Collections.Generic;

class Program {
    static void Main() {
        List<string> names = new List<string> { "Alice", "Bob", "Charlie" };
        names.Add("David");
        Console.WriteLine(names[2]); // Charlie
    }
}
```

**6.3. Dictionaries**

```
using System;
using System.Collections.Generic;

class Program {
    static void Main() {
        Dictionary<string, int> scores = new Dictionary<string, int> {
            { "Alice", 90 },
            { "Bob", 85 }
        };
        Console.WriteLine(scores["Alice"]); // 90
    }
}
```

  

---

**7. Exception Handling**

```
class Program {
    static void Main() {
        try {
            int result = 10 / 0;
        } catch (DivideByZeroException e) {
            Console.WriteLine("Error: " + e.Message);
        }
    }
}
```

  

---

**8. File Handling (Reading & Writing Files)**

  

**8.1. Writing to a File**

```
using System.IO;

class Program {
    static void Main() {
        File.WriteAllText("output.txt", "Hello, C#!");
    }
}
```

**8.2. Reading from a File**

```
using System;
using System.IO;

class Program {
    static void Main() {
        string content = File.ReadAllText("output.txt");
        Console.WriteLine(content);
    }
}
```

  

---

**9. Building a Simple Console Application**

```
using System;

class Program {
    static void Main() {
        Console.Write("Enter your name: ");
        string name = Console.ReadLine();
        Console.WriteLine("Hello, " + name + "!");
    }
}
```

  

---

**Conclusion**

  

**What You Learned in C# Level 1:**

  

✅ **C# Basics (Syntax, Variables, Data Types, Operators)**

✅ **Control Flow (If-Else, Loops, Switch Statements)**

✅ **Methods & Parameters**

✅ **Object-Oriented Programming (Classes, Structs, Inheritance)**

✅ **Collections (Lists, Dictionaries, Arrays)**

✅ **Exception Handling**

✅ **File Handling (Reading & Writing Files)**

✅ **Built a Simple Console Application**

  

Now, you’re ready for **C# Level 2**, where we explore **LINQ, Asynchronous Programming, Web Development with ASP.NET, and Entity Framework!** 🚀