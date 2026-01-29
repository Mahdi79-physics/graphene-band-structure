import numpy as np
import matplotlib.pyplot as plt
from src.constants import a, t
from src.dispersion import graphene_energy

Gamma = np.array([0, 0])
M = np.array([2*np.pi/(3*a), 0])
K = np.array([2*np.pi/(3*a), 2*np.pi/(3*np.sqrt(3)*a)])

points = [Gamma, M, K, Gamma]

def interpolate(p1, p2, n=200):
    return np.linspace(p1, p2, n)

k_path = np.concatenate([
    interpolate(points[i], points[i+1])
    for i in range(len(points)-1)
])

kx, ky = k_path[:,0], k_path[:,1]
E_plus, E_minus = graphene_energy(kx, ky, a, t)

k_dist = np.zeros(len(kx))
for i in range(1, len(kx)):
    k_dist[i] = k_dist[i-1] + np.linalg.norm([kx[i]-kx[i-1], ky[i]-ky[i-1]])

plt.plot(k_dist, E_plus, 'b')
plt.plot(k_dist, E_minus, 'r')
plt.ylabel('Energy (eV)')
plt.xlabel('k-path')
plt.title('Graphene Band Structure (Γ–M–K–Γ)')
plt.tight_layout()
plt.show()
