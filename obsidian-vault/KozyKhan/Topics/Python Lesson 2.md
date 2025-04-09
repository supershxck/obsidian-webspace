> **March 14th, 2025**  **11:55:23** 
> **Topics:** [[Python Lesson 3]] 
> **Tags:** #
---
> prompt: Lesson 2, Python. Teach all intermediate concepts in simple terms and with examples. By the end of this lesson, all the material for one to be able to be an advanced Python programmer should be available

**Python Crash Course: From Intermediate to Advanced in One Lesson**

  

**Introduction**

  

Now that you have a strong foundation in Python, it’s time to dive into **intermediate** and **advanced** concepts that will help you write efficient, scalable, and professional Python code. By the end of this lesson, you’ll be capable of handling **real-world** applications and preparing for **expert-level Python programming**.

---

**1. Advanced Data Structures**

  

Python offers **powerful built-in data structures** beyond lists and dictionaries.

  

**1.1. Named Tuples**

  

Named tuples make tuples more readable by allowing **attribute-based access**.

```
from collections import namedtuple

Person = namedtuple("Person", ["name", "age"])
alice = Person(name="Alice", age=25)

print(alice.name)  # Alice
print(alice.age)   # 25
```

**1.2. Default Dictionaries**

  

A defaultdict automatically provides a default value for missing keys.

```
from collections import defaultdict

scores = defaultdict(int)
scores["Alice"] += 10  # Default value is 0, then adds 10

print(scores["Alice"])  # 10
print(scores["Bob"])    # 0 (instead of KeyError)
```

**1.3. Deques (Fast Append/Pop)**

```
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)  # Add to the right
queue.appendleft(0)  # Add to the left

print(queue)  # deque([0, 1, 2, 3, 4])

queue.pop()  # Remove from right
queue.popleft()  # Remove from left
```

  

---

**2. Functional Programming in Python**

  

Python supports functional programming with **map, filter, reduce, and lambdas**.

  

**2.1. Map Function**

  

Applies a function to each element in an iterable.

```
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16]
```

**2.2. Filter Function**

  

Filters elements based on a condition.

```
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
```

**2.3. Reduce Function**

  

Performs cumulative operations.

```
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
print(product)  # 24 (1*2*3*4)
```

  

---

**3. Advanced Object-Oriented Programming (OOP)**

  

**3.1. Class Inheritance**

```
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Woof!
```

**3.2. Abstract Classes**

  

Abstract classes enforce method implementation in subclasses.

```
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Engine started!"

my_car = Car()
print(my_car.start_engine())  # Engine started!
```

**3.3. Magic Methods (__str__, __repr__, __len__)**

```
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} - {self.pages} pages"

    def __len__(self):
        return self.pages

book = Book("Python Mastery", 300)
print(book)  # Python Mastery - 300 pages
print(len(book))  # 300
```

  

---

**4. Exception Handling Best Practices**

  

**4.1. Custom Exceptions**

```
class NegativeNumberError(Exception):
    pass

def check_number(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")

try:
    check_number(-5)
except NegativeNumberError as e:
    print(e)
```

  

---

**5. Multithreading and Multiprocessing**

  

**5.1. Multithreading (Concurrency)**

```
import threading

def print_numbers():
    for i in range(5):
        print(i)

t1 = threading.Thread(target=print_numbers)
t1.start()
t1.join()  # Wait for the thread to complete
```

**5.2. Multiprocessing (Parallel Execution)**

```
import multiprocessing

def worker(num):
    print(f"Worker {num}")

if __name__ == "__main__":
    processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(5)]
    
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()
```

  

---

**6. Decorators**

  

Decorators modify functions dynamically.

  

**6.1. Basic Decorator**

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

**6.2. Decorators with Arguments**

```
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()
```

  

---

**7. Generators and Iterators**

  

**7.1. Generator Function**

```
def count_up_to(n):
    for i in range(n):
        yield i

gen = count_up_to(5)
print(next(gen))  # 0
print(next(gen))  # 1
```

**7.2. Custom Iterator**

```
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max:
            raise StopIteration
        self.current += 1
        return self.current

counter = Counter(5)
for num in counter:
    print(num)
```

  

---

**8. Asynchronous Programming**

  

**8.1. Async and Await**

```
import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello!")

asyncio.run(say_hello())
```

  

---

**9. Python Design Patterns**

  

**9.1. Singleton Pattern**

  

Ensures a class has only **one instance**.

```
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # True
```

  

---

**10. Final Project: Web Scraper**

```
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for item in soup.find_all("a", class_="titlelink"):
    print(item.text)
```

  

---

**Conclusion**

  

You’ve now covered **advanced Python concepts**, including:

• **Advanced data structures**

• **Functional programming**

• **OOP & Design Patterns**

• **Concurrency & Parallelism**

• **Async programming**

• **Decorators & Generators**

• **Web scraping & Real-world projects**

  

You’re now **ready to build high-level Python applications** and explore **machine learning, AI, web development, or automation**. 🚀 Keep coding!