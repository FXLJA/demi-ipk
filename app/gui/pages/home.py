import os.path
import matplotlib
import tkinter as tk

from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from PIL import ImageTk, Image
import cv2
from app.core.utils.gann_io import load_gann

from app.core.common.color_converter import *
from app.core.utils.color_gann_helper import *
from app.core.utils.dominant_color_analyzer import DominantColorAnalyzer

from app.config.gui_config import *
from app.config.global_config import *

from app.gui.common.slider import HSlider
from app.gui.common.frame_group import FrameGroup
from app.gui.common.fancy_color import FancyColor

from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class HomeFrame(ttk.Frame):
    def __init__(self, togi_gui, **kw):
        self.togi_gui = togi_gui
        self.gambar_poster = None
        self.poster_path = None
        self.main_gann = load_gann(MAIN_GANN_PATH)

        super().__init__(**kw)
        self._init_components()

    def _init_components(self):
        self.top_frame = ttk.Frame(self)

        self.btn_cari = ttk.Button(self.top_frame, text="Open FIle", command=self._on_btn_cari_pressed)
        self.btn_cari.pack(side=tk.LEFT, padx=(0, DEFAULT_PAD_X))

        self.btn_analyze = ttk.Button(self.top_frame, text="Check Genre", command=self._on_btn_analyze_pressed)
        self.btn_analyze.pack(side=tk.LEFT)

        self.top_frame.pack(side=tk.TOP, pady=(0, DEFAULT_PAD_Y*3))

        self.image_frame = tk.Canvas(self, width=POSTER_CANVAS_WIDTH, height=POSTER_CANVAS_HEIGHT)
        self.image_frame.pack(side=tk.TOP)

    def _on_btn_cari_pressed(self):
        filename = filedialog.askopenfilename(
            title="Open an image file",
            filetypes=IMAGE_FILE_TYPES
        )

        if filename == "":
            return

        self.set_poster_image(filename)

    def set_poster_image(self, image_path):
        image = cv2.imread(image_path)

        if image is None:
            messagebox.showerror("Error load image", "Failed to load image at %s" % image_path)
            return

        self.poster_path = image_path

        hasil = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        hasil = cv2.resize(hasil, (int(POSTER_CANVAS_WIDTH), int(POSTER_CANVAS_HEIGHT)))
        self.gambar_poster = ImageTk.PhotoImage(Image.fromarray(hasil))
        self.image_frame.create_image(0, 0, anchor=tk.NW, image=self.gambar_poster)

    def _on_btn_analyze_pressed(self):
        if self.poster_path is None:
            messagebox.showerror("Error! Missing Poster!", "Tidak ada poster untuk dianalisis" % image_path)
            return

        colors, percentages = self._analyze_poster(self.poster_path, K_MEANS_CLUSTER_TOTAL_DEFAULT)
        poster_theme = self._get_poster_theme(self.main_gann, colors, percentages)
        messagebox.showinfo("Hasil Analisis", "Poster tersebut bergenre : %s" % poster_theme)

    def _analyze_poster(self, file_name, k_means_value):
        analyzer = DominantColorAnalyzer(k_means_value)
        analyzer.analyze_path(file_name)
        colors = analyzer.get_top_5_colors()
        percentages = analyzer.get_top_5_colors_percentage()

        return colors, percentages

    def _get_poster_theme(self, main_gann, colors, percentages):
        gann_input = create_to_gann_input(colors / 255.0, percentages)
        gann_result = main_gann.forward(gann_input)
        return self.get_catagory_from_gann_result(gann_result)

    def get_catagory_from_gann_result(self, gann_result):
        gann_result = gann_result[0]

        if gann_result[0] > gann_result[1] and gann_result[0] > gann_result[2] and gann_result[0] > 0.5:
            return "Horror"
        if gann_result[1] > gann_result[0] and gann_result[1] > gann_result[2] and gann_result[1] > 0.5:
            return "Romantic"
        if gann_result[2] > gann_result[0] and gann_result[2] > gann_result[1] and gann_result[2] > 0.5:
            return "Sci-fi"
        return "No Category"