#!/usr/bin/env python3
"""Batch Normalization Upgraded"""
import tensorflow as tf


def create_batch_norm_layer(prev, n, activation):
    """create_batch_norm_layer: creates a batch normalization
                                layer for a neural network in tensorflow:

    Args:
        prev: is the activated output of the previous layer
        n: is the number of nodes in the layer to be created
        activation: is the activation function that should be used
                    on the output of the layer

    Returns:
        a tensor of the activated output for the layer
    """
    initializer = tf.contrib.layers.variance_scaling_initializer(
        mode="FAN_AVG")
    layer = tf.layers.Dense(units=n, activation=None,
                            kernel_initializer=initializer,
                            name='layer')

    m, v = tf.nn.moments(layer(prev), axes=[0])
    beta = tf.Variable(
        tf.zeros(shape=(1, n), dtype=tf.float32),
        trainable=True, name='beta'
    )
    gamma = tf.Variable(
        tf.ones(shape=(1, n), dtype=tf.float32),
        trainable=True, name='gamma'
    )
    epsilon = 1e-08

    Z_b_norm = tf.nn.batch_normalization(
        x=layer(prev), mean=m, variance=v, offset=beta, scale=gamma,
        variance_epsilon=epsilon, name=None
    )
    if activation:
        return activation(Z_b_norm)
    return Z_b_norm
