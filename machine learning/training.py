import tensorflow as tf

def train_model(data, labels, config):
    # Define the model architecture
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(config['hidden_units'], activation=config['activation']),
        tf.keras.layers.Dense(config['output_units'], activation=config['output_activation'])
    ])

    # Compile the model
    model.compile(optimizer=config['optimizer'],
                  loss=config['loss'],
                  metrics=[config['metric']])

    # Train the model
    model.fit(data, labels, epochs=config['epochs'], batch_size=config['batch_size'])

    return model
