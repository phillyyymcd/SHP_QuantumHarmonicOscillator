"""Lattice potentials (dimensionless units).

Each function here takes the physical parameters and returns a function V(x),
which is what local_action / metropolis_sweep expect as `potential`.
"""


def harmonic(m_tilde, omega_tilde):
    def V(x):
        return 0.5 * m_tilde * omega_tilde**2 * x**2
    return V


def anharmonic(m_tilde, omega_tilde, lam):
    def V(x):
        quadratic = 0.5 * m_tilde * omega_tilde**2 * x**2  # taken from westbroek
        quartic = lam * m_tilde**2 * omega_tilde**3 * x**4
        # quartic = lam * (x**4) * delta_tau**4  # taken from westbroek
        return quadratic + quartic
    return V
