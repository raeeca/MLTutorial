#######################################
#  Tutorial credit: François Chollet
#######################################

import tensorflow as tf
from tensorflow import keras

model = keras.Sequential()

# Adds a densely-connected layer with 64 units to the model:
model.add(keras.layers.Dense(64, activation='relu'))
# Add another:
model.add(keras.layers.Dense(64, activation='relu'))
# Add a softmax layer with 10 output units:
model.add(keras.layers.Dense(10, activation='softmax'))


class CustomModel(keras.Model):
    def train_step(self, data):
        inputs, targets = data
        with tf.GradientTape() as tape:
            predictions = self(inputs, training=True)                       # forward pass
            loss = self.compiled_loss(targets, predictions)                 # forward pass
        gradients = tape.gradient(loss, model.trainable_weights)            # backwards pass
        optimizer.apply_gradients(zip(gradients, model.trainable_weights))  # backwards pass
        self.compiled_metrics.update_state(targets, predictions)            # update and return metrics
        return {m.name:m.results() for m in self.metrics}                   # update and return metrics


inputs = keras.Input(shape = (28*28,))
features = keras.layers.Dense(512, activation = 'relu')(inputs)
features = keras.layers.Dropout(0.5)(features)
outputs = keras.layers.Dense(10, activation='softmax')(features)
model = CustomModel(inputs, outputs)


##################################
#   use compile and fit as usual
##################################

opimizer = keras.optimizers.RMSprop()
loss = keras.losses.SparseCategoricalCrossentropy()
metrics = [keras.metrics.SparseCategoricalAccuracy()]

model.compile(opimizer, loss, metrics)
    
# model.fit(train_images, train_labels, epochs=3)
        
def main():
    print("python main function")
    main()
