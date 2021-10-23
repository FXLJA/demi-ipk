import tkinter.font as tk_font
import tkinter as tk
import tkinter.ttk as ttk

from app.gui.pages.home import HomeFrame
from app.gui.pages.training import TrainingFrame
from app.gui.config.config import *


class TogiGUI:
    def __init__(self, root):
        self.root = root
        self._init_components()
        self.update_default_font()

    def _init_components(self):
        tab_parent = ttk.Notebook(self.root)

        home_frame = HomeFrame(master=tab_parent)
        training_frame = TrainingFrame(master=tab_parent)

        padding = (DEFAULT_PAD_X, DEFAULT_PAD_Y, DEFAULT_PAD_X, DEFAULT_PAD_Y)
        tab_parent.add(home_frame, text="Home", padding=padding)
        tab_parent.add(training_frame, text="Training", padding=padding)
        tab_parent.pack(expand=True, fill=tk.BOTH)

    def update_default_font(self):
        default_font = tk_font.nametofont("TkDefaultFont")
        default_font.config(family=DEFAULT_FONT)
        default_font.config(size=FONT_SIZE_NORMAL)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Togi - The Ultimate Movie Poster Analyzer")
    TogiGUI(root)
    root.mainloop()
