> **March 3rd, 2025**  **14:20:14** 
> **Topics:** [[
> **Tags:** #article 
---

Below is a basic [[HTML]] and [[CSS]] template for a CV website. You can copy this code, customize it with your information, and host it on a platform like GitHub Pages, Netlify, or any web hosting service. I’ll explain each section and provide the code in markdown code blocks for easy reading.

---

## CV Website for You

A CV website showcases your professional background, skills, and contact information in an online format. Here’s a simple, responsive design with sections for an introduction, experience, education, skills, and contact details. You can edit the content with your own details.

### Steps to Use This Template
1. **Copy the Code**: Save the HTML and CSS into separate files (e.g., `index.html` and `styles.css`).
2. **Customize**: Replace the placeholder text with your personal information.
3. **Host**: Upload it to a web hosting service to make it live.
4. **Enhance**: Add images, links, or additional styling as needed.

### HTML Code (`index.html`)
This is the structure of your CV website.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Name - CV</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Your Name</h1>
        <p>Job Title | Your Tagline</p>
    </header>

    <section class="about">
        <h2>About Me</h2>
        <p>
            I am a [your profession] with [X years] of experience in [your field]. 
            Passionate about [your interests], I strive to [your goal]. 
            Based in [your location].
        </p>
    </section>

    <section class="experience">
        <h2>Experience</h2>
        <div class="job">
            <h3>Job Title</h3>
            <p class="company">Company Name | Start Date - End Date</p>
            <ul>
                <li>Responsibility or achievement 1</li>
                <li>Responsibility or achievement 2</li>
                <li>Responsibility or achievement 3</li>
            </ul>
        </div>
        <div class="job">
            <h3>Previous Job Title</h3>
            <p class="company">Previous Company | Start Date - End Date</p>
            <ul>
                <li>Responsibility or achievement 1</li>
                <li>Responsibility or achievement 2</li>
            </ul>
        </div>
    </section>

    <section class="education">
        <h2>Education</h2>
        <div class="degree">
            <h3>Degree Name</h3>
            <p>University Name | Year Graduated</p>
        </div>
    </section>

    <section class="skills">
        <h2>Skills</h2>
        <ul>
            <li>Skill 1</li>
            <li>Skill 2</li>
            <li>Skill 3</li>
            <li>Skill 4</li>
        </ul>
    </section>

    <section class="contact">
        <h2>Contact</h2>
        <p>Email: <a href="mailto:your.email@example.com">your.email@example.com</a></p>
        <p>Phone: (123) 456-7890</p>
        <p>LinkedIn: <a href="https://linkedin.com/in/yourprofile" target="_blank">linkedin.com/in/yourprofile</a></p>
        <p>Portfolio: <a href="https://yourportfolio.com" target="_blank">yourportfolio.com</a></p>
    </section>

    <footer>
        <p>&copy; 2023 Your Name. All rights reserved.</p>
    </footer>
</body>
</html>
```

### CSS Code (`styles.css`)
This styles the website to make it clean and professional.

```css
/* Reset default margins and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

header {
    text-align: center;
    padding: 20px 0;
    border-bottom: 2px solid #007BFF;
}

header h1 {
    font-size: 2.5em;
    color: #007BFF;
}

header p {
    font-size: 1.2em;
    color: #666;
}

section {
    margin: 20px 0;
}

h2 {
    color: #007BFF;
    border-bottom: 1px solid #ddd;
    padding-bottom: 5px;
    margin-bottom: 10px;
}

.job, .degree {
    margin-bottom: 20px;
}

.job h3, .degree h3 {
    font-size: 1.3em;
}

.company {
    font-style: italic;
    color: #666;
}

ul {
    list-style-type: disc;
    margin-left: 20px;
}

.skills ul {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.skills li {
    background: #f4f4f4;
    padding: 5px 10px;
    border-radius: 5px;
}

.contact a {
    color: #007BFF;
    text-decoration: none;
}

.contact a:hover {
    text-decoration: underline;
}

footer {
    text-align: center;
    padding: 10px 0;
    font-size: 0.9em;
    color: #666;
    border-top: 1px solid #ddd;
    margin-top: 20px;
}

/* Responsive Design */
@media (max-width: 600px) {
    header h1 {
        font-size: 2em;
    }

    header p {
        font-size: 1em;
    }

    body {
        padding: 10px;
    }
}
```

### Explanation of Sections
- **Header**: Displays your name and a tagline or job title.
- **About Me**: A brief introduction to who you are.
- **Experience**: Lists your work history with details.
- **Education**: Shows your academic background.
- **Skills**: Highlights your key abilities in a visually appealing way.
- **Contact**: Provides ways to reach you, with clickable links.
- **Footer**: Adds a professional touch with a copyright notice.

### Customization Tips
- **Personal Info**: Replace "Your Name," "Job Title," and other placeholders with your details.
- **Colors**: Change `#007BFF` (blue) in the CSS to a color you prefer (e.g., `#FF5733` for orange).
- **Add More**: Include a photo by adding `<img src="yourphoto.jpg" alt="Your Name" class="profile-pic">` in the header and styling it in CSS.
- **Links**: Update the LinkedIn and portfolio URLs to your actual profiles.

### Hosting Your Website
- **GitHub Pages**: Create a GitHub repository, upload these files, and enable GitHub Pages in the settings.
- **Netlify**: Drag and drop the folder with these files into Netlify’s dashboard for free hosting.
- **Domain**: Purchase a custom domain (e.g., `yourname.com`) and link it for a professional touch.

---

This template gives you a functional CV website. Let me know if you’d like additional features, such as a download button for a PDF resume or more advanced styling!