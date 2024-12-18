const fs = require('fs');
const axios = require('axios');
const path = require('path');

// Function to encode file data to Base64
function base64_encode(file) {
    // read binary data
    const bitmap = fs.readFileSync(file);
    // convert binary data to base64 encoded string
    return Buffer.from(bitmap).toString('base64');
}

// Path to the image file you want to upload
const imagePath = path.join(__dirname, 'img.png');

// Encode image to Base64
const base64Image = base64_encode(imagePath);

// URL of the server endpoint where you want to upload the image (localhost in this case)
const serverUrl = 'http://localhost:3000/upload';

// Construct the URL with the Base64 encoded image data as a query parameter
const urlWithParams = `${serverUrl}?image=${encodeURIComponent(base64Image)}`;

// Function to send image with retry logic
function sendImageWithRetry(url, retryCount = 3) {
    axios.get(url, {
        timeout: 10000, // 10 seconds timeout
        retryDelay: 1000, // 1 second delay between retries
        retry: 3 // retry 3 times
    })
    .then(response => {
        console.log('Server Response:', response.data);
    })
    .catch(error => {
        if (retryCount > 0) {
            console.log(`Error sending image. Retrying... Attempts left: ${retryCount}`);
            sendImageWithRetry(url, retryCount - 1);
        } else {
            console.error('Maximum retries reached. Could not send image.', error);
        }
    });
}

// Initiate sending with retry
sendImageWithRetry(urlWithParams);
