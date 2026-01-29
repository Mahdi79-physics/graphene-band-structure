import numpy as np
import matplotlib.pyplot as plt
from src.constants import a, t
from src.dispersion import graphene_energy

# k-space grid
kx = np.linspace(-np.pi/a, np.pi/a, 300)
ky = np.linspace(-np.pi/a, np.pi/a, 300)
KX, KY = np.meshgrid(kx, ky)

# energy bands
E_plus, E_minus = graphene_energy(KX, KY, a, t)

# high-symmetry points
Gamma = (0, 0)
M = (2*np.pi/(3*a), 0)
K = (2*np.pi/(3*a),  2*np.pi/(3*np.sqrt(3)*a))
Kp = (2*np.pi/(3*a), -2*np.pi/(3*np.sqrt(3)*a))

# plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(KX, KY, E_plus, cmap='plasma', alpha=0.9, linewidth=0)
ax.plot_surface(KX, KY, E_minus, cmap='plasma', alpha=0.9, linewidth=0)

for name, (x, y) in zip(['Γ', 'M', 'K', "K'"], [Gamma, M, K, Kp]):
    ax.scatter(x, y, 0, color='black', s=50)
    ax.text(x, y, 0.5, name, fontsize=12, ha='center')

ax.set_xlabel('$k_x$ (Å$^{-1}$)')
ax.set_ylabel('$k_y$ (Å$^{-1}$)')
ax.set_zlabel('Energy (eV)')
ax.set_title('3D Band Structure of Graphene')

ax.view_init(elev=20, azim=40)
plt.tight_layout()
plt.show()
