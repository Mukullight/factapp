const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'factapp')));

// Define routes for your HTML files
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'home.html'));
});

app.get('/data', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'data.html'));
});

app.get('/forums', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'forums.html'));
});

app.get('/details', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'details.html'));
});

app.get('/projects', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'projects.html'));
});



app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});