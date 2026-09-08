import ttkbootstrap as ttk
from ttkbootstrap.constants import BOTH, LEFT, X, BOTTOM, RIGHT, Y, VERTICAL
from ttkbootstrap import ScrolledFrame
from config import *
from ui.cipher_views import CipherWindow
from ui.custom_widgets import ShadowCard

class MainWindow(ttk.Window):
    def __init__(self):
        super().__init__(
            title="Sistema de Cifrados",
            themename="flatly",
            size=(1080, 750)  # Tamaño inicial cómodo
        )
        self.configure(bg=COLOR_BG_PRINCIPAL)
        
        # Lista de los 8 métodos con sus descripciones
        self.cifrados = [
            ("César Normal", "Desplazamiento clásico de posiciones en el alfabeto.", "cesar_normal"),
            ("César por Posición", "Desplazamiento ejecutable con valor 'n' personalizable.", "cesar_posicion"),
            ("Cifrado Adición", "Desplazamiento numérico con aritmética modular.", "adicion"),
            ("Método Fracmasón", "Cifrado gráfico por sustitución de símbolos.", "fracmason"),
            ("Cifrado Polybius", "Sustitución por coordenadas mediante matriz 5x5.", "polybius"),
            ("Cifrado RailFence", "Transposición en zigzag a través de raíles.", "railfence"),
            ("Transposición", "Reordenamiento posicional (Grupos, Serial y Columnas).", "transposicion"),
            ("Cifrado Vigenère", "Cifrado polialfabético basado en una palabra clave.", "vigenere"),
        ]

        self._crear_navbar()
        self._crear_header()
        self._crear_grid_tarjetas()
        self._crear_footer()

    def _crear_navbar(self):
        navbar = ttk.Frame(self, bootstyle="dark", padding=(25, 15))
        navbar.pack(fill=X)

        lbl_logo = ttk.Label(
            navbar, 
            text="🔒  Sistema de cifrados", 
            font=("Helvetica", 15, "bold"), 
            bootstyle="inverse-dark"
        )
        lbl_logo.pack(side=LEFT)

    def _crear_header(self):
        header = ttk.Frame(self, padding=(0, 20))
        header.pack(fill=X)

        lbl_titulo = ttk.Label(
            header, 
            text="Explora y aprende", 
            font=("Helvetica", 20, "bold"), 
            anchor="center"
        )
        lbl_titulo.pack()

        lbl_subtitulo = ttk.Label(
            header, 
            text="Selecciona un método de cifrado para comenzar, y desliza para ver todos los cifrados disponibles.", 
            font=("Helvetica", 10), 
            bootstyle="secondary", 
            anchor="center"
        )
        lbl_subtitulo.pack(pady=(4, 0))

    def _crear_grid_tarjetas(self):
        # Frame desplazable con scrollbar integrada de ttkbootstrap
        self.scroll_container = ScrolledFrame(
            self,
            padding=30,
            autohide=False,
            bootstyle="round"
        )
        self.scroll_container.pack(fill=BOTH, expand=True)

        # El contenedor interno donde van las tarjetas
        container = self.scroll_container

        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)

        for index, (nombre, desc, clave) in enumerate(self.cifrados):
            fila = index // 2
            columna = index % 2
            self._crear_tarjeta(container, nombre, desc, clave, fila, columna)

        # Vincular eventos del ratón para desplazamiento cómodo
        self.bind_all("<MouseWheel>", self._al_desplazar_rueda)

    def _al_desplazar_rueda(self, event):
        """Permite hacer scroll con la rueda del ratón en Windows/Linux/macOS."""
        if hasattr(self, 'scroll_container'):
            self.scroll_container.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _crear_tarjeta(self, parent, titulo, descripcion, clave, fila, columna):
        # Instanciamos la tarjeta con sombra
        card_canvas = ShadowCard(
            parent,
            width=440,
            height=150,
            bg_color="#F4F6F9",
            card_color="#FFFFFF",
            shadow_color="#CBD5E1",
        )
        card_canvas.grid(row=fila, column=columna, padx=15, pady=12, sticky="nsew")

        # Contenedor interno donde van las etiquetas y el botón
        container = card_canvas.inner_frame

        # 1. Título Centrado
        lbl_title = ttk.Label(
            container,
            text=titulo,
            font=("Helvetica", 15, "bold"),
            anchor="center",
        )
        lbl_title.pack(fill=X, pady=(2, 0))

        # 2. Descripción Centrada
        lbl_desc = ttk.Label(
            container,
            text=descripcion,
            font=("Helvetica", 9),
            bootstyle="secondary",
            justify="center",
            anchor="center",
            wraplength=360,
        )
        lbl_desc.pack(fill=X, pady=(4, 12))

        # 3. Botón Centrado
        btn = ttk.Button(
            container,
            text="Ingresar →",
            bootstyle="primary",
            command=lambda c=clave, t=titulo: self._abrir_cifrado(c, t),
        )
        btn.pack(anchor="center")

    def _crear_footer(self):
        footer = ttk.Frame(self, padding=(25, 10))
        footer.pack(fill=X, side=BOTTOM)

        lbl_footer = ttk.Label(
            footer, 
            text="🛡️  Criptografía para un mundo más seguro", 
            font=("Helvetica", 8), 
            bootstyle="secondary"
        )
        lbl_footer.pack(side=LEFT)

        lbl_version = ttk.Label(footer, text="v1.0.0", font=("Helvetica", 8), bootstyle="secondary")
        lbl_version.pack(side=RIGHT)

    def _abrir_cifrado(self, clave_cifrado, titulo):
        ventana_cifrado = CipherWindow(self, clave_cifrado, titulo)
        ventana_cifrado.focus()