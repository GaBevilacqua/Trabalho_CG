import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Funções para os modelos de iluminação
def modelo1(Ia, Ka, Il, Kd, cos_theta, **kwargs):
    return Ia * Ka + Il * Kd * cos_theta

def modelo2(Ia, Ka, Il, Kd, Ks, cos_theta, cos_alpha, d, K, n, **kwargs):
    return Ia * Ka + (Il / (d + K)) * (Kd * cos_theta + Ks * cos_alpha**n)

# Função para calcular a iluminação em cada ponto do objeto
def calcular_iluminacao(modelo, x, y, z, observador, luz, Ka, Kd, Ks, **kwargs):
    L = luz - np.array([x, y, z])
    L = L / np.linalg.norm(L)

    N = np.array([0, 0, 1])  # Normal padrão (para simplificação)
    V = observador - np.array([x, y, z])
    V = V / np.linalg.norm(V)

    R = 2 * np.dot(L, N) * N - L

    cos_theta = max(np.dot(L, N), 0)
    cos_alpha = max(np.dot(R, V), 0)

    if modelo == modelo1:
        return modelo(Ia=kwargs['Ia'], Ka=Ka, Il=kwargs['Il'], Kd=Kd, cos_theta=cos_theta)
    elif modelo == modelo2:
        return modelo(Ia=kwargs['Ia'], Ka=Ka, Il=kwargs['Il'], Kd=Kd, Ks=Ks, cos_theta=cos_theta, cos_alpha=cos_alpha, 
                      d=kwargs['d'], K=kwargs['K'], n=kwargs['n'])

# Função para desenhar os objetos
def desenhar_esfera(ax, centro, raio, modelo, **kwargs):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = centro[0] + raio * np.outer(np.cos(u), np.sin(v))
    y = centro[1] + raio * np.outer(np.sin(u), np.sin(v))
    z = centro[2] + raio * np.outer(np.ones(np.size(u)), np.cos(v))

    intensidade = np.vectorize(lambda x, y, z: calcular_iluminacao(modelo, x, y, z, **kwargs))
    cor = intensidade(x, y, z)

    ax.plot_surface(x, y, z, facecolors=plt.cm.viridis(cor), rstride=5, cstride=5)

def desenhar_plano(ax, lado, modelo, **kwargs):
    x = np.linspace(-lado / 2, lado / 2, 100)
    y = np.linspace(-lado / 2, lado / 2, 100)
    x, y = np.meshgrid(x, y)
    z = np.zeros_like(x)

    intensidade = np.vectorize(lambda x, y, z: calcular_iluminacao(modelo, x, y, z, **kwargs))
    cor = intensidade(x, y, z)

    ax.plot_surface(x, y, z, facecolors=plt.cm.viridis(cor), rstride=5, cstride=5)

# Função principal para exibir a interface
def main():
    def atualizar_grafico():
        try:
            valores = {
                'Ia': float(entry_Ia.get()),
                'Il': float(entry_Il.get()),
                'Ka': float(entry_Ka.get()),
                'Kd': float(entry_Kd.get()),
                'Ks': float(entry_Ks.get()),
                'd': float(entry_d.get()),
                'K': float(entry_K.get()),
                'n': float(entry_n.get()),
            }

            observador = np.array([0, 0, 100])
            luz = np.array([100, 100, 100])

            # Escolher o modelo
            modelo = modelo1 if modelo_var.get() == "Modelo 1" else modelo2

            ax.clear()
            desenhar_esfera(ax, centro=[0, 0, 0], raio=50, modelo=modelo, 
                            observador=observador, luz=luz, **valores)
            desenhar_plano(ax, lado=100, modelo=modelo, 
                           observador=observador, luz=luz, **valores)

            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')

            canvas.draw()
        except ValueError:
            print("Por favor, insira valores válidos.")

    # Configuração da janela principal
    root = tk.Tk()
    root.title("Modelos de Iluminação")

    # Configuração do frame de entradas
    frame_inputs = tk.Frame(root)
    frame_inputs.pack(side=tk.LEFT, padx=10, pady=10)

    # Campos de entrada com valores padrão
    tk.Label(frame_inputs, text="Ia (Intensidade ambiente):").pack()
    entry_Ia = tk.Entry(frame_inputs)
    entry_Ia.insert(0, "0.5")  # Valor padrão
    entry_Ia.pack()

    tk.Label(frame_inputs, text="Il (Intensidade da luz):").pack()
    entry_Il = tk.Entry(frame_inputs)
    entry_Il.insert(0, "1.0")  # Valor padrão
    entry_Il.pack()

    tk.Label(frame_inputs, text="Ka (Coeficiente ambiente):").pack()
    entry_Ka = tk.Entry(frame_inputs)
    entry_Ka.insert(0, "0.3")  # Valor padrão
    entry_Ka.pack()

    tk.Label(frame_inputs, text="Kd (Coeficiente difuso):").pack()
    entry_Kd = tk.Entry(frame_inputs)
    entry_Kd.insert(0, "0.7")  # Valor padrão
    entry_Kd.pack()

    tk.Label(frame_inputs, text="Ks (Coeficiente especular):").pack()
    entry_Ks = tk.Entry(frame_inputs)
    entry_Ks.insert(0, "0.5")  # Valor padrão
    entry_Ks.pack()

    tk.Label(frame_inputs, text="d (Distância):").pack()
    entry_d = tk.Entry(frame_inputs)
    entry_d.insert(0, "2.0")  # Valor padrão
    entry_d.pack()

    tk.Label(frame_inputs, text="K (Constante):").pack()
    entry_K = tk.Entry(frame_inputs)
    entry_K.insert(0, "1.0")  # Valor padrão
    entry_K.pack()

    tk.Label(frame_inputs, text="n (Expoente):").pack()
    entry_n = tk.Entry(frame_inputs)
    entry_n.insert(0, "10")  # Valor padrão
    entry_n.pack()

    # Menu para selecionar o modelo
    tk.Label(frame_inputs, text="Selecione o modelo:").pack()
    modelo_var = tk.StringVar(value="Modelo 1")
    modelo_menu = tk.OptionMenu(frame_inputs, modelo_var, "Modelo 1", "Modelo 2")
    modelo_menu.pack()

    tk.Button(frame_inputs, text="Atualizar", command=atualizar_grafico).pack(pady=10)

    # Configuração da área de plotagem
    frame_plot = tk.Frame(root)
    frame_plot.pack(side=tk.RIGHT, padx=10, pady=10)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    canvas = FigureCanvasTkAgg(fig, master=frame_plot)
    canvas.get_tk_widget().pack()

    # Atualiza o gráfico automaticamente ao iniciar
    atualizar_grafico()

    root.mainloop()

if __name__ == "__main__":
    main()
