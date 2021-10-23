import tkinter as tk
from tkinter import ttk

from app.gui.config.config import *
from app.gui.common.frame_group import FrameGroup
from app.gui.common.slider import HSlider


class TrainingFrame(tk.Frame):
    def __init__(self, **kw):
        super().__init__(**kw)
        self._init_components()

    # region init_components
    def _init_components(self):
        self.root_frame = ttk.Frame(self)
        self.root_frame.pack(expand=True, fill=tk.X, pady=(0, DEFAULT_PAD_Y*3))

        self.top_frame = ttk.Frame(self.root_frame)
        self._init_top_frame_content(self.top_frame)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH, pady=(0, DEFAULT_PAD_Y*2))

        self.middle_frame = ttk.Frame(self.root_frame)
        self._init_middle_frame_content(self.middle_frame)
        self.middle_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH, pady=DEFAULT_PAD_Y*2)

        self.bottom_frame = ttk.Frame(self.root_frame)
        self._init_bottom_frame_content(self.bottom_frame)
        self._configure_bottom_frame_weight()
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(DEFAULT_PAD_Y*2, 0))

    def _init_top_frame_content(self, root_frame):
        self.load_dataset_frame = self._create_load_dataset_frame(root_frame)
        self.load_dataset_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, DEFAULT_PAD_X))

        self.load_gann_frame = self._create_load_gann_frame(root_frame)
        self.load_gann_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(DEFAULT_PAD_X, 0))

    def _init_middle_frame_content(self, root_frame):
        self.training_ratio_frame = self._create_training_ratio_frame(root_frame)
        self.training_ratio_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, DEFAULT_PAD_X))

        self.total_population_frame = self._create_total_population_frame(root_frame)
        self.total_population_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=DEFAULT_PAD_X)

        self.mutation_rate_frame = self._create_mutation_rate_frame(root_frame)
        self.mutation_rate_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(DEFAULT_PAD_X, 0))

    def _init_bottom_frame_content(self, root_frame):
        self.btn_training = self._create_btn_training(root_frame)
        self.btn_training.grid(row=0, column=0, sticky="w")

        self.lbl_test_score = self._create_lbl_test_score(root_frame)
        self.lbl_test_score.grid(row=0, column=1)

        self.lbl_train_score = self._create_lbl_train_score(root_frame)
        self.lbl_train_score.grid(row=0, column=2)

        self.cb_auto_train = self._create_cb_auto_train(root_frame)
        self.cb_auto_train.grid(row=0, column=3, sticky="e")

        self.progress_training = self._create_progress_training(root_frame)
        self.progress_training.grid(row=1, column=0, columnspan=4, sticky="ew", pady=(DEFAULT_PAD_Y, 0))

    def _configure_bottom_frame_weight(self):
        self.bottom_frame.columnconfigure(0, weight=1)
        self.bottom_frame.columnconfigure(1, weight=1)
        self.bottom_frame.columnconfigure(2, weight=1)
        self.bottom_frame.columnconfigure(3, weight=1)

    # region top_frame_components
    def _create_load_dataset_frame(self, root_frame):
        return FrameGroup(
            master=root_frame,
            title="Load Data Set",
            title_font_size=FONT_SIZE_H2,
            create_content_callback=self._create_load_dataset_content
        )

    def _create_load_dataset_content(self, root_frame):
        content_frame = ttk.Frame(master=root_frame)

        self.entry_load_dataset = ttk.Entry(content_frame, width=10, font=(DEFAULT_FONT, FONT_SIZE_NORMAL))
        self.entry_load_dataset.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.btn_load_dataset_search = self._create_btn_load_dataset_search(content_frame)
        self.btn_load_dataset_search.pack(side=tk.LEFT)

        return content_frame

    def _create_btn_load_dataset_search(self, root_frame):
        return ttk.Button(
            master=root_frame,
            text="Search",
            command=self._on_load_dataset_search_button_pressed
        )

    def _create_load_gann_frame(self, root_frame):
        return FrameGroup(
            master=root_frame,
            title="Load GANN",
            title_font_size=FONT_SIZE_H2,
            create_content_callback=self._create_load_gann_content
        )

    def _create_load_gann_content(self, root_frame):
        content_frame = ttk.Frame(master=root_frame)

        self.entry_load_gann = ttk.Entry(content_frame, width=10, font=(DEFAULT_FONT, FONT_SIZE_NORMAL))
        self.entry_load_gann.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.btn_load_gann_search = self._create_btn_load_gann_search(content_frame)
        self.btn_load_gann_search.pack(side=tk.LEFT)

        self.btn_save_gann = self._create_btn_save_gann(content_frame)
        self.btn_save_gann.pack(side=tk.RIGHT)

        return content_frame

    def _create_btn_load_gann_search(self, root_frame):
        return ttk.Button(
            master=root_frame,
            text="Search",
            command=self._on_load_gann_search_button_pressed
        )

    def _create_btn_save_gann(self, root_frame):
        return ttk.Button(
            master=root_frame,
            text="Save GANN",
            command=self._on_save_gann_button_pressed
        )
    # endregion
    # region middle_frame_components
    def _create_training_ratio_frame(self, root_frame):
        return FrameGroup(
            master=root_frame,
            title="Training Ratio",
            title_font_size=FONT_SIZE_H2,
            create_content_callback=self._create_training_ratio_content
        )

    def _create_training_ratio_content(self, root_frame):
        content_frame = ttk.Frame(master=root_frame)

        self.slider_training_ratio= self._create_training_ratio_slider(content_frame)
        self.slider_training_ratio.pack(expand=True, fill=tk.X)

        return content_frame

    def _create_training_ratio_slider(self, root_frame):
        return HSlider(
            master=root_frame,
            value=0.8,
            min_value=0,
            max_value=1,
            step=0.01,
            label_format="{:.2f}"
        )

    def _create_total_population_frame(self, root_frame):
        return FrameGroup(
            master=root_frame,
            title="Total Population",
            title_font_size=FONT_SIZE_H2,
            create_content_callback=self._create_total_population_content
        )

    def _create_total_population_content(self, root_frame):
        content_frame = ttk.Frame(master=root_frame)

        self.slider_total_population = self._create_total_population_slider(content_frame)
        self.slider_total_population.pack(expand=True, fill=tk.X)

        return content_frame

    def _create_total_population_slider(self, root_frame):
        return HSlider(
            master=root_frame,
            value=1000,
            min_value=100,
            max_value=5000,
            step=100,
            label_format="{:.0f}"
        )

    def _create_mutation_rate_frame(self, root_frame):
        return FrameGroup(
            master=root_frame,
            title="Mutation Rate",
            title_font_size=FONT_SIZE_H2,
            create_content_callback=self._create_mutation_rate_content
        )

    def _create_mutation_rate_content(self, root_frame):
        content_frame = ttk.Frame(master=root_frame)

        self.slider_mutation_rate = self._create_mutation_rate_slider(content_frame)
        self.slider_mutation_rate.pack(expand=True, fill=tk.X)

        return content_frame

    def _create_mutation_rate_slider(self, root_frame):
        return HSlider(
            master=root_frame,
            value=0.1,
            min_value=0.0001,
            max_value=0.25,
            step=0.0001,
            label_format="{:.4f}"
        )
    # endregion
    # region bottom_frame_components
    def _create_btn_training(self, root_frame):
        return ttk.Button(
            master=root_frame,
            text="Training",
            command=self._on_train_button_pressed
        )

    def _create_lbl_test_score(self, root_frame):
        return ttk.Label(
            master=root_frame,
            text="Test Score: 100.0%"
        )

    def _create_lbl_train_score(self, root_frame):
        return ttk.Label(
            master=root_frame,
            text="Training Score: 100.0%"
        )

    def _create_cb_auto_train(self, root_frame):
        return ttk.Checkbutton(
            master=root_frame,
            text="Auto-train"
        )

    def _create_progress_training(self, root_frame):
        return ttk.Progressbar(
            master=root_frame,
            orient='horizontal',
            mode='indeterminate'
        )
    # endregion
    # endregion

    def _on_load_dataset_search_button_pressed(self):
        print("Load Dataset search pressed!")

    def _on_load_gann_search_button_pressed(self):
        print("Load GANN search pressed!")

    def _on_save_gann_button_pressed(self):
        print("Save GANN pressed!")

    def _on_train_button_pressed(self):
        print("Train button pressed!")
