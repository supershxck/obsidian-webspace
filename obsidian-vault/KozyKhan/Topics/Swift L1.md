> **March 15th, 2025**  **18:47:46** 
> **Topics:** [[Swift L2]] 
> **Tags:** #CS 
---

**Swift Level 1: Introduction to Swift Programming**

  

**Introduction**

  

Swift is **Apple’s powerful and intuitive programming language**, used for **iOS, macOS, watchOS, and tvOS development**. It is designed to be **safe, fast, and interactive**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Swift Basics (Syntax, Variables, Data Types, Operators)**

✅ **Control Flow (If-Else, Loops, Switch Statements)**

✅ **Functions & Closures**

✅ **Object-Oriented Programming (Classes, Structs, Enums, Inheritance)**

✅ **Optionals & Error Handling**

✅ **Collections (Arrays, Dictionaries, Sets)**

✅ **Basic SwiftUI & UIKit Introduction**

✅ **Building a Simple iOS App in Swift**

  

By the end of this lesson, you will be able to **write basic Swift programs and understand core iOS development concepts**.

---

**1. Setting Up Swift**

  

**1.1. Installing Swift**

• **macOS:** Swift is pre-installed (Use Xcode or Terminal).

• **Windows/Linux:** Install Swift from [swift.org](https://swift.org/download/).

  

**1.2. Running Swift Code**

• Open **Xcode**, create a Swift Playground, or run Swift in the **Terminal**:

```
swift
```

• Run a Swift script:

```
swift my_script.swift
```

  

---

**2. Swift Basics: Variables, Data Types & Operators**

  

**2.1. Variables & Constants**

```
var age = 25          // Mutable variable
let name = "Alice"    // Constant (Immutable)
```

**2.2. Data Types**

```
var number: Int = 42
var pi: Double = 3.14
var isSwiftAwesome: Bool = true
var message: String = "Hello, Swift!"
```

**2.3. Type Inference**

  

Swift **automatically infers types**, so explicit declarations aren’t always needed.

```
var greeting = "Hello"  // Inferred as String
var score = 95          // Inferred as Int
```

**2.4. Operators**

```
let sum = 5 + 3      // Addition
let diff = 10 - 4    // Subtraction
let product = 2 * 6  // Multiplication
let quotient = 9 / 3 // Division
let remainder = 7 % 3 // Modulus

let isEqual = (5 == 5)   // true
let isNotEqual = (5 != 4) // true
```

  

---

**3. Control Flow (If-Else, Loops, Switch)**

  

**3.1. If-Else Statement**

```
let temperature = 30
if temperature > 25 {
    print("It's hot outside!")
} else {
    print("It's cool outside.")
}
```

**3.2. For Loop**

```
for i in 1...5 {
    print("Iteration \(i)")
}
```

**3.3. While Loop**

```
var count = 0
while count < 3 {
    print("Count: \(count)")
    count += 1
}
```

**3.4. Switch Statement**

```
let day = "Monday"
switch day {
case "Monday":
    print("Start of the week!")
case "Friday":
    print("Weekend is coming!")
default:
    print("A regular day.")
}
```

  

---

**4. Functions & Closures**

  

**4.1. Defining a Function**

```
func greet(name: String) -> String {
    return "Hello, \(name)!"
}

print(greet(name: "Alice"))
```

**4.2. Function with Default Parameter**

```
func greet(name: String = "Guest") {
    print("Hello, \(name)!")
}

greet()      // Hello, Guest!
greet(name: "Bob") // Hello, Bob!
```

**4.3. Closures (Anonymous Functions)**

```
let square = { (num: Int) -> Int in
    return num * num
}

print(square(5))  // 25
```

  

---

**5. Object-Oriented Programming (OOP)**

  

**5.1. Creating a Class & Object**

```
class Car {
    var brand: String
    var speed: Int

    init(brand: String, speed: Int) {
        self.brand = brand
        self.speed = speed
    }

    func drive() {
        print("\(brand) is driving at \(speed) km/h")
    }
}

let myCar = Car(brand: "Tesla", speed: 120)
myCar.drive()
```

**5.2. Structs vs. Classes**

```
struct CarStruct {
    var brand: String
    var speed: Int
}

var car1 = CarStruct(brand: "Ford", speed: 100)
var car2 = car1  // Creates a copy (value type)
car2.speed = 150
print(car1.speed) // 100 (Original remains unchanged)
```

  

---

**6. Optionals & Error Handling**

  

**6.1. Optionals (Handling Null Values)**

```
var name: String? = nil
print(name ?? "No name available")  // Default value if nil
```

**6.2. Optional Binding**

```
if let safeName = name {
    print("Hello, \(safeName)")
} else {
    print("No name found")
}
```

**6.3. Error Handling**

```
enum NetworkError: Error {
    case noInternet
}

func fetchData() throws {
    throw NetworkError.noInternet
}

do {
    try fetchData()
} catch {
    print("Error: \(error)")
}
```

  

---

**7. Collections (Arrays, Dictionaries, Sets)**

  

**7.1. Arrays**

```
var fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Orange")
print(fruits[1]) // Banana
```

**7.2. Dictionaries**

```
var scores = ["Alice": 90, "Bob": 85]
print(scores["Alice"] ?? "No Score")
```

**7.3. Sets (Unique Elements)**

```
var uniqueNumbers: Set = [1, 2, 3, 1, 2]
print(uniqueNumbers)  // {1, 2, 3}
```

  

---

**8. Basic SwiftUI & UIKit Introduction**

  

Swift is used to **build iOS apps** with **SwiftUI** and **UIKit**.

  

**8.1. Basic SwiftUI App**

```
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Text("Hello, SwiftUI!")
                .font(.largeTitle)
                .padding()
            Button("Click Me") {
                print("Button Clicked")
            }
        }
    }
}
```

**8.2. UIKit (Storyboard-Based Apps)**

```
import UIKit

class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        print("UIKit Loaded")
    }
}
```

  

---

**9. Final Project: Simple iOS App**

  

**Objective:**

• Create a **button that changes text when clicked**.

```
import SwiftUI

struct ContentView: View {
    @State private var message = "Hello, Swift!"

    var body: some View {
        VStack {
            Text(message)
                .font(.title)
                .padding()
            Button("Tap Me") {
                message = "Button Clicked!"
            }
            .padding()
            .background(Color.blue)
            .foregroundColor(.white)
            .cornerRadius(10)
        }
    }
}
```

  

---

**Conclusion**

  

**What You Learned in Swift Level 1:**

  

✅ **Swift Basics (Syntax, Variables, Data Types, Operators)**

✅ **Control Flow (If-Else, Loops, Switch Statements)**

✅ **Functions & Closures**

✅ **Object-Oriented Programming (Classes, Structs, Enums, Inheritance)**

✅ **Optionals & Error Handling**

✅ **Collections (Arrays, Dictionaries, Sets)**

✅ **Basic SwiftUI & UIKit Introduction**

✅ **Built a Simple iOS App**

  

Now, you’re ready for **Swift Level 2**, where we explore **Advanced Swift, Networking, Database Integration, and Full iOS Development with SwiftUI!** 🚀