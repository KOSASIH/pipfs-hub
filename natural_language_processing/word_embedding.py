import tensorflow as tf
from tensorflow.keras.layers import Embedding

def generate_word_embeddings(vocab_size, embedding_dim):
    # Generate word embeddings using a pre-trained embedding layer
    embeddings = Embedding(vocab_size, embedding_dim, input_length=1)

    return embeddings
