> **March 15th, 2025**  **18:51:49** 
> **Topics:** [[Go L1]] 
> **Tags:** #CS 
---

**Rust Level 2: Intermediate to Advanced Rust Programming**

  

**Introduction**

  

Now that you understand **Rust fundamentals**, it’s time to explore **advanced topics** such as **concurrency, lifetimes, async programming, and web development**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Advanced Ownership & Lifetimes**

✅ **Smart Pointers (Box, Rc, RefCell)**

✅ **Concurrency & Multithreading**

✅ **Async Programming (Tokio, async/await)**

✅ **Web Development with Actix & Warp**

✅ **File Handling & Serialization (JSON, TOML, CSV)**

✅ **Error Handling & Panic Recovery**

✅ **Building a Full-Stack Rust Web App**

  

By the end of this lesson, you will be able to **write high-performance Rust applications, manage memory effectively, and develop web applications**.

---

**1. Advanced Ownership & Lifetimes**

  

**1.1. Understanding Lifetimes**

  

Lifetimes **prevent dangling references**.

```
fn longest<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() { s1 } else { s2 }
}

fn main() {
    let result;
    {
        let str1 = String::from("Rust");
        let str2 = String::from("Programming");
        result = longest(&str1, &str2);
    }
    println!("{}", result); // Error: `result` borrows a value that is out of scope
}
```

Fix it by ensuring **all references live long enough**.

---

**2. Smart Pointers (Box, Rc, RefCell)**

  

Smart pointers manage memory dynamically.

  

**2.1. Using Box<T> for Heap Allocation**

```
fn main() {
    let b = Box::new(5);
    println!("{}", b); // 5
}
```

**2.2. Using Rc<T> for Reference Counting**

  

Rc<T> allows **multiple owners**.

```
use std::rc::Rc;

fn main() {
    let shared = Rc::new(10);
    let a = Rc::clone(&shared);
    let b = Rc::clone(&shared);
    println!("{}", Rc::strong_count(&shared)); // 3
}
```

**2.3. Using RefCell<T> for Mutable Borrowing**

```
use std::cell::RefCell;

fn main() {
    let data = RefCell::new(5);
    *data.borrow_mut() += 10;
    println!("{}", data.borrow()); // 15
}
```

  

---

**3. Concurrency & Multithreading**

  

Rust ensures **safe parallelism**.

  

**3.1. Creating Threads**

```
use std::thread;

fn main() {
    let handle = thread::spawn(|| {
        println!("Hello from thread!");
    });
    handle.join().unwrap();
}
```

**3.2. Using Mutex for Shared Data**

```
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..5 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Final count: {}", *counter.lock().unwrap());
}
```

  

---

**4. Async Programming (Tokio & async/await)**

  

**4.1. Installing Tokio**

```
[dependencies]
tokio = { version = "1", features = ["full"] }
```

**4.2. Async Functions**

```
use tokio::time::{sleep, Duration};

async fn say_hello() {
    sleep(Duration::from_secs(2)).await;
    println!("Hello, Async Rust!");
}

#[tokio::main]
async fn main() {
    say_hello().await;
}
```

  

---

**5. Web Development with Actix & Warp**

  

**5.1. Setting Up a Web Server (Actix)**

  

Install dependencies:

```
[dependencies]
actix-web = "4"
```

Create a simple server:

```
use actix_web::{get, App, HttpResponse, HttpServer};

#[get("/")]
async fn index() -> HttpResponse {
    HttpResponse::Ok().body("Hello, Actix!")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(index))
        .bind("127.0.0.1:8080")?
        .run()
        .await
}
```

Run:

```
cargo run
```

Visit http://127.0.0.1:8080 in the browser.

---

**6. File Handling & Serialization**

  

**6.1. Writing to a File**

```
use std::fs::File;
use std::io::Write;

fn main() {
    let mut file = File::create("output.txt").expect("Cannot create file");
    file.write_all(b"Hello, Rust!").expect("Write failed");
}
```

**6.2. Reading a File**

```
use std::fs;

fn main() {
    let contents = fs::read_to_string("output.txt").expect("Cannot read file");
    println!("{}", contents);
}
```

**6.3. JSON Serialization**

```
use serde::{Serialize, Deserialize};
use serde_json;

#[derive(Serialize, Deserialize)]
struct User {
    name: String,
    age: u8,
}

fn main() {
    let user = User { name: "Alice".to_string(), age: 30 };
    let json = serde_json::to_string(&user).unwrap();
    println!("{}", json);
}
```

  

---

**7. Error Handling & Panic Recovery**

  

**7.1. Recovering from a Panic**

```
fn main() {
    let result = std::panic::catch_unwind(|| {
        panic!("Something went wrong!");
    });

    if result.is_err() {
        println!("Recovered from panic!");
    }
}
```

  

---

**8. Building a Full-Stack Rust Web App**

  

**8.1. Setting Up the Backend**

```
use actix_web::{web, App, HttpResponse, HttpServer, Responder};

async fn greet() -> impl Responder {
    HttpResponse::Ok().body("Hello from Rust Backend!")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().route("/", web::get().to(greet)))
        .bind("127.0.0.1:8080")?
        .run()
        .await
}
```

**8.2. Connecting to a Frontend (React)**

  

Frontend can fetch data using:

```
fetch("http://127.0.0.1:8080")
  .then(response => response.text())
  .then(data => console.log(data));
```

  

---

**Conclusion**

  

**What You Learned in Rust Level 2:**

  

✅ **Advanced Ownership & Lifetimes**

✅ **Smart Pointers (Box, Rc, RefCell)**

✅ **Concurrency & Multithreading**

✅ **Async Programming (Tokio, async/await)**

✅ **Web Development with Actix & Warp**

✅ **File Handling & Serialization (JSON, TOML, CSV)**

✅ **Error Handling & Panic Recovery**

✅ **Built a Full-Stack Rust Web App**

  

Now, you’re ready for **Rust Level 3**, where we explore **Blockchain Development, Embedded Rust, WebAssembly (WASM), and AI with Rust!** 🚀