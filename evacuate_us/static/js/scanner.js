document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('fileInput');
    const scanButton = document.getElementById('scanButton');
    const scannedImages = document.getElementById('scannedImages');

   
    function captureImage() {
        const video = document.createElement('video');
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');

        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                video.srcObject = stream;
                video.play();

                video.addEventListener('loadedmetadata', function() {
                    canvas.width = video.videoWidth;
                    canvas.height = video.videoHeight;

                    setInterval(function() {
                        context.drawImage(video, 0, 0, canvas.width, canvas.height);
                        const imageUrl = canvas.toDataURL('image/jpeg'); 
                        const imageElement = new Image();
                        imageElement.src = imageUrl;
                        scannedImages.appendChild(imageElement);
                    }, 1000); 
                });
            })
            .catch(function(error) {
                console.error('Error accessing webcam:', error);
            });
    }

    scanButton.addEventListener('click', captureImage);

   
});
document.getElementById("image-input").addEventListener("change", function(event) {
    const inputImage = document.getElementById("input-image");
    const outputSvg = document.getElementById("output-svg");

   
    if (event.target.files.length > 0) {
        const selectedImage = event.target.files[0];

       
        inputImage.src = URL.createObjectURL(selectedImage);
        inputImage.style.display = "block";

       
        const convertedSvg = convertImageToSvg(selectedImage);

       
        outputSvg.value = convertedSvg;
    } else {
       
        inputImage.style.display = "none";
        outputSvg.value = "";
    }
});


function convertImageToSvg(imageFile) {
    
    return '<svg width="100" height="100"><circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" /></svg>';
}


