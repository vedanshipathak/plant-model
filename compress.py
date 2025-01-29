import tensorflow as tf

# Load the Keras model
model = tf.keras.models.load_model(r"C:\Users\VEDANSHI\OneDrive\Desktop\plant\plantdisease.h5")  # Replace with your .h5 model file

# Convert the model to TFLite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # Apply default optimizations
tflite_model = converter.convert()

# Save the compressed model
with open("model.tflite", "wb") as f:
    f.write(tflite_model)

print("Model successfully converted to TensorFlow Lite and saved as model.tflite")
