document.getElementById('file').addEventListener('change', function(e) {
  const file = e.target.files[0];
  if (file) {
      document.getElementById('file-name').textContent = file.name;
      const reader = new FileReader();
      reader.onload = function(event) {
          const imgElement = document.getElementById('preview-img');
          imgElement.src = event.target.result;
          imgElement.style.display = "block";
          imgElement.style.width = "200px";  // Fixed width
          imgElement.style.height = "200px"; // Fixed height
          imgElement.style.objectFit = "cover"; // Maintain aspect ratio
          imgElement.style.borderRadius = "8px"; // Rounded corners
      };
      reader.readAsDataURL(file);
  }
});


document.getElementById('upload-form').addEventListener('submit', function(e) {
  e.preventDefault();

  const resultBox = document.getElementById('result');
  const resultText = document.getElementById('result-text');
  const confidenceBar = document.getElementById('confidence-bar');
  const confidenceValue = document.getElementById('confidence-value');
  const plantType = document.getElementById('plant-select').value;

  resultBox.style.display = "block";
  resultText.textContent = '🔄 Analyzing...';
  confidenceBar.style.width = '0%';
  confidenceValue.textContent = '0%';

  const formData = new FormData();
  const fileInput = document.getElementById('file');
  formData.append('file', fileInput.files[0]);
  formData.append('plant_type', plantType); // Send plant type to backend

  fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      if (data.error) {
          resultText.textContent = '⚠️ Error: ' + data.error;
      } else {
          resultText.textContent = `🦠 Disease for ${plantType}: ${data.disease}`;
          const confidence = Math.round(data.confidence * 100);
          confidenceBar.style.width = confidence + '%';
          confidenceValue.textContent = confidence + '%';
      }
  })
  .catch(error => {
      resultText.textContent = '⚠️ Error: ' + error;
  });
});
