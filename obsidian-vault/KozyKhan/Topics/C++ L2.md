> **March 14th, 2025**  **12:20:11** 
> **Topics:** [[C++ L3]] 
> **Tags:** #
---

**C++ Level 2: Intermediate to Advanced Mastery**

  

**Introduction**

  

Now that you understand the **basics of C++**, it’s time to explore **intermediate and advanced topics**, including:

• **Standard Template Library (STL)**

• **Advanced OOP (Inheritance, Polymorphism, Virtual Functions)**

• **Multithreading & Parallel Programming**

• **Exception Handling & Debugging**

• **Memory Management (Smart Pointers, Stack vs Heap)**

• **File Handling (Binary Files, Streams)**

• **Advanced Data Structures (Maps, Sets, Stacks, Queues)**

• **Algorithm Optimization & Time Complexity**

  

By the end of this lesson, you’ll be able to **write efficient, scalable, and high-performance C++ applications**.

---

**1. Standard Template Library (STL)**

  

The **STL** provides **generic algorithms and data structures** for **efficiency and simplicity**.

  

**1.1. Vectors (Dynamic Arrays)**

```
#include <vector>
#include <iostream>
using namespace std;

int main() {
    vector<int> nums = {10, 20, 30};
    nums.push_back(40);
    
    for (int num : nums) {
        cout << num << " ";
    }
    return 0;
}
```

**1.2. Sets (Unique Elements)**

```
#include <set>
set<int> s = {3, 1, 4, 1, 2};
s.insert(5);
cout << s.size(); // 5
```

**1.3. Maps (Key-Value Pairs)**

```
#include <map>
map<string, int> ages;
ages["Alice"] = 25;
ages["Bob"] = 30;
cout << ages["Alice"]; // 25
```

  

---

**2. Advanced Object-Oriented Programming (OOP)**

  

**2.1. Inheritance**

```
class Animal {
public:
    void eat() { cout << "Eating...\n"; }
};

class Dog : public Animal {
public:
    void bark() { cout << "Woof!\n"; }
};

int main() {
    Dog d;
    d.eat();  // Inherited method
    d.bark(); // Dog-specific method
}
```

**2.2. Polymorphism & Virtual Functions**

```
class Animal {
public:
    virtual void makeSound() { cout << "Animal Sound\n"; }
};

class Dog : public Animal {
public:
    void makeSound() override { cout << "Bark!\n"; }
};

int main() {
    Animal* a = new Dog();
    a->makeSound(); // "Bark!" (Runtime Polymorphism)
    delete a;
}
```

**2.3. Abstract Classes**

```
class Shape {
public:
    virtual void draw() = 0;  // Pure virtual function
};

class Circle : public Shape {
public:
    void draw() override { cout << "Drawing Circle\n"; }
};
```

  

---

**3. Multithreading & Parallel Programming**

  

**3.1. Creating Threads**

```
#include <thread>
void printHello() {
    cout << "Hello from thread!" << endl;
}

int main() {
    thread t(printHello);
    t.join();  // Wait for the thread to finish
}
```

**3.2. Mutex for Thread Safety**

```
#include <mutex>
mutex mtx;

void safeFunction() {
    mtx.lock();
    cout << "Thread-Safe Code\n";
    mtx.unlock();
}
```

  

---

**4. Exception Handling & Debugging**

  

**4.1. Using Try-Catch**

```
try {
    int x = 10 / 0;
} catch (exception& e) {
    cout << "Error: " << e.what() << endl;
}
```

  

---

**5. Memory Management (Smart Pointers)**

  

**5.1. Unique Pointer**

```
#include <memory>
unique_ptr<int> p(new int(10));
cout << *p;
```

**5.2. Shared Pointer**

```
#include <memory>
shared_ptr<int> sp1 = make_shared<int>(10);
shared_ptr<int> sp2 = sp1;  // Reference count increases
```

  

---

**6. Advanced File Handling**

  

**6.1. Writing to Binary Files**

```
#include <fstream>
ofstream file("data.bin", ios::binary);
int num = 100;
file.write(reinterpret_cast<char*>(&num), sizeof(num));
file.close();
```

**6.2. Reading from Binary Files**

```
ifstream file("data.bin", ios::binary);
int num;
file.read(reinterpret_cast<char*>(&num), sizeof(num));
cout << num;
file.close();
```

  

---

**7. Advanced Data Structures**

  

**7.1. Stack (LIFO)**

```
#include <stack>
stack<int> s;
s.push(10);
s.push(20);
cout << s.top(); // 20
```

**7.2. Queue (FIFO)**

```
#include <queue>
queue<int> q;
q.push(1);
q.push(2);
cout << q.front(); // 1
```

  

---

**8. Algorithm Optimization & Time Complexity**

  

**8.1. Sorting with STL**

```
#include <algorithm>
vector<int> v = {3, 1, 4, 1, 5};
sort(v.begin(), v.end());
```

**8.2. Binary Search**

```
if (binary_search(v.begin(), v.end(), 4)) {
    cout << "Found!";
}
```

  

---

**Final Project: Multithreaded Task Manager**

```
#include <iostream>
#include <thread>
#include <vector>
using namespace std;

void task(int id) {
    cout << "Task " << id << " is running\n";
}

int main() {
    vector<thread> threads;
    
    for (int i = 0; i < 5; i++) {
        threads.push_back(thread(task, i));
    }
    
    for (auto &t : threads) {
        t.join();
    }
    
    return 0;
}
```

  

---

**Conclusion**

  

**What You Learned in C++ Level 2:**

  

✅ **STL (Vectors, Maps, Sets, Queues, Stacks)**

✅ **Advanced OOP (Inheritance, Polymorphism, Virtual Functions, Abstract Classes)**

✅ **Multithreading (Threads, Mutex, Parallelism)**

✅ **Memory Management (Smart Pointers, Heap vs Stack)**

✅ **Binary File Handling (Streams, Serialization)**

✅ **Algorithm Optimization (Sorting, Searching, Time Complexity)**

  

Now, you are ready for **C++ Level 3**, where we explore **Design Patterns, Network Programming, Advanced Data Structures, and Game Development**. 🚀