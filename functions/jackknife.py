import numpy as np


def jackknife(S, B, statistic):
    S = np.array(S)
    N = len(S)

    remainder = N % B
    if remainder != 0:
        S = S[remainder:]
        N = len(S)

    N_blocks = N // B
    if N_blocks < 2:
        raise ValueError('Need at least 2 blocks.')

    estimates_j = []
    estimate = statistic(S)

    for i in range(N_blocks):
        start = i * B
        end = start + B

        S_leave_out = np.concatenate((S[:start], S[end:]), axis=0)
        estimates_j.append(statistic(S_leave_out))

    estimates_j = np.array(estimates_j)

    mean_j = estimates_j.mean(axis=0)
    var_j = (N_blocks - 1) / N_blocks * np.sum((estimates_j - mean_j)**2, axis=0)
    error_j = np.sqrt(var_j)

    return estimate, error_j
