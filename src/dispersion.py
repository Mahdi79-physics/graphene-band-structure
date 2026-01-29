import numpy as np

def graphene_energy(kx, ky, a, t):
    term = (
        1
        + 4*np.cos(np.sqrt(3)*ky*a/2)*np.cos(3*kx*a/2)
        + 4*np.cos(np.sqrt(3)*ky*a/2)**2
    )
    E_plus =  t * np.sqrt(term)
    E_minus = -E_plus
    return E_plus, E_minus
