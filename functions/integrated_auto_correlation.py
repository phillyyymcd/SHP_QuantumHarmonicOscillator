import warnings

import numpy as np


def integrated_auto_correlation(a, c=5):

    a = np.asarray(a) - np.mean(a) #ensuring series is centered (mean = 0)

    N = len(a)
    var = np.mean(a**2)
    max_lag = N//2

    #C(L) is the correlation between two measurements that are L sweeps apart
    #must be computed one at a time
    C = np.zeros(max_lag)

    if not np.isfinite(var) or var<=0:
        raise ValueError(
            "The series has zero or invalid variance;"
            "autocorrelation time cannot be estimated"
        )
    # a[:N-lag] is the series with the last entry chopped off
    # a[lag:] is the series with the first entry chopped off]
    for lag in range(max_lag):
        C[lag] = np.mean(a[:N-lag]*a[lag:]) / var

    A = np.cumsum(C[1:])

    tau_path = 1/2 + A

    #we will use Sokal's cutoff criterion to ensure that once the error reduces into noise we stop itnegrating
    for W in range(1, len(tau_path) + 1):
        tau_int = tau_path[W-1]
        if W >= c*tau_int:
            return tau_int, W, C, tau_path

    warnings.warn(
        "Sokal window criterion did not close."
        "The autocorrelation estimate may be unreliable;"
        "consider running more sweeps.",
        RuntimeWarning
    )

    #what to return if the window never closed due to not enough sweeps
    return tau_path[-1], max_lag, C, tau_path
