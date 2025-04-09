> **March 14th, 2025**  **11:53:13** 
> **Topics:** [[Python Lesson 2]] 
> **Tags:** #
---
> prompt: Lesson 1, [[Python]]. Teach all the basics in simple terms and with examples. By the end of this lesson, all the material for one to become an intermediate Python programmer should be delivered.


**Python Crash Course: From Beginner to Intermediate in One Lesson**

  

**Introduction**

  

Python is a powerful, high-level programming language known for its simplicity and readability. It is widely used in web development, data science, artificial intelligence, automation, and more. In this lesson, you’ll learn all the fundamentals to get started with Python and advance to an intermediate level.

---

**1. Setting Up Python**

  

**Installing Python**

1. Download and install Python from [python.org](https://www.python.org/).

2. Verify installation:

• Open the terminal (Command Prompt on Windows) and type:

```
python --version
```

  

1. Open Python in interactive mode by typing python or use an Integrated Development Environment (IDE) like VS Code, PyCharm, or Jupyter Notebook.

---

**2. Python Syntax and Basic Operations**

  

**Printing Output**

```
print("Hello, World!")
```

**Variables and Data Types**

  

Python automatically assigns data types:

```
x = 10      # Integer
y = 3.14    # Float
name = "Alice"  # String
is_active = True  # Boolean
```

**Basic Math Operations**

```
a = 10 + 5  # Addition
b = 10 - 5  # Subtraction
c = 10 * 5  # Multiplication
d = 10 / 3  # Division (returns float)
e = 10 // 3  # Floor Division (returns integer)
f = 10 % 3  # Modulus (remainder)
g = 2 ** 3  # Exponentiation (2^3 = 8)
```

  

---

**3. Control Flow: Conditions and Loops**

  

**If-Else Statements**

```
age = 18

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

**Loops**

  

**For Loop**

```
for i in range(5):  # Loops from 0 to 4
    print(i)
```

**While Loop**

```
count = 0
while count < 5:
    print(count)
    count += 1
```

**Loop Control Statements**

```
for i in range(10):
    if i == 5:
        break  # Stops the loop at 5
    if i == 2:
        continue  # Skips 2
    print(i)
```

  

---

**4. Data Structures**

  

**Lists (Arrays)**

```
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add item
fruits.remove("banana")  # Remove item
print(fruits[0])  # Access first element
```

**Tuples (Immutable Lists)**

```
coordinates = (10, 20)
print(coordinates[0])  # Access first element
```

**Dictionaries (Key-Value Pairs)**

```
person = {"name": "Alice", "age": 25}
print(person["name"])  # Get value by key
person["city"] = "New York"  # Add new key-value pair
```

**Sets (Unique Unordered Elements)**

```
unique_numbers = {1, 2, 3, 3, 2, 1}
print(unique_numbers)  # {1, 2, 3}
```

  

---

**5. Functions and Modular Code**

  

**Defining Functions**

```
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

**Lambda Functions (Short Anonymous Functions)**

```
square = lambda x: x ** 2
print(square(5))  # 25
```

**Importing Modules**

```
import math
print(math.sqrt(16))  # 4.0
```

  

---

**6. Object-Oriented Programming (OOP)**

  

**Defining a Class**

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

alice = Person("Alice", 25)
print(alice.greet())
```

  

---

**7. File Handling**

  

**Reading Files**

```
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

**Writing to Files**

```
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.")
```

  

---

**8. Exception Handling (Error Handling)**

```
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input, enter a number.")
finally:
    print("Execution finished.")
```

  

---

**9. Working with External Libraries**

  

**Installing Libraries**

```
pip install requests
```

**Using External Libraries**

```
import requests
response = requests.get("https://api.github.com")
print(response.json())  # Print API response
```

  

---

**10. Intermediate Topics**

  

**List Comprehensions**

```
squares = [x ** 2 for x in range(10)]
print(squares)
```

**Dictionary Comprehensions**

```
squared_numbers = {x: x ** 2 for x in range(5)}
print(squared_numbers)
```

**Decorators**

```
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
```

**Generators**

```
def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))  # 0
print(next(gen))  # 1
```

  

---

**11. Final Project: Simple To-Do App**

```
tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    action = input("Enter 'add' to add task, 'show' to see tasks, 'exit' to quit: ")
    if action == "add":
        task = input("Enter task: ")
        add_task(task)
    elif action == "show":
        show_tasks()
    elif action == "exit":
        break
```

  

---

**Conclusion**

  

You’ve learned:

1. **Basic Syntax** – Variables, data types, operators.

2. **Control Flow** – If statements, loops.

3. **Data Structures** – Lists, tuples, dictionaries, sets.

4. **Functions & OOP** – Writing functions, classes, and methods.

5. **File Handling** – Reading and writing files.

6. **Error Handling** – Try-except for debugging.

7. **Intermediate Topics** – List comprehensions, decorators, generators.

8. **External Libraries** – Installing and using third-party modules.

9. **Final Project** – Building a simple interactive to-do list.

  

Now, you can start working on real projects and deepen your Python knowledge. Keep coding! 🚀