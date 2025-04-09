> **March 16th, 2025**  **21:56:51** 
> **Topics:** [[API Integration]] 
> **Tags:** #CS 
---

**VB.NET Level 2: Intermediate to Advanced Development**

  

**Introduction**

  

Now that you understand **VB.NET basics**, it’s time to explore **database integration, multi-threading, networking, advanced UI design, and API development**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Working with Databases (SQL, ADO.NET, CRUD Operations)**

✅ **Multi-Threading & Background Tasks**

✅ **Networking (Sockets, HTTP Requests, API Calls)**

✅ **Advanced Windows Forms UI (Custom Controls, Events)**

✅ **Error Handling & Logging**

✅ **Deploying a VB.NET Application**

✅ **Building a Full Database-Connected Windows Application**

  

By the end of this lesson, you will be able to **build database-driven applications, handle concurrent tasks, and create robust networked applications**.

---

**1. Working with Databases (SQL, ADO.NET)**

  

**1.1. Setting Up SQL Server**

1. Install **SQL Server Express** and **SQL Server Management Studio (SSMS)**.

2. Create a database called MyDatabase.

3. Create a table Users:

```
CREATE TABLE Users (
    ID INT PRIMARY KEY IDENTITY,
    Name NVARCHAR(100),
    Email NVARCHAR(100)
);
```

  

  

**1.2. Connecting to a Database (ADO.NET)**

```
Imports System.Data.SqlClient

Dim connString As String = "Server=localhost;Database=MyDatabase;Trusted_Connection=True;"
Dim connection As New SqlConnection(connString)

Try
    connection.Open()
    Console.WriteLine("Database connected!")
Catch ex As Exception
    Console.WriteLine("Error: " & ex.Message)
Finally
    connection.Close()
End Try
```

**1.3. Inserting Data into SQL**

```
Dim query As String = "INSERT INTO Users (Name, Email) VALUES (@Name, @Email)"
Dim cmd As New SqlCommand(query, connection)
cmd.Parameters.AddWithValue("@Name", "Alice")
cmd.Parameters.AddWithValue("@Email", "alice@example.com")

connection.Open()
cmd.ExecuteNonQuery()
connection.Close()
Console.WriteLine("User added successfully!")
```

**1.4. Fetching Data from SQL**

```
Dim query As String = "SELECT * FROM Users"
Dim cmd As New SqlCommand(query, connection)
connection.Open()
Dim reader As SqlDataReader = cmd.ExecuteReader()
While reader.Read()
    Console.WriteLine("User: " & reader("Name") & " - " & reader("Email"))
End While
connection.Close()
```

  

---

**2. Multi-Threading & Background Tasks**

  

**2.1. Running Code in a Background Thread**

```
Imports System.Threading

Sub BackgroundTask()
    Console.WriteLine("Background task started...")
    Thread.Sleep(5000)
    Console.WriteLine("Task completed!")
End Sub

Dim thread As New Thread(AddressOf BackgroundTask)
thread.Start()
```

**2.2. Using Task for Asynchronous Operations**

```
Imports System.Threading.Tasks

Async Function FetchData() As Task
    Await Task.Delay(3000) ' Simulating a long task
    Console.WriteLine("Data fetched!")
End Function

Await FetchData()
```

  

---

**3. Networking (Sockets, HTTP Requests, API Calls)**

  

**3.1. Making an HTTP Request**

```
Imports System.Net.Http

Async Function FetchAPI() As Task
    Dim client As New HttpClient()
    Dim response As String = Await client.GetStringAsync("https://jsonplaceholder.typicode.com/posts/1")
    Console.WriteLine(response)
End Function

Await FetchAPI()
```

**3.2. Sending Data via POST Request**

```
Dim client As New HttpClient()
Dim content As New StringContent("{""name"":""Alice""}", Encoding.UTF8, "application/json")
Dim response As HttpResponseMessage = Await client.PostAsync("https://jsonplaceholder.typicode.com/posts", content)
Dim result As String = Await response.Content.ReadAsStringAsync()
Console.WriteLine(result)
```

**3.3. Creating a TCP Server**

```
Imports System.Net.Sockets
Imports System.Text

Dim server As New TcpListener(System.Net.IPAddress.Any, 5000)
server.Start()
Console.WriteLine("Server started...")

While True
    Dim client As TcpClient = server.AcceptTcpClient()
    Dim stream As NetworkStream = client.GetStream()
    Dim buffer(1024) As Byte
    stream.Read(buffer, 0, buffer.Length)
    Console.WriteLine("Received: " & Encoding.ASCII.GetString(buffer))
End While
```

  

---

**4. Advanced Windows Forms UI (Custom Controls, Events)**

  

**4.1. Handling Button Click Events**

```
Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Label1.Text = "Button Clicked!"
    End Sub
End Class
```

**4.2. Using a ListBox to Display Data**

```
ListBox1.Items.Add("Item 1")
ListBox1.Items.Add("Item 2")
```

**4.3. Loading Data from SQL into a DataGridView**

```
Dim query As String = "SELECT * FROM Users"
Dim adapter As New SqlDataAdapter(query, connection)
Dim table As New DataTable()
adapter.Fill(table)
DataGridView1.DataSource = table
```

  

---

**5. Exception Handling & Logging**

  

**5.1. Using Try-Catch for Error Handling**

```
Try
    Dim result As Integer = 10 / 0  ' Will cause error
Catch ex As DivideByZeroException
    Console.WriteLine("Error: " & ex.Message)
End Try
```

**5.2. Logging Errors to a File**

```
Imports System.IO

Try
    Dim result As Integer = 10 / 0
Catch ex As Exception
    File.WriteAllText("error.log", "Error: " & ex.Message)
End Try
```

  

---

**6. Deploying a VB.NET Application**

  

**6.1. Publishing a Windows Forms Application**

1. Open **Visual Studio** → Click **Build** → Select **Publish**.

2. Choose **Folder or ClickOnce Deployment**.

3. Click **Publish** to generate the installer.

---

**7. Building a Full Database-Connected Windows Application**

  

**7.1. Creating a Windows Form with a Database Connection**

1. **Create a Form (Form1.vb)** with:

• **TextBox** (txtName)

• **TextBox** (txtEmail)

• **Button** (btnAdd)

• **DataGridView** (dataGridView1)

1. **Add Code to btnAdd Click Event:**

```
Imports System.Data.SqlClient

Dim connString As String = "Server=localhost;Database=MyDatabase;Trusted_Connection=True;"
Dim connection As New SqlConnection(connString)

Private Sub btnAdd_Click(sender As Object, e As EventArgs) Handles btnAdd.Click
    Dim query As String = "INSERT INTO Users (Name, Email) VALUES (@Name, @Email)"
    Dim cmd As New SqlCommand(query, connection)
    cmd.Parameters.AddWithValue("@Name", txtName.Text)
    cmd.Parameters.AddWithValue("@Email", txtEmail.Text)
    
    connection.Open()
    cmd.ExecuteNonQuery()
    connection.Close()

    MessageBox.Show("User added successfully!")
    LoadData()
End Sub

Private Sub LoadData()
    Dim query As String = "SELECT * FROM Users"
    Dim adapter As New SqlDataAdapter(query, connection)
    Dim table As New DataTable()
    adapter.Fill(table)
    dataGridView1.DataSource = table
End Sub
```

  

---

**8. Conclusion**

  

**What You Learned in VB.NET Level 2:**

  

✅ **Working with Databases (SQL, ADO.NET, CRUD Operations)**

✅ **Multi-Threading & Background Tasks**

✅ **Networking (Sockets, HTTP Requests, API Calls)**

✅ **Advanced Windows Forms UI (Custom Controls, Events)**

✅ **Error Handling & Logging**

✅ **Deploying a VB.NET Application**

✅ **Built a Full Database-Connected Windows Application**

  

Now, you’re ready for **VB.NET Level 3**, where we explore **Advanced Web Development, Cloud Integration, API Development, and Microservices with VB.NET!** 🚀