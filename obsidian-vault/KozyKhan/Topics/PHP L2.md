> **March 15th, 2025**  **19:01:00** 
> **Topics:** [[PHP L3]] 
> **Tags:** #CS 
---

**PHP Level 2: Intermediate to Advanced PHP Programming**

  

**Introduction**

  

Now that you’ve mastered **PHP basics**, it’s time to dive into **database integration, authentication, object-oriented programming (OOP), and building dynamic web applications**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Object-Oriented Programming (Classes, Inheritance, Interfaces, Traits)**

✅ **Database Interaction (MySQL, PDO, CRUD Operations)**

✅ **Sessions & Cookies (User Authentication, Remember Me)**

✅ **Error Handling & Logging**

✅ **File Uploads & Image Processing**

✅ **Security Best Practices (SQL Injection Prevention, Hashing Passwords)**

✅ **Building a Full-Stack PHP Web App**

  

By the end of this lesson, you will be able to **develop dynamic PHP applications with secure authentication and database connectivity**.

---

**1. Object-Oriented Programming (OOP)**

  

**1.1. Defining a Class & Creating Objects**

```
<?php
class Car {
    public $brand;
    public $speed;

    public function __construct($brand, $speed) {
        $this->brand = $brand;
        $this->speed = $speed;
    }

    public function drive() {
        return "{$this->brand} is moving at {$this->speed} km/h";
    }
}

$car = new Car("Tesla", 120);
echo $car->drive();
?>
```

**1.2. Inheritance**

```
<?php
class Vehicle {
    protected $brand;
    public function __construct($brand) {
        $this->brand = $brand;
    }
}

class Car extends Vehicle {
    public function drive() {
        return "Driving a {$this->brand}";
    }
}

$myCar = new Car("BMW");
echo $myCar->drive();
?>
```

**1.3. Interfaces**

```
<?php
interface Animal {
    public function makeSound();
}

class Dog implements Animal {
    public function makeSound() {
        return "Woof!";
    }
}

$dog = new Dog();
echo $dog->makeSound();
?>
```

**1.4. Traits (Multiple Inheritance Alternative)**

```
<?php
trait Logger {
    public function log($message) {
        echo "Log: $message";
    }
}

class User {
    use Logger;
}

$user = new User();
$user->log("User logged in.");
?>
```

  

---

**2. Database Interaction (MySQL + PDO)**

  

**2.1. Connecting to MySQL using PDO**

```
<?php
$dsn = "mysql:host=localhost;dbname=mydb";
$username = "root";
$password = "";
try {
    $db = new PDO($dsn, $username, $password);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected!";
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}
?>
```

**2.2. Creating a Table**

```
<?php
$db->exec("CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
)");
?>
```

**2.3. Insert Data**

```
<?php
$stmt = $db->prepare("INSERT INTO users (name, email) VALUES (?, ?)");
$stmt->execute(["Alice", "alice@example.com"]);
?>
```

**2.4. Fetch Data**

```
<?php
$stmt = $db->query("SELECT * FROM users");
foreach ($stmt as $row) {
    echo $row['name'] . " - " . $row['email'] . "<br>";
}
?>
```

  

---

**3. Sessions & Cookies**

  

**3.1. Using Sessions (User Login)**

```
<?php
session_start();
$_SESSION['username'] = "Alice";
echo "Session started for " . $_SESSION['username'];
?>
```

**3.2. Using Cookies (Remember Me)**

```
<?php
setcookie("user", "Alice", time() + 3600);
if (isset($_COOKIE["user"])) {
    echo "Welcome back, " . $_COOKIE["user"];
}
?>
```

  

---

**4. Error Handling & Logging**

  

**4.1. Try-Catch Blocks**

```
<?php
try {
    $db->query("SELECT * FROM nonexistent_table");
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>
```

**4.2. Logging Errors to a File**

```
<?php
error_log("An error occurred!", 3, "errors.log");
?>
```

  

---

**5. File Uploads & Image Processing**

  

**5.1. Handling File Uploads**

```
<form method="POST" enctype="multipart/form-data">
    Upload File: <input type="file" name="file">
    <input type="submit">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    move_uploaded_file($_FILES["file"]["tmp_name"], "uploads/" . $_FILES["file"]["name"]);
    echo "File uploaded successfully!";
}
?>
```

**5.2. Resizing Images with GD Library**

```
<?php
$image = imagecreatefromjpeg("uploads/sample.jpg");
$resized = imagescale($image, 200, 200);
imagejpeg($resized, "uploads/resized.jpg");
?>
```

  

---

**6. Security Best Practices**

  

**6.1. Preventing SQL Injection**

```
<?php
$stmt = $db->prepare("SELECT * FROM users WHERE email = ?");
$stmt->execute([$_GET["email"]]);
?>
```

**6.2. Hashing Passwords**

```
<?php
$hashed = password_hash("mypassword", PASSWORD_BCRYPT);
if (password_verify("mypassword", $hashed)) {
    echo "Password is correct!";
}
?>
```

  

---

**7. Building a Full-Stack PHP Web App**

  

**7.1. User Registration Form**

```
<form method="POST">
    Name: <input type="text" name="name"><br>
    Email: <input type="email" name="email"><br>
    <input type="submit" name="register">
</form>

<?php
if (isset($_POST["register"])) {
    $stmt = $db->prepare("INSERT INTO users (name, email) VALUES (?, ?)");
    $stmt->execute([$_POST["name"], $_POST["email"]]);
    echo "User registered!";
}
?>
```

**7.2. User Login System**

```
<form method="POST">
    Email: <input type="email" name="email"><br>
    <input type="submit" name="login">
</form>

<?php
if (isset($_POST["login"])) {
    session_start();
    $_SESSION["user"] = $_POST["email"];
    echo "Welcome, " . $_SESSION["user"];
}
?>
```

**7.3. Displaying User Data**

```
<?php
$stmt = $db->query("SELECT * FROM users");
foreach ($stmt as $row) {
    echo $row["name"] . " - " . $row["email"] . "<br>";
}
?>
```

  

---

**Conclusion**

  

**What You Learned in PHP Level 2:**

  

✅ **Object-Oriented Programming (Classes, Inheritance, Interfaces, Traits)**

✅ **Database Interaction (MySQL, PDO, CRUD Operations)**

✅ **Sessions & Cookies (User Authentication, Remember Me)**

✅ **Error Handling & Logging**

✅ **File Uploads & Image Processing**

✅ **Security Best Practices (SQL Injection Prevention, Hashing Passwords)**

✅ **Built a Full-Stack PHP Web App**

  

Now, you’re ready for **PHP Level 3**, where we explore **REST APIs, MVC Architecture, Laravel Framework, and Cloud Deployment!** 🚀