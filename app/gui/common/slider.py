import math
import tkinter as tk

from tkinter import ttk


class HSlider(ttk.Frame):
    def __init__(self, value=0, min_value=0, max_value=100, step=1.0, label_format="{:}", label_width=0, **kw):
        self._min_value = min_value
        self._max_value = max_value
        self._step = step
        self._slider_value = self._convert_to_slider_value(value)
        self._label_format = label_format
        self._label_width = label_width

        super().__init__(**kw)
        self._init_components()

    def _init_components(self):
        self._label = ttk.Label(self, text=self.get_value(), width=self._label_width)
        self._label.pack(side=tk.LEFT)

        slider_max_value = self._convert_to_slider_value(self._max_value)
        self._slider = ttk.Scale(
            self,
            from_=0,
            to=slider_max_value,
            orient='horizontal',
            command=self._on_slider_value_changed
        )
        self._slider.set(self._slider_value)
        self._slider.pack(side=tk.RIGHT, expand=True, fill=tk.X)

    def _on_slider_value_changed(self, *args):
        self._slider_value = self._slider.get()
        self.set_label_value(self.get_value())

    def _convert_to_slider_value(self, value):
        return (value - self._min_value) / self._step

    def _convert_to_real_value(self, value):
        floored_value = math.floor(value)
        return (floored_value * self._step) + self._min_value

    def set_value(self, new_value):
        self._slider_value = self._convert_to_slider_value(new_value)
        self._slider.set(self._slider_value)

    def get_value(self):
        return self._convert_to_real_value(self._slider_value)

    def set_min_value(self, new_min_value):
        self._min_value = new_min_value

    def get_min_value(self):
        return self._min_value

    def set_max_value(self, new_max_value):
        self._max_value = new_max_value

    def get_max_value(self):
        return self._max_value

    def set_label_value(self, new_value):
        formatted_text = self._label_format.format(new_value)
        self._label.configure(text=formatted_text)
