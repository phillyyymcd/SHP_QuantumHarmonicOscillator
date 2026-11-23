import numpy as np


def correlation(S):
    """Two-point correlation C(n) from an (N_sweeps, N_tau) array of paths."""
    S = np.array(S)

    if S.ndim != 2:
        raise ValueError("Expected a 2D array of shape (N_sweeps, N_tau)")

    N_sweeps_local, N_tau_local = S.shape

    C = np.zeros(N_tau_local)

    for n in range(N_tau_local):
        C[n] = np.mean(S * np.roll(S, -n, axis=1)) - S.mean()**2
    return C
