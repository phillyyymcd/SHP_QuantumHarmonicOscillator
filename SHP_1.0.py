import numpy as np
import matplotlib.pyplot as plt
import random, math

#Define Parameters
m = omega = hbar = 1.0
N_tau = 100
delta_tau = 

def qho_potential(x):
    return (m*(omega**2)*(x**2))/2

def qho_kinetic(x):
    return 1/2*(x[tau_new] - x[tau])**2

def local_action(x, tau, tau_new):
    return (1/2)*m*((x[tau_new] - x[tau])**2) + (1/2)*m*(omega**2)*(x[tau]**2)

def metropolis_update(x, tau, tau_new, tau_old):
    u = random.rand(-1,1)
    x[tau] = x[tau] + u
    S_old = local_action(x, tau_old, tau)
    S_new = local_action(x, tau, tau_new)
    if S_new > S_old:
        S_new = math.exp(-(S_new - S_old))
    return S_new

def monte_carlo():




