from app.gui.common.frame_group import FrameGroup


class FrameGroupBuilder:
    def __init__(self):
        self._title = ""
        self._title_font_size = 24

    def with_title(self, title):
        self._title = title
        return self

    def with_title_font_size(self, font_size):
        self._title_font_size = font_size
        return self

    def reset(self):
        self.__init__()

    def build(self):
        frame_group = FrameGroup(title=self._title, title_font_size=self._title_font_size)
        self.reset()
        return frame_group
