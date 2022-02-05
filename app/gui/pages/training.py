import tkinter as tk

from threading import Thread

from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from app.core.utils.gann_io import *
from app.core.utils.color_analyzer_dataset_io import *
from app.core.utils.gann_trainer import GANNTrainer, GANNTrainerConfig

from app.config.gui_config import *
from app.config.global_config import *

from app.gui.common.slider import HSlider
from app.gui.common.frame_group import FrameGroup


class TrainingFrame(tk.Frame):
    def __init__(self, togi_gui, **kw):
        self.togi_gui = togi_gui
        self.dataset = None
        self.gann_trainer = None
        self.gann_trainer_config = GANNTrainerConfig()

        super().__init__(**kw)
        self._init_components()

    # region init_components
    def _init_components(self):
        self.root_frame = ttk.Frame(self)
        self.root_frame.pack(expand=True, fill=tk.BOTH, pady=(0, DEFAULT_PAD_Y * 3))

        self.lbl_title = ttk.Label(self.root_frame, text="Training Form", font=(DEFAULT_FONT, FONT_SIZE_H0))
        self.lbl_title.pack(side=tk.TOP, pady=(0, DEFAULT_PAD_Y * 2))

        self.top_frame = ttk.Frame(self.root_frame)
        self._init_top_frame_content(self.top_frame)
        self._configure_top_frame_weight()
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH, pady=DEFAULT_PAD_Y * 2)

        self.middle_frame = ttk.Frame(self.root_frame)
        self._init_middle_frame_content(self.middle_frame)
        self.middle_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH, pady=DEFAULT_PAD_Y * 2)

        self.bottom_frame = ttk.Frame(self.root_frame)
        self._init_bottom_frame_content(self.bottom_frame)
        self._configure_bottom_frame_weight()
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(DEFAULT_PAD_Y * 2, 0))

    def _init_top_frame_content(self, root_frame):
        self.load_dataset_frame = self._create_load_dataset_frame(root_frame)
        self.load_dataset_frame.grid(row=0, column=0, sticky="ew", padx=(0, DEFAULT_PAD_X))
        # self.load_dataset_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, DEFAULT_PAD_X))

        self.load_gann_frame = self._create_load_gann_frame(root_frame)
        self.load_gann_frame.grid(row=0, column=1, sticky="ew", padx=(DEFAULT_PAD_X, 0))
        # self.load_gann_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(DEFAULT_PAD_X, 0))

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

    def _configure_top_frame_weight(self):
        self.top_frame.columnconfigure(0, weight=1, uniform="col-group")
        self.top_frame.columnconfigure(1, weight=1, uniform="col-group")

    def _configure_bottom_frame_weight(self):
        self.bottom_frame.columnconfigure(0, weight=1)
        self.bottom_frame.columnconfigure(1, weight=1)
        self.bottom_frame.columnconfigure(2, weight=1)
        self.bottom_frame.columnconfigure(3, weight=1)

    # region top_frame_components
    def _create_load_dataset_frame(self, root_frame):
        return FrameGroup(
            master=root_frame,
            title="Load Dataset",
            title_font_size=FONT_SIZE_H2,
            create_content_callback=self._create_load_dataset_content
        )

    def _create_load_dataset_content(self, root_frame):
        content_frame = ttk.Frame(master=root_frame)

        self.entry_load_dataset = self._create_entry_load_dataset(content_frame)
        self.entry_load_dataset.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.btn_load_dataset_search = self._create_btn_load_dataset_search(content_frame)
        self.btn_load_dataset_search.pack(side=tk.LEFT)

        return content_frame

    def _create_entry_load_dataset(self, root_frame):
        entry = ttk.Entry(root_frame, width=30, font=(DEFAULT_FONT, FONT_SIZE_NORMAL))
        entry.insert(0, DEFAULT_DATASET_FILE_PATH)
        return entry

    def _create_btn_load_dataset_search(self, root_frame):
        return ttk.Button(
            master=root_frame,
            text="Search",
            command=self._on_load_dataset_search_button_pressed
        )

    def _create_load_gann_frame(self, root_frame):
        return FrameGroup(
            master=root_frame,
            title="Load GNN",
            title_font_size=FONT_SIZE_H2,
            create_content_callback=self._create_load_gann_content
        )

    def _create_load_gann_content(self, root_frame):
        content_frame = ttk.Frame(master=root_frame)

        self.entry_load_gann = self._create_entry_load_gann(content_frame)
        self.entry_load_gann.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.btn_load_gann_search = self._create_btn_load_gann_search(content_frame)
        self.btn_load_gann_search.pack(side=tk.LEFT)

        self.btn_save_gann = self._create_btn_save_gann(content_frame)
        self.btn_save_gann.pack(side=tk.RIGHT, padx=(DEFAULT_PAD_X, 0))

        return content_frame

    def _create_entry_load_gann(self, root_frame):
        entry = ttk.Entry(root_frame, width=30, font=(DEFAULT_FONT, FONT_SIZE_NORMAL))
        entry.insert(0, DEFAULT_GANN_FILE_PATH)
        return entry

    def _create_btn_load_gann_search(self, root_frame):
        return ttk.Button(
            master=root_frame,
            text="Search",
            command=self._on_load_gann_search_button_pressed
        )

    def _create_btn_save_gann(self, root_frame):
        return ttk.Button(
            master=root_frame,
            text="Save GNN",
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

        self.slider_training_ratio = self._create_training_ratio_slider(content_frame)
        self.slider_training_ratio.pack(expand=True, fill=tk.X)

        return content_frame

    def _create_training_ratio_slider(self, root_frame):
        return HSlider(
            master=root_frame,
            value=TRAINING_RATIO_DEFAULT,
            min_value=TRAINING_RATIO_MIN,
            max_value=TRAINING_RATIO_MAX,
            step=TRAINING_RATIO_STEP,
            label_format=TRAINING_RATIO_TEXT_FORMAT,
            label_width=TRAINING_RATIO_TEXT_WIDTH
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
            value=TOTAL_POPULATION_DEFAULT,
            min_value=TOTAL_POPULATION_MIN,
            max_value=TOTAL_POPULATION_MAX,
            step=TOTAL_POPULATION_STEP,
            label_format=TOTAL_POPULATION_TEXT_FORMAT,
            label_width=TOTAL_POPULATION_TEXT_WIDTH
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
            value=MUTATION_RATE_DEFAULT,
            min_value=MUTATION_RATE_MIN,
            max_value=MUTATION_RATE_MAX,
            step=MUTATION_RATE_STEP,
            label_format=MUTATION_RATE_TEXT_FORMAT,
            label_width=MUTATION_RATE_TEXT_WIDTH
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
            text="Test Score: 100.0000%"
        )

    def _create_lbl_train_score(self, root_frame):
        return ttk.Label(
            master=root_frame,
            text="Training Score: 100.0000%"
        )

    def _create_cb_auto_train(self, root_frame):
        self.cb_auto_train_value = tk.BooleanVar()

        return ttk.Checkbutton(
            master=root_frame,
            text="Auto-train",
            variable=self.cb_auto_train_value,
            onvalue=True,
            offvalue=False
        )

    def _create_progress_training(self, root_frame):
        return ttk.Progressbar(
            master=root_frame,
            orient='horizontal',
            mode='determinate'
        )

    # endregion
    # endregion

    def _on_load_dataset_search_button_pressed(self):
        filename = filedialog.askopenfilename(
            title="Open a dataset file",
            initialdir=DEFAULT_DATASET_DIR_PATH,
            filetypes=DATASET_FILE_TYPES
        )

        if filename == "":
            return

        self.gann_trainer = self._create_gann_trainer(filename)
        if self.get_best_gann() is not None:
            self.gann_trainer.set_best_gann(self.get_best_gann())
        self.update_best_gann_from_trainer()
        self.set_dataset_entry_text(filename)

    def _on_load_gann_search_button_pressed(self):
        filename = filedialog.askopenfilename(
            title="Open a GNN file",
            initialdir=DEFAULT_GANN_DIR_PATH,
            filetypes=GANN_FILE_TYPES
        )

        if filename == "":
            return

        gann, training_score, test_score = load_gann(filename)
        if self.gann_trainer is not None:
            self.gann_trainer.set_best_gann(gann)
        self.set_best_gann(gann)
        self.set_gann_entry_text(filename)
        self.set_training_score_text(training_score)
        self.set_test_score_text(test_score)

    def _on_save_gann_button_pressed(self):
        if self.get_best_gann() is None:
            messagebox.showerror("Missing GNN!", "GANN belom ada, udah main simpen-simpen aja ya")
            return

        filename = filedialog.asksaveasfilename(
            title="Save a GNN file",
            initialdir=DEFAULT_GANN_DIR_PATH,
            filetypes=GANN_FILE_TYPES
        )

        if filename == "":
            return
        if not filename.endswith(".gnn"):
            filename = filename + ".gnn"

        best_gann = self.get_best_gann()
        save_gann(filename, best_gann, self.gann_trainer.get_best_gann_train_score(),
                  self.gann_trainer.get_best_gann_test_score())

    def _on_train_button_pressed(self):
        if self.gann_trainer is None:
            messagebox.showerror("Missing Dataset!", "Datasetnya mana, Bapak?!")
            return

        self.btn_training['state'] = tk.DISABLED
        self._update_GANN_trainer_config()
        self.start_training_thread()

    def _on_training_thread_finished(self):
        isAutoTrain = self.cb_auto_train_value.get()
        if isAutoTrain:
            self.update_best_gann_from_trainer()
            self.start_training_thread()
        else:
            self.update_best_gann_from_trainer()
            self.btn_training['state'] = tk.ACTIVE

    def update_best_gann_from_trainer(self):
        best_gann = self.gann_trainer.get_best_gann()
        self.set_best_gann(best_gann)

    def start_training_thread(self):
        self._update_GANN_trainer_config()

        training_thread = ASyncTraining(self.gann_trainer)
        training_thread.start()

        self._monitor_training_thread(training_thread)

    def set_best_gann(self, gann):
        self.togi_gui.best_gann = gann

    def get_best_gann(self):
        return self.togi_gui.best_gann

    def set_dataset_entry_text(self, new_text):
        self.entry_load_dataset.delete(0, tk.END)
        self.entry_load_dataset.insert(0, new_text)

    def set_gann_entry_text(self, new_text):
        self.entry_load_gann.delete(0, tk.END)
        self.entry_load_gann.insert(0, new_text)

    def set_training_score_text(self, score):
        self.lbl_train_score.config(text="Training Score: %.4f%%" % (score * 100))

    def set_test_score_text(self, score):
        self.lbl_test_score.config(text="Test Score: %.4f%%" % (score * 100))

    def get_training_ratio(self):
        return self.slider_training_ratio.get_value()

    def get_mutation_rate(self):
        return self.slider_mutation_rate.get_value()

    def get_total_population(self):
        return self.slider_total_population.get_value()

    def _create_gann_trainer(self, filename):
        raw_dataset = load_dataset(filename)
        dataset = self._create_dataset_analyzer(raw_dataset)
        return self._create_GANN_trainer(dataset)

    def _create_dataset_analyzer(self, raw_dataset):
        training_ratio = self.get_training_ratio()
        return ColorAnalyzerDataset(raw_dataset, training_ratio)

    def _create_GANN_trainer(self, dataset):
        self._update_GANN_trainer_config()
        return GANNTrainer(dataset, self.gann_trainer_config)

    def _update_GANN_trainer_config(self):
        self.gann_trainer_config.gann_shape = DEFAULT_GANN_SHAPE
        self.gann_trainer_config.mutation_rate = self.get_mutation_rate()
        self.gann_trainer_config.population_size = self.get_total_population()

    def _monitor_training_thread(self, thread):
        if thread.is_alive():
            self.progress_training['value'] = thread.get_progress() * 100
            self.after(100, lambda: self._monitor_training_thread(thread))
        else:
            self._on_training_thread_finished()


class ASyncTraining(Thread):
    def __init__(self, gann_trainer):
        super().__init__()
        self.gann_trainer = gann_trainer

    def run(self):
        self.gann_trainer.next_generation()

    def get_progress(self):
        return self.gann_trainer.get_evaluation_progress_percentage()
