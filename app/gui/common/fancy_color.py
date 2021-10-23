from tkinter import ttk
import tkinter as tk


class FancyColor(tk.Frame):
    def __init__(self, color=(255, 255, 255), **kw):
        self._color = color

        super().__init__(**kw)
        self._init_components()

    def _init_components(self):
        self._canvas = tk.Canvas(self, width=50, height=50)
        self._canvas.grid(row=0, column=0, rowspan=2)
        self._canvas.create_rectangle(00, 0, 50, 50, fill='white')

        self._lbl_hex = tk.Label(self, text="HEX: {}".format("#FFFFFF"))
        self._lbl_hex.grid(row=0, column=1, sticky='w')

        self._lbl_rgb = tk.Label(self, text="RGB: {}".format("255, 255, 255"))
        self._lbl_rgb.grid(row=1, column=1, sticky='w')

    def set_color(self):
        pass

    def get_color(self):
        pass
