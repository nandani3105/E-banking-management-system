const tabButtons = document.querySelectorAll(".tab-button");
const tabContents = document.querySelectorAll(".tab-content");

tabButtons.forEach(button => {
  button.addEventListener("click", () => {
    tabButtons.forEach(btn => btn.classList.remove("active"));
    tabContents.forEach(content => content.classList.remove("active"));

    button.classList.add("active");
    const tabId = button.getAttribute("data-tab");
    const tab = document.getElementById(tabId);
    tab.classList.add("active");

    // If Photo tab is activated, start webcam
    if (tabId === "photo-tab") {
      startWebcam();
    }
  });
});

function startWebcam() {
  const video = document.getElementById("video");
  if (!video.srcObject) {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        video.srcObject = stream;
      })
      .catch(err => {
        alert("Webcam error: " + err);
      });
  }
}

// Photo capture
document.getElementById("captureBtn").addEventListener("click", () => {
  const video = document.getElementById("video");
  const canvas = document.getElementById("canvas");
  const photoInput = document.getElementById("kycPhotoData");

  canvas.style.display = "block";
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);
  const dataURL = canvas.toDataURL("image/png");
  photoInput.value = dataURL;
});
