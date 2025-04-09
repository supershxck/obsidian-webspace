> **March 15th, 2025**  **18:50:16** 
> **Topics:** [[Rust L2]] 
> **Tags:** #CS 
---

**Rust Level 1: Introduction to Rust Programming**

  

**Introduction**

  

Rust is a **systems programming language** focused on **speed, memory safety, and concurrency**. It’s used in **high-performance applications, web assembly, blockchain, and embedded systems**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Rust Basics (Syntax, Variables, Data Types, Operators)**

✅ **Ownership & Borrowing (Rust’s Memory Safety Model)**

✅ **Control Flow (If-Else, Loops, Pattern Matching)**

✅ **Functions & Closures**

✅ **Structs, Enums & Pattern Matching**

✅ **Error Handling (Result & Option Types)**

✅ **Collections (Vectors, HashMaps, Strings)**

✅ **Building a Simple Rust Application**

  

By the end of this lesson, you will be able to **write basic Rust programs and understand its unique memory safety model**.

---

**1. Setting Up Rust**

  

**1.1. Installing Rust**

• Install Rust using **Rustup** (recommended):

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

  

• Verify installation:

```
rustc --version
```

  

  

**1.2. Running Rust Code**

• **Interactive Mode (Rust Playground)**: [play.rust-lang.org](https://play.rust-lang.org/)

• **Compile & Run a Rust Program**:

```
rustc main.rs
./main
```

  

---

**2. Rust Basics: Variables, Data Types & Operators**

  

**2.1. Variables & Constants**

```
fn main() {
    let age = 25; // Immutable variable
    let mut score = 100; // Mutable variable
    const PI: f64 = 3.1415; // Constant
}
```

**2.2. Data Types**

```
fn main() {
    let num: i32 = 42;  // Integer
    let pi: f64 = 3.14; // Floating-point number
    let is_rust_fun: bool = true; // Boolean
    let letter: char = 'R'; // Character
    let message: &str = "Hello, Rust!"; // String slice
}
```

**2.3. Operators**

```
fn main() {
    let sum = 5 + 3;      // Addition
    let diff = 10 - 4;    // Subtraction
    let product = 2 * 6;  // Multiplication
    let quotient = 9 / 3; // Division
    let remainder = 7 % 3;// Modulus

    let is_equal = (5 == 5);   // true
    let is_not_equal = (5 != 4); // true
}
```

  

---

**3. Ownership & Borrowing (Memory Safety)**

  

Rust’s **ownership system** prevents memory leaks without garbage collection.

  

**3.1. Ownership Rules**

• Each value has **one owner**.

• When the owner goes out of scope, Rust **frees memory automatically**.

• **No data races or dangling pointers**.

```
fn main() {
    let s1 = String::from("Hello");
    let s2 = s1; // Ownership moves to s2, s1 is invalid

    println!("{}", s2); // Works
    // println!("{}", s1); // Error! s1 is no longer valid
}
```

**3.2. Borrowing & References**

```
fn main() {
    let s = String::from("Hello");
    print_string(&s); // Borrowing without transferring ownership
}

fn print_string(text: &String) {
    println!("{}", text);
}
```

  

---

**4. Control Flow (If-Else, Loops, Pattern Matching)**

  

**4.1. If-Else Statement**

```
fn main() {
    let temp = 30;
    if temp > 25 {
        println!("It's hot!");
    } else {
        println!("It's cold!");
    }
}
```

**4.2. Loops**

  

**For Loop**

```
fn main() {
    for i in 1..=5 {
        println!("Iteration {}", i);
    }
}
```

**While Loop**

```
fn main() {
    let mut count = 0;
    while count < 3 {
        println!("Count: {}", count);
        count += 1;
    }
}
```

**4.3. Match Statement (Pattern Matching)**

```
fn main() {
    let day = "Monday";
    match day {
        "Monday" => println!("Start of the week!"),
        "Friday" => println!("Weekend is coming!"),
        _ => println!("A regular day."),
    }
}
```

  

---

**5. Functions & Closures**

  

**5.1. Defining a Function**

```
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)
}

fn main() {
    let message = greet("Alice");
    println!("{}", message);
}
```

**5.2. Closures (Anonymous Functions)**

```
fn main() {
    let square = |num: i32| num * num;
    println!("{}", square(5)); // 25
}
```

  

---

**6. Structs, Enums & Pattern Matching**

  

**6.1. Defining & Using Structs**

```
struct Car {
    brand: String,
    speed: i32,
}

fn main() {
    let my_car = Car { brand: String::from("Tesla"), speed: 120 };
    println!("{} is driving at {} km/h", my_car.brand, my_car.speed);
}
```

**6.2. Using Enums**

```
enum TrafficLight {
    Red,
    Yellow,
    Green,
}

fn main() {
    let signal = TrafficLight::Green;
    match signal {
        TrafficLight::Red => println!("Stop!"),
        TrafficLight::Yellow => println!("Slow down!"),
        TrafficLight::Green => println!("Go!"),
    }
}
```

  

---

**7. Error Handling (Result & Option Types)**

  

**7.1. Handling Missing Values (Option)**

```
fn main() {
    let maybe_number: Option<i32> = Some(5);
    match maybe_number {
        Some(n) => println!("Number: {}", n),
        None => println!("No number found"),
    }
}
```

**7.2. Handling Errors (Result)**

```
fn divide(x: i32, y: i32) -> Result<i32, String> {
    if y == 0 {
        Err(String::from("Cannot divide by zero"))
    } else {
        Ok(x / y)
    }
}

fn main() {
    match divide(10, 0) {
        Ok(result) => println!("Result: {}", result),
        Err(error) => println!("Error: {}", error),
    }
}
```

  

---

**8. Collections (Vectors, HashMaps, Strings)**

  

**8.1. Vectors (Dynamic Arrays)**

```
fn main() {
    let mut numbers = vec![1, 2, 3];
    numbers.push(4);
    println!("{:?}", numbers); // [1, 2, 3, 4]
}
```

**8.2. HashMaps (Key-Value Pairs)**

```
use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();
    scores.insert("Alice", 90);
    println!("{:?}", scores.get("Alice")); // Some(90)
}
```

  

---

**9. Building a Simple Rust Application**

  

**Project: Simple Temperature Converter**

```
fn convert_to_fahrenheit(celsius: f64) -> f64 {
    (celsius * 1.8) + 32.0
}

fn main() {
    let temp_c = 30.0;
    let temp_f = convert_to_fahrenheit(temp_c);
    println!("{}°C is {}°F", temp_c, temp_f);
}
```

  

---

**Conclusion**

  

**What You Learned in Rust Level 1:**

  

✅ **Rust Basics & Ownership Model**

✅ **Control Flow & Pattern Matching**

✅ **Functions, Closures & Structs**

✅ **Error Handling (Result & Option)**

✅ **Collections (Vectors, HashMaps)**

✅ **Built a Simple Rust Application**

  

Now, you’re ready for **Rust Level 2**, where we explore **Concurrency, Lifetimes, Web Development, and Embedded Systems!** 🚀