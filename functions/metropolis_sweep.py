import numpy as np

from .local_action import local_action


def metropolis_sweep(path, h, m_tilde, potential):
    """One Metropolis sweep over the lattice.

    path      : array of x values on the time lattice (updated in place)
    h         : maximum step size for proposed moves
    m_tilde   : dimensionless mass
    potential : function V(x), e.g. functions.potentials.harmonic(m_tilde, omega_tilde)
    """

    #for every lattice site:
    #choose a site               (1)
    #propose a new x             (2)
    #calculate ΔS                (3)
    #decide whether to accept    (4)

    acceptance = 0
    N_tau = len(path) #define number of elements in time lattice

    for i in range(N_tau):
        tau = np.random.randint(N_tau) #(1), choosing random site to start at
        #tau = i #option for going through systematically instead of randomly
        j = np.random.uniform(-h, h) #generating the amount to change the site to

        x_old = path[tau] #defining old position in array
        x_new = x_old + j #(2)

        S_old = local_action(path, tau, x_old, m_tilde, potential)
        S_new = local_action(path, tau, x_new, m_tilde, potential)

        dS = S_new - S_old #(3)
        if dS <= 0 or np.random.rand() < np.exp(-dS): #(4)
            path[tau] = x_new
            acceptance += 1
                # New values that lower the action are always accepted
                # While those that would increase the action are
                # accepted with probablity exp(-delta_S)
    acc_rate = acceptance/N_tau

    return path, acc_rate
