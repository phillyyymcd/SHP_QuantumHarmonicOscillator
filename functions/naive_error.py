import numpy as np


def naive_error(a):
    a = np.asarray(a)
    return a.std(ddof=1)/np.sqrt(len(a))
