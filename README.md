# Plant Disease Detection Model

This project utilizes the Xception model architecture with transfer learning to classify diseases in various plants based on images of their leaves. It achieved an accuracy of 99.61% using the PlantVillage dataset.

## Features

- **High Accuracy**: Achieved 99.61% accuracy through transfer learning.
- **Multi-class Classification**: Capable of identifying various plant diseases affecting crops like tomatoes, potatoes, and apples.

## Dataset

The model was trained using the PlantVillage dataset, which contains images of healthy and diseased plant leaves across multiple species.

## Model Architecture

The Xception model, a deep convolutional neural network architecture, was employed for this project. Transfer learning techniques were applied to leverage pre-trained weights, enhancing model performance on the plant disease classification task.

## Deployment

The model is deployed as a web application using Flask. Users can upload images of plant leaves, and the application will predict the presence and type of disease.

## Requirements

- Python 3.x
- Flask
- TensorFlow
- Other dependencies listed in `requirements.txt`

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/vedanshipathak/plant-model.git
   ```

2. Navigate to the project directory:

   ```bash
   cd plant-model
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python app.py
   ```

## Acknowledgements

- The PlantVillage dataset for providing the images used in training.
- The developers of the Xception model architecture.


