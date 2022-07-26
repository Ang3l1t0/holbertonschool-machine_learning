#!/usr/bin/env python3
"""
Evaluate
"""
import tensorflow as tf


def evaluate(X, Y, save_path):
    """evaluates the output of a neural network

    Args:
        X: is a numpy.ndarray containing the input data to evaluate
        Y: is a numpy.ndarray containing the one-hot labels for X
        save_path: is the location to load the model from

    Returns:
        the network’s prediction, accuracy, and loss, respectively
    """
    with tf.Session() as sess:
        loader = tf.train.import_meta_graph(save_path + '.meta')
        loader.restore(sess, save_path)

        var_names = ['x', 'y', 'y_pred', 'accuracy', 'loss']
        for var_name in var_names:
            globals()[var_name] = tf.get_collection(var_name)[0]
            # print(globals()[var_name])

        y_pred = sess.run(globals()['y_pred'], feed_dict={x: X, y: Y})
        loss = sess.run(globals()['loss'], feed_dict={x: X, y: Y})
        acc = sess.run(globals()['accuracy'], feed_dict={x: X, y: Y})

    return y_pred, acc, loss
