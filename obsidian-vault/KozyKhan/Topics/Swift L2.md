> **March 15th, 2025**  **18:48:16** 
> **Topics:** [[Rust L1]] 
> **Tags:** #CS 
---

**Swift Level 2: Intermediate to Advanced Swift Programming**

  

**Introduction**

  

Now that you understand **Swift fundamentals**, it’s time to explore **intermediate and advanced Swift programming techniques** for building **efficient and scalable iOS applications**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Advanced Functions (Higher-Order Functions, Closures, Generics)**

✅ **Protocols & Protocol-Oriented Programming (POP)**

✅ **Concurrency with Grand Central Dispatch (GCD) & Async/Await**

✅ **Networking with URLSession & API Calls**

✅ **Data Persistence (UserDefaults, Core Data, SQLite, CloudKit)**

✅ **Dependency Management with Swift Package Manager & CocoaPods**

✅ **Advanced SwiftUI Techniques (Animations, Navigation, State Management)**

✅ **Building a Full-Stack iOS App with a Backend**

  

By the end of this lesson, you will be able to **write advanced Swift programs, interact with APIs, manage data efficiently, and build production-ready iOS apps**.

---

**1. Advanced Functions & Closures**

  

**1.1. Higher-Order Functions (Map, Filter, Reduce)**

  

Swift allows **functional programming** with **higher-order functions**.

```
let numbers = [1, 2, 3, 4, 5]

// Map: Multiply each element by 2
let doubled = numbers.map { $0 * 2 }
print(doubled)  // [2, 4, 6, 8, 10]

// Filter: Keep only even numbers
let evens = numbers.filter { $0 % 2 == 0 }
print(evens)  // [2, 4]

// Reduce: Sum all numbers
let sum = numbers.reduce(0, +)
print(sum)  // 15
```

**1.2. Closures with Capturing Values**

```
func makeIncrementer(incrementAmount: Int) -> () -> Int {
    var total = 0
    return {
        total += incrementAmount
        return total
    }
}

let incrementByTwo = makeIncrementer(incrementAmount: 2)
print(incrementByTwo()) // 2
print(incrementByTwo()) // 4
```

**1.3. Generics (Reusable Code)**

  

Generics allow **flexible and type-safe functions**.

```
func swapValues<T>(_ a: inout T, _ b: inout T) {
    let temp = a
    a = b
    b = temp
}

var x = 5, y = 10
swapValues(&x, &y)
print(x, y) // 10, 5
```

  

---

**2. Protocols & Protocol-Oriented Programming (POP)**

  

**2.1. Defining & Conforming to a Protocol**

```
protocol Drawable {
    func draw()
}

class Circle: Drawable {
    func draw() {
        print("Drawing a circle")
    }
}
```

**2.2. Protocol Extensions**

```
extension Drawable {
    func fill() {
        print("Filling with color")
    }
}

let shape: Drawable = Circle()
shape.fill() // "Filling with color"
```

  

---

**3. Concurrency & Multithreading**

  

**3.1. Grand Central Dispatch (GCD)**

```
DispatchQueue.global().async {
    print("Running in background")
}
```

**3.2. Async/Await (Swift 5.5+)**

```
func fetchData() async -> String {
    return "Data fetched"
}

Task {
    let result = await fetchData()
    print(result)
}
```

  

---

**4. Networking & API Calls**

  

**4.1. Fetching Data with URLSession**

```
func fetchUsers() {
    let url = URL(string: "https://jsonplaceholder.typicode.com/users")!
    URLSession.shared.dataTask(with: url) { data, _, _ in
        if let data = data {
            let users = try? JSONDecoder().decode([User].self, from: data)
            print(users ?? [])
        }
    }.resume()
}
```

**4.2. Decoding JSON into a Model**

```
struct User: Codable {
    let id: Int
    let name: String
}
```

  

---

**5. Data Persistence & Storage**

  

**5.1. UserDefaults (Simple Key-Value Storage)**

```
UserDefaults.standard.set("Alice", forKey: "username")
let username = UserDefaults.standard.string(forKey: "username")
print(username ?? "No user")
```

**5.2. Core Data (Database for iOS)**

```
import CoreData

func saveUser(name: String, context: NSManagedObjectContext) {
    let user = UserEntity(context: context)
    user.name = name
    try? context.save()
}
```

  

---

**6. Dependency Management**

  

**6.1. Swift Package Manager (SPM)**

```
swift package init --type library
```

Add dependencies in **Package.swift**:

```
dependencies: [
    .package(url: "https://github.com/Alamofire/Alamofire.git", from: "5.4.0")
]
```

**6.2. CocoaPods**

```
pod init
pod install
```

  

---

**7. Advanced SwiftUI Techniques**

  

**7.1. Animations**

```
import SwiftUI

struct AnimatedView: View {
    @State private var scale: CGFloat = 1.0

    var body: some View {
        Button("Tap Me") {
            withAnimation {
                scale += 0.2
            }
        }
        .scaleEffect(scale)
    }
}
```

**7.2. Navigation & State Management**

```
import SwiftUI

struct MainView: View {
    var body: some View {
        NavigationView {
            NavigationLink("Go to Details", destination: DetailView())
        }
    }
}

struct DetailView: View {
    var body: some View {
        Text("Detail Screen")
    }
}
```

  

---

**8. Building a Full-Stack iOS App**

  

**8.1. Project: Weather App**

  

**1. Fetch Weather Data**

```
struct Weather: Codable {
    let temperature: Double
}

func fetchWeather() async -> Weather? {
    let url = URL(string: "https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=London")!
    let (data, _) = try! await URLSession.shared.data(from: url)
    return try? JSONDecoder().decode(Weather.self, from: data)
}
```

**2. Display Data in SwiftUI**

```
import SwiftUI

struct ContentView: View {
    @State private var weather: Weather?

    var body: some View {
        VStack {
            Text(weather?.temperature.description ?? "Loading...")
                .font(.largeTitle)
                .padding()

            Button("Fetch Weather") {
                Task {
                    weather = await fetchWeather()
                }
            }
        }
    }
}
```

  

---

**Conclusion**

  

**What You Learned in Swift Level 2:**

  

✅ **Advanced Functions (Higher-Order Functions, Closures, Generics)**

✅ **Protocols & Protocol-Oriented Programming (POP)**

✅ **Concurrency with Grand Central Dispatch (GCD) & Async/Await**

✅ **Networking with URLSession & API Calls**

✅ **Data Persistence (UserDefaults, Core Data, SQLite, CloudKit)**

✅ **Dependency Management with Swift Package Manager & CocoaPods**

✅ **Advanced SwiftUI Techniques (Animations, Navigation, State Management)**

✅ **Built a Full-Stack iOS App**

  

Now, you’re ready for **Swift Level 3**, where we explore **Machine Learning, Augmented Reality (ARKit), Advanced Security, and Performance Optimization in Swift!** 🚀