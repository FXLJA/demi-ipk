import tkinter as tk

from app.core.common.color_converter import *


class FancyColor(tk.Frame):
    def __init__(self, color=(255, 255, 255), percentage=0, **kw):
        self._color = color
        self._percentage = percentage

        super().__init__(**kw)
        self._init_components()

    def _init_components(self):
        self._canvas = tk.Canvas(self, width=50, height=50)
        self._canvas.grid(row=0, column=0, rowspan=3)
        self._update_canvas_color()

        self._lbl_hex = tk.Label(self)
        self._update_hex_text()
        self._lbl_hex.grid(row=0, column=1, sticky='w')

        self._lbl_rgb = tk.Label(self, width=16, anchor="w")
        self._update_rgb_text()
        self._lbl_rgb.grid(row=1, column=1, sticky='w')

        self._lbl_percentage = tk.Label(self, width=16, anchor="w")
        self._update_percentage_text()
        self._lbl_percentage.grid(row=2, column=1, sticky='w')

    def set_color(self, new_color):
        self._color = new_color
        self._update_canvas_color()
        self._update_rgb_text()
        self._update_hex_text()

    def get_color(self):
        return self._color

    def set_percentage(self, new_percentage):
        self._percentage = new_percentage
        self._update_percentage_text()

    def get_percentage(self):
        return self._percentage

    def _update_canvas_color(self):
        hex = rgb_to_hex(self._color)
        self._canvas.create_rectangle(0, 0, 50, 50, fill=hex)

    def _update_hex_text(self):
        hex = rgb_to_hex(self._color)
        new_text = "HEX: {}".format(hex)
        self._lbl_hex.config(text=new_text)

    def _update_rgb_text(self):
        new_text = "RGB: %d, %d, %d" % tuple(self._color)
        self._lbl_rgb.config(text=new_text)

    def _update_percentage_text(self):
        new_text = "%%: %.4f%%" % (self._percentage * 100.0)
        self._lbl_percentage.config(text=new_text)
