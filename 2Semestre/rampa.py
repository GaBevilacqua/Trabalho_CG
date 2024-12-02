import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Função para calcular a superfície bilinear
def bilinear_surface(p1, p2, p3, p4, resolution=10):
    u = np.linspace(0, 1, resolution)
    v = np.linspace(0, 1, resolution)
    u, v = np.meshgrid(u, v)

    surface = (
        (1 - u)[:, :, np.newaxis] * (1 - v)[:, :, np.newaxis] * np.array(p1) +
        u[:, :, np.newaxis] * (1 - v)[:, :, np.newaxis] * np.array(p2) +
        u[:, :, np.newaxis] * v[:, :, np.newaxis] * np.array(p3) +
        (1 - u)[:, :, np.newaxis] * v[:, :, np.newaxis] * np.array(p4)
    )
    return surface[:, :, 0], surface[:, :, 1], surface[:, :, 2]

# Configurações das superfícies
define_faces = [
    ("verde", [(0, 0, 80), (20, 0, 80), (20, 40, 80), (0, 40, 80)]),
    ("verde", [(0, 0, 0), (20, 0, 0), (20, 0, 80), (0, 0, 80)]),
    ("amarelo", [(20, 0, 80), (20, 0, 0), (20, 40, 00), (20, 40, 80)]),
    ("azul", [(20, 40, 80), (100, 40, 0), (100, 0, 0), (20, 0, 80)]),
    ("marron", [(100, 40, 0), (120, 40, 0), (120, 0, 0), (100, 0, 0)]),
    ("vermelho", [(20, 0, 0), (20, 40, 0), (100, 40, 0), (100, 0, 0)])
]

# Cores correspondentes a cada superfície
cores = {
    "verde": "green",
    "amarelo": "yellow",
    "azul": "blue",
    "marron": "brown",
    "vermelho": "red"
}

# Configuração do gráfico
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Adiciona as superfícies ao gráfico
for cor, pontos in define_faces:
    x, y, z = bilinear_surface(*pontos)
    ax.plot_surface(x, y, z, color=cores[cor], alpha=0.7, edgecolor='k')

# Configura os limites dos eixos
ax.set_xlim(0, 120)
ax.set_ylim(0, 40)
ax.set_zlim(0, 80)

# Adiciona rótulos aos eixos
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Mostra o gráfico
plt.show()