from tkinter import ttk
import tkinter as tk

from app.gui.config.config import *


class FrameGroup(tk.Frame):
    def __init__(self, title="", title_font_size=24, create_content_callback=None, **kw):
        self._content = None
        self._title = title
        self._title_font_size= title_font_size

        super().__init__(**kw)
        self._init_components(create_content_callback)

    def _init_components(self, create_content_callback):
        self._label = ttk.Label(
            master=self,
            text=self._title,
            font=(DEFAULT_FONT, self._title_font_size)
        )
        self._label.pack(side=tk.TOP)

        if create_content_callback is not None:
            content = create_content_callback(self)
            self.set_content(content)

    def set_content(self, content):
        content.pack(side=tk.BOTTOM)
