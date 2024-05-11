import tensorflow as tf


def evaluate_model(model, data, labels):
    # Evaluate the performance of the trained model
    loss, metric = model.evaluate(data, labels)

    return loss, metric
