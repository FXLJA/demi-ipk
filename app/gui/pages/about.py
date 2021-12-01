import tkinter as tk

from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from threading import Thread

from app.core.utils.gann_io import *
from app.core.utils.color_analyzer_dataset_io import *
from app.core.utils.gann_trainer import GANNTrainer, GANNTrainerConfig

from app.config.gui_config import *
from app.config.global_config import *

from app.gui.common.slider import HSlider
from app.gui.common.frame_group import FrameGroup


class AboutFrame(tk.Frame):
    def __init__(self, **kw):
        super().__init__(**kw)
        self._init_components()

    def _init_components(self):
        self.about_panel = FrameGroup(
            master=self,
            title=ABOUT_TITLE,
            title_font_size=FONT_SIZE_H1,
            create_content_callback=self._create_about_content)
        self.about_panel.pack(expand=True, fill=tk.BOTH)

    def _create_about_content(self, root_frame):
        content_frame = ttk.Frame(master=root_frame)

        self.top_panel = ttk.Frame(content_frame)
        self._init_top_panel(self.top_panel)
        self.top_panel.pack(expand=True, fill=tk.BOTH)

        self.bottom_panel = ttk.Frame(content_frame)
        self.bottom_panel.pack(expand=True, fill=tk.BOTH)

        return content_frame

    def _init_top_panel(self, root_frame):
        self.profile_picture = tk.Canvas(root_frame, width=PROFILE_PICTURE_WIDTH, height=PROFILE_PICTURE_HEIGHT)
        self.profile_picture.create_rectangle(0, 0, PROFILE_PICTURE_WIDTH, PROFILE_PICTURE_HEIGHT, fill='white')
        self.profile_picture.pack(side=tk.LEFT)

        self.biodata_panel = ttk.Frame(root_frame)
        self._init_biodata_panel(self.biodata_panel)
        self.biodata_panel.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    # region top_panel_components
    def _init_biodata_panel(self, root_frame):
        self.lbl_name_caption = self._create_label(root_frame, "Nama")
        self.lbl_name_caption.grid(row=0, column=0, sticky="w")

        self.lbl_name_content = self._create_label(root_frame, ABOUT_NAME)
        self.lbl_name_content.grid(row=0, column=1, sticky="w")

        self.lbl_nim_caption = self._create_label(root_frame, "NIM")
        self.lbl_nim_caption.grid(row=1, column=0, sticky="w")

        self.lbl_nim_content = self._create_label(root_frame, ABOUT_NIM)
        self.lbl_nim_content.grid(row=1, column=1, sticky="w")

        self.lbl_class_caption = self._create_label(root_frame, "Kelas")
        self.lbl_class_caption.grid(row=2, column=0, sticky="w")

        self.lbl_class_content = self._create_label(root_frame, ABOUT_CLASS)
        self.lbl_class_content.grid(row=2, column=1, sticky="w")

        self.lbl_lecturer_caption = self._create_label(root_frame, "Dosen")
        self.lbl_lecturer_caption.grid(row=3, column=0, sticky="w")

        self.lbl_lecturer_content = self._create_label(root_frame, ABOUT_LECTURER)
        self.lbl_lecturer_content.grid(row=3, column=1, sticky="w")

    def _create_label(self, root_frame, text):
        return ttk.Label(
            master=root_frame,
            text= text,
            font=(DEFAULT_FONT, FONT_SIZE_NORMAL)
        )
    # endregion top_panel_components

    # region bottom_panel_components

    # endregion bottom_panel_components
