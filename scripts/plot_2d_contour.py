import numpy as np
import matplotlib.pyplot as plt
from src.constants import a, t
from src.dispersion import graphene_energy

# k-space grid
kx = np.linspace(-np.pi/a, np.pi/a, 400)
ky = np.linspace(-np.pi/a, np.pi/a, 400)
KX, KY = np.meshgrid(kx, ky)

# conduction band
E_plus, _ = graphene_energy(KX, KY, a, t)

# high-symmetry points
Gamma = (0, 0)
M = (2*np.pi/(3*a), 0)
K = (2*np.pi/(3*a),  2*np.pi/(3*np.sqrt(3)*a))
Kp = (2*np.pi/(3*a), -2*np.pi/(3*np.sqrt(3)*a))

# plot
plt.figure(figsize=(7,6))
cont = plt.contourf(KX, KY, E_plus, levels=80, cmap='plasma')
plt.colorbar(cont, label='Energy (eV)')

for name, (x, y) in zip(['Γ', 'M', 'K', "K'"], [Gamma, M, K, Kp]):
    plt.scatter(x, y, color='black', s=40)
    plt.text(x, y, name, color='white', fontsize=12,
             ha='center', va='center',
             bbox=dict(facecolor='black', alpha=0.5, lw=0))

plt.xlabel('$k_x$ (Å$^{-1}$)')
plt.ylabel('$k_y$ (Å$^{-1}$)')
plt.title('2D Energy Contour of Graphene (Conduction Band)')
plt.tight_layout()
plt.show()
