> **February 8th, 2025**  **14:00:52** 
> **Topics:** [[
> **Tags:** #
---

**CSS Basics: Styling the Web**

  

**What is CSS?**

  

**CSS (Cascading Style Sheets)** is a language used to **style and layout** web pages. It allows developers to control **colors, fonts, spacing, positioning, animations, and responsiveness** of elements on a webpage.

**1. CSS Syntax**

  

A **CSS rule** consists of a **selector** and a **declaration block**.

```
selector {
    property: value;
}
```

**Example**

```
h1 {
    color: blue;
    font-size: 24px;
}
```

• **Selector** → h1 (targets all <h1> elements).

• **Property** → color, font-size.

• **Value** → blue, 24px.

**2. Ways to Apply CSS**

  

CSS can be added in **three ways**:

  

**1. Inline CSS (Directly in HTML Elements)**

```
<p style="color: red; font-size: 20px;">This is a red paragraph.</p>
```

• ✅ Quick changes

• ❌ Not recommended for large projects

**2. Internal CSS (Inside <style> in HTML <head>)**

```
<head>
    <style>
        p {
            color: green;
            font-size: 18px;
        }
    </style>
</head>
```

• ✅ Good for small projects

• ❌ Not reusable across multiple files

**3. External CSS (Separate .css File)**

```
/* styles.css */
p {
    color: blue;
    font-size: 18px;
}
```

Linked in HTML:

```
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

• ✅ Best practice (separates design from content)

• ✅ Reusable and maintainable

**3. CSS Selectors**

  

Selectors **target HTML elements** to apply styles.

  

**1. Universal Selector (*)**

  

Applies to **all** elements.

```
* {
    margin: 0;
    padding: 0;
}
```

**2. Type Selector**

  

Targets specific HTML tags.

```
h1 {
    color: blue;
}
```

**3. Class Selector (.)**

  

Targets elements with a class.

```
.paragraph {
    font-size: 16px;
}
```

Applied in HTML:

```
<p class="paragraph">Styled paragraph</p>
```

**4. ID Selector (#)**

  

Targets a unique element.

```
#main-title {
    font-size: 24px;
}
```

Applied in HTML:

```
<h1 id="main-title">Main Title</h1>
```

**5. Group Selector (,)**

  

Applies styles to multiple elements.

```
h1, p {
    color: darkblue;
}
```

**6. Descendant Selector (parent child)**

  

Targets elements **inside another element**.

```
div p {
    color: red;
}
```

```
<div>
    <p>This will be red.</p>
</div>
```

**7. Pseudo-Classes**

  

Apply styles based on **state or interaction**.

```
button:hover {
    background-color: yellow;
}
```

**4. CSS Box Model**

  

Every HTML element is treated as a **box** consisting of:

1. **Content** – The actual text/image.

2. **Padding** – Space around content.

3. **Border** – Outline around the element.

4. **Margin** – Space outside the border.

  

**Example**

```
.box {
    width: 200px;
    height: 100px;
    padding: 20px;
    border: 2px solid black;
    margin: 10px;
}
```

**5. CSS Positioning**

  

Controls element placement.

|**Property**|**Description**|
|---|---|
|static|Default position (normal flow)|
|relative|Positioned **relative to itself**|
|absolute|Positioned **relative to the nearest positioned ancestor**|
|fixed|Stays fixed relative to the viewport|
|sticky|Sticks while scrolling|

**Example**

```
.fixed-box {
    position: fixed;
    top: 0;
    left: 0;
    background: red;
    width: 100%;
}
```

**6. CSS Flexbox (For Layouts)**

  

Flexbox is used to **align and distribute elements**.

  

**Example**

```
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 200px;
}
```

```
<div class="container">
    <div>Centered Content</div>
</div>
```

• justify-content: center; → Centers horizontally.

• align-items: center; → Centers vertically.

**7. CSS Grid (Advanced Layout)**

  

Grid is a powerful system for **designing complex layouts**.

  

**Example**

```
.grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
}
```

```
<div class="grid-container">
    <div>Box 1</div>
    <div>Box 2</div>
    <div>Box 3</div>
</div>
```

**8. CSS Media Queries (Responsive Design)**

  

Media queries allow CSS to be **responsive on different screen sizes**.

  

**Example**

```
@media (max-width: 600px) {
    body {
        background-color: lightblue;
    }
}
```

• When the screen width is **600px or smaller**, the **background color changes**.

**9. CSS Animations**

```
@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

.box {
    animation: fadeIn 2s ease-in-out;
}
```

**10. Conclusion**

  

CSS **enhances the visual appearance** of web pages. It provides:

✔ **Styling (colors, fonts, layouts)**

✔ **Positioning & alignment (Flexbox, Grid)**

✔ **Responsiveness (Media Queries)**

✔ **Animations & effects**

  

Mastering CSS allows you to create **modern, beautiful, and responsive** web pages! 🚀