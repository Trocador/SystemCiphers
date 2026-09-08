import tkinter as tk
import ttkbootstrap as ttk

class ShadowCard(tk.Canvas):
    def __init__(self, parent, width=420, height=160, bg_color="#F4F6F9", card_color="#FFFFFF", shadow_color="#E2E8F0", radius=12):
        super().__init__(parent, width=width, height=height, bg=bg_color, highlightthickness=0)
        
        self.width = width
        self.height = height
        self.radius = radius
        self.card_color = card_color
        
        # 1. Dibujar la sombra desplazada (efecto flotante)
        self._draw_rounded_rect(4, 4, width - 2, height - 2, radius, shadow_color)
        # 2. Dibujar la tarjeta blanca principal sobre la sombra
        self.card_id = self._draw_rounded_rect(0, 0, width - 6, height - 6, radius, card_color)
        
        # Frame interno invisible para colocar las etiquetas y botones de Tkinter
        self.inner_frame = ttk.Frame(self, bootstyle="light")
        self.create_window((15, 15), window=self.inner_frame, anchor="nw", width=width-36, height=height-36)

    def _draw_rounded_rect(self, x1, y1, x2, y2, radius, color):
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1, x2, y1 + radius,
            x2, y2 - radius,
            x2, y2, x2 - radius, y2,
            x1 + radius, y2,
            x1, y2, x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        return self.create_polygon(points, fill=color, smooth=True)