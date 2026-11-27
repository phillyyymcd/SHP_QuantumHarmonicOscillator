import numpy as np

from .correlation import correlation


def energy_gap(data, n_max):
    """Effective gap -ln(C(n+1)/C(n)) for n = 0 .. n_max-2."""
    c = correlation(data)[:n_max]
    ratio = c[1:] / c[:-1]
    return -np.log(np.where(ratio > 0, ratio, np.nan))
