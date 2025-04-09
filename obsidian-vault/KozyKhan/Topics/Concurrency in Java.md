> **February 8th, 2025**  **14:57:50** 
> **Topics:** [[
> **Tags:** #
---

**Concurrency in Java: Multithreading and Parallel Execution**

  

**1. What is Concurrency in Java?**

  

Concurrency in Java refers to the **ability of a program to execute multiple tasks simultaneously** by using **multiple threads**. It helps in **optimizing CPU utilization, improving performance, and handling multiple operations concurrently**.

  

**Why is Concurrency Important?**

  

✔ **Efficient CPU utilization** – Runs multiple tasks in parallel.

✔ **Faster execution** – Reduces wait time for long-running tasks.

✔ **Better responsiveness** – Useful in GUI applications and web services.

✔ **Handles multiple requests simultaneously** – Essential in server applications.

**2. Key Concepts in Java Concurrency**

|**Concept**|**Description**|
|---|---|
|**Thread**|Smallest unit of execution in a program.|
|**Multithreading**|Running multiple threads concurrently.|
|**Parallelism**|Executing tasks **simultaneously on multiple cores**.|
|**Synchronization**|Managing access to shared resources to avoid conflicts.|

**3. Creating Threads in Java**

  

Java provides two ways to create threads:

  

**1. Extending Thread Class**

  

✔ **Example: Creating and Starting a Thread**

```
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running...");
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start();  // Starts the thread
    }
}
```

✔ **Explanation:**

• MyThread extends Thread and overrides run().

• start() method begins execution in a **new thread**.

**2. Implementing Runnable Interface**

  

✔ **Example: Using Runnable Interface**

```
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Thread is running using Runnable...");
    }
}

public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new MyRunnable());
        thread.start();
    }
}
```

✔ **Explanation:**

• Runnable is preferred as it supports **multiple inheritance**.

• Thread(new MyRunnable()) allows **flexibility**.

**4. Thread Lifecycle in Java**

  

A thread goes through the following states:

|**State**|**Description**|
|---|---|
|**New**|Thread is created but not started (Thread t = new Thread();).|
|**Runnable**|Thread is ready to run (t.start();).|
|**Running**|Thread is currently executing.|
|**Blocked/Waiting**|Thread is paused, waiting for resources.|
|**Terminated**|Thread has finished execution.|

✔ **Example: Observing Thread States**

```
Thread t = new Thread();
System.out.println(t.getState());  // NEW
t.start();
System.out.println(t.getState());  // RUNNABLE
```

**5. Thread Synchronization**

  

When multiple threads **access shared resources**, race conditions can occur. **Synchronization ensures thread safety.**

  

**Using synchronized Keyword**

  

✔ **Example: Preventing Race Condition**

```
class SharedResource {
    private int count = 0;

    public synchronized void increment() {
        count++;
        System.out.println("Count: " + count);
    }
}

public class Main {
    public static void main(String[] args) {
        SharedResource resource = new SharedResource();

        Thread t1 = new Thread(resource::increment);
        Thread t2 = new Thread(resource::increment);

        t1.start();
        t2.start();
    }
}
```

✔ **Explanation:**

• synchronized ensures only **one thread modifies count at a time**.

**Using Lock (More Flexible)**

  

✔ **Example: Using ReentrantLock**

```
import java.util.concurrent.locks.ReentrantLock;

class SharedResource {
    private int count = 0;
    private final ReentrantLock lock = new ReentrantLock();

    public void increment() {
        lock.lock();
        try {
            count++;
            System.out.println("Count: " + count);
        } finally {
            lock.unlock();
        }
    }
}
```

✔ **Explanation:**

• **Locks provide better control** over synchronization than synchronized.

**6. Thread Communication: wait() and notify()**

  

Threads can **communicate using wait(), notify(), and notifyAll()**.

  

✔ **Example: Producer-Consumer Problem**

```
class Shared {
    private int data;
    private boolean available = false;

    public synchronized void produce(int value) throws InterruptedException {
        while (available) {
            wait();
        }
        data = value;
        available = true;
        System.out.println("Produced: " + value);
        notify();
    }

    public synchronized void consume() throws InterruptedException {
        while (!available) {
            wait();
        }
        System.out.println("Consumed: " + data);
        available = false;
        notify();
    }
}
```

✔ **Explanation:**

• wait() makes a thread **wait until notified**.

• notify() wakes up waiting threads.

**7. Java Concurrency API**

  

Java provides java.util.concurrent package for better **thread management**.

  

**1. Using ExecutorService for Thread Management**

  

✔ **Example: Creating a Thread Pool**

```
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ThreadPoolExample {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3);

        for (int i = 0; i < 5; i++) {
            executor.submit(() -> System.out.println("Task executed by " + Thread.currentThread().getName()));
        }

        executor.shutdown();
    }
}
```

✔ **Explanation:**

• ExecutorService **manages a pool of threads**, improving performance.

**2. Using Callable for Returning Values from Threads**

  

✔ **Example: Using Callable Instead of Runnable**

```
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class CallableExample {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newSingleThreadExecutor();
        
        Callable<Integer> task = () -> {
            return 10 * 10;
        };
        
        Future<Integer> future = executor.submit(task);
        System.out.println("Result: " + future.get());

        executor.shutdown();
    }
}
```

✔ **Explanation:**

• Unlike Runnable, Callable<T> **returns a value**.

**8. Common Concurrency Issues**

|**Issue**|**Description**|**Solution**|
|---|---|---|
|**Race Condition**|Multiple threads modifying shared data|Use synchronized, Lock|
|**Deadlock**|Two threads wait for each other indefinitely|Avoid nested locks|
|**Livelock**|Threads keep responding but make no progress|Add timeouts|
|**Starvation**|One thread never gets CPU time|Use fair scheduling|

✔ **Example: Deadlock Situation**

```
synchronized (resource1) {
    synchronized (resource2) {
        // Deadlock can occur if another thread locks resources in reverse order
    }
}
```

✔ **Solution:** **Lock resources in a consistent order**.

**9. Conclusion**

  

Java **Concurrency API and multithreading** provide powerful mechanisms for **parallel execution and performance improvement**. Understanding **thread creation, synchronization, thread pools, and executors** is essential for writing **efficient and scalable Java applications**. 🚀