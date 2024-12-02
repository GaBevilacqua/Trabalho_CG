import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Função para gerar o objeto 1 (azul)
def objeto_azul(x_range, y_range):
    x, y = np.meshgrid(x_range, y_range)
    z = x**2 + y
    return x, y, z

# Função para gerar o objeto 2 (vermelho)
def objeto_vermelho(x_range, y_range):
    x, y = np.meshgrid(x_range, y_range)
    z = -3*x + 2*y + 5
    return x, y, z

# Função para gerar o objeto 3 (amarelo)
def objeto_amarelo(t_range, y_range):
    t = np.linspace(t_range[0], t_range[1], 100)
    y = np.linspace(y_range[0], y_range[1], 100)
    T, Y = np.meshgrid(t, y)  # Criando a grade 2D
    X = 30 + np.cos(T)  # x varia com t
    Z = 50 + np.sin(T)  # z varia com t
    return X, Y, Z

# Função para gerar o objeto 4 (verde)
def objeto_verde(a_range, b_range):
    a, b = np.meshgrid(a_range, b_range)
    x = 100 + 30 * np.cos(a) * np.cos(b)
    y = 50 + 30 * np.cos(a) * np.sin(b)
    z = 20 + 30 * np.sin(a)
    return x, y, z

# Função para gerar o objeto 5 (cubo branco)
def objeto_branco():
    # Cubo de lado 40 centrado na origem
    size = 20  # Lado/2, já que o cubo é de 40
    x = np.array([[-size, size], [-size, size], [-size, size], [-size, size]])
    y = np.array([[-size, -size], [-size, size], [-size, -size], [size, size]])
    z = np.array([[-size, -size], [size, size], [-size, -size], [-size, size]])
    return x, y, z

# Função para o Z-Buffer
def z_buffer(x, y, z, buffer, color, ax):
    # Plotando a superfície 3D com os valores corretos de x, y e z
    ax.plot_surface(x, y, z, color=color, rstride=1, cstride=1, alpha=0.7)

# Função para visualização com interação Tkinter
def visualizar():
    # Criando o Z-Buffer (inicializando com um valor alto)
    buffer = np.ones((100, 100)) * 1000

    # Criando a janela Tkinter
    root = tk.Tk()
    root.title("Visualização de Objetos 3D com Z-Buffer")

    # Criando o gráfico
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Gerando os objetos
    x1, y1, z1 = objeto_azul(np.linspace(10, 30, 100), np.linspace(20, 40, 100))
    x2, y2, z2 = objeto_vermelho(np.linspace(50, 100, 100), np.linspace(30, 80, 100))
    x3, y3, z3 = objeto_amarelo([0, 50], [30, 60])  # Adicionamos um intervalo para y
    x4, y4, z4 = objeto_verde(np.linspace(0, 2*np.pi, 100), np.linspace(0, 2*np.pi, 100))
    x5, y5, z5 = objeto_branco()

    # Aplicando Z-Buffer e renderizando cada objeto
    z_buffer(x1, y1, z1, buffer, 'b', ax)  # azul
    z_buffer(x2, y2, z2, buffer, 'r', ax)  # vermelho
    z_buffer(x3, y3, z3, buffer, 'y', ax)  # amarelo
    z_buffer(x4, y4, z4, buffer, 'g', ax)  # verde
    z_buffer(x5, y5, z5, buffer, 'w', ax)  # branco

    # Definindo limites
    ax.set_xlim([-50, 50])
    ax.set_ylim([-50, 50])
    ax.set_zlim([-50, 50])

    # Adicionando o gráfico no Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    # Botão para fechar a janela
    quit_button = tk.Button(root, text="Fechar", command=root.quit)
    quit_button.pack()

    # Iniciando o loop da interface gráfica
    root.mainloop()

# Executando a visualização
visualizar()
