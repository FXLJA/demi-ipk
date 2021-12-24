import webbrowser
import tkinter as tk

from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from threading import Thread
from PIL import ImageTk, Image

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
        self.image_buffers = []

        self.lbl_title = ttk.Label(self, text="Biodata Pengembang", font=(DEFAULT_FONT, FONT_SIZE_H0))
        self.lbl_title.pack(side=tk.TOP, pady=(0, DEFAULT_PAD_Y * 2))

        self.top_panel = ttk.Frame(self)
        self._init_top_panel(self.top_panel)
        self.top_panel.pack(expand=True, fill=tk.Y)

        self.bottom_panel = ttk.Frame(self)
        self._init_bottom_panel(self.bottom_panel)
        self.bottom_panel.pack()

    def _init_top_panel(self, root_frame):
        self.profile_picture = tk.Canvas(root_frame, width=PROFILE_PICTURE_WIDTH, height=PROFILE_PICTURE_HEIGHT)
        self.profile_picture.create_rectangle(0, 0, PROFILE_PICTURE_WIDTH, PROFILE_PICTURE_HEIGHT, fill='white')
        self._init_profile_picture(self.profile_picture)
        self.profile_picture.pack(side=tk.TOP, pady=(0, DEFAULT_PAD_Y * 5))

        self.biodata_panel = ttk.Frame(root_frame)
        self._init_biodata_panel(self.biodata_panel)
        self.biodata_panel.pack(side=tk.TOP)

    def _init_bottom_panel(self, root_frame):
        self.icon_discord = self._create_clickable_icon(root_frame, DISCORD_PICTURE_PATH, self._on_discord_picture_clicked)
        self.icon_discord.pack(side=tk.LEFT)

        self.icon_github = self._create_clickable_icon(root_frame, GITHUB_PICTURE_PATH, self._on_github_picture_clicked)
        self.icon_github.pack(side=tk.LEFT)

        self.icon_linkedin = self._create_clickable_icon(root_frame, LINKEDIN_PICTURE_PATH, self._on_linkedin_picture_clicked)
        self.icon_linkedin.pack(side=tk.LEFT)

        self.icon_steam = self._create_clickable_icon(root_frame, STEAM_PICTURE_PATH, self._on_steam_picture_clicked)
        self.icon_steam.pack(side=tk.LEFT)

    # region top_panel_components
    def _init_profile_picture(self, canvas):
        img_raw = Image.open(PROFILE_PICTURE_PATH)
        img = ImageTk.PhotoImage(img_raw)
        self.image_buffers += [img]

        canvas.create_image(0, 0, anchor=tk.NW, image=img)

    def _init_biodata_panel(self, root_frame):
        self.lbl_name_caption = self._create_label(root_frame, "Nama")
        self.lbl_name_caption.grid(row=0, column=0, sticky="w", padx=(0, DEFAULT_PAD_X * 5), pady=DEFAULT_PAD_Y)

        self.lbl_name_content = self._create_label(root_frame, ABOUT_NAME)
        self.lbl_name_content.grid(row=0, column=1, sticky="w")

        self.lbl_nim_caption = self._create_label(root_frame, "NIM")
        self.lbl_nim_caption.grid(row=1, column=0, sticky="w", padx=(0, DEFAULT_PAD_X * 5), pady=DEFAULT_PAD_Y)

        self.lbl_nim_content = self._create_label(root_frame, ABOUT_NIM)
        self.lbl_nim_content.grid(row=1, column=1, sticky="w")

        self.lbl_class_caption = self._create_label(root_frame, "Kelas")
        self.lbl_class_caption.grid(row=2, column=0, sticky="w", padx=(0, DEFAULT_PAD_X * 5), pady=DEFAULT_PAD_Y)

        self.lbl_class_content = self._create_label(root_frame, ABOUT_CLASS)
        self.lbl_class_content.grid(row=2, column=1, sticky="w")

        self.lbl_lecturer_caption = self._create_label(root_frame, "Dosen")
        self.lbl_lecturer_caption.grid(row=3, column=0, sticky="w", padx=(0, DEFAULT_PAD_X * 5), pady=DEFAULT_PAD_Y)

        self.lbl_lecturer_content = self._create_label(root_frame, ABOUT_LECTURER)
        self.lbl_lecturer_content.grid(row=3, column=1, sticky="w")

    def _create_label(self, root_frame, text):
        return ttk.Label(
            master=root_frame,
            text=text,
            font=(DEFAULT_FONT, FONT_SIZE_H2)
        )

    # endregion top_panel_components

    # region bottom_panel_components
    def _create_clickable_icon(self, root_frame, image_path, callback):
        image_raw = Image.open(image_path)
        image = ImageTk.PhotoImage(image_raw)

        self.image_buffers += [image]
        lbl = ttk.Label(master=root_frame, image=image, text="test")
        lbl.bind('<Button-1>', callback)
        return lbl

    # endregion bottom_panel_components
    def _on_discord_picture_clicked(self, event):
        webbrowser.open(LINK_DISCORD)

    def _on_github_picture_clicked(self, event):
        webbrowser.open(LINK_GITHUB)

    def _on_linkedin_picture_clicked(self, event):
        webbrowser.open(LINK_LINKEDIN)

    def _on_steam_picture_clicked(self, event):
        webbrowser.open(LINK_STEAM)
