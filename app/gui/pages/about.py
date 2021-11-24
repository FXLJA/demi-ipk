import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from threading import Thread

from app.core.utils.color_analyzer_dataset_io import *
from app.core.utils.gann_trainer import GANNTrainer, GANNTrainerConfig
from app.core.utils.gann_io import *
from app.gui.common.frame_group import FrameGroup
from app.gui.common.slider import HSlider
from app.config.gui_config import *
from app.config.global_config import *


class AboutFrame(tk.Frame):
    def __init__(self, togi_gui, **kw):
        super().__init__(**kw)
        self._init_components()

    def _init_components(self):
        self._lbl_Title = tk.Label(self, text=ABOUT_TITLE)
        self._lbl_Title.pack(side=tk.TOP, expand=True, fill=tk.X)

        #TODO add image
        self._lbl_Name = tk.Label(self, text=ABOUT_DESCRIPTION)
        self._lbl_Name.pack(side=tk.TOP, expand=True, fill=tk.X)


