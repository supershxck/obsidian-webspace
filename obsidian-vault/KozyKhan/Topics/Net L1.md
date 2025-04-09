> **March 16th, 2025**  **22:26:32** 
> **Topics:** [[
> **Tags:** #
---

**.NET Level 1: Introduction to .NET Development**

  

**Introduction**

  

.NET is a **cross-platform, open-source development framework** created by Microsoft. It allows developers to build **web, desktop, cloud, and mobile applications** using languages like **C#, VB.NET, and F#**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Understanding .NET Framework, .NET Core, and .NET 6+**

✅ **Setting Up .NET Development Environment**

✅ **Building a Simple Console Application in C# and VB.NET**

✅ **Basic Syntax (Variables, Data Types, Operators, Control Flow)**

✅ **Object-Oriented Programming (Classes & Objects)**

✅ **Working with Files & Exception Handling**

✅ **Building a Simple .NET Web API**

  

By the end of this lesson, you will be able to **write basic .NET programs, understand OOP principles, and build your first .NET application**.

---

**1. Understanding .NET Framework, .NET Core, and .NET 6+**

  

**1.1. What is .NET?**

• **.NET Framework**: Windows-only, legacy version of .NET.

• **.NET Core**: Cross-platform, open-source version of .NET.

• **.NET 6+**: Unified framework combining .NET Core and .NET Framework.

|**Version**|**Features**|
|---|---|
|.NET Framework|Windows only, used for legacy apps|
|.NET Core|Cross-platform, lightweight, faster|
|.NET 6+|Unified, latest version, recommended|

  

---

**2. Setting Up .NET Development Environment**

  

**2.1. Install .NET SDK**

  

Download from [Microsoft’s .NET website](https://dotnet.microsoft.com/en-us/download).

  

**2.2. Verify Installation**

```
dotnet --version
```

**2.3. Create a New .NET Console Application**

```
dotnet new console -n MyFirstApp
cd MyFirstApp
dotnet run
```

  

---

**3. Building a Simple .NET Console Application**

  

**3.1. C# Console App**

  

Edit Program.cs:

```
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, .NET!");
    }
}
```

Run:

```
dotnet run
```

**3.2. VB.NET Console App**

  

Edit Program.vb:

```
Module Program
    Sub Main()
        Console.WriteLine("Hello, .NET!")
    End Sub
End Module
```

Run:

```
dotnet run
```

  

---

**4. Basic Syntax: Variables, Data Types & Operators**

  

**4.1. Declaring Variables in C#**

```
int age = 25;
double pi = 3.14;
string name = "Alice";
bool isActive = true;

Console.WriteLine($"Name: {name}, Age: {age}, Pi: {pi}, Active: {isActive}");
```

**4.2. Declaring Variables in VB.NET**

```
Dim age As Integer = 25
Dim pi As Double = 3.14
Dim name As String = "Alice"
Dim isActive As Boolean = True

Console.WriteLine($"Name: {name}, Age: {age}, Pi: {pi}, Active: {isActive}")
```

**4.3. Arithmetic & Logical Operators**

```
int a = 10, b = 5;
Console.WriteLine(a + b);  // Addition
Console.WriteLine(a > b);  // Boolean comparison
```

```
Dim a As Integer = 10, b As Integer = 5
Console.WriteLine(a + b)  ' Addition
Console.WriteLine(a > b)  ' Boolean comparison
```

  

---

**5. Control Flow: If-Else, Loops**

  

**5.1. If-Else Statements**

```
int num = 10;
if (num > 5)
    Console.WriteLine("Greater than 5");
else
    Console.WriteLine("Less than or equal to 5");
```

```
Dim num As Integer = 10
If num > 5 Then
    Console.WriteLine("Greater than 5")
Else
    Console.WriteLine("Less than or equal to 5")
End If
```

**5.2. For Loops**

```
for (int i = 1; i <= 5; i++)
{
    Console.WriteLine($"Iteration {i}");
}
```

```
For i As Integer = 1 To 5
    Console.WriteLine($"Iteration {i}")
Next
```

  

---

**6. Object-Oriented Programming (OOP)**

  

**6.1. Creating a Class & Object in C#**

```
class Car
{
    public string Brand;
    public int Speed;

    public void Drive()
    {
        Console.WriteLine($"{Brand} is moving at {Speed} km/h");
    }
}

Car myCar = new Car();
myCar.Brand = "Tesla";
myCar.Speed = 120;
myCar.Drive();
```

**6.2. Creating a Class & Object in VB.NET**

```
Class Car
    Public Brand As String
    Public Speed As Integer

    Public Sub Drive()
        Console.WriteLine($"{Brand} is moving at {Speed} km/h")
    End Sub
End Class

Dim myCar As New Car()
myCar.Brand = "Tesla"
myCar.Speed = 120
myCar.Drive()
```

  

---

**7. File Handling & Exception Handling**

  

**7.1. Writing & Reading Files**

```
using System.IO;
File.WriteAllText("test.txt", "Hello, .NET!");
string content = File.ReadAllText("test.txt");
Console.WriteLine(content);
```

```
Imports System.IO
File.WriteAllText("test.txt", "Hello, .NET!")
Dim content As String = File.ReadAllText("test.txt")
Console.WriteLine(content)
```

**7.2. Handling Exceptions**

```
try
{
    int result = 10 / 0;
}
catch (DivideByZeroException ex)
{
    Console.WriteLine("Error: " + ex.Message);
}
```

```
Try
    Dim result As Integer = 10 / 0
Catch ex As DivideByZeroException
    Console.WriteLine("Error: " & ex.Message)
End Try
```

  

---

**8. Building a Simple .NET Web API**

  

**8.1. Creating a .NET Web API**

```
dotnet new webapi -n MyApi
cd MyApi
dotnet run
```

**8.2. Modifying the API Controller (WeatherForecastController.cs)**

```
[Route("api/users")]
[ApiController]
public class UsersController : ControllerBase
{
    private static List<string> users = new List<string> { "Alice", "Bob" };

    [HttpGet]
    public IEnumerable<string> GetUsers()
    {
        return users;
    }

    [HttpPost]
    public IActionResult AddUser([FromBody] string name)
    {
        users.Add(name);
        return Ok(users);
    }
}
```

**8.3. Testing the API**

```
curl -X GET http://localhost:5000/api/users
```

```
curl -X POST -H "Content-Type: application/json" -d '"Charlie"' http://localhost:5000/api/users
```

  

---

**9. Conclusion**

  

**What You Learned in .NET Level 1:**

  

✅ **Understanding .NET Framework, .NET Core, and .NET 6+**

✅ **Setting Up .NET Development Environment**

✅ **Building a Simple Console Application in C# and VB.NET**

✅ **Basic Syntax (Variables, Data Types, Operators, Control Flow)**

✅ **Object-Oriented Programming (Classes & Objects)**

✅ **Working with Files & Exception Handling**

✅ **Built a Simple .NET Web API**

  

Now, you’re ready for **.NET Level 2**, where we explore **Database Integration (SQL, Entity Framework), Multi-threading, Advanced API Development, and Cloud Deployment!** 🚀