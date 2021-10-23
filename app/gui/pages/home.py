import tkinter as tk
from tkinter import ttk

from app.gui.config.config import *
from app.gui.common.frame_group import FrameGroup
from app.gui.common.fancy_color import FancyColor
from app.gui.common.slider import HSlider


class HomeFrame(ttk.Frame):
    def __init__(self, **kw):
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
        self.color_frame.pack(side=tk.LEFT, expand=True, fill=tk.Y, padx=(DEFAULT_PAD_X, 0))

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

        self.entry_search_image = ttk.Entry(content_frame, width=10, font=(DEFAULT_FONT, FONT_SIZE_NORMAL))
        self.entry_search_image.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.btn_search_image = self._create_search_image_button(content_frame)
        self.btn_search_image.pack(side=tk.RIGHT)

        return content_frame

    def _create_search_image_button(self, root_frame):
        return ttk.Button(
            master=root_frame,
            text="Search",
            command=self._on_search_button_pressed
        )

    def _create_k_value_frame(self, root_frame):
        return FrameGroup(
            master=root_frame,
            title="K Value",
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
            value=12,
            min_value=5,
            max_value=32,
            label_format="{:.0f}",
            label_width=2
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

        self.canvas_poster = tk.Canvas(root_frame, width=230, height=345)
        self.canvas_poster.create_rectangle(0, 0, 230, 345, fill='white')
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
    # endregion
    # endregion

    def _on_search_button_pressed(self):
        print("Search button pressed!")

    def _on_analyze_button_pressed(self):
        print("Analyze button pressed!")
