import os.path
import matplotlib
import tkinter as tk

from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from PIL import ImageTk, Image

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
        self.poster_img_raw = None
        self.poster_img = None

        super().__init__(**kw)
        self._init_components()

    # region init_components
    def _init_components(self):
        self.upper_frame = ttk.Frame(self)
        self._init_upper_frame_content(self.upper_frame)
        self.upper_frame.pack(side=tk.TOP, fill=tk.BOTH, pady=(0, DEFAULT_PAD_Y))

        self.lower_frame = ttk.Frame(self)
        self._init_lower_frame_content(self.lower_frame)
        self.lower_frame.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH, pady=(DEFAULT_PAD_Y, 0))

    def _init_upper_frame_content(self, root_frame):
        self.search_img_frame = self._create_search_image_frame(root_frame)
        self.search_img_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, DEFAULT_PAD_X))

        self.k_means_frame = self._create_k_value_frame(root_frame)
        self.k_means_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=DEFAULT_PAD_X)

        self.analyze_frame = self._create_analyze_frame(root_frame)
        self.analyze_frame.pack(side=tk.LEFT, padx=(DEFAULT_PAD_X, 0))

    def _init_lower_frame_content(self, root_frame):
        self.poster_frame = self._create_poster_frame(root_frame)
        self.poster_frame.pack(side=tk.LEFT, expand=True, fill=tk.Y, padx=(0, DEFAULT_PAD_X))

        self.color_frame = self._create_color_frame(root_frame)
        self.color_frame.pack(side=tk.LEFT, expand=True, fill=tk.Y, padx=(DEFAULT_PAD_X, DEFAULT_PAD_X))

        self.histogram_frame = self._create_histogram_frame(root_frame)
        self.histogram_frame.pack(side=tk.LEFT, expand=True, fill=tk.Y, padx=(DEFAULT_PAD_X, 0))

    # region upper_frame_components
    def _create_search_image_frame(self, root_frame):
        return FrameGroup(
            master=root_frame,
            title="Search Image",
            title_font_size=FONT_SIZE_H2,
            create_content_callback=self._create_search_image_content
        )

    def _create_search_image_content(self, root_frame):
        content_frame = ttk.Frame(master=root_frame)

        self.entry_search_image = self._create_entry_search_image(content_frame)
        self.entry_search_image.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.btn_search_image = self._create_search_image_button(content_frame)
        self.btn_search_image.pack(side=tk.RIGHT, padx=DEFAULT_PAD_X)

        return content_frame

    def _create_entry_search_image(self, root_frame):
        entry = ttk.Entry(root_frame, width=30, font=(DEFAULT_FONT, FONT_SIZE_NORMAL))
        entry.insert(0, DEFAULT_POSTER_FILE_PATH)
        return entry

    def _create_search_image_button(self, root_frame):
        return ttk.Button(
            master=root_frame,
            text="Search",
            command=self._on_search_button_pressed
        )

    def _create_k_value_frame(self, root_frame):
        return FrameGroup(
            master=root_frame,
            title="K-Value",
            title_font_size=FONT_SIZE_H2,
            create_content_callback=self._create_k_value_content
        )

    def _create_k_value_content(self, root_frame):
        content_frame = ttk.Frame(master=root_frame)

        self.slider_k_value = self._create_slider_k_value(content_frame)
        self.slider_k_value.pack(side=tk.LEFT, expand=True, fill=tk.X)

        return content_frame

    def _create_slider_k_value(self, root_frame):
        return HSlider(
            master=root_frame,
            value=K_MEANS_CLUSTER_TOTAL_DEFAULT,
            min_value=K_MEANS_CLUSTER_TOTAL_MIN,
            max_value=K_MEANS_CLUSTER_TOTAL_MAX,
            step=K_MEANS_CLUSTER_TOTAL_STEP,
            label_format=K_MEANS_CLUSTER_TOTAL_TEXT_FORMAT,
            label_width=K_MEANS_CLUSTER_TOTAL_TEXT_WIDTH
        )

    def _create_analyze_frame(self, root_frame):
        return FrameGroup(
            master=root_frame,
            title_font_size=FONT_SIZE_H2,
            create_content_callback=self._create_analyze_content
        )

    def _create_analyze_content(self, root_frame):
        content_frame = tk.Frame(root_frame)

        self.btn_analyze = self._create_analyze_button(content_frame)
        self.btn_analyze.pack()

        return content_frame

    def _create_analyze_button(self, root_frame):
        return ttk.Button(
            master=root_frame,
            text="Analyze",
            command=self._on_analyze_button_pressed
        )

    # endregion upper_frame_components
    # region lower_frame_components
    def _create_poster_frame(self, root_frame):
        return FrameGroup(
            master=root_frame,
            title="Poster",
            title_font_size=FONT_SIZE_H1,
            create_content_callback=self._create_poster_content
        )

    def _create_poster_content(self, root_frame):
        content_frame = ttk.Frame(master=root_frame)

        self.canvas_poster = tk.Canvas(root_frame, width=POSTER_CANVAS_WIDTH, height=POSTER_CANVAS_HEIGHT)
        self.canvas_poster.create_rectangle(0, 0, POSTER_CANVAS_WIDTH, POSTER_CANVAS_HEIGHT, fill='white')
        self.canvas_poster.pack()

        return content_frame

    def _create_color_frame(self, root_frame):
        return FrameGroup(
            master=root_frame,
            title="Dominant Color",
            title_font_size=FONT_SIZE_H1,
            create_content_callback=self._create_color_content
        )

    def _create_color_content(self, root_frame):
        content_frame = ttk.Frame(master=root_frame)
        self.fancy_colors = self._create_fancy_colors(content_frame, 5)
        return content_frame

    def _create_fancy_colors(self, root_frame, total):
        fancy_colors = []
        for _i in range(total):
            fancy_colors += [self._create_fancy_color(root_frame)]
        return fancy_colors

    def _create_fancy_color(self, root_frame):
        fancy_color = FancyColor(master=root_frame)
        fancy_color.pack(side=tk.TOP, pady=8)
        return fancy_color

    def _create_histogram_frame(self, root_frame):
        return FrameGroup(
            master=root_frame,
            title="Histogram",
            title_font_size=FONT_SIZE_H1,
            create_content_callback=self._create_histogram_content,
        )

    def _create_histogram_content(self, root_frame):
        content_frame = ttk.Frame(master=root_frame)

        self.histogram_fig = Figure(figsize=(HISTOGRAM_CANVAS_WIDTH, HISTOGRAM_CANVAS_HEIGHT), dpi=100, tight_layout=True)

        self.canvas_histogram = FigureCanvasTkAgg(self.histogram_fig, master=root_frame)
        self.canvas_histogram.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1, pady=(0, DEFAULT_PAD_Y / 2))

        return content_frame

    # endregion
    # endregion

    def _on_search_button_pressed(self):
        filename = filedialog.askopenfilename(
            title="Open an image file",
            initialdir=DEFAULT_POSTER_DIR_PATH,
            filetypes=IMAGE_FILE_TYPES
        )

        if filename == "":
            return

        self.set_search_image_entry_text(filename)
        self.set_poster_image(filename)

    def _on_analyze_button_pressed(self):
        filename = self.get_poster_filename()
        k_means_value = self.get_k_means_value()
        main_gann = self.get_best_gann()

        if not os.path.isfile(filename):
            messagebox.showerror("Missing Poster!", "Posternya mana WOI!")
            return

        if main_gann is None:
            messagebox.showerror("Missing GANN!", "Tolong Load GANN dulu atau Load Dataset untuk buat GANN baru")
            return

        colors, percentages = self._analyze_poster(filename, k_means_value)
        poster_theme, gann_result = self._get_poster_theme(main_gann, colors, percentages)

        self.set_poster_image(filename)
        self.set_displayed_dominant_colors(colors)
        self.update_histogram()
        self._display_poster_theme_result(poster_theme, gann_result)

    def update_histogram(self):
        if self.histogram_fig.axes:
            self.histogram_fig.delaxes(self.histogram_fig.axes[0])

        img = cv2.imread(self.get_poster_filename())
        color = ('b', 'g', 'r')
        plt = self.histogram_fig.add_subplot(111)
        plt.set_xlabel('Nilai channel')
        plt.set_ylabel('Jumlah piksel')

        for i, col in enumerate(color):
            hist = cv2.calcHist([img], [i], None, [256], [0, 256])
            plt.plot(hist, color=col)

        self.canvas_histogram.draw()

    def set_best_gann(self, gann):
        self.togi_gui.best_gann = gann

    def get_best_gann(self):
        return self.togi_gui.best_gann

    def set_search_image_entry_text(self, new_text):
        self.entry_search_image.delete(0, tk.END)
        self.entry_search_image.insert(0, new_text)

    def set_poster_image(self, filename):
        image = cv2.imread(filename)

        if image is None:
            messagebox.showerror("Error load image", "Failed to load image at %s" % image_path)
            return

        hasil = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        hasil = cv2.resize(hasil, (int(POSTER_CANVAS_WIDTH), int(POSTER_CANVAS_HEIGHT)))
        self.poster_img = ImageTk.PhotoImage(Image.fromarray(hasil))
        self.canvas_poster.create_image(0, 0, anchor=tk.NW, image=self.poster_img)

    def set_displayed_dominant_colors(self, colors):
        for i in range(5):
            rgb = yuv_to_rgb(colors[i])
            self.fancy_colors[i].set_color(rgb)

    def get_poster_filename(self):
        return self.entry_search_image.get()

    def get_k_means_value(self):
        return self.slider_k_value.get_value()

    def get_catagory_from_gann_result(self, gann_result):
        gann_result = gann_result[0]

        if gann_result[0] > gann_result[1] and gann_result[0] > gann_result[2] and gann_result[0] > 0.5:
            return "Horror", gann_result[0] * 100
        if gann_result[1] > gann_result[0] and gann_result[1] > gann_result[2] and gann_result[1] > 0.5:
            return "Romantic", gann_result[1] * 100
        if gann_result[2] > gann_result[0] and gann_result[2] > gann_result[1] and gann_result[2] > 0.5:
            return "Sci-fi", gann_result[2] * 100
        return "Unidentified", 0

    def _analyze_poster(self, file_name, k_means_value):
        analyzer = DominantColorAnalyzer(k_means_value)
        analyzer.analyze_path(file_name)
        colors = analyzer.get_top_5_colors()
        percentages = analyzer.get_top_5_colors_percentage()

        return colors, percentages

    def _get_poster_theme(self, main_gann, colors, percentages):
        gann_input = create_to_gann_input(colors / 255.0, percentages)
        gann_result = main_gann.forward(gann_input)
        return self.get_catagory_from_gann_result(gann_result), gann_result

    def _display_poster_theme_result(self, poster_theme, themes):
        title = "Analyse Result"
        msg = "The Poster's color scheme is indicating:\n\n%s (Confidence: %.2f%%)" % poster_theme
        msg += "\n Horror: %.4f \n Romance: %.4f \n Sci-Fi: %.4f" % (themes[0][0], themes[0][1], themes[0][2])
        messagebox.showinfo(title, msg)
