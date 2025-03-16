from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import json

app = Flask(__name__)
CORS(app)

# Load the model
model = tf.keras.models.load_model("plantdisease.h5")

# Load disease names from JSON
with open("class_labels.json", "r") as f:
    disease_labels = json.load(f)

# Preprocessing function
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize as per model input
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    image = Image.open(io.BytesIO(file.read()))
    processed_image = preprocess_image(image)
    
    prediction = model.predict(processed_image)
    predicted_class = np.argmax(prediction, axis=1)[0]
    confidence = float(np.max(prediction))
    disease_name = disease_labels.get(str(predicted_class), "Unknown ❓")

    return jsonify({
        "class": int(predicted_class),
        "disease": disease_name,
        "confidence": confidence
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
