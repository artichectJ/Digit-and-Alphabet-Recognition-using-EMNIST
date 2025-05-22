# Digit-and-Alphabet-Recognition-using-EMNIST
This project aims to recognize handwritten digits and alphabets using a graphical user interface (GUI) built with Tkinter. The application utilizes the Keras library to obtain the EMNIST dataset and create a machine learning model for recognition.

# Features
 - CNN model built with Keras + TensorFlow backend
 - Trained on the **Extended MNIST (EMNIST)** dataset
 - Tkinter-based drawing canvas for digit/letter input
 - High accuracy on handwritten characters
 - PostScript-free image capture (cross-platform)

# Dataset
The model uses the EMNIST Balanced(https://www.nist.gov/itl/products-and-services/emnist-dataset) split, which includes:
 - **47 classes**: digits (0-9) + letters (A-Z, a-z) in balanced proportion
 - **Balanced across uppercase/lowercase**
 - Preprocessing includes grayscale normalization and resizing to 28x28
 - Download the matlab zip file

# Tech Stack

 - Python 3.8+
 - TensorFlow / Keras
 - NumPy
 - Pillow
 - Tkinter
 - Matlab

# Train the Model
The model is trained but if you want to retrain the model run the ml.py file which uses matplotlib to extract the emnist dataset downloaded as the matlab zip file.

After training the model gets saved as 'emnist_merge_model.h5' and 'emnist_merge_model.keras'

# Run the GUI App
Run the main.py file which will load a drawing window where we can:
 - Draw a digit or a letter
 - Click "recognize" to predict it
 - Click "clear" to reset the canvas

# Model Architecture
 - Conv2D → ReLU → MaxPooling
 - Conv2D → ReLU → MaxPooling
 - Flatten
 - Dense → ReLU
 - Dropout
 - Dense (softmax for classification)
