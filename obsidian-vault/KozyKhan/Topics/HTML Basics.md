> **February 8th, 2025**  **14:00:05** 
> **Topics:** [[
> **Tags:** #
---

**HTML Basics: The Foundation of Web Development**

  

**What is HTML?**

  

**HTML (HyperText Markup Language)** is the **standard language for creating web pages**. It provides the **structure** of a webpage using **elements and tags**.

**1. HTML Structure**

  

An HTML document consists of **tags** enclosed in < > (angle brackets).

  

**Basic HTML Template**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Web Page</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a simple webpage.</p>
</body>
</html>
```

**Explanation:**

1. **<!DOCTYPE html>** → Declares HTML5.

2. **<html>** → Root element.

3. **<head>** → Contains metadata (title, styles, scripts).

4. **<title>** → Sets the page title (visible on the browser tab).

5. **<body>** → Contains the **visible content**.

**2. HTML Elements & Tags**

  

HTML consists of **elements** enclosed in **opening (<tag>) and closing (</tag>) tags**.

  

**Common HTML Tags**

|**Tag**|**Description**|
|---|---|
|<h1> to <h6>|Headings (largest to smallest)|
|<p>|Paragraph|
|<a href="">|Link (Anchor)|
|<img src="">|Image|
|<ul> / <ol>|Unordered / Ordered List|
|<li>|List Item|
|<div>|Generic Container|
|<span>|Inline Container|

**Example: Headings and Paragraphs**

```
<h1>Main Title</h1>
<h2>Subheading</h2>
<p>This is a paragraph of text.</p>
```

**Example: Links and Images**

```
<a href="https://example.com">Visit Example</a>
<img src="image.jpg" alt="A sample image">
```

**Example: Lists**

```
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>

<ol>
    <li>First</li>
    <li>Second</li>
</ol>
```

**3. HTML Forms (User Input)**

  

Forms collect user input (e.g., login, contact forms).

```
<form action="submit.php" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email">
    
    <button type="submit">Submit</button>
</form>
```

**4. HTML Tables (Displaying Data)**

```
<table border="1">
    <tr>
        <th>Name</th>
        <th>Age</th>
    </tr>
    <tr>
        <td>Alice</td>
        <td>25</td>
    </tr>
</table>
```

**5. HTML Semantic Elements**

  

Semantic elements **improve readability** and SEO.

|**Element**|**Purpose**|
|---|---|
|<header>|Defines the header section|
|<nav>|Navigation menu|
|<section>|Section of content|
|<article>|Self-contained content|
|<aside>|Sidebar content|
|<footer>|Footer section|

**Example**

```
<header>
    <h1>Website Name</h1>
    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
    </nav>
</header>

<section>
    <h2>About Us</h2>
    <p>We build amazing websites.</p>
</section>

<footer>
    <p>&copy; 2024 My Website</p>
</footer>
```

**6. HTML Forms with Input Types**

```
<form>
    <input type="text" placeholder="Enter name">
    <input type="email" placeholder="Enter email">
    <input type="password" placeholder="Enter password">
    <input type="submit" value="Register">
</form>
```

**7. HTML Attributes**

  

Attributes provide **additional information** about elements.

  

**Example Attributes:**

• href (for links)

• src (for images)

• alt (image alternative text)

• id (unique identifier)

• class (CSS class)

• style (inline CSS)

```
<img src="logo.png" alt="Website Logo" width="200">
```

**8. HTML Comments**

```
<!-- This is a comment -->
```

**Conclusion**

  

HTML provides the **structure** of a webpage. Combined with **CSS (styling) and JavaScript (interactivity)**, it forms the foundation of **modern web development**. 🚀