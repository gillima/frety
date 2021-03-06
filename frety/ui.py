from tkinter import Frame, BOTH, Canvas, ROUND, YES, Label, LEFT, RIGHT, RAISED, X

from frety.utils import CallableCollection


class Window(Frame):
    def __init__(self, root, *args, **kwargs):
        self._model = kwargs.pop('model')

        super().__init__(root, *args, **kwargs)
        root.title('Frety')
        self.pack(fill=BOTH, expand=True)

        frame = Frame(self)
        frame.pack(fill=X)
        self._question = Label(frame, text='A', font='-size 30')
        self._question.pack(side=LEFT)
        self._selected = Label(frame, text='', font='-size 30')
        self._selected.pack(side=RIGHT)

        self._board = FretBoard(self, *args, **kwargs, model=self._model)
        self.note_selected = self._board.note_selected

    def ask_for_note(self, note):
        self._question.configure(text=note)

    def show_selected(self, note):
        self._selected.configure(text=note)


class FretBoard(Frame):
    FRET_COLOR = 'gray'
    MARKER_COLOR = 'lightgray'
    STRING_COLOR = 'black'

    def __init__(self, *args, **kwargs):
        self._model = kwargs.pop('model')
        self._width = kwargs.pop('width', 1200)
        self._height = kwargs.pop('height', 300)

        super().__init__(*args, **kwargs)

        self._padding = 0
        self._factor = self._model.mansur / self._model.fret_positions[-1]
        self._model.resize(self._width * self._factor)

        self._canvas = Canvas(self, bg='white', **kwargs)
        self._canvas.pack(fill=BOTH, expand=YES)
        self._init_board()
        self.pack(fill=BOTH, expand=YES)

        self.bind('<Configure>', self._on_configure)
        self._canvas.bind("<Button-1>", self._on_button_1)

        self.note_selected = CallableCollection()

    def _on_configure(self, event):
        wscale = float(event.width) / self._width
        hscale = float(event.height) / self._height
        self._width = event.width
        self._height = event.height
        self._padding *= wscale
        self._model.resize(self._width * self._factor)
        self._canvas.scale('all', 0, 0, wscale, hscale)

    def _on_button_1(self, event):
        fret = [i for i, distance in enumerate(self._model.fret_positions) if event.x < distance + self._padding][0]
        string = (event.y - self._padding) // ((self._height - self._padding * 2) / len(self._model.string_thickness))

        fret = int(min(max(0, fret), len(self._model.fret_positions) - 1))
        string = int(min(max(0, string), len(self._model.string_thickness) - 1))

        self.note_selected(string, fret)

    def _init_board(self):
        self._padding = self._height // 10
        space = (self._height - (self._padding * 2)) // len(self._model.string_thickness)

        self._canvas.create_line(
            self._padding // 2,
            0,
            self._padding,
            self._padding,
            width=8, fill=FretBoard.FRET_COLOR, capstyle=ROUND, joinstyle=ROUND)
        self._canvas.create_line(
            self._padding,
            self._height - self._padding,
            self._padding // 2,
            self._height,
            width=8, fill=FretBoard.FRET_COLOR, capstyle=ROUND, joinstyle=ROUND)

        for i, c in self._model.markers:
            pos = (self._model.fret_positions[i - 1] + self._model.fret_positions[i]) / 2
            radius = (self._padding / 3)
            if c == 1:
                self._canvas.create_oval(
                    self._padding + pos - radius,
                    self._height / 2 - radius,
                    self._padding + pos + radius,
                    self._height / 2 + radius,
                    fill=FretBoard.MARKER_COLOR)
            else:
                self._canvas.create_oval(
                    self._padding + pos - radius,
                    self._height / 2 - space - radius,
                    self._padding + pos + radius,
                    self._height / 2 - space + radius,
                    fill=FretBoard.MARKER_COLOR)
                self._canvas.create_oval(
                    self._padding + pos - radius,
                    self._height / 2 + space - radius,
                    self._padding + pos + radius,
                    self._height / 2 + space + radius,
                    fill=FretBoard.MARKER_COLOR)

        for fret in range(0, len(self._model.fret_positions)):
            self._canvas.create_line(
                self._padding + self._model.fret_positions[fret],
                self._padding,
                self._padding + self._model.fret_positions[fret],
                self._height - self._padding,
                width=8, fill=FretBoard.FRET_COLOR, capstyle=ROUND, joinstyle=ROUND)

        for i, thickness in enumerate(self._model.string_thickness):
            self._canvas.create_line(
                0,
                self._padding + (i + .5) * space,
                self._width,
                self._padding + (i + .5) * space,
                width=thickness, fill=FretBoard.STRING_COLOR, capstyle=ROUND)
