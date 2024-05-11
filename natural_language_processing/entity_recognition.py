import tensorflow as tf

def train_entity_recognition_model(data, labels, config):
    # Define the model architecture
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(config['vocab_size'], config['embedding_dim'], input_length=config['max_sequence_length']),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(config['hidden_units'], return_sequences=True)),
        tf.keras.layers.Dense(config['output_units'], activation=config['output_activation'])
    ])

    # Compile the model
    model.compile(optimizer=config['optimizer'],
                  loss=config['loss'],
                  metrics=[config['metric']])

    # Train the model
    model.fit(data, labels, epochs=config['epochs'], batch_size=config['batch_size'])

    return model
