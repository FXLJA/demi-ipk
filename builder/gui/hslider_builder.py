from app.gui.common.slider import HSlider
import tkinter as tk


class HSliderBuilder:
    def __init__(self):
        self._value = 0
        self._min_value = 0
        self._max_value = 100
        self._step = 1.0
        self._label_format = "{:}"
        self._master = None

    def with_value(self, value):
        self._value = value
        return self

    def with_min_value(self, min_value):
        self._min_value = min_value
        return self

    def with_max_value(self, max_value):
        self._max_value = max_value
        return self

    def with_step(self, step):
        self._step = step
        return self

    def with_range(self, min_value, max_value, step):
        self._min_value = min_value
        self._max_value = max_value
        self._step = step
        return self

    def with_master(self, master):
        self._master = master
        return self

    def with_label_format(self, label_format):
        self._label_format = label_format
        return self

    def reset(self):
        self.__init__()

    def build(self):
        if self._master is None:
            self._master = tk.Tk()

        _hslider = self._create_slider()
        self.reset()
        return _hslider

    def _create_slider(self):
        return HSlider(
            value=self._value,
            min_value=self._min_value,
            max_value=self._max_value,
            step=self._step,
            master=self._master,
            label_format=self._label_format
        )
