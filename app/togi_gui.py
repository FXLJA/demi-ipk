import tkinter.font as tk_font
import tkinter as tk
import tkinter.ttk as ttk

from app.gui.pages.home import HomeFrame
from app.gui.pages.training import TrainingFrame


class TogiGUI:
    def __init__(self, root):
        self.root = root
        self._init_components()
        self.update_default_font()

    def _init_components(self):
        tab_parent = ttk.Notebook(self.root)

        home_frame = HomeFrame(master=tab_parent)
        training_frame = TrainingFrame(master=tab_parent)

        tab_parent.add(home_frame, text="Home")
        tab_parent.add(training_frame, text="Training")
        tab_parent.pack()

    def update_default_font(self):
        default_font = tk_font.nametofont("TkDefaultFont")
        default_font.config(size=18)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Togi - The Ultimate Movie Poster Analyzer")
    TogiGUI(root)
    root.mainloop()
