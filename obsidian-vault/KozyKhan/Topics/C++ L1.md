> **March 14th, 2025**  **12:19:58** 
> **Topics:** [[C++ L2]] 
> **Tags:** #
---

**C++ Lesson 1: From Beginner to Intermediate in One Lesson**

  

**Introduction**

  

C++ is a **powerful, high-performance** programming language used for **game development, system programming, embedded systems, AI, and competitive programming**.

  

By the end of this lesson, you will understand:

1. **Basic C++ Syntax**

2. **Variables, Data Types, and Operators**

3. **Control Flow (If Statements & Loops)**

4. **Functions & Modular Code**

5. **Object-Oriented Programming (OOP)**

6. **Pointers & Memory Management**

7. **File Handling**

8. **Basic Data Structures (Arrays, Vectors, Strings)**

9. **Error Handling & Debugging**

---

**1. Setting Up C++**

  

**1.1. Install a C++ Compiler**

  

You need a compiler to run C++ code. Install:

• **GCC (GNU Compiler Collection)** on Linux/macOS:

```
sudo apt install g++  # Ubuntu/Debian
```

  

• **MinGW (for Windows)** from [mingw-w64.org](https://www.mingw-w64.org/)

• **Visual Studio Code (VS Code) + C++ Extension**

  

**1.2. Writing Your First C++ Program**

  

Create a file **hello.cpp** and write:

```
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

Compile and run:

```
g++ hello.cpp -o hello
./hello
```

  

---

**2. Basic Syntax: Variables, Data Types & Operators**

  

C++ is **statically typed**, meaning **data types must be declared**.

  

**2.1. Data Types**

```
int age = 25;        // Integer
float pi = 3.14;     // Floating point number
char grade = 'A';    // Character
bool isStudent = true;  // Boolean
string name = "Alice";  // String (Requires #include <string>)
```

**2.2. Arithmetic Operators**

```
int a = 10, b = 3;
cout << "Addition: " << (a + b) << endl;  // 13
cout << "Subtraction: " << (a - b) << endl;  // 7
cout << "Multiplication: " << (a * b) << endl;  // 30
cout << "Division: " << (a / b) << endl;  // 3 (Integer division)
cout << "Modulus: " << (a % b) << endl;  // 1 (Remainder)
```

  

---

**3. Control Flow (If Statements & Loops)**

  

**3.1. If-Else Statements**

```
int age = 18;
if (age >= 18) {
    cout << "You are an adult" << endl;
} else {
    cout << "You are a minor" << endl;
}
```

**3.2. Loops**

  

**For Loop**

```
for (int i = 0; i < 5; i++) {
    cout << "Iteration: " << i << endl;
}
```

**While Loop**

```
int count = 0;
while (count < 5) {
    cout << count << endl;
    count++;
}
```

**Do-While Loop**

```
int num = 0;
do {
    cout << "Number: " << num << endl;
    num++;
} while (num < 5);
```

  

---

**4. Functions & Modular Code**

  

**4.1. Defining a Function**

```
#include <iostream>
using namespace std;

void greet(string name) {
    cout << "Hello, " << name << "!" << endl;
}

int main() {
    greet("Alice");
    return 0;
}
```

**4.2. Returning Values**

```
int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(5, 7);
    cout << "Sum: " << result << endl;
    return 0;
}
```

  

---

**5. Object-Oriented Programming (OOP)**

  

C++ supports **classes and objects**.

  

**5.1. Defining a Class**

```
class Car {
public:
    string brand;
    int speed;

    void drive() {
        cout << brand << " is driving at " << speed << " km/h" << endl;
    }
};

int main() {
    Car myCar;
    myCar.brand = "Toyota";
    myCar.speed = 120;
    myCar.drive();
    return 0;
}
```

**5.2. Constructor & Destructor**

```
class Person {
public:
    string name;

    Person(string n) {  // Constructor
        name = n;
    }

    ~Person() {  // Destructor
        cout << "Object Destroyed!" << endl;
    }

    void sayHello() {
        cout << "Hello, my name is " << name << endl;
    }
};

int main() {
    Person p("Alice");
    p.sayHello();
    return 0;
}
```

  

---

**6. Pointers & Memory Management**

  

Pointers store **memory addresses**, essential for **dynamic memory allocation**.

  

**6.1. Using Pointers**

```
int x = 10;
int *ptr = &x;  // Pointer stores the address of x

cout << "Value of x: " << x << endl;
cout << "Address of x: " << ptr << endl;
cout << "Value using pointer: " << *ptr << endl;
```

**6.2. Dynamic Memory Allocation**

```
int *p = new int(42);
cout << "Value: " << *p << endl;
delete p;  // Free allocated memory
```

  

---

**7. File Handling**

  

**7.1. Writing to a File**

```
#include <fstream>
using namespace std;

int main() {
    ofstream file("example.txt");
    file << "Hello, file!" << endl;
    file.close();
    return 0;
}
```

**7.2. Reading from a File**

```
#include <fstream>
using namespace std;

int main() {
    ifstream file("example.txt");
    string line;
    while (getline(file, line)) {
        cout << line << endl;
    }
    file.close();
    return 0;
}
```

  

---

**8. Basic Data Structures**

  

**8.1. Arrays**

```
int numbers[] = {10, 20, 30, 40};
cout << numbers[2] << endl;  // 30
```

**8.2. Vectors (Dynamic Arrays)**

```
#include <vector>
vector<int> nums = {1, 2, 3};
nums.push_back(4);
cout << nums[3] << endl;  // 4
```

**8.3. Strings**

```
#include <string>
string name = "Alice";
cout << name.length() << endl;  // 5
```

  

---

**9. Error Handling & Debugging**

  

**9.1. Try-Catch for Exception Handling**

```
try {
    int x = 10 / 0;  // Division by zero error
} catch (exception &e) {
    cout << "An error occurred!" << endl;
}
```

  

---

**Final Project: Simple Calculator**

```
#include <iostream>
using namespace std;

int main() {
    double num1, num2;
    char op;

    cout << "Enter first number: ";
    cin >> num1;
    cout << "Enter operator (+, -, *, /): ";
    cin >> op;
    cout << "Enter second number: ";
    cin >> num2;

    switch (op) {
        case '+': cout << "Result: " << num1 + num2; break;
        case '-': cout << "Result: " << num1 - num2; break;
        case '*': cout << "Result: " << num1 * num2; break;
        case '/': cout << "Result: " << num1 / num2; break;
        default: cout << "Invalid operator!";
    }
    return 0;
}
```

  

---

**Conclusion**

  

**What You Learned:**

  

✅ **Basic Syntax, Variables & Data Types**

✅ **Control Flow (If-Else, Loops)**

✅ **Functions & OOP (Classes, Objects, Pointers)**

✅ **Memory Management & File Handling**

✅ **Basic Data Structures (Arrays, Vectors, Strings)**

  

Now, you’re ready to **start C++ Level 2**, where we explore **STL, Multithreading, and Advanced OOP Concepts!** 🚀