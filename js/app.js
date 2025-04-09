const express = require("express");
const fetch = require("node-fetch"); // Add this dependency
const app = express();
const port = 3000;

app.use(express.static("public")); // Serve static files from 'public' folder
app.use(express.json());

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});

app.post("/search", async (req, res) => {
  const query = req.body.query;
  const response = await fetch("http://python-app:5000/search", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query }),
  });
  const data = await response.json();
  res.json(data);
});

app.listen(port, () => {
  console.log(`App running at http://localhost:${port}`);
});
