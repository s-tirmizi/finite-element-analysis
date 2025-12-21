import numpy as np
import matplotlib.pyplot as plt

# 1. Setup the Mesh
# We use a grid from -1 to 1 to match the visual plots, 
# even though the text mentions (0,1)^2.
n_points = 21
x = np.linspace(-1, 1, n_points)
y = np.linspace(-1, 1, n_points)
X, Y = np.meshgrid(x, y)

# 2. Define the Fields
# Displacement u(x) = 0.1x_1 e_1 - 0.1x_2 e_2
U = 0.1 * X
V = -0.1 * Y
Displacement_Mag = np.sqrt(U**2 + V**2)

# Strains (constant over the body)
# e11 = 0.1, e22 = -0.1
E11 = np.full_like(X, 0.1)
E22 = np.full_like(X, -0.1)

# 3. Plotting
fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

# --- Plot 1: Displacement Magnitude & Vectors ---
# We use pcolormesh for the magnitude background
# cmap='plasma' is a good approximation for the blue-orange gradient
im1 = axes[0].pcolormesh(X, Y, Displacement_Mag, cmap='plasma', shading='auto')
# We use quiver for the arrows
axes[0].quiver(X, Y, U, V, color='black', alpha=0.6)
axes[0].set_title(r"Biaxial Loading (Displacements $\mathbf{u}$)")
fig.colorbar(im1, ax=axes[0], orientation='horizontal', fraction=0.05, pad=0.1)

# --- Plot 2: Strain e11 ---
# Since the value is constant (0.1), the whole plot is one color.
# We set vmin/vmax to give it context or match a specific range.
im2 = axes[1].pcolormesh(X, Y, E11, cmap='plasma', vmin=0, vmax=0.2, shading='auto')
axes[1].set_title(r"Biaxial Loading (Strain $\varepsilon_{11} = 0.1$)")
fig.colorbar(im2, ax=axes[1], orientation='horizontal', fraction=0.05, pad=0.1)

# --- Plot 3: Strain e22 ---
im3 = axes[2].pcolormesh(X, Y, E22, cmap='plasma', vmin=-0.2, vmax=0, shading='auto')
axes[2].set_title(r"Biaxial Loading (Strain $\varepsilon_{22} = -0.1$)")
fig.colorbar(im3, ax=axes[2], orientation='horizontal', fraction=0.05, pad=0.1)

# Formatting axes
for ax in axes:
    ax.set_aspect('equal')
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")

plt.tight_layout()
plt.savefig("1.png")
plt.show()