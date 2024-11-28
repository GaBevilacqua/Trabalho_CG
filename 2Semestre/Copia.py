import numpy as np
import matplotlib.pyplot as plt

def desenhar_varias_linhas_com_espelhamento():
    # Configurar a figura
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_title("Desenhe no lado esquerdo. O espelhamento aparece automaticamente no lado direito.")
    ax.axvline(0, color="black", linestyle="--", linewidth=1)  # Linha divisória
    ax.grid(True)

    # Armazenar todas as linhas desenhadas e suas espelhadas
    linhas_x = []
    linhas_y = []

    # Listas temporárias para armazenar pontos de uma linha
    temp_x = []
    temp_y = []

    def on_press(event):
        # Iniciar uma nova linha se o botão esquerdo for pressionado
        if event.button == 1 and event.inaxes == ax:
            temp_x.clear()
            temp_y.clear()

    def on_move(event):
        # Desenhar enquanto o botão esquerdo estiver pressionado
        if event.button == 1 and event.inaxes == ax:
            x, y = event.xdata, event.ydata
            if x <= 0:  # Apenas desenhar no lado esquerdo
                temp_x.append(x)
                temp_y.append(y)

                # Atualizar o desenho
                ax.plot(temp_x, temp_y, 'b-', lw=2)
                ax.plot([-xi for xi in temp_x], temp_y, 'r-', lw=2)  # Espelhamento
                fig.canvas.draw()

    def on_release(event):
        # Finalizar a linha atual
        if event.button == 1 and event.inaxes == ax:
            linhas_x.extend(temp_x)
            linhas_y.extend(temp_y)

    # Conectar eventos de mouse
    fig.canvas.mpl_connect("button_press_event", on_press)
    fig.canvas.mpl_connect("motion_notify_event", on_move)
    fig.canvas.mpl_connect("button_release_event", on_release)

    plt.show()

    return np.array(linhas_x), np.array(linhas_y)

def criar_objeto_3d(x, y):
    # Ordenar os pontos pelo eixo Y
    sorted_indices = np.argsort(y)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]

    # Criar a malha para rotação
    theta = np.linspace(0, 2 * np.pi, 100)
    theta_grid, y_grid = np.meshgrid(theta, y_sorted)

    # Coordenadas 3D
    x_3d = np.outer(x_sorted, np.cos(theta))
    z_3d = np.outer(x_sorted, np.sin(theta))
    y_3d = y_grid

    return x_3d, y_3d, z_3d

def visualizar_objeto_3d(x, y, z):
    # Visualizar o objeto 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, color='c', alpha=0.8, edgecolor='k')

    ax.set_title("Objeto 3D Obtido")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()

# Programa principal
linhas_x, linhas_y = desenhar_varias_linhas_com_espelhamento()

# Usar apenas o lado direito positivo para criar o perfil de rotação
perfil_x = np.concatenate([linhas_x, -np.array(linhas_x)])
perfil_y = np.concatenate([linhas_y, linhas_y])

# Gerar o objeto 3D
x_3d, y_3d, z_3d = criar_objeto_3d(perfil_x, perfil_y)

# Visualizar o objeto 3D
visualizar_objeto_3d(x_3d, y_3d, z_3d)
