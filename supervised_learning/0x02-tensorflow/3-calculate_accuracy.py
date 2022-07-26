#!/usr/bin/env python3
"""Accuracy"""
import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """calculate_accuracy: calculates the accuracy of a prediction"

    Args:
        y :  is a placeholder for the labels of the input data
        y_pred is a tensor containing the network’s predictions

    Returns:
        a tensor containing the decimal accuracy of the prediction
    """
    label = tf.argmax(y, axis=1)
    pred = tf.argmax(y_pred, axis=1)
    accuracy = tf.reduce_mean(tf.cast(tf.equal(pred, label), tf.float32))
    return accuracy
