> **March 15th, 2025**  **18:53:23** 
> **Topics:** [[Go L2]] 
> **Tags:** #CS 
---

**Go Level 1: Introduction to Go (Golang) Programming**

  

**Introduction**

  

Go (Golang) is a **fast, concurrent, and simple programming language** developed by Google. It is widely used in **web development, cloud computing, networking, and microservices**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Go Basics (Syntax, Variables, Data Types, Operators)**

✅ **Control Flow (If-Else, Loops, Switch Statements)**

✅ **Functions & Defer**

✅ **Pointers & Structs**

✅ **Error Handling & Panic Recovery**

✅ **Concurrency with Goroutines & Channels**

✅ **File Handling & JSON Parsing**

✅ **Building a Simple Web Server in Go**

  

By the end of this lesson, you will be able to **write basic Go programs, understand concurrency, and build a simple web application**.

---

**1. Setting Up Go**

  

**1.1. Installing Go**

  

Download and install Go from [golang.org](https://go.dev/dl/).

Verify installation:

```
go version
```

**1.2. Running Go Code**

• **Run a Go script**:

```
go run main.go
```

  

• **Compile and execute**:

```
go build main.go
./main
```

  

---

**2. Go Basics: Variables, Data Types & Operators**

  

**2.1. Variables & Constants**

```
package main
import "fmt"

func main() {
    var age int = 25
    name := "Alice" // Short declaration
    const PI float64 = 3.1415

    fmt.Println(name, "is", age, "years old.")
}
```

**2.2. Data Types**

```
func main() {
    var number int = 42
    var pi float64 = 3.14
    var isGoAwesome bool = true
    var letter rune = 'G'  // Unicode character
    var message string = "Hello, Go!"
    
    fmt.Println(number, pi, isGoAwesome, letter, message)
}
```

**2.3. Operators**

```
func main() {
    a, b := 10, 3
    fmt.Println("Sum:", a+b)
    fmt.Println("Diff:", a-b)
    fmt.Println("Product:", a*b)
    fmt.Println("Quotient:", a/b)
    fmt.Println("Remainder:", a%b)
}
```

  

---

**3. Control Flow (If-Else, Loops, Switch)**

  

**3.1. If-Else Statement**

```
func main() {
    temperature := 30
    if temperature > 25 {
        fmt.Println("It's hot outside!")
    } else {
        fmt.Println("It's cool outside.")
    }
}
```

**3.2. For Loop**

```
func main() {
    for i := 1; i <= 5; i++ {
        fmt.Println("Iteration", i)
    }
}
```

**3.3. While Loop Equivalent (for with condition)**

```
func main() {
    count := 0
    for count < 3 {
        fmt.Println("Count:", count)
        count++
    }
}
```

**3.4. Switch Statement**

```
func main() {
    day := "Monday"
    switch day {
    case "Monday":
        fmt.Println("Start of the week!")
    case "Friday":
        fmt.Println("Weekend is coming!")
    default:
        fmt.Println("A regular day.")
    }
}
```

  

---

**4. Functions & Defer**

  

**4.1. Defining a Function**

```
func greet(name string) string {
    return "Hello, " + name + "!"
}

func main() {
    fmt.Println(greet("Alice"))
}
```

**4.2. Function with Multiple Return Values**

```
func swap(x, y int) (int, int) {
    return y, x
}

func main() {
    a, b := swap(3, 7)
    fmt.Println(a, b) // 7 3
}
```

**4.3. Defer (Execute at End of Function)**

```
func main() {
    defer fmt.Println("This will run last")
    fmt.Println("This runs first")
}
```

  

---

**5. Pointers & Structs**

  

**5.1. Pointers**

```
func main() {
    num := 10
    ptr := &num // Pointer to num

    fmt.Println("Value:", *ptr)  // Dereferencing pointer
}
```

**5.2. Structs (Custom Data Types)**

```
type Car struct {
    Brand string
    Speed int
}

func main() {
    myCar := Car{Brand: "Tesla", Speed: 120}
    fmt.Println(myCar.Brand, "is moving at", myCar.Speed, "km/h")
}
```

  

---

**6. Error Handling & Panic Recovery**

  

**6.1. Handling Errors**

```
import "errors"

func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("cannot divide by zero")
    }
    return a / b, nil
}

func main() {
    result, err := divide(10, 0)
    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Println("Result:", result)
    }
}
```

**6.2. Recovering from Panic**

```
func safeDivide() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered from panic:", r)
        }
    }()
    panic("Something went wrong!")
}

func main() {
    safeDivide()
}
```

  

---

**7. Concurrency with Goroutines & Channels**

  

**7.1. Goroutines (Lightweight Threads)**

```
import "fmt"
import "time"

func sayHello() {
    fmt.Println("Hello from Goroutine!")
}

func main() {
    go sayHello()
    time.Sleep(1 * time.Second) // Prevent program from exiting early
}
```

**7.2. Channels for Communication**

```
func main() {
    messages := make(chan string)

    go func() {
        messages <- "Hello from Goroutine!"
    }()

    msg := <-messages
    fmt.Println(msg)
}
```

  

---

**8. File Handling & JSON Parsing**

  

**8.1. Writing to a File**

```
import "os"

func main() {
    os.WriteFile("output.txt", []byte("Hello, Go!"), 0644)
}
```

**8.2. Reading from a File**

```
import "os"

func main() {
    data, _ := os.ReadFile("output.txt")
    fmt.Println(string(data))
}
```

**8.3. JSON Parsing**

```
import "encoding/json"
import "fmt"

type User struct {
    Name string `json:"name"`
    Age  int    `json:"age"`
}

func main() {
    jsonString := `{"name": "Alice", "age": 30}`
    var user User
    json.Unmarshal([]byte(jsonString), &user)
    fmt.Println(user.Name, "is", user.Age, "years old.")
}
```

  

---

**9. Building a Simple Web Server**

```
import "net/http"
import "fmt"

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Hello, Go Web Server!")
}

func main() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}
```

Run:

```
go run main.go
```

Visit http://localhost:8080.

---

**Conclusion**

  

**What You Learned in Go Level 1:**

  

✅ **Go Basics (Syntax, Variables, Data Types, Operators)**

✅ **Control Flow (If-Else, Loops, Switch Statements)**

✅ **Functions & Defer**

✅ **Pointers & Structs**

✅ **Error Handling & Panic Recovery**

✅ **Concurrency with Goroutines & Channels**

✅ **File Handling & JSON Parsing**

✅ **Built a Simple Web Server**

  

Now, you’re ready for **Go Level 2**, where we explore **Microservices, Database Integration, Advanced Concurrency, and WebSockets in Go!** 🚀