import ttkbootstrap as ttk
from tkinter import PhotoImage
from ttkbootstrap.constants import BOTH, END, LEFT, X
from cifrados.cesar import cifrado_cesar, descifrado_cesar
from cifrados.adicion import cifrado_adicion, descifrado_adicion
from cifrados.fracmason import cifrado_fracmason, descifrado_fracmason
from cifrados.polybius import cifrado_polybius, descifrado_polybius
from cifrados.railfence import cifrado_railfence, descifrado_railfence
from cifrados.transposicion import (
    cifrar_grupos, descifrar_grupos,
    cifrar_serial, descifrar_serial,
    cifrar_columnas, descifrar_columnas
)


class CipherWindow(ttk.Toplevel):

    def __init__(self, parent, clave_cifrado, titulo):
        super().__init__(parent)
        self.title(f"Módulo de Cifrado: {titulo}")
        self.geometry("700x620")
        self.clave_cifrado = clave_cifrado

        # Contenedor Principal
        main_container = ttk.Frame(self, padding=20)
        main_container.pack(fill=BOTH, expand=True)

        # 1. ENCABEZADO
        lbl_titulo = ttk.Label(
            main_container,
            text=titulo,
            font=("Helvetica", 16, "bold"),
            bootstyle="primary",
        )
        lbl_titulo.pack(anchor="w", pady=(0, 15))

        # 2. PANEL DE CONFIGURACIÓN/PARÁMETROS
        self.frame_config = ttk.Labelframe(
            main_container, text="Parámetros del Cifrado", padding=15
        )
        self.frame_config.pack(fill=X, pady=(0, 15))

        self._configurar_panel_parametros()

        # 3. ENTRADA DE TEXTO
        lbl_input = ttk.Label(
            main_container,
            text="Texto de entrada:",
            font=("Helvetica", 10, "bold"),
        )
        lbl_input.pack(anchor="w", pady=(0, 5))

        self.txt_entrada = ttk.Text(main_container, height=4, font=("Consolas", 10))
        self.txt_entrada.pack(fill=X, pady=(0, 15))

        # 4. BOTONES DE ACCIÓN
        frame_botones = ttk.Frame(main_container)
        frame_botones.pack(fill=X, pady=(0, 15))

        btn_cifrar = ttk.Button(
            frame_botones,
            text="🔒 Cifrar",
            bootstyle="success",
            command=self._ejecutar_cifrado,
        )
        btn_cifrar.pack(side=LEFT, padx=(0, 10))

        btn_descifrar = ttk.Button(
            frame_botones,
            text="🔓 Descifrar",
            bootstyle="info",
            command=self._ejecutar_descifrado,
        )
        btn_descifrar.pack(side=LEFT)

        # 5. SALIDA DE TEXTO (RESULTADO)
        lbl_output = ttk.Label(
            main_container, text="Resultado:", font=("Helvetica", 10, "bold")
        )
        lbl_output.pack(anchor="w", pady=(0, 5))

        self.txt_salida = ttk.Text(
            main_container,
            height=4,
            font=("Consolas", 10),
            state="disabled",
            background="#f8f9fa",
        )
        self.txt_salida.pack(fill=X)

    def _configurar_panel_parametros(self):
        """Muestra componentes según el tipo de cifrado seleccionado."""

        # CASO: CÉSAR (NORMAL Y POR POSICIÓN)
        if self.clave_cifrado in ["cesar", "cesar_normal", "cesar_posicion"]:
            
            frame_spin = ttk.Frame(self.frame_config)
            frame_spin.pack(anchor="w", fill=X)

            lbl_shift = ttk.Label(
                frame_spin, text="Posiciones a desplazar (n):", font=("Helvetica", 10)
            )
            lbl_shift.pack(side=LEFT, padx=(0, 10))

            # Selector Spinbox
            self.spin_shift = ttk.Spinbox(
                frame_spin,
                from_=1,
                to=25,
                width=6,
                command=self._actualizar_vista_alfabeto, # Se actualiza al presionar las flechas
            )
            self.spin_shift.set(3)

            # Vincular la escritura manual en el teclado para actualizar el alfabeto en vivo
            self.spin_shift.bind("<KeyRelease>", lambda e: self._actualizar_vista_alfabeto())

            # Si es el César Normal, bloqueamos el campo en 3
            if self.clave_cifrado in ["cesar", "cesar_normal"]:
                self.spin_shift.config(state="disabled")

            self.spin_shift.pack(side=LEFT)

            # VISOR VISUAL DEL ALFABETO MOVIDO DYNAMICAMENTE
            frame_preview = ttk.Frame(self.frame_config, padding=(0, 10))
            frame_preview.pack(fill=X)

            ttk.Label(
                frame_preview,
                text="Mapeo del Alfabeto:",
                font=("Helvetica", 9, "bold"),
            ).pack(anchor="w")

            self.lbl_alfabeto_orig = ttk.Label(
                frame_preview,
                text="Origen:   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z",
                font=("Consolas", 8),
                bootstyle="secondary",
            )
            self.lbl_alfabeto_orig.pack(anchor="w")

            self.lbl_alfabeto_cif = ttk.Label(
                frame_preview, text="", font=("Consolas", 8, "bold"), bootstyle="primary"
            )
            self.lbl_alfabeto_cif.pack(anchor="w")

            # Dibujar mapeo inicial
            self._actualizar_vista_alfabeto()

        # CASO: CIFRADO POR ADICIÓN
        elif self.clave_cifrado == "adicion":
            frame_adicion = ttk.Frame(self.frame_config)
            frame_adicion.pack(anchor="w", fill=X)

            lbl_key = ttk.Label(
                frame_adicion, text="Clave numérica (K):", font=("Helvetica", 10)
            )
            lbl_key.pack(side=LEFT, padx=(0, 10))

            self.spin_key = ttk.Spinbox(
                frame_adicion,
                from_=0,
                to=100,
                width=8,
                command=self._actualizar_formula_adicion,
            )
            self.spin_key.set(5)
            self.spin_key.pack(side=LEFT)
            self.spin_key.bind("<KeyRelease>", lambda e: self._actualizar_formula_adicion())

            # VISOR VISUAL: Representación de la Fórmula Modular
            frame_preview = ttk.Frame(self.frame_config, padding=(0, 10))
            frame_preview.pack(fill=X)

            ttk.Label(
                frame_preview,
                text="Fórmula Aritmética Modular:",
                font=("Helvetica", 9, "bold"),
            ).pack(anchor="w")

            self.lbl_formula = ttk.Label(
                frame_preview, text="", font=("Consolas", 10, "bold"), bootstyle="info"
            )
            self.lbl_formula.pack(anchor="w", pady=(2, 0))

            self._actualizar_formula_adicion()

        # CASO: CIFRADO FRACMASÓN
        elif self.clave_cifrado == "fracmason":
            frame_preview = ttk.Frame(self.frame_config, padding=(0, 5))
            frame_preview.pack(fill=X)

            ttk.Label(
                frame_preview,
                text="Guía visual del alfabeto Fracmasón:",
                font=("Helvetica", 9, "bold"),
            ).pack(anchor="w", pady=(0, 5))

            try:
                # Cargar la imagen utilizando PhotoImage
                self.img_fracmason = PhotoImage(file="assets/fracmason_mapa.png")
                
                # Opcional: Redimensionar si la imagen es muy grande (ejemplo: subsample)
                self.img_fracmason = self.img_fracmason.subsample(4, 4)

                lbl_imagen = ttk.Label(frame_preview, image=self.img_fracmason)
                lbl_imagen.pack(anchor="center", pady=5)
            except Exception:
                # Mensaje de respaldo si no encuentra la imagen
                ttk.Label(
                    frame_preview, 
                    text="[Imagen 'assets/fracmason_mapa.png' no encontrada]", 
                    bootstyle="warning"
                ).pack(anchor="w")

        # CASO: CIFRADO POLYBIUS
        elif self.clave_cifrado == "polybius":
            frame_preview = ttk.Frame(self.frame_config, padding=(0, 5))
            frame_preview.pack(fill=X)

            ttk.Label(
                frame_preview,
                text="Matriz de Coordenadas 5x5 (I/J combinadas):",
                font=("Helvetica", 9, "bold"),
            ).pack(anchor="w", pady=(0, 5))

            # Visualización interactiva de la Matriz 5x5
            frame_grid = ttk.Frame(frame_preview)
            frame_grid.pack(anchor="w")

            # Encabezados de columnas (1..5)
            ttk.Label(frame_grid, text=" ", font=("Consolas", 8, "bold")).grid(row=0, column=0, padx=4)
            for c in range(1, 6):
                ttk.Label(frame_grid, text=str(c), font=("Consolas", 8, "bold"), bootstyle="primary").grid(row=0, column=c, padx=4)

            # Matriz con filas (1..5)
            filas_datos = [
                ['A', 'B', 'C', 'D', 'E'],
                ['F', 'G', 'H', 'I/J', 'K'],
                ['L', 'M', 'N', 'O', 'P'],
                ['Q', 'R', 'S', 'T', 'U'],
                ['V', 'W', 'X', 'Y', 'Z']
            ]

            for r, fila in enumerate(filas_datos, start=1):
                ttk.Label(frame_grid, text=str(r), font=("Consolas", 8, "bold"), bootstyle="primary").grid(row=r, column=0, padx=4)
                for c, char in enumerate(fila, start=1):
                    ttk.Label(frame_grid, text=char, font=("Consolas", 8), bootstyle="secondary").grid(row=r, column=c, padx=4)

        # CASO: CIFRADO RAILFENCE
        elif self.clave_cifrado == "railfence":
            frame_rail = ttk.Frame(self.frame_config)
            frame_rail.pack(anchor="w", fill=X)

            lbl_rails = ttk.Label(
                frame_rail, text="Número de Rieles / Filas:", font=("Helvetica", 10)
            )
            lbl_rails.pack(side=LEFT, padx=(0, 10))

            self.spin_rails = ttk.Spinbox(
                frame_rail,
                from_=2,
                to=10,
                width=6,
                command=self._actualizar_info_railfence,
            )
            self.spin_rails.set(3)
            self.spin_rails.pack(side=LEFT)
            self.spin_rails.bind("<KeyRelease>", lambda e: self._actualizar_info_railfence())

            # VISOR VISUAL DE PATRÓN ZIGZAG
            frame_preview = ttk.Frame(self.frame_config, padding=(0, 10))
            frame_preview.pack(fill=X)

            ttk.Label(
                frame_preview,
                text="Esquema del recorrido:",
                font=("Helvetica", 9, "bold"),
            ).pack(anchor="w")

            self.lbl_rail_pattern = ttk.Label(
                frame_preview, text="", font=("Consolas", 9, "bold"), bootstyle="info"
            )
            self.lbl_rail_pattern.pack(anchor="w", pady=(2, 0))
            
            ttk.Label(self.frame_config, text="Esquema visual en Rieles:", font=("Helvetica", 9, "bold")).pack(anchor="w", pady=(10, 2))
    
            self.txt_esquema_rail = ttk.Text(self.frame_config, height=5, font=("Consolas", 10), state="disabled", background="#1e1e1e", foreground="#00ffcc")
            self.txt_esquema_rail.pack(fill=X)

            self._actualizar_info_railfence()

        # CASO: TRANSPOSICIÓN
        elif self.clave_cifrado == "transposicion":
            frame_subtipo = ttk.Frame(self.frame_config)
            frame_subtipo.pack(fill=X, pady=(0, 10))

            ttk.Label(frame_subtipo, text="Método de Transposición:", font=("Helvetica", 10, "bold")).pack(anchor="w")

            self.combo_subtipo = ttk.Combobox(
                frame_subtipo,
                values=["Por Grupos", "Serial", "Por Columnas (Vertical)"],
                state="readonly"
            )
            self.combo_subtipo.set("Por Grupos")
            self.combo_subtipo.pack(fill=X, pady=(5, 10))
            self.combo_subtipo.bind("<<ComboboxSelected>>", lambda e: self._cambiar_inputs_transposicion())

            # Contenedor dinámico de campos de entrada
            self.frame_inputs_transp = ttk.Frame(self.frame_config)
            self.frame_inputs_transp.pack(fill=X)

            self._cambiar_inputs_transposicion()

    def _cambiar_inputs_transposicion(self):
        """Alterna los inputs requeridos según el subtipo de transposición."""
        for widget in self.frame_inputs_transp.winfo_children():
            widget.destroy()

        subtipo = self.combo_subtipo.get()

        if subtipo == "Por Grupos":
            ttk.Label(self.frame_inputs_transp, text="Clave de permutación (ej: 5,2,4,1,3):").pack(anchor="w")
            self.ent_clave_transp = ttk.Entry(self.frame_inputs_transp)
            self.ent_clave_transp.insert(0, "5,2,4,1,3")
            self.ent_clave_transp.pack(fill=X, pady=(2, 0))

        elif subtipo == "Serial":
            ttk.Label(self.frame_inputs_transp, text="Modo Serial: No requiere clave explícita.", bootstyle="secondary").pack(anchor="w")

        elif subtipo == "Por Columnas (Vertical)":
            ttk.Label(self.frame_inputs_transp, text="Palabra Clave (ej: VINO):").pack(anchor="w")
            self.ent_clave_transp = ttk.Entry(self.frame_inputs_transp)
            self.ent_clave_transp.insert(0, "VINO")
            self.ent_clave_transp.pack(fill=X, pady=(2, 0))

    def _actualizar_info_railfence(self):
        """Muestra una previsualización conceptual del patrón en zigzag según el número de rieles."""
        try:
            r = int(self.spin_rails.get())
        except ValueError:
            r = 3

        self.lbl_rail_pattern.config(
            text=f"Patrón activo: Transposición distribuida alternando sobre {r} niveles verticales."
        )

    def _actualizar_formula_adicion(self):
        """Muestra de forma dinámica la ecuación matemática $C = (P + K) \\pmod{26}."""
        try:
            k = int(self.spin_key.get())
        except ValueError:
            k = 0
        
        self.lbl_formula.config(
            text=f"Cifrado:  C ≡ (P + {k}) mod 26    |    Descifrado:  P ≡ (C - {k}) mod 26"
        )

    def _actualizar_vista_alfabeto(self):
        """Sombra visual que muestra cómo cambia el alfabeto en directo."""
        try:
            n = int(self.spin_shift.get())
        except ValueError:
            n = 3

        alfabeto_orig = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alfabeto_cif = cifrado_cesar(alfabeto_orig, n)
        
        # Formatear con espacios para mejor legibilidad visual
        texto_formateado = " ".join(list(alfabeto_cif))
        self.lbl_alfabeto_cif.config(text=f"Destino:  {texto_formateado}")

    def _obtener_desplazamiento(self):
        """Obtiene de forma segura el valor N actual."""
        try:
            return int(self.spin_shift.get())
        except Exception:
            return 3

    def _ejecutar_cifrado(self):
        texto = self.txt_entrada.get("1.0", "end-1c")

        if self.clave_cifrado in ["cesar", "cesar_normal", "cesar_posicion"]:
            n = self._obtener_desplazamiento()
            resultado = cifrado_cesar(texto, n)
        elif self.clave_cifrado == "adicion":
            try:
                k = int(self.spin_key.get())
            except ValueError:
                k = 0
            resultado = cifrado_adicion(texto, k)
        elif self.clave_cifrado == "fracmason":
            resultado = cifrado_fracmason(texto)
        elif self.clave_cifrado == "polybius":
            resultado = cifrado_polybius(texto)
        elif self.clave_cifrado == "railfence":
            try:
                rieles = int(self.spin_rails.get())
            except ValueError:
                rieles = 3
                
            resultado, esquema = cifrado_railfence(texto, rieles)
            
            # Mostrar el esquema gráfico en pantalla
            self.txt_esquema_rail.config(state="normal")
            self.txt_esquema_rail.delete("1.0", END)
            self.txt_esquema_rail.insert("1.0", esquema)
            self.txt_esquema_rail.config(state="disabled")
        
        if self.clave_cifrado == "transposicion":
            subtipo = self.combo_subtipo.get()
            if subtipo == "Por Grupos":
                try:
                    clave = [int(x.strip()) for x in self.ent_clave_transp.get().split(",")]
                    resultado = cifrar_grupos(texto, clave)
                except Exception as e:
                    resultado = f"[ERROR EN CLAVE DE GRUPOS]: {e}"
            elif subtipo == "Serial":
                resultado = cifrar_serial(texto)
            elif subtipo == "Por Columnas (Vertical)":
                clave = self.ent_clave_transp.get().strip()
                if clave:
                    resultado = cifrar_columnas(texto, clave)
                else:
                    resultado = "[ERROR]: Ingrese una palabra clave válida."
        else:#...
            pass

        self._actualizar_salida(resultado)

    def _ejecutar_descifrado(self):
        texto = self.txt_entrada.get("1.0", "end-1c")

        if self.clave_cifrado in ["cesar", "cesar_normal", "cesar_posicion"]:
            n = self._obtener_desplazamiento()
            resultado = descifrado_cesar(texto, n)
        elif self.clave_cifrado == "adicion":
            try:
                k = int(self.spin_key.get())
            except ValueError:
                k = 0
            resultado = descifrado_adicion(texto, k)
        elif self.clave_cifrado == "fracmason":
            resultado = descifrado_fracmason(texto)
        elif self.clave_cifrado == "polybius":
            resultado = descifrado_polybius(texto)
        elif self.clave_cifrado == "railfence":
            try:
                rieles = int(self.spin_rails.get())
            except ValueError:
                rieles = 3
            resultado = descifrado_railfence(texto, rieles)
        else:
            resultado = f"[DESCIFRANDO {self.clave_cifrado.upper()}] Texto: '{texto}'"
        if self.clave_cifrado == "transposicion":
            subtipo = self.combo_subtipo.get()
            if subtipo == "Por Grupos":
                try:
                    clave = [int(x.strip()) for x in self.ent_clave_transp.get().split(",")]
                    resultado = descifrar_grupos(texto, clave)
                except Exception as e:
                    resultado = f"[ERROR EN CLAVE DE GRUPOS]: {e}"
            elif subtipo == "Serial":
                resultado = descifrar_serial(texto)
            elif subtipo == "Por Columnas (Vertical)":
                clave = self.ent_clave_transp.get().strip()
                if clave:
                    resultado = descifrar_columnas(texto, clave)
                else:
                    resultado = "[ERROR]: Ingrese una palabra clave válida."
        else:
            # ...
            pass

        self._actualizar_salida(resultado)

    def _actualizar_salida(self, mensaje):
        self.txt_salida.config(state="normal")
        self.txt_salida.delete("1.0", END)
        self.txt_salida.insert("1.0", mensaje)
        self.txt_salida.config(state="disabled")