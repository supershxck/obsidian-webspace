> **March 14th, 2025**  **18:14:46** 
> **Topics:** [[JavaScript L1]] 
> **Tags:** #
---

**C++ Level 3: Mastering Advanced C++ Concepts**

  

**Introduction**

  

In **C++ Level 3**, we explore **high-performance programming**, covering:

• **Design Patterns (Singleton, Factory, Observer, etc.)**

• **Templates & Metaprogramming**

• **Advanced Multithreading (Locks, Condition Variables, Atomic Operations)**

• **Networking (Sockets & HTTP Requests in C++)**

• **Advanced Data Structures (Graph, Trie, Hash Table, etc.)**

• **Game Development & Graphics (SFML, OpenGL Basics)**

• **C++ and AI (Neural Networks, Machine Learning Basics)**

  

By the end of this lesson, you will be capable of building **real-world applications in system programming, AI, game development, and networking**.

---

**1. Design Patterns in C++**

  

Design patterns are **proven architectural solutions** for common programming problems.

  

**1.1. Singleton Pattern (Ensures a Class Has Only One Instance)**

```
class Singleton {
private:
    static Singleton* instance;
    Singleton() {} // Private constructor

public:
    static Singleton* getInstance() {
        if (!instance) instance = new Singleton();
        return instance;
    }
};
Singleton* Singleton::instance = nullptr;
```

**1.2. Factory Pattern (Creates Objects Without Specifying Exact Class)**

```
class Animal {
public:
    virtual void speak() = 0;
};
class Dog : public Animal {
public:
    void speak() override { cout << "Woof!" << endl; }
};
class AnimalFactory {
public:
    static Animal* createAnimal() {
        return new Dog();
    }
};
```

**1.3. Observer Pattern (Event-Driven Programming)**

```
#include <vector>
class Observer {
public:
    virtual void notify() = 0;
};
class Subject {
private:
    vector<Observer*> observers;
public:
    void addObserver(Observer* obs) { observers.push_back(obs); }
    void notifyAll() { for (auto obs : observers) obs->notify(); }
};
class ConcreteObserver : public Observer {
public:
    void notify() override { cout << "Notification received!" << endl; }
};
```

  

---

**2. Templates & Metaprogramming**

  

**2.1. Function Templates**

```
template <typename T>
T add(T a, T b) { return a + b; }

cout << add(5, 10);  // 15
cout << add(5.5, 2.2);  // 7.7
```

**2.2. Class Templates**

```
template <typename T>
class Box {
public:
    T value;
    Box(T val) : value(val) {}
};
Box<int> intBox(10);
Box<string> strBox("Hello");
```

  

---

**3. Advanced Multithreading**

  

**3.1. Lock Guard (Avoid Deadlocks)**

```
#include <mutex>
mutex mtx;
void safeFunction() {
    lock_guard<mutex> lock(mtx);
    cout << "Safe execution" << endl;
}
```

**3.2. Condition Variables (Thread Synchronization)**

```
#include <condition_variable>
mutex mtx;
condition_variable cv;
bool ready = false;

void printMessage() {
    unique_lock<mutex> lock(mtx);
    cv.wait(lock, [] { return ready; });
    cout << "Message printed!" << endl;
}

int main() {
    thread t(printMessage);
    this_thread::sleep_for(chrono::seconds(1));
    ready = true;
    cv.notify_one();
    t.join();
}
```

**3.3. Atomic Operations (Avoid Race Conditions)**

```
#include <atomic>
atomic<int> counter(0);
void increment() { counter++; }
```

  

---

**4. Networking in C++**

  

**4.1. Socket Programming (TCP Server)**

```
#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
using namespace std;

int main() {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    sockaddr_in address = {AF_INET, htons(8080), INADDR_ANY};
    bind(server_fd, (struct sockaddr*)&address, sizeof(address));
    listen(server_fd, 3);
    
    int client_fd = accept(server_fd, nullptr, nullptr);
    send(client_fd, "Hello, Client!", 14, 0);
    close(client_fd);
}
```

**4.2. HTTP Request with C++**

```
#include <curl/curl.h>
CURL* curl = curl_easy_init();
curl_easy_setopt(curl, CURLOPT_URL, "https://example.com");
curl_easy_perform(curl);
curl_easy_cleanup(curl);
```

  

---

**5. Advanced Data Structures**

  

**5.1. Graph Implementation (Adjacency List)**

```
#include <vector>
vector<int> graph[100];

void addEdge(int u, int v) {
    graph[u].push_back(v);
    graph[v].push_back(u);
}
```

**5.2. Trie (Efficient String Search)**

```
struct TrieNode {
    TrieNode* children[26];
    bool isEndOfWord;
    TrieNode() { fill(begin(children), end(children), nullptr); isEndOfWord = false; }
};
void insert(TrieNode* root, string key) {
    for (char c : key) {
        if (!root->children[c - 'a'])
            root->children[c - 'a'] = new TrieNode();
        root = root->children[c - 'a'];
    }
    root->isEndOfWord = true;
}
```

  

---

**6. Game Development with SFML**

  

**6.1. Simple Window**

```
#include <SFML/Graphics.hpp>
int main() {
    sf::RenderWindow window(sf::VideoMode(800, 600), "SFML Window");
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event))
            if (event.type == sf::Event::Closed) window.close();
        window.clear();
        window.display();
    }
}
```

**6.2. Drawing a Shape**

```
sf::CircleShape circle(50);
circle.setFillColor(sf::Color::Green);
window.draw(circle);
```

  

---

**7. C++ & AI: Building a Simple Neural Network**

  

**7.1. Creating a Neuron**

```
#include <vector>
struct Neuron {
    vector<double> weights;
    double bias;
};
```

**7.2. Forward Propagation**

```
double activate(double input, vector<double> weights, double bias) {
    double sum = bias;
    for (int i = 0; i < weights.size(); i++)
        sum += input * weights[i];
    return sum > 0 ? 1 : 0;  // Step activation
}
```

  

---

**Final Project: Multithreaded Chat Server**

```
#include <iostream>
#include <thread>
#include <vector>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
using namespace std;

void handleClient(int clientSocket) {
    char buffer[1024] = {0};
    read(clientSocket, buffer, 1024);
    cout << "Client: " << buffer << endl;
    send(clientSocket, "Message received", 16, 0);
    close(clientSocket);
}

int main() {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    sockaddr_in address = {AF_INET, htons(8080), INADDR_ANY};
    bind(server_fd, (struct sockaddr*)&address, sizeof(address));
    listen(server_fd, 3);

    while (true) {
        int client_fd = accept(server_fd, nullptr, nullptr);
        thread t(handleClient, client_fd);
        t.detach();
    }
}
```

  

---

**Conclusion**

  

**What You Learned in C++ Level 3:**

  

✅ **Design Patterns (Singleton, Factory, Observer)**

✅ **Templates & Metaprogramming**

✅ **Advanced Multithreading (Mutex, Locks, Atomics)**

✅ **Networking in C++ (Sockets, HTTP Requests)**

✅ **Graphs, Tries, Hash Tables**

✅ **Game Development with SFML**

✅ **C++ for AI (Basic Neural Networks)**

  

Now, you are ready for **C++ Level 4**, where we explore **Embedded Systems, Operating System Design, Deep Learning, and Quantum Computing with C++**! 🚀