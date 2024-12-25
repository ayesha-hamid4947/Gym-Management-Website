// Array of background images
const images = [
    '/static/images/image1.jpg',
    '/static/images/image2.jpg',
    '/static/images/image3.jpg'
];

// Function to change background image every few seconds
let currentImageIndex = 0;
function changeBackgroundImage() {
    document.body.style.backgroundImage = `url(${images[currentImageIndex]})`;
    // Move to the next image in the array
    currentImageIndex = (currentImageIndex + 1) % images.length;
}

// Change background image every 5 seconds
setInterval(changeBackgroundImage, 5000);

// Initial background image set on page load
changeBackgroundImage();
