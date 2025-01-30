from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from PIL import Image
import numpy as np
import json
import os
from urllib.parse import quote

app = Flask(__name__)

# Load the TFLite model and allocate tensors
def load_tflite_model(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

# interpreter = tf.lite.Interpreter(model_path=r'C:\Users\VEDANSHI\OneDrive\Desktop\plant\model.tflite')
# # Load the compressed TFLite model
interpreter = load_tflite_model(r'C:\Users\VEDANSHI\OneDrive\Desktop\plant\model.tflite')

# Load class labels
with open(r'C:\Users\VEDANSHI\OneDrive\Desktop\plant\class_labels.json', 'r') as f:
    labels = json.load(f)

# Preprocess the image
def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((224, 224))  # Ensure this matches the TFLite model input size
    img = np.array(img) / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0).astype(np.float32)
    return img

# Run inference with the TFLite model
def predict_tflite(interpreter, input_data):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Set input tensor
    interpreter.set_tensor(input_details[0]['index'], input_data)

    # Run inference
    interpreter.invoke()

    # Get output tensor
    output = interpreter.get_tensor(output_details[0]['index'])
    return output

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    try:
        image_path = 'temp_image.jpg'
        file.save(image_path)

        # Preprocess the image
        img = preprocess_image(image_path)

        # Make prediction using TFLite model
        prediction = predict_tflite(interpreter, img)
        predicted_class = np.argmax(prediction, axis=1)[0]
        confidence = float(np.max(prediction))  # Get confidence score

        predicted_label = labels[str(predicted_class)]

        os.remove(image_path)  # Clean up temporary image

        return jsonify({
            'prediction': predicted_label,
            'confidence': confidence * 100  # Convert to percentage
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
