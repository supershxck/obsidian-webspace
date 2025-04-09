> **March 15th, 2025**  **18:54:56** 
> **Topics:** [[Go L3]] 
> **Tags:** #CS 
---

**Go Level 2: Intermediate to Advanced Go Programming**

  

**Introduction**

  

Now that you understand **Go fundamentals**, it’s time to dive into **microservices, database integration, advanced concurrency, and WebSockets**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Advanced Functions (Higher-Order Functions, Variadic Functions, Closures)**

✅ **Interfaces & Polymorphism**

✅ **Concurrency with Worker Pools & Mutexes**

✅ **Building REST APIs with Gin**

✅ **Database Integration with PostgreSQL (GORM)**

✅ **WebSockets & Real-Time Communication**

✅ **Microservices & gRPC**

✅ **Building a Scalable Go Web Application**

  

By the end of this lesson, you will be able to **develop scalable, high-performance Go applications with database integration and microservices**.

---

**1. Advanced Functions in Go**

  

**1.1. Higher-Order Functions**

  

A function that takes another function as a parameter.

```
package main
import "fmt"

func apply(f func(int, int) int, a int, b int) int {
    return f(a, b)
}

func add(x, y int) int {
    return x + y
}

func main() {
    result := apply(add, 5, 3)
    fmt.Println("Result:", result) // 8
}
```

**1.2. Variadic Functions**

  

A function that accepts a variable number of arguments.

```
func sum(numbers ...int) int {
    total := 0
    for _, num := range numbers {
        total += num
    }
    return total
}

func main() {
    fmt.Println(sum(1, 2, 3, 4, 5)) // 15
}
```

**1.3. Closures (Anonymous Functions)**

```
func main() {
    multiply := func(a, b int) int {
        return a * b
    }
    fmt.Println(multiply(3, 4)) // 12
}
```

  

---

**2. Interfaces & Polymorphism**

  

**2.1. Defining an Interface**

```
package main
import "fmt"

type Speaker interface {
    Speak() string
}

type Dog struct{}
func (d Dog) Speak() string {
    return "Woof!"
}

type Cat struct{}
func (c Cat) Speak() string {
    return "Meow!"
}

func main() {
    var animal Speaker = Dog{}
    fmt.Println(animal.Speak()) // Woof!
}
```

  

---

**3. Advanced Concurrency**

  

**3.1. Worker Pool (Managing Multiple Goroutines Efficiently)**

```
package main
import (
    "fmt"
    "time"
)

func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        fmt.Println("Worker", id, "processing job", j)
        time.Sleep(time.Second)
        results <- j * 2
    }
}

func main() {
    jobs := make(chan int, 5)
    results := make(chan int, 5)

    for w := 1; w <= 3; w++ {
        go worker(w, jobs, results)
    }

    for j := 1; j <= 5; j++ {
        jobs <- j
    }
    close(jobs)

    for a := 1; a <= 5; a++ {
        <-results
    }
}
```

**3.2. Mutex for Safe Concurrent Access**

```
package main
import (
    "fmt"
    "sync"
)

var count int
var mu sync.Mutex

func increment(wg *sync.WaitGroup) {
    mu.Lock()
    count++
    mu.Unlock()
    wg.Done()
}

func main() {
    var wg sync.WaitGroup
    for i := 0; i < 10; i++ {
        wg.Add(1)
        go increment(&wg)
    }
    wg.Wait()
    fmt.Println("Final count:", count)
}
```

  

---

**4. Building REST APIs with Gin**

  

**4.1. Install Gin**

```
go get -u github.com/gin-gonic/gin
```

**4.2. Create a Simple API**

```
package main
import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{"message": "pong"})
    })
    r.Run(":8080")
}
```

Run:

```
go run main.go
```

Visit http://localhost:8080/ping in the browser.

---

**5. Database Integration with PostgreSQL (GORM)**

  

**5.1. Install GORM & PostgreSQL Driver**

```
go get -u gorm.io/gorm
go get -u gorm.io/driver/postgres
```

**5.2. Connecting to the Database**

```
package main
import (
    "gorm.io/driver/postgres"
    "gorm.io/gorm"
    "fmt"
)

type User struct {
    ID    uint   `gorm:"primaryKey"`
    Name  string
    Email string
}

func main() {
    dsn := "host=localhost user=postgres password=secret dbname=mydb port=5432 sslmode=disable"
    db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
    if err != nil {
        fmt.Println("Failed to connect to the database")
        return
    }
    db.AutoMigrate(&User{})
}
```

  

---

**6. WebSockets & Real-Time Communication**

  

**6.1. Install Gorilla WebSocket**

```
go get -u github.com/gorilla/websocket
```

**6.2. Create a WebSocket Server**

```
package main
import (
    "github.com/gorilla/websocket"
    "net/http"
)

var upgrader = websocket.Upgrader{}

func handleConnection(w http.ResponseWriter, r *http.Request) {
    conn, _ := upgrader.Upgrade(w, r, nil)
    for {
        messageType, p, err := conn.ReadMessage()
        if err != nil {
            return
        }
        conn.WriteMessage(messageType, p)
    }
}

func main() {
    http.HandleFunc("/ws", handleConnection)
    http.ListenAndServe(":8080", nil)
}
```

Connect using JavaScript:

```
const ws = new WebSocket("ws://localhost:8080/ws");
ws.onmessage = event => console.log(event.data);
ws.send("Hello WebSocket!");
```

  

---

**7. Microservices & gRPC**

  

**7.1. Install gRPC**

```
go get google.golang.org/grpc
```

**7.2. Create a Simple gRPC Server**

```
package main
import (
    "google.golang.org/grpc"
    "net"
    "fmt"
)

func main() {
    lis, _ := net.Listen("tcp", ":50051")
    grpcServer := grpc.NewServer()
    fmt.Println("gRPC Server running on port 50051")
    grpcServer.Serve(lis)
}
```

  

---

**8. Building a Scalable Go Web Application**

  

**8.1. Full-Stack Go Web App (Gin + PostgreSQL)**

```
package main
import (
    "github.com/gin-gonic/gin"
    "gorm.io/driver/postgres"
    "gorm.io/gorm"
)

type User struct {
    ID    uint   `gorm:"primaryKey"`
    Name  string
    Email string
}

func main() {
    dsn := "host=localhost user=postgres password=secret dbname=mydb port=5432 sslmode=disable"
    db, _ := gorm.Open(postgres.Open(dsn), &gorm.Config{})
    db.AutoMigrate(&User{})

    r := gin.Default()
    r.POST("/users", func(c *gin.Context) {
        var user User
        c.BindJSON(&user)
        db.Create(&user)
        c.JSON(201, user)
    })
    r.Run(":8080")
}
```

  

---

**Conclusion**

  

**What You Learned in Go Level 2:**

  

✅ **Advanced Functions & Interfaces**

✅ **Concurrency with Worker Pools & Mutexes**

✅ **Building REST APIs with Gin**

✅ **Database Integration with PostgreSQL (GORM)**

✅ **WebSockets & Real-Time Communication**

✅ **Microservices & gRPC**

✅ **Built a Scalable Go Web App**

  

Now, you’re ready for **Go Level 3**, where we explore **Cloud Deployment (Docker, Kubernetes), Advanced Security, and High-Performance Go!** 🚀