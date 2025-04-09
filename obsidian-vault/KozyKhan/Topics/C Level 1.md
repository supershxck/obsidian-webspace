> **March 16th, 2025**  **22:29:54** 
> **Topics:** [[C Level 2]] 
> **Tags:** #CS  
---

**C Programming Level 1: Introduction to C Programming**

  

**Introduction**

  

C is a **powerful, procedural programming language** used for **system programming, embedded systems, operating systems, and high-performance applications**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Setting Up a C Development Environment**

✅ **Basic Syntax (Variables, Data Types, Operators, Input/Output)**

✅ **Control Flow (If-Else, Loops, Switch)**

✅ **Functions & Modular Programming**

✅ **Arrays & Pointers (Introduction)**

✅ **Working with Files**

✅ **Building a Simple C Program**

  

By the end of this lesson, you will be able to **write basic C programs, understand procedural programming, and use file handling in C**.

---

**1. Setting Up a C Development Environment**

  

**1.1. Installing a C Compiler**

  

**Windows**

• Install **MinGW** from [mingw-w64.org](https://www.mingw-w64.org/)

• Install **GCC (GNU Compiler Collection)**

  

**Linux/macOS**

```
sudo apt install gcc        # Debian/Ubuntu
sudo yum install gcc        # Fedora
brew install gcc            # macOS (Homebrew)
```

**1.2. Checking GCC Installation**

```
gcc --version
```

  

---

**2. Writing Your First C Program**

  

**2.1. Hello World Program**

  

Create hello.c:

```
#include <stdio.h>

int main() {
    printf("Hello, C Programming!\n");
    return 0;
}
```

**2.2. Compiling and Running**

```
gcc hello.c -o hello
./hello
```

  

---

**3. Basic Syntax: Variables, Data Types & Operators**

  

**3.1. Declaring Variables**

```
#include <stdio.h>

int main() {
    int age = 25;
    float pi = 3.14;
    char grade = 'A';

    printf("Age: %d\n", age);
    printf("Pi: %.2f\n", pi);
    printf("Grade: %c\n", grade);

    return 0;
}
```

**3.2. Taking User Input**

```
#include <stdio.h>

int main() {
    int age;
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("You entered: %d\n", age);
    
    return 0;
}
```

**3.3. Arithmetic & Logical Operators**

```
#include <stdio.h>

int main() {
    int a = 10, b = 5;
    printf("Sum: %d\n", a + b);
    printf("Product: %d\n", a * b);
    printf("Comparison (a > b): %d\n", a > b);

    return 0;
}
```

  

---

**4. Control Flow: If-Else, Loops, Switch**

  

**4.1. If-Else Statement**

```
#include <stdio.h>

int main() {
    int num = 10;
    if (num > 5)
        printf("Greater than 5\n");
    else
        printf("Less than or equal to 5\n");

    return 0;
}
```

**4.2. For Loop**

```
#include <stdio.h>

int main() {
    for (int i = 1; i <= 5; i++) {
        printf("Iteration %d\n", i);
    }
    return 0;
}
```

**4.3. While Loop**

```
#include <stdio.h>

int main() {
    int count = 0;
    while (count < 3) {
        printf("Count: %d\n", count);
        count++;
    }
    return 0;
}
```

**4.4. Switch Case**

```
#include <stdio.h>

int main() {
    int choice = 2;
    switch (choice) {
        case 1: printf("Option 1 selected\n"); break;
        case 2: printf("Option 2 selected\n"); break;
        default: printf("Invalid option\n");
    }
    return 0;
}
```

  

---

**5. Functions & Modular Programming**

  

**5.1. Writing Functions**

```
#include <stdio.h>

void greet() {
    printf("Hello from a function!\n");
}

int main() {
    greet();
    return 0;
}
```

**5.2. Function with Parameters**

```
#include <stdio.h>

void square(int num) {
    printf("Square: %d\n", num * num);
}

int main() {
    square(5);
    return 0;
}
```

  

---

**6. Arrays & Pointers (Introduction)**

  

**6.1. Arrays**

```
#include <stdio.h>

int main() {
    int numbers[3] = {10, 20, 30};
    printf("First number: %d\n", numbers[0]);
    return 0;
}
```

**6.2. Pointers**

```
#include <stdio.h>

int main() {
    int a = 10;
    int *ptr = &a;

    printf("Value of a: %d\n", a);
    printf("Address of a: %p\n", &a);
    printf("Pointer stores address: %p\n", ptr);
    printf("Value at pointer address: %d\n", *ptr);

    return 0;
}
```

  

---

**7. File Handling**

  

**7.1. Writing to a File**

```
#include <stdio.h>

int main() {
    FILE *file = fopen("output.txt", "w");
    fprintf(file, "Hello, File Handling in C!\n");
    fclose(file);
    return 0;
}
```

**7.2. Reading from a File**

```
#include <stdio.h>

int main() {
    FILE *file = fopen("output.txt", "r");
    char buffer[100];
    fgets(buffer, 100, file);
    printf("File content: %s", buffer);
    fclose(file);
    return 0;
}
```

  

---

**8. Building a Simple C Program**

  

**8.1. A Simple Calculator**

```
#include <stdio.h>

int main() {
    int a, b, choice;
    
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    printf("Choose operation: 1-Add, 2-Subtract: ");
    scanf("%d", &choice);

    if (choice == 1)
        printf("Result: %d\n", a + b);
    else if (choice == 2)
        printf("Result: %d\n", a - b);
    else
        printf("Invalid choice\n");

    return 0;
}
```

Compile and Run:

```
gcc calculator.c -o calculator
./calculator
```

  

---

**9. Conclusion**

  

**What You Learned in C Level 1:**

  

✅ **Setting Up a C Development Environment**

✅ **Basic Syntax (Variables, Data Types, Operators, Input/Output)**

✅ **Control Flow (If-Else, Loops, Switch)**

✅ **Functions & Modular Programming**

✅ **Arrays & Pointers (Introduction)**

✅ **Working with Files**

✅ **Built a Simple C Program**

  

Now, you’re ready for **C Level 2**, where we explore **Advanced Pointers, Memory Management, Data Structures, and System Programming!** 🚀