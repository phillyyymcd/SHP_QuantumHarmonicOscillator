def local_action(path, tau, x, m_tilde, potential):
    """Contribution to the lattice action from site `tau` if it held value `x`.

    `potential` is a function V(x) that returns the (dimensionless) lattice
    potential at x, e.g. built with functions.potentials.harmonic(...).
    """
    N_tau = len(path)

    # Every site needs two neighbours but the array only has indicies from
    # 0 to N_tau-1, so the two ends would run off the array
    # the %N wraps the values around so the periodic boundary conditions are satisfied
    left = path[(tau - 1) % N_tau]
    right = path[(tau + 1) % N_tau]

    kinetic = (m_tilde / 2
               * ((x - left)**2 + (right - x)**2))

    return kinetic + potential(x)
