> **March 16th, 2025**  **21:47:06** 
> **Topics:** [[VB.Net L2]] 
> **Tags:** #CS 
---

**VB.NET Level 1: Introduction to VB.NET Programming**

  

**Introduction**

  

Visual Basic .NET (VB.NET) is a **modern, object-oriented programming language** developed by Microsoft. It is primarily used for **desktop applications, database integration, and enterprise software** using the .NET framework.

  

**What You’ll Learn in This Lesson:**

  

✅ **VB.NET Basics (Syntax, Variables, Data Types, Operators)**

✅ **Control Flow (If-Else, Loops, Select Case)**

✅ **Functions & Subroutines**

✅ **Object-Oriented Programming (Classes & Objects)**

✅ **Working with Arrays & Collections**

✅ **Exception Handling**

✅ **File Handling (Reading & Writing Files)**

✅ **Building a Simple Windows Forms Application**

  

By the end of this lesson, you will be able to **write basic VB.NET programs, work with OOP, and create a Windows Forms application**.

---

**1. Setting Up VB.NET**

  

**1.1. Installing VB.NET**

• **Option 1: Visual Studio (Recommended)**

• Download **Visual Studio Community Edition** from [Visual Studio](https://visualstudio.microsoft.com).

• Install **.NET Desktop Development**.

• **Option 2: .NET Core CLI (For Console Apps)**

```
dotnet new console -n MyVBApp
cd MyVBApp
dotnet run
```

  

---

**2. VB.NET Basics: Variables, Data Types & Operators**

  

**2.1. Declaring Variables**

```
Module Program
    Sub Main()
        Dim name As String = "Alice"
        Dim age As Integer = 25
        Dim pi As Double = 3.14159
        Dim isVB As Boolean = True

        Console.WriteLine("Name: " & name)
        Console.WriteLine("Age: " & age)
        Console.WriteLine("Pi: " & pi)
        Console.WriteLine("VB.NET is awesome: " & isVB)
    End Sub
End Module
```

**2.2. Operators**

```
Dim a As Integer = 10
Dim b As Integer = 3
Console.WriteLine("Sum: " & (a + b))
Console.WriteLine("Product: " & (a * b))
Console.WriteLine("Exponent: " & (a ^ b)) ' 10^3 = 1000
```

  

---

**3. Control Flow (If-Else, Loops, Select Case)**

  

**3.1. If-Else Statement**

```
Dim num As Integer = 15
If num > 10 Then
    Console.WriteLine("Number is greater than 10")
Else
    Console.WriteLine("Number is 10 or less")
End If
```

**3.2. For Loop**

```
For i As Integer = 1 To 5
    Console.WriteLine("Iteration " & i)
Next
```

**3.3. While Loop**

```
Dim count As Integer = 0
While count < 3
    Console.WriteLine("Count: " & count)
    count += 1
End While
```

**3.4. Select Case Statement**

```
Dim grade As String = "A"
Select Case grade
    Case "A"
        Console.WriteLine("Excellent")
    Case "B"
        Console.WriteLine("Good")
    Case "C"
        Console.WriteLine("Average")
    Case Else
        Console.WriteLine("Failed")
End Select
```

  

---

**4. Functions & Subroutines**

  

**4.1. Defining a Function**

```
Function Square(num As Integer) As Integer
    Return num * num
End Function

Dim result As Integer = Square(5)
Console.WriteLine("Square of 5: " & result)
```

**4.2. Subroutines (No Return Value)**

```
Sub Greet(name As String)
    Console.WriteLine("Hello, " & name & "!")
End Sub

Greet("Alice")
```

  

---

**5. Object-Oriented Programming (Classes & Objects)**

  

**5.1. Creating a Class & Object**

```
Class Car
    Public Brand As String
    Public Speed As Integer

    Public Sub Drive()
        Console.WriteLine(Brand & " is moving at " & Speed & " km/h")
    End Sub
End Class

Dim myCar As New Car()
myCar.Brand = "Tesla"
myCar.Speed = 120
myCar.Drive()
```

**5.2. Constructors in VB.NET**

```
Class Car
    Public Brand As String
    Public Speed As Integer

    Public Sub New(brand As String, speed As Integer)
        Me.Brand = brand
        Me.Speed = speed
    End Sub

    Public Sub Drive()
        Console.WriteLine(Brand & " is moving at " & Speed & " km/h")
    End Sub
End Class

Dim myCar As New Car("BMW", 150)
myCar.Drive()
```

  

---

**6. Working with Arrays & Collections**

  

**6.1. Arrays**

```
Dim fruits As String() = {"Apple", "Banana", "Cherry"}
Console.WriteLine(fruits(1)) ' Output: Banana
```

**6.2. Lists (Collections)**

```
Imports System.Collections.Generic

Dim numbers As New List(Of Integer)({1, 2, 3, 4, 5})
numbers.Add(6)
Console.WriteLine(numbers(2)) ' Output: 3
```

  

---

**7. Exception Handling**

```
Try
    Dim num As Integer = 10 / 0 ' Causes division by zero error
Catch ex As DivideByZeroException
    Console.WriteLine("Error: Division by zero is not allowed")
Finally
    Console.WriteLine("Execution continues")
End Try
```

  

---

**8. File Handling (Reading & Writing Files)**

  

**8.1. Writing to a File**

```
Imports System.IO

Dim path As String = "output.txt"
File.WriteAllText(path, "Hello, VB.NET!")
```

**8.2. Reading from a File**

```
Dim content As String = File.ReadAllText("output.txt")
Console.WriteLine(content)
```

  

---

**9. Building a Simple Windows Forms Application**

  

**9.1. Creating a Windows Forms App**

1. **Open Visual Studio** → **Create New Project** → **Windows Forms App (.NET)**

2. **Drag a Button & Label** from the Toolbox.

3. **Double-click the Button** and add:

```
Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Label1.Text = "Hello, VB.NET!"
    End Sub
End Class
```

  

1. **Run the App** (F5).

---

**10. Conclusion**

  

**What You Learned in VB.NET Level 1:**

  

✅ **VB.NET Basics (Syntax, Variables, Data Types, Operators)**

✅ **Control Flow (If-Else, Loops, Select Case)**

✅ **Functions & Subroutines**

✅ **Object-Oriented Programming (Classes & Objects)**

✅ **Working with Arrays & Collections**

✅ **Exception Handling**

✅ **File Handling (Reading & Writing Files)**

✅ **Built a Simple Windows Forms Application**

  

Now, you’re ready for **VB.NET Level 2**, where we explore **Database Integration (SQL), Multi-threading, Networking, and Advanced UI Development with WinForms & WPF!** 🚀