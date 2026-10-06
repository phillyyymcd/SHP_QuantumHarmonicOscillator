import numpy as np
import matplotlib.pyplot as plt
import random, math

#Define Parameters
m = omega = hbar = 1.0
N_tau = 100
path = np.random.randn(N_tau)
beta = 10
delta_tau = beta / N_tau

#length of path is N_tau
def local_action(path, tau, x):
    N_tau = len(path)

    left = path[(tau - 1) % N_tau]
    right = path[(tau + 1) % N_tau]

    kinetic = (m / (2 * delta_tau) 
               * ((x - left)**2 + (right - x)**2))

    potential = (delta_tau
        * 0.5 * m * (omega**2) * (x**2))
    
    return kinetic + potential

#for every lattice site:
    #choose a site               (1)
    #propose a new x             (2)
    #calculate ΔS                (3)
    #decide whether to accept    (4)

def metropolis_sweep1(path, delta_tau):
    N_tau = len(path)

    for i in range(N_tau):
        tau = np.random.randint(N_tau) #(1)
        j = np.random.uniform(-1,1)

        x_old = path[tau] 
        x_new = x_old + j #(2)

        S_old = local_action(path, tau, x_old)
        S_new = local_action(path, tau, x_new)

        delta_S = S_new - S_old #(3)
        if delta_S <= 0: #(4)
            path[tau] = x_new
        else:
            if np.random.rand() < np.exp(-delta_S):
                path[tau] = x_new
                # New values that lower the action are always accepted
                # While those that would increase the action are 
                # accepted with probablity exp(-delta_S)

    return path

# below was my first attempt at this 
def metropolis_sweep2(path, h, m, omega):
    N_tau = len(path)
    
    index = random.randint(N_tau)

    for i in range(N_tau):
        j = random.rand(-1,1)
        tau = index[i]
        tau_min = (tau + N_tau - 1) % N_tau
        tau_max = (tau + 1) % N_tau 
        x_new = path[tau] + 2*
        S_old = local_action(path, tau, path[tau])
        S_new = local_action(path, tau, x_new)
        if S_new > S_old:
            S_new = math.exp(-(S_new - S_old))
        return S_new


