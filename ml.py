import numpy as np
import scipy.io
from keras import layers
from matplotlib import pyplot as plt
from tensorflow import keras

class Data:
    def __init__(self):
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None

        mat=scipy.io.loadmat('emnist-bymerge.mat')
        data=mat['dataset']

        x_train = data['train'][0, 0]['images'][0, 0]
        y_train = data['train'][0, 0]['labels'][0, 0]
        x_test = data['test'][0, 0]['images'][0, 0]
        y_test = data['test'][0, 0]['labels'][0, 0]

        
        # Reshape, normalize, and correct orientation
        self.x_train = x_train.reshape((-1, 28, 28)).astype("float32") / 255.0
        self.x_test = x_test.reshape((-1, 28, 28)).astype("float32") / 255.0

        # EMNIST images are transposed, fix that
        self.x_train = np.transpose(self.x_train, (0, 2, 1))
        self.x_test = np.transpose(self.x_test, (0, 2, 1))


        # Add a channels dimension - needed when passing through neural network
        self.x_train = np.expand_dims(self.x_train, -1)
        self.x_test = np.expand_dims(self.x_test, -1)

        self.y_train = y_train
        self.y_test = y_test
        # Convert class vectors to binary class matrices
        num_classes=47
        self.y_train = keras.utils.to_categorical(self.y_train, num_classes)
        self.y_test = keras.utils.to_categorical(self.y_test, num_classes)

        print(f"x_train shape: {self.x_train.shape} - y_train shape: {self.y_train.shape}")


class NeuralNetwork:
    def __init__(self):
        self.model = keras.Sequential(
            [
                keras.Input(shape=(28, 28, 1)),
                layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
                layers.MaxPooling2D(pool_size=(2, 2)),
                layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
                layers.MaxPooling2D(pool_size=(2, 2)),
                layers.Flatten(),
                layers.Dropout(0.5),
                layers.Dense(47, activation="softmax"),
            ]
        )

        self.model.summary()

    def train(self, data, batch_size=128, epochs=15):
        self.model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
        training_history = self.model.fit(data.x_train, data.y_train, batch_size=batch_size, epochs=epochs,
                                          validation_split=0.2)
        score = self.model.evaluate(data.x_test, data.y_test, verbose=0)
        print("Test loss:", score[0])
        print("Test accuracy:", score[1])
        return training_history

    @staticmethod
    def plot_learning_curve(training):
        plt.plot(training.history['loss'])
        plt.plot(training.history['val_loss'])
        plt.title('Learning Curve')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()


def main():
    data = Data()
    neural_network = NeuralNetwork()
    training = neural_network.train(data, 128, 50)
    neural_network.plot_learning_curve(training)

    # Save the trained model
    neural_network.model.save('emnist_merge_model.h5')
    neural_network.model.save('emnist_merge_model.keras')
    print("Model saved as 'emnist_merge_,odel.h5' and 'emnist_merge_model.keras'.")


if __name__ == "__main__":
    main()
