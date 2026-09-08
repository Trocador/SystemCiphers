import tkinter as tk
class AplicacionPigpen:
    def __init__(self, root):
        self.root = root
        self.root.title("francmason")
        self.root.geometry("650x500")
        self.root.config(bg="#f0f4f8") # Fondo general azul muy clarito
        # Frame central blanco para simular la "tarjeta" del diseño
        main_frame = tk.Frame(root, bg="white")
        main_frame.pack(expand=True, fill="both", padx=30, pady=30)
        # Título
        title_label = tk.Label(main_frame, text="CIFRADO FRANCMASON", 
                               font=("Helvetica", 20, "bold"), bg="white", fg="#0d3b66")
        title_label.pack(pady=(20, 15))
        # Etiqueta "Texto plano"
        tk.Label(main_frame, text="Texto plano:", font=("Helvetica", 11, "bold"), 
                 bg="white", fg="#0d3b66").pack(pady=(10, 5))
        # Campo de entrada
        self.entry = tk.Entry(main_frame, font=("Arial", 14), width=45, justify="center", relief="solid", bd=1)
        self.entry.pack(pady=5, ipady=5) # ipady le da un poco más de altura interna
        # Frame para organizar los botones horizontalmente
        button_frame = tk.Frame(main_frame, bg="white")
        button_frame.pack(pady=15)
        # Botón CIFRAR (Azul)
        self.btn_cifrar = tk.Button(button_frame, text="🔒 CIFRAR", font=("Helvetica", 10, "bold"), 
                                    bg="#1976D2", fg="white", width=15, cursor="hand2", relief="flat",
                                    command=self.actualizar_canvas)
        self.btn_cifrar.pack(side=tk.LEFT, padx=10, ipady=5)
        # Botón DESCIFRAR (Verde)
        self.btn_descifrar = tk.Button(button_frame, text="🔓 DESCIFRAR", font=("Helvetica", 10, "bold"),
                                       bg="#2e7d32", fg="white", width=15, cursor="hand2", relief="flat",
                                       command=self.descifrar_texto)
        self.btn_descifrar.pack(side=tk.LEFT, padx=10, ipady=5)
        # Botón LIMPIAR (Gris claro)
        self.btn_limpiar = tk.Button(button_frame, text="LIMPIAR", font=("Helvetica", 10, "bold"), 
                                     bg="#e0e6ed", fg="#0d3b66", width=15, cursor="hand2", relief="flat",
                                     command=self.limpiar_todo)
        self.btn_limpiar.pack(side=tk.LEFT, padx=10, ipady=5)
        
        # Etiqueta "Resultado en Pigpen"
        tk.Label(main_frame, text="Resultado en Pigpen:", font=("Helvetica", 11, "bold"), 
                 bg="white", fg="#0d3b66").pack(pady=(15, 5))
        # Lienzo (Canvas) donde se dibujarán los símbolos
        self.canvas = tk.Canvas(main_frame, bg="white", width=550, height=180, relief="solid", bd=1)
        self.canvas.pack(pady=(0, 20))
        
        # Poner el texto inicial en el canvas
        self.mostrar_placeholder()

    def mostrar_placeholder(self):
        self.canvas.delete("all")
        self.canvas.create_text(275, 90, text="El cifrado aparecerá aquí", 
                                font=("Helvetica", 12), fill="#9ba4b5")

    def limpiar_todo(self):
        self.entry.delete(0, tk.END)
        self.mostrar_placeholder()

    def descifrar_texto(self):
        # Como el resultado se dibuja como símbolos gráficos (no como texto),
        # no se puede "leer" el canvas letra por letra automáticamente.
        # Esta función reinterpreta el contenido actual del campo de entrada
        # como si ya estuviera en pigpen y lo vuelve a mostrar en texto plano,
        # dejando el campo listo para que el usuario ingrese el mensaje cifrado
        # (en letras) que desea convertir de vuelta a texto plano.
        texto = self.entry.get().upper()
        if not texto.strip():
            self.canvas.delete("all")
            self.canvas.create_text(275, 90, text="Ingresa el texto para descifrar",
                                    font=("Helvetica", 12), fill="#9ba4b5")
            return
        self.canvas.delete("all")
        self.canvas.create_text(275, 90, text=f"Texto plano: {texto}",
                                font=("Helvetica", 14, "bold"), fill="#0d3b66")

    def actualizar_canvas(self):
        texto = self.entry.get().upper()
        
        # Si no hay texto, volver a mostrar el placeholder
        if not texto.strip():
            self.mostrar_placeholder()
            return
            
        self.canvas.delete("all") # Limpiar el lienzo
        
        size = 30       # Tamaño de cada símbolo
        margin_x = 25   # Margen horizontal
        margin_y = 25   # Margen vertical
        x, y = margin_x, margin_y
        
        for char in texto:
            if char.isalpha():
                self.dibujar_simbolo(char, x, y, size)
                x += size + 8
                
                # Salto de línea si el texto es muy largo
                if x > 550 - size - margin_x:
                    x = margin_x
                    y += size + 20
            elif char == ' ':
                x += size # Espacio en blanco
                if x > 550 - size - margin_x:
                    x = margin_x
                    y += size + 20
                    
    def dibujar_simbolo(self, char, x, y, size):
        cx = x + size / 2
        cy = y + size / 2
        dot_r = size * 0.12 # Radio del punto central
        
        # Mapeo de paredes (Arriba, Abajo, Izquierda, Derecha)
        grid_map = {
            'A': (0,1,0,1), 'B': (0,1,1,1), 'C': (0,1,1,0),
            'D': (1,1,0,1), 'E': (1,1,1,1), 'F': (1,1,1,0),
            'G': (1,0,0,1), 'H': (1,0,1,1), 'I': (1,0,1,0),
            'J': (0,1,0,1), 'K': (0,1,1,1), 'L': (0,1,1,0),
            'M': (1,1,0,1), 'N': (1,1,1,1), 'O': (1,1,1,0),
            'P': (1,0,0,1), 'Q': (1,0,1,1), 'R': (1,0,1,0),
        }
        
        # Mapeo de coordenadas (Cruces)
        cross_map = {
            'S': [(0.1, 0.1), (0.5, 0.9), (0.9, 0.1)],  # \/
            'T': [(0.1, 0.1), (0.9, 0.5), (0.1, 0.9)],  # >
            'U': [(0.9, 0.1), (0.1, 0.5), (0.9, 0.9)],  # 
            'V': [(0.1, 0.9), (0.5, 0.1), (0.9, 0.9)],  # /\
            'W': [(0.1, 0.1), (0.5, 0.9), (0.9, 0.1)],
            'X': [(0.1, 0.1), (0.9, 0.5), (0.1, 0.9)],
            'Y': [(0.9, 0.1), (0.1, 0.5), (0.9, 0.9)],
            'Z': [(0.1, 0.9), (0.5, 0.1), (0.9, 0.9)],
        }
        
        grosor = 3 # Grosor de las líneas
        color_linea = "black"
        
        if char in grid_map:
            t, b, l, r = grid_map[char]
            if t: self.canvas.create_line(x, y, x+size, y, width=grosor, fill=color_linea)
            if b: self.canvas.create_line(x, y+size, x+size, y+size, width=grosor, fill=color_linea)
            if l: self.canvas.create_line(x, y, x, y+size, width=grosor, fill=color_linea)
            if r: self.canvas.create_line(x+size, y, x+size, y+size, width=grosor, fill=color_linea)
            
            if char in 'JKLMNOPQR':
                self.canvas.create_oval(cx-dot_r, cy-dot_r, cx+dot_r, cy+dot_r, fill=color_linea)
                
        elif char in cross_map:
            pts = cross_map[char]
            self.canvas.create_line(x+pts[0][0]*size, y+pts[0][1]*size,
                                    x+pts[1][0]*size, y+pts[1][1]*size, width=grosor, fill=color_linea)
            self.canvas.create_line(x+pts[1][0]*size, y+pts[1][1]*size,
                                    x+pts[2][0]*size, y+pts[2][1]*size, width=grosor, fill=color_linea)
                                    
            if char in 'WXYZ':
                self.canvas.create_oval(cx-dot_r, cy-dot_r, cx+dot_r, cy+dot_r, fill=color_linea)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionPigpen(ventana)
    ventana.mainloop()