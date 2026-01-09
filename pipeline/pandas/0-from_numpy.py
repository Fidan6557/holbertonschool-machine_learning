import pandas as pd


def from_numpy(array):
    """ creates a pd.DataFrame from a np.ndarray """
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return pd.DataFrame(array, columns = alphabet[:array.shape[1]])