#!/usr/bin/env python3
"""
Train
"""
import tensorflow as tf
create_placeholders = __import__('0-create_placeholders').create_placeholders
forward_prop = __import__('2-forward_prop').forward_prop
calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
calculate_loss = __import__('4-calculate_loss').calculate_loss
create_train_op = __import__('5-create_train_op').create_train_op


def train(X_train, Y_train, X_valid, Y_valid, layer_sizes, activations, alpha,
          iterations, save_path="/tmp/model.ckpt"):
    """ builds, trains, and saves a neural network classifier

    Args:
        X_train : is a numpy.ndarray containing the training input data
        Y_train : is a numpy.ndarray containing the training labels
        X_valid : is a numpy.ndarray containing the validation input data
        Y_valid : is a numpy.ndarray containing the validation labels
        layer_sizes : is a list containing the number of nodes in
                        each layer of the network
        activations : is a list containing the activation functions
                        for each layer of the network
        alpha : is the learning rate
        iterations : is the number of iterations to train over
        save_path : designates where to save the model.
                    Defaults to "/tmp/model.ckpt".

    Returns:
        the path where the model was saved"""

    x, y = create_placeholders(X_train.shape[1], Y_train.shape[1])
    y_pred = forward_prop(x, layer_sizes, activations)
    accuracy = calculate_accuracy(y, y_pred)
    loss = calculate_loss(y, y_pred)
    train_op = create_train_op(loss, alpha)

    params = {'x': x, 'y': y, 'y_pred': y_pred, 'accuracy': accuracy,
              'loss': loss, 'train_op': train_op}
    for k, v in params.items():
        tf.add_to_collection(k, v)

    saver = tf.train.Saver()
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        for i in range(iterations + 1):
            sess.run(y_pred, feed_dict={x: X_train, y: Y_train})
            if i % 100 == 0 or i == iterations:
                loss_t = sess.run(loss, feed_dict={x: X_train, y: Y_train})
                acc_t = sess.run(accuracy, feed_dict={x: X_train, y: Y_train})
                loss_v = sess.run(loss, feed_dict={x: X_valid, y: Y_valid})
                acc_v = sess.run(accuracy, feed_dict={x: X_valid, y: Y_valid})
                print("After {} iterations:".format(i))
                print("\tTraining Cost: {}".format(loss_t))
                print("\tTraining Accuracy: {}".format(acc_t))
                print("\tValidation Cost: {}".format(loss_v))
                print("\tValidation Accuracy: {}".format(acc_v))
            if i < iterations:
                sess.run(train_op, feed_dict={x: X_train, y: Y_train})
        save_path = saver.save(sess, save_path)
    return save_path
