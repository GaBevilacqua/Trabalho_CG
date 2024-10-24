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
        self.entry_tx = tk.Entry(self.frame_translation)
        self.entry_tx.pack()
        tk.Label(self.frame_translation, text="Y").pack()
        self.entry_ty = tk.Entry(self.frame_translation)
        self.entry_ty.pack()
        tk.Label(self.frame_translation, text="Z").pack()
        self.entry_tz = tk.Entry(self.frame_translation)
        self.entry_tz.pack()

        self.frame_scale_local = tk.LabelFrame(self.frame_left, text="Escala Local", padx=10, pady=10)
        self.frame_scale_local.pack(padx=10, pady=10)
        tk.Label(self.frame_scale_local, text="X").pack()
        self.entry_local_scale_x = tk.Entry(self.frame_scale_local)
        self.entry_local_scale_x.pack()
        tk.Label(self.frame_scale_local, text="Y").pack()
        self.entry_local_scale_y = tk.Entry(self.frame_scale_local)
        self.entry_local_scale_y.pack()
        tk.Label(self.frame_scale_local, text="Z").pack()
        self.entry_local_scale_z = tk.Entry(self.frame_scale_local)
        self.entry_local_scale_z.pack()

        
        self.frame_scale_global = tk.LabelFrame(self.frame_left, text="Escala Global", padx=10, pady=10)
        self.frame_scale_global.pack(padx=10, pady=10)
        # Combobox para escolher o eixo
        tk.Label(self.frame_scale_global, text="Eixo:").pack()
        self.combo_axis = ttk.Combobox(self.frame_scale_global, values=["X", "Y", "Z"])
        self.combo_axis.pack()
        tk.Label(self.frame_scale_global, text="Angulo:").pack()
        self.entry_global_scale = tk.Entry(self.frame_scale_global)
        self.entry_global_scale.pack()

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

        button = tk.Button(self.frame_left, text="TRANSFORMAR", command=self.get_transformations)
        button.pack(pady=20)

 
        self.frame_right = tk.Frame(self.master)
        self.frame_right.pack(side=tk.RIGHT, padx=10, pady=10)
        self.fig = plt.Figure(figsize=(7, 7), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_right)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.apply_transformations()

    #Tranformações
    def apply_transformations(self, tx=0, ty=0, tz=0, local_scale=None, global_scale=(1, 1, 1), shearing_matrix=None):
        # Definindo os vértices da casa
        vertices = [
            [0, 0, 0], [100, 0, 0], [100, 100, 0], [0, 100, 0],  
            [0, 0, 100], [100, 0, 100], [100, 100, 100], [0, 100, 100], 
            [50, 150, 0], [50, 150, 100] 
        ]

        # Translação
        verticesT = [[v[0] + tx, v[1] + ty, v[2] + tz] for v in vertices]

        # Escala local
        if local_scale is not None:
            vertices_scaled = [
                [v[0] * local_scale[0], v[1] * local_scale[1], v[2] * local_scale[2]] for v in verticesT
            ]
        else:
            vertices_scaled = verticesT

        # Escala global
        vertices_scaled = [
            [v[0] * global_scale[0], v[1] * global_scale[1], v[2] * global_scale[2]] for v in vertices_scaled
        ]

        # Cinsilhar
        if shearing_matrix is not None:
            vertices_sheared = []
            for v in vertices_scaled:
                x, y, z = v
                sheared_x = shearing_matrix[0][0] * x + shearing_matrix[0][1] * y + shearing_matrix[0][2] * z + shearing_matrix[0][3]
                sheared_y = shearing_matrix[1][0] * x + shearing_matrix[1][1] * y + shearing_matrix[1][2] * z + shearing_matrix[1][3]
                sheared_z = shearing_matrix[2][0] * x + shearing_matrix[2][1] * y + shearing_matrix[2][2] * z + shearing_matrix[2][3]
                vertices_sheared.append([sheared_x, sheared_y, sheared_z])
            vertices_scaled = vertices_sheared

        edges = [[vertices_scaled[j] for j in [0, 1, 2, 3, 0]], 
                 [vertices_scaled[j] for j in [4, 5, 6, 7, 4]],  
                 [vertices_scaled[j] for j in [0, 4]],  
                 [vertices_scaled[j] for j in [1, 5]],  
                 [vertices_scaled[j] for j in [2, 6]],  
                 [vertices_scaled[j] for j in [3, 7]],  
                 [vertices_scaled[j] for j in [7, 9]],  
                 [vertices_scaled[j] for j in [6, 9]],  
                 [vertices_scaled[j] for j in [3, 8]],  
                 [vertices_scaled[j] for j in [2, 8]],  
                 [vertices_scaled[j] for j in [8, 9]]]  

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
    def get_transformations(self):
        tx = self.try_parse_float(self.entry_tx.get())
        ty = self.try_parse_float(self.entry_ty.get())
        tz = self.try_parse_float(self.entry_tz.get())
        local_scale_x = self.try_parse_float(self.entry_local_scale_x.get())
        local_scale_y = self.try_parse_float(self.entry_local_scale_y.get())
        local_scale_z = self.try_parse_float(self.entry_local_scale_z.get())
        local_scale = (local_scale_x, local_scale_y, local_scale_z)
        global_scale_value = self.try_parse_float(self.entry_global_scale.get())
        axis = self.combo_axis.get()
        global_scale = [1, 1, 1]
        if axis == "X":
            global_scale[0] = global_scale_value
        elif axis == "Y":
            global_scale[1] = global_scale_value
        elif axis == "Z":
            global_scale[2] = global_scale_value
        shearing_matrix = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append(self.try_parse_float(self.shearing_entries[i][j].get()))
            shearing_matrix.append(row)

        self.apply_transformations(tx, ty, tz, local_scale, global_scale, shearing_matrix)

    def try_parse_float(self, value):
        try:
            return float(value)
        except ValueError:
            return 1.0  

root = tk.Tk()
app = CasaApp(root)
root.mainloop()