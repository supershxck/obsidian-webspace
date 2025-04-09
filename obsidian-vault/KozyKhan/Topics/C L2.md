> **March 15th, 2025**  **18:58:52** 
> **Topics:** [[PHP L1]] 
> **Tags:** #CS 
---

**C# Level 2: Intermediate to Advanced C# Programming**

  

**Introduction**

  

Now that you’ve mastered **C# fundamentals**, it’s time to explore **asynchronous programming, LINQ, database integration, and web development with ASP.NET Core**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Advanced Methods (Delegates, Events, Lambda Expressions)**

✅ **LINQ (Filtering, Sorting, Aggregation, Query Expressions)**

✅ **Asynchronous Programming (Async/Await, Tasks, Threads)**

✅ **Working with Databases (Entity Framework Core, SQL Server, SQLite)**

✅ **Web Development with ASP.NET Core (MVC, APIs, Middleware)**

✅ **Dependency Injection & Design Patterns**

✅ **Building a Full-Stack C# Web App**

  

By the end of this lesson, you will be able to **build scalable C# applications with databases, APIs, and web interfaces**.

---

**1. Advanced Methods & Delegates**

  

**1.1. Using Delegates (Function Pointers)**

```
using System;

delegate int MathOperation(int a, int b);

class Program {
    static int Add(int x, int y) => x + y;
    static void Main() {
        MathOperation operation = Add;
        Console.WriteLine(operation(5, 3)); // Output: 8
    }
}
```

**1.2. Events & Event Handlers**

```
using System;

class Button {
    public event Action Clicked;
    public void Click() {
        Clicked?.Invoke();
    }
}

class Program {
    static void Main() {
        Button btn = new Button();
        btn.Clicked += () => Console.WriteLine("Button clicked!");
        btn.Click();
    }
}
```

**1.3. Lambda Expressions**

```
Func<int, int, int> multiply = (a, b) => a * b;
Console.WriteLine(multiply(3, 4)); // Output: 12
```

  

---

**2. LINQ (Language-Integrated Query)**

  

LINQ simplifies data queries in **arrays, collections, and databases**.

  

**2.1. Filtering Data**

```
using System;
using System.Linq;

class Program {
    static void Main() {
        int[] numbers = { 1, 2, 3, 4, 5, 6 };
        var evens = numbers.Where(n => n % 2 == 0);
        Console.WriteLine(string.Join(", ", evens)); // Output: 2, 4, 6
    }
}
```

**2.2. Sorting & Aggregation**

```
var sorted = numbers.OrderByDescending(n => n).ToList();
var sum = numbers.Sum();
Console.WriteLine("Sorted: " + string.Join(", ", sorted)); // 6, 5, 4, 3, 2, 1
Console.WriteLine("Sum: " + sum); // 21
```

  

---

**3. Asynchronous Programming**

  

**3.1. Using async and await**

```
using System;
using System.Threading.Tasks;

class Program {
    static async Task Main() {
        Console.WriteLine("Fetching data...");
        string data = await FetchDataAsync();
        Console.WriteLine(data);
    }

    static async Task<string> FetchDataAsync() {
        await Task.Delay(2000); // Simulate delay
        return "Data received";
    }
}
```

**3.2. Using Task.Run for Background Work**

```
var result = await Task.Run(() => {
    return "Processed in background";
});
Console.WriteLine(result);
```

  

---

**4. Working with Databases (Entity Framework Core)**

  

**4.1. Installing Entity Framework Core**

```
dotnet add package Microsoft.EntityFrameworkCore.Sqlite
dotnet add package Microsoft.EntityFrameworkCore.Tools
```

**4.2. Defining a Database Model**

```
using Microsoft.EntityFrameworkCore;

class User {
    public int Id { get; set; }
    public string Name { get; set; }
}

class AppDbContext : DbContext {
    public DbSet<User> Users { get; set; }
    protected override void OnConfiguring(DbContextOptionsBuilder options) {
        options.UseSqlite("Data Source=mydb.db");
    }
}
```

**4.3. Inserting Data**

```
using (var db = new AppDbContext()) {
    db.Users.Add(new User { Name = "Alice" });
    db.SaveChanges();
}
```

**4.4. Querying Data**

```
var users = db.Users.Where(u => u.Name.StartsWith("A")).ToList();
users.ForEach(u => Console.WriteLine(u.Name));
```

  

---

**5. Web Development with ASP.NET Core**

  

**5.1. Setting Up ASP.NET Core**

```
dotnet new webapi -n MyWebApi
cd MyWebApi
dotnet run
```

**5.2. Creating a Simple API**

  

Modify Controllers/WeatherForecastController.cs:

```
using Microsoft.AspNetCore.Mvc;

[Route("api/[controller]")]
[ApiController]
public class UsersController : ControllerBase {
    [HttpGet]
    public IActionResult GetUsers() {
        return Ok(new string[] { "Alice", "Bob", "Charlie" });
    }
}
```

Run:

```
dotnet run
```

Visit http://localhost:5000/api/users in the browser.

---

**6. Dependency Injection & Design Patterns**

  

**6.1. Using Dependency Injection**

```
interface IGreetingService {
    string Greet(string name);
}

class GreetingService : IGreetingService {
    public string Greet(string name) => $"Hello, {name}!";
}

class Startup {
    public void ConfigureServices(IServiceCollection services) {
        services.AddTransient<IGreetingService, GreetingService>();
    }
}
```

**6.2. Repository Pattern for Data Access**

```
interface IUserRepository {
    IEnumerable<User> GetUsers();
}

class UserRepository : IUserRepository {
    private readonly AppDbContext _context;
    public UserRepository(AppDbContext context) {
        _context = context;
    }

    public IEnumerable<User> GetUsers() {
        return _context.Users.ToList();
    }
}
```

  

---

**7. Building a Full-Stack C# Web App**

  

**7.1. Backend (ASP.NET Core API)**

  

Create an endpoint:

```
[HttpPost]
public IActionResult CreateUser([FromBody] User user) {
    db.Users.Add(user);
    db.SaveChanges();
    return CreatedAtAction(nameof(GetUsers), new { id = user.Id }, user);
}
```

**7.2. Frontend (React Fetching Data from API)**

```
fetch("http://localhost:5000/api/users")
  .then(response => response.json())
  .then(data => console.log(data));
```

  

---

**8. Deploying a C# Application**

  

**8.1. Deploying to Docker**

  

Create a **Dockerfile**:

```
FROM mcr.microsoft.com/dotnet/aspnet:7.0
WORKDIR /app
COPY . .
ENTRYPOINT ["dotnet", "MyWebApi.dll"]
```

Build & Run:

```
docker build -t my-csharp-app .
docker run -p 5000:5000 my-csharp-app
```

**8.2. Deploying to Azure**

```
az webapp up --name mycsharpapp --runtime "DOTNET:7.0"
```

  

---

**Conclusion**

  

**What You Learned in C# Level 2:**

  

✅ **Advanced Methods (Delegates, Events, Lambda Expressions)**

✅ **LINQ (Filtering, Sorting, Aggregation, Query Expressions)**

✅ **Asynchronous Programming (Async/Await, Tasks, Threads)**

✅ **Working with Databases (Entity Framework Core, SQL Server, SQLite)**

✅ **Web Development with ASP.NET Core (MVC, APIs, Middleware)**

✅ **Dependency Injection & Design Patterns**

✅ **Built a Full-Stack C# Web App**

  

Now, you’re ready for **C# Level 3**, where we explore **Microservices, Cloud Computing, Machine Learning, and Performance Optimization!** 🚀