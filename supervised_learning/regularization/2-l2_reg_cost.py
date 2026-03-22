#!/usr/bin/env python3
""" L2 regularization cost"""
import tensorflow as tf


def l2_reg_cost(cost, model):
    """ L2 regularization cost """
    return cost + [layer.losses for layer in model.layers if layer.losses]
