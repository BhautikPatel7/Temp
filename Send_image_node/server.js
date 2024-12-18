const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware to parse JSON and URL-encoded request bodies
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// Endpoint to receive the image via GET request
app.get('/upload', (req, res) => {
    // Get the Base64 encoded image data from query parameter
    const base64Image = req.query.image;

    // Decode Base64 and save the image locally
    if (base64Image) {
        const imageData = Buffer.from(base64Image, 'base64');
        const imagePath = path.join(__dirname, 'img.png');

        // Write the image file
        fs.writeFile(imagePath, imageData, (err) => {
            if (err) {
                console.error('Error saving image:', err);
                res.status(500).send('Error saving image');
            } else {
                console.log('Image saved successfully:', imagePath);
                res.send('Image uploaded and saved successfully');
            }
        });
    } else {
        res.status(400).send('Base64 image data not provided');
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
