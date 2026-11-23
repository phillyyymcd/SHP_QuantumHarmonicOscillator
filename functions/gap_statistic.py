import numpy as np


def gap_statistic(S, n, a):
    """Energy gap E_1 - E_0 (physical units) from the slope of ln C(tau).

    S : (N_sweeps, N_tau) array of paths
    n : lattice separation to compare with tau = 0 (physical tau = n * a)
    a : lattice spacing delta_tau

    Uses C(tau) ~ exp(-(E_1 - E_0) tau), so  E_1 - E_0 = -ln(C(n a) / C(0)) / (n a).
    For the harmonic oscillator only one excited state contributes, so any n works;
    for the anharmonic oscillator n should be on the plateau of the effective energy.
    """
    S = np.asarray(S)
    x_bar = S.mean()
    C_0 = np.mean(S * S) - x_bar**2
    C_n = np.mean(S * np.roll(S, -n, axis=1)) - x_bar**2
    ratio = C_n / C_0
    return -np.log(ratio) / (n * a) if ratio > 0 else np.nan
