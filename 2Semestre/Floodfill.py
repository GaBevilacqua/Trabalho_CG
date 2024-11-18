import numpy as np
import matplotlib.pyplot as plt

# Função para visualizar a imagem
def plot_image(image):
    plt.imshow(image, cmap='hot', interpolation='nearest')
    plt.show()

# Matriz que representa a imagem:
# 0 = Branco, 1 = Vermelho (borda), 2 = Verde (seed)
image = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 3, 0, 0],
    [0, 0, 0, 0, 0, 3, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
])

# Função Seed-Fill Recursiva
def seed_fill(image, x, y, new_color):
    rows, cols = image.shape
    original_color = image[x, y]

    # Se o ponto já estiver preenchido ou for uma borda, saímos
    if original_color == new_color or original_color == 1:
        return

    # Preenchemos o ponto com a nova cor
    image[x, y] = new_color

    # Verificamos e chamamos recursivamente para os vizinhos (cima, baixo, esquerda, direita)
    if x + 1 < rows and image[x + 1, y] != 1 and image[x + 1, y] != new_color:
        seed_fill(image, x + 1, y, new_color)
    if x - 1 >= 0 and image[x - 1, y] != 1 and image[x - 1, y] != new_color:
        seed_fill(image, x - 1, y, new_color)
    if y + 1 < cols and image[x, y + 1] != 1 and image[x, y + 1] != new_color:
        seed_fill(image, x, y + 1, new_color)
    if y - 1 >= 0 and image[x, y - 1] != 1 and image[x, y - 1] != new_color:
        seed_fill(image, x, y - 1, new_color)

# Usando o ponto seed (1, 3) que é verde na imagem e preenchendo com a cor 4
seed_fill(image, 1, 3, new_color=4)
plot_image(image)
