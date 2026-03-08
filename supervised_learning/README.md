# Neuron

This project implements a **Neuron class** that performs **binary classification**.

The neuron is initialized with a number of input features `nx`. The class validates that `nx` is a positive integer and raises the appropriate exceptions if not.

## Attributes

* **W**: Weights vector initialized using a random normal distribution.
* **b**: Bias initialized to `0`.
* **A**: Activated output (prediction) initialized to `0`.

## Requirements

* Python 3
* NumPy
