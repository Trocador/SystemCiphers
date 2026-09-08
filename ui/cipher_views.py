import ttkbootstrap as ttk
from ttkbootstrap.constants import BOTH, END, LEFT, X
from cifrados.cesar import cifrado_cesar, descifrado_cesar
from cifrados.adicion import cifrado_adicion, descifrado_adicion


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
        else:
            resultado = f"[PROCESANDO {self.clave_cifrado.upper()}] Texto: '{texto}'"

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
        else:
            resultado = f"[DESCIFRANDO {self.clave_cifrado.upper()}] Texto: '{texto}'"

        self._actualizar_salida(resultado)

    def _actualizar_salida(self, mensaje):
        self.txt_salida.config(state="normal")
        self.txt_salida.delete("1.0", END)
        self.txt_salida.insert("1.0", mensaje)
        self.txt_salida.config(state="disabled")