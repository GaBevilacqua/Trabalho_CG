import numpy as np
import matplotlib.pyplot as plt

# Matriz que representa a imagem
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

# Função para visualizar a imagem
def plot_image(image):
    plt.imshow(image, cmap='hot', interpolation='nearest')
    plt.show()

# Definindo a bounding box (linhas e colunas de início e fim)
row_start, row_end = 1, 9  # Exemplo de range de linhas
col_start, col_end = 1, 12  # Exemplo de range de colunas

# Inverter as cores na bounding box
inverted_image = image.copy()
for i in range(row_start, row_end):
    for j in range(col_start, col_end):
        if inverted_image[i, j] == 0:
            inverted_image[i, j] = 1
        elif inverted_image[i, j] == 1:
            inverted_image[i, j] = 0

plot_image(inverted_image)
