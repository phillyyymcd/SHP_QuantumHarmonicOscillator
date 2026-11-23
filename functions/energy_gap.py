import numpy as np

from .correlation import correlation


def energy_gap(data):
    c = correlation(data)[:5]
    ratio = c[1:] / c[:-1]
    return -np.log(np.where(ratio > 0, ratio, np.nan))
