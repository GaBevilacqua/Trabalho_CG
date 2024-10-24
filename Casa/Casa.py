import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CasaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CASA")
        self.master.geometry("1200x700")

        # Inputs
        self.frame_left = tk.Frame(self.master)
        self.frame_left.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame_translation = tk.LabelFrame(self.frame_left, text="Translação", padx=10, pady=10)
        self.frame_translation.pack(padx=10, pady=10)
        tk.Label(self.frame_translation, text="X").pack()
        self.input_transformacao_x = tk.Entry(self.frame_translation)
        self.input_transformacao_x.pack()
        tk.Label(self.frame_translation, text="Y").pack()
        self.input_transformacao_y = tk.Entry(self.frame_translation)
        self.input_transformacao_y.pack()
        tk.Label(self.frame_translation, text="Z").pack()
        self.input_transformacao_z = tk.Entry(self.frame_translation)
        self.input_transformacao_z.pack()

        self.frame_scale_local = tk.LabelFrame(self.frame_left, text="Escala Local", padx=10, pady=10)
        self.frame_scale_local.pack(padx=10, pady=10)
        tk.Label(self.frame_scale_local, text="X").pack()
        self.entry_escala_local_x = tk.Entry(self.frame_scale_local)
        self.entry_escala_local_x.pack()
        tk.Label(self.frame_scale_local, text="Y").pack()
        self.entry_escala_local_y = tk.Entry(self.frame_scale_local)
        self.entry_escala_local_y.pack()
        tk.Label(self.frame_scale_local, text="Z").pack()
        self.entry_escala_local_z = tk.Entry(self.frame_scale_local)
        self.entry_escala_local_z.pack()

        
        self.frame_scale_global = tk.LabelFrame(self.frame_left, text="Escala Global", padx=10, pady=10)
        self.frame_scale_global.pack(padx=10, pady=10)
        # Combobox para escolher o eixo
        tk.Label(self.frame_scale_global, text="Eixo:").pack()
        self.combo_axis = ttk.Combobox(self.frame_scale_global, values=["X", "Y", "Z"])
        self.combo_axis.pack()
        tk.Label(self.frame_scale_global, text="Angulo:").pack()
        self.entry_escala_global = tk.Entry(self.frame_scale_global)
        self.entry_escala_global.pack()

        # Shearing
        self.frame_shearing = tk.LabelFrame(self.master, text="Shearing", padx=10, pady=10)
        self.frame_shearing.pack(side=tk.LEFT, padx=10, pady=10)


        self.shearing_entries = []
        for i in range(4):
            row = []
            for j in range(4):
                entry = tk.Entry(self.frame_shearing, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row.append(entry)
            self.shearing_entries.append(row)

        inicial = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
        for i in range(4):
            for j in range(4):
                self.shearing_entries[i][j].insert(0, inicial[i][j])

        button = tk.Button(self.frame_left, text="TRANSFORMAR", command=self.Transformar)
        button.pack(pady=20)

 
        self.frame_right = tk.Frame(self.master)
        self.frame_right.pack(side=tk.RIGHT, padx=10, pady=10)
        self.fig = plt.Figure(figsize=(7, 7), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_right)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.aplicar()

    #Tranformações
    def aplicar(self, transformacao_x=0, transformacao_y=0, transformacao_z=0, escala_local=None, escala_global=(1, 1, 1), matriz=None):
        # Definindo os vértices da casa
        vertices = [
            [0, 0, 0], [100, 0, 0], [100, 100, 0], [0, 100, 0],  
            [0, 0, 100], [100, 0, 100], [100, 100, 100], [0, 100, 100], 
            [50, 150, 0], [50, 150, 100] 
        ]

        # Translação
        verticesT = [[v[0] + transformacao_x, v[1] + transformacao_y, v[2] + transformacao_z] for v in vertices]

        # Escala local
        if escala_local is not None:
            Vertice_aux = [
                [v[0] * escala_local[0], v[1] * escala_local[1], v[2] * escala_local[2]] for v in verticesT
            ]
        else:
            Vertice_aux = verticesT

        # Escala global
        Vertice_aux = [
            [v[0] * escala_global[0], v[1] * escala_global[1], v[2] * escala_global[2]] for v in Vertice_aux
        ]

        # Cinsilhar
        if matriz is not None:
            verteces_matriz = []
            for v in Vertice_aux:
                x, y, z = v
                matriz_x = matriz[0][0] * x + matriz[0][1] * y + matriz[0][2] * z + matriz[0][3]
                matriz_y = matriz[1][0] * x + matriz[1][1] * y + matriz[1][2] * z + matriz[1][3]
                matriz_z = matriz[2][0] * x + matriz[2][1] * y + matriz[2][2] * z + matriz[2][3]
                verteces_matriz.append([matriz_x, matriz_y, matriz_z])
            Vertice_aux = verteces_matriz

        edges = [[Vertice_aux[j] for j in [0, 1, 2, 3, 0]], 
                 [Vertice_aux[j] for j in [4, 5, 6, 7, 4]],  
                 [Vertice_aux[j] for j in [0, 4]],  
                 [Vertice_aux[j] for j in [1, 5]],  
                 [Vertice_aux[j] for j in [2, 6]],  
                 [Vertice_aux[j] for j in [3, 7]],  
                 [Vertice_aux[j] for j in [7, 9]],  
                 [Vertice_aux[j] for j in [6, 9]],  
                 [Vertice_aux[j] for j in [3, 8]],  
                 [Vertice_aux[j] for j in [2, 8]],  
                 [Vertice_aux[j] for j in [8, 9]]]  

        self.ax.cla()
        for edge in edges:
            self.ax.plot3D(*zip(*edge), color='b')
        self.ax.set_xlim([0, 300])
        self.ax.set_ylim([0, 300])
        self.ax.set_zlim([0, 300])
        self.ax.set_xlabel("Eixo X")
        self.ax.set_ylabel("Eixo Y")
        self.ax.set_zlabel("Eixo Z")
        self.canvas.draw()

    #Coletar
    def Transformar(self):
        transformacao_x = self.try_parse_float(self.input_transformacao_x.get())
        transformacao_y = self.try_parse_float(self.input_transformacao_y.get())
        transformacao_z = self.try_parse_float(self.input_transformacao_z.get())
        escala_local_x = self.try_parse_float(self.entry_escala_local_x.get())
        escala_local_y = self.try_parse_float(self.entry_escala_local_y.get())
        escala_local_z = self.try_parse_float(self.entry_escala_local_z.get())
        escala_local = (escala_local_x, escala_local_y, escala_local_z)
        valor_global = self.try_parse_float(self.entry_escala_global.get())
        axis = self.combo_axis.get()
        escala_global = [1, 1, 1]
        if axis == "X":
            escala_global[0] = valor_global
        elif axis == "Y":
            escala_global[1] = valor_global
        elif axis == "Z":
            escala_global[2] = valor_global
        matriz = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append(self.try_parse_float(self.shearing_entries[i][j].get()))
            matriz.append(row)

        self.aplicar(transformacao_x, transformacao_y, transformacao_z, escala_local, escala_global, matriz)

    def try_parse_float(self, value):
        try:
            return float(value)
        except ValueError:
            return 1.0  

root = tk.Tk()
app = CasaApp(root)
root.mainloop()