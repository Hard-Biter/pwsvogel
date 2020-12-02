import tensorflow
from tensorflow import keras
from tensorflow.keras import layers


class Model:  # base class for model
    # --------------------------------------------------------------------------------------------------------
    # Build the model
    # --------------------------------------------------------------------------------------------------------
    def build_model():
        model = tensorflow.keras.Sequential([
            layers.Flatten(input_shape=(30,)),
            layers.Dense(32, activation='relu'),
            layers.Dropout(.4),
            # layers.Dense(32, activation='relu'),
            # layers.Dropout(.4),
            # layers.Dense(32, activation='relu'),
            layers.Dense(11, activation='relu')
        ])

        model.summary()
        model.compile(optimizer='RMSprop', loss=keras.losses.MeanSquaredLogarithmicError(  # adadelta, adagrad
        ), metrics=['accuracy'])
        return model

        # --------------------------------------------------------------------------------------------------------
        # Predict with model.
        # --------------------------------------------------------------------------------------------------------
    def predict_with_model(model, input_data):
        predicted_data = model.predict(x=input_data)
        return predicted_data
