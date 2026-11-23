import numpy as np


def fit_continuum(a, y, y_err, order=1):
    """Weighted fit of y(a) = y_cont + c_1 a^2 (+ c_2 a^4 if order=2).

    Returns (y_cont, y_cont_err, coef, cov, chi2_dof).
    coef is in np.polyfit order (highest power of a^2 first), so coef[-1] = y_cont.
    """
    a, y, y_err = np.asarray(a), np.asarray(y), np.asarray(y_err)
    x = a**2

    coef, cov = np.polyfit(x, y, order, w=1/y_err, cov="unscaled")

    dof = len(y) - (order + 1)
    chi2 = np.sum(((y - np.polyval(coef, x)) / y_err)**2)
    chi2_dof = chi2 / dof if dof > 0 else np.nan

    return coef[-1], np.sqrt(cov[-1, -1]), coef, cov, chi2_dof
