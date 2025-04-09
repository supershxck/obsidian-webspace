> **February 8th, 2025**  **15:13:50** 
> **Topics:** [[
> **Tags:** #
---

**Concurrency vs. Parallelism: Understanding Multitasking in Programming**

  

**1. What are Concurrency and Parallelism?**

  

Concurrency and parallelism are concepts used in **multitasking** to improve efficiency in programs. While they are related, they have **different goals and execution models**.

• **Concurrency**: Deals with managing **multiple tasks at the same time** (interleaving execution).

• **Parallelism**: Deals with executing **multiple tasks simultaneously** on multiple CPU cores.

  

**Key Differences**

|**Feature**|**Concurrency**|**Parallelism**|
|---|---|---|
|**Definition**|Multiple tasks making progress at the same time|Multiple tasks running at the exact same time|
|**Execution Model**|Tasks take turns using shared resources|Tasks run independently on multiple processors|
|**Example**|Handling multiple user requests on a web server|Processing large datasets with multiple CPU cores|
|**Performance Benefit**|Improves responsiveness|Increases processing speed|
|**Hardware Dependency**|Works on a **single-core** or **multi-core CPU**|Requires **multi-core CPU or GPU**|

**2. Understanding Concurrency**

  

Concurrency allows **multiple tasks to start, run, and complete in overlapping time periods**, but not necessarily at the same exact moment.

  

✔ **Example: Concurrency in Real Life**

• A cashier at a grocery store **switches between** customers when handling payments and scanning items.

• A web server **handles multiple user requests** by switching between them quickly.

  

**How Concurrency Works in Programming**

  

✔ **Single-core CPU**: Uses **context switching** to handle multiple tasks.

✔ **Multi-core CPU**: Uses **threads** and **asynchronous execution**.

  

✔ **Example: Concurrency in Java (Multithreading)**

```
class MyThread extends Thread {
    public void run() {
        System.out.println(Thread.currentThread().getName() + " is running");
    }
}

public class ConcurrencyExample {
    public static void main(String[] args) {
        MyThread t1 = new MyThread();
        MyThread t2 = new MyThread();
        t1.start();  // Starts thread 1
        t2.start();  // Starts thread 2
    }
}
```

✔ **Explanation:**

• The program **creates multiple threads**, which execute independently.

• The **CPU switches between threads** to create concurrency.

  

✔ **Example: Concurrency in Python (AsyncIO)**

```
import asyncio

async def task(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)  # Simulates waiting
    print(f"Task {name} completed")

async def main():
    await asyncio.gather(task(1), task(2), task(3))

asyncio.run(main())
```

✔ **Explanation:**

• asyncio allows tasks to run **concurrently** by switching when waiting.

**3. Understanding Parallelism**

  

Parallelism **divides a task into smaller sub-tasks** and executes them **simultaneously** on multiple processors.

  

✔ **Example: Parallelism in Real Life**

• A factory **assembles a car using multiple workers** simultaneously.

• A GPU **processes multiple pixels at the same time** for graphics rendering.

  

**How Parallelism Works in Programming**

  

✔ **Requires multiple CPU cores or GPUs**.

✔ **No context switching** – Each task runs on a **separate processor core**.

  

✔ **Example: Parallelism in Python (Multiprocessing)**

```
import multiprocessing

def process_task(n):
    print(f"Processing {n}")

if __name__ == "__main__":
    with multiprocessing.Pool(4) as pool:
        pool.map(process_task, range(4))  # Runs 4 processes in parallel
```

✔ **Explanation:**

• Uses multiprocessing.Pool(4), which **spawns 4 separate processes** on different CPU cores.

  

✔ **Example: Parallelism in Java (ForkJoinPool)**

```
import java.util.concurrent.RecursiveTask;
import java.util.concurrent.ForkJoinPool;

class ParallelSum extends RecursiveTask<Integer> {
    private int start, end;

    ParallelSum(int start, int end) {
        this.start = start;
        this.end = end;
    }

    @Override
    protected Integer compute() {
        if (end - start <= 2) {
            return start + end;
        }

        int mid = (start + end) / 2;
        ParallelSum left = new ParallelSum(start, mid);
        ParallelSum right = new ParallelSum(mid + 1, end);

        left.fork();
        return right.compute() + left.join();
    }
}

public class ParallelismExample {
    public static void main(String[] args) {
        ForkJoinPool pool = new ForkJoinPool();
        int result = pool.invoke(new ParallelSum(1, 10));
        System.out.println("Sum: " + result);
    }
}
```

✔ **Explanation:**

• Uses **ForkJoinPool** to split the task into smaller **parallel sub-tasks**.

**4. When to Use Concurrency vs. Parallelism**

|**Use Case**|**Best Approach**|
|---|---|
|**Handling many user requests**|**Concurrency** (e.g., Web servers, async I/O)|
|**Processing large datasets**|**Parallelism** (e.g., Data analysis, AI computations)|
|**Multitasking in a single-core system**|**Concurrency**|
|**Heavy computation on multi-core systems**|**Parallelism**|

✔ **Concurrency Example: Web Server Handling Multiple Users**

```
Web request 1 → Processed
Web request 2 → Processed
Web request 3 → Processed
```

✔ **Parallelism Example: Image Processing on GPU**

```
Pixel 1 → Processed
Pixel 2 → Processed
Pixel 3 → Processed
```

**5. Combining Concurrency and Parallelism**

  

Many modern systems **use both** concurrency and parallelism together.

  

✔ **Example: A Web Server with Concurrent & Parallel Tasks**

• **Concurrency**: Handles multiple user requests asynchronously.

• **Parallelism**: Uses multiple CPU cores to process data faster.

  

✔ **Example: Python Concurrent + Parallel Execution**

```
import asyncio
import concurrent.futures

async def concurrent_task(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)
    print(f"Task {name} completed")

def parallel_task(n):
    return n * n

async def main():
    # Concurrency (Async Tasks)
    await asyncio.gather(concurrent_task(1), concurrent_task(2))

    # Parallelism (Multiple Processes)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(parallel_task, range(5)))
        print(results)

asyncio.run(main())
```

✔ **Explanation:**

• **asyncio.gather()** runs **concurrent** tasks.

• **ProcessPoolExecutor()** runs **parallel** tasks on multiple cores.

**6. Conclusion**

  

✔ **Concurrency** manages multiple tasks efficiently **on a single or multi-core system**.

✔ **Parallelism** runs tasks **simultaneously on multiple processors**, increasing performance.

✔ **Modern applications use both** to handle high performance workloads effectively. 🚀