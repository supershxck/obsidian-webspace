> **March 15th, 2025**  **18:59:12** 
> **Topics:** [[PHP L2]] 
> **Tags:** #CS 
---

**PHP Level 1: Introduction to PHP Programming**

  

**Introduction**

  

PHP is a **server-side scripting language** primarily used for **web development**. It powers **80% of websites**, including **WordPress, Facebook, and Wikipedia**.

  

**What You’ll Learn in This Lesson:**

  

✅ **PHP Basics (Syntax, Variables, Data Types, Operators)**

✅ **Control Flow (If-Else, Loops, Switch Statements)**

✅ **Functions & Scope**

✅ **Forms & User Input Handling**

✅ **Arrays & Associative Arrays**

✅ **Error Handling & Superglobals**

✅ **File Handling (Reading & Writing Files)**

✅ **Building a Simple PHP Web App**

  

By the end of this lesson, you will be able to **write basic PHP scripts, handle user input, and interact with files**.

---

**1. Setting Up PHP**

  

**1.1. Installing PHP**

• **Windows**: Install [XAMPP](https://www.apachefriends.org/download.html)

• **Mac/Linux**: Install using Homebrew or APT:

```
sudo apt install php  # Ubuntu/Debian
brew install php  # macOS
```

  

  

**1.2. Running PHP Code**

• **Run a PHP script**:

```
php script.php
```

  

• **Run PHP Built-in Server**:

```
php -S localhost:8000
```

Open http://localhost:8000 in your browser.

---

**2. PHP Basics: Variables, Data Types & Operators**

  

**2.1. Variables & Constants**

```
<?php
$name = "Alice";
$age = 25;
define("PI", 3.1415);  // Constant
echo "$name is $age years old.";
?>
```

**2.2. Data Types**

```
<?php
$integer = 42;
$float = 3.14;
$boolean = true;
$string = "Hello, PHP!";
$array = array("Apple", "Banana", "Cherry");

echo gettype($integer);  // integer
?>
```

**2.3. Operators**

```
<?php
$a = 10; $b = 3;
echo "Sum: " . ($a + $b);
echo "Difference: " . ($a - $b);
?>
```

  

---

**3. Control Flow (If-Else, Loops, Switch)**

  

**3.1. If-Else Statement**

```
<?php
$temperature = 30;
if ($temperature > 25) {
    echo "It's hot outside!";
} else {
    echo "It's cool outside.";
}
?>
```

**3.2. For Loop**

```
<?php
for ($i = 1; $i <= 5; $i++) {
    echo "Iteration $i <br>";
}
?>
```

**3.3. While Loop**

```
<?php
$count = 0;
while ($count < 3) {
    echo "Count: $count <br>";
    $count++;
}
?>
```

**3.4. Switch Statement**

```
<?php
$day = "Monday";
switch ($day) {
    case "Monday":
        echo "Start of the week!";
        break;
    case "Friday":
        echo "Weekend is coming!";
        break;
    default:
        echo "A regular day.";
}
?>
```

  

---

**4. Functions & Scope**

  

**4.1. Defining a Function**

```
<?php
function greet($name) {
    return "Hello, $name!";
}
echo greet("Alice");
?>
```

**4.2. Default Parameters**

```
<?php
function greet($name = "Guest") {
    echo "Hello, $name!";
}
greet();  // Hello, Guest!
?>
```

  

---

**5. Forms & User Input Handling**

  

**5.1. Handling GET Requests**

```
<form method="GET">
    Enter your name: <input type="text" name="username">
    <input type="submit">
</form>

<?php
if (isset($_GET["username"])) {
    echo "Hello, " . htmlspecialchars($_GET["username"]);
}
?>
```

**5.2. Handling POST Requests**

```
<form method="POST">
    Enter password: <input type="password" name="password">
    <input type="submit">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    echo "Password received.";
}
?>
```

  

---

**6. Arrays & Associative Arrays**

  

**6.1. Indexed Arrays**

```
<?php
$fruits = ["Apple", "Banana", "Cherry"];
echo $fruits[1];  // Banana
?>
```

**6.2. Associative Arrays**

```
<?php
$scores = ["Alice" => 90, "Bob" => 85];
echo $scores["Alice"];  // 90
?>
```

**6.3. Looping Through Arrays**

```
<?php
foreach ($scores as $name => $score) {
    echo "$name scored $score. <br>";
}
?>
```

  

---

**7. Error Handling & Superglobals**

  

**7.1. Handling Errors**

```
<?php
function divide($a, $b) {
    if ($b == 0) {
        throw new Exception("Cannot divide by zero.");
    }
    return $a / $b;
}

try {
    echo divide(10, 0);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```

**7.2. Using Superglobals ($_SERVER)**

```
<?php
echo "Your IP Address: " . $_SERVER["REMOTE_ADDR"];
?>
```

  

---

**8. File Handling (Reading & Writing Files)**

  

**8.1. Writing to a File**

```
<?php
file_put_contents("output.txt", "Hello, PHP!");
?>
```

**8.2. Reading from a File**

```
<?php
$content = file_get_contents("output.txt");
echo $content;
?>
```

  

---

**9. Building a Simple PHP Web App**

  

**9.1. Basic Contact Form**

```
<form method="POST">
    Name: <input type="text" name="name"><br>
    Message: <textarea name="message"></textarea><br>
    <input type="submit">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST["name"]);
    $message = htmlspecialchars($_POST["message"]);
    file_put_contents("messages.txt", "$name: $message\n", FILE_APPEND);
    echo "Message saved!";
}
?>
```

**9.2. Displaying Messages**

```
<?php
$messages = file("messages.txt");
foreach ($messages as $msg) {
    echo nl2br($msg);
}
?>
```

  

---

**Conclusion**

  

**What You Learned in PHP Level 1:**

  

✅ **PHP Basics (Syntax, Variables, Data Types, Operators)**

✅ **Control Flow (If-Else, Loops, Switch Statements)**

✅ **Functions & Scope**

✅ **Forms & User Input Handling**

✅ **Arrays & Associative Arrays**

✅ **Error Handling & Superglobals**

✅ **File Handling (Reading & Writing Files)**

✅ **Built a Simple PHP Web App**

  

Now, you’re ready for **PHP Level 2**, where we explore **Databases (MySQL), Sessions, Authentication, and Object-Oriented PHP!** 🚀