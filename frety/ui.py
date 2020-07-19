from tkinter import Frame, BOTH, Canvas, ROUND, YES

class Window(Frame):
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._model = model
        self._board = Board(model, *args, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        self.note_selected = lambda *a, **kw: None
        self._board.note_selected = lambda *a, **kw: self.note_selected(*a, **kw)


class Board(Frame):
    def __init__(self, model, *args, **kwargs):
        self._model = model
        self._width = kwargs.pop('width', 1200)
        self._height = kwargs.pop('height', 300)

        super().__init__(*args, **kwargs)
        self.master.title('Frety')

        self._padding = 0
        self._factor =  self._model.Mansur / self._model.Frets[-1]
        self._model.resize(self._width * self._factor)

        self._canvas = Canvas(self, bg='white', **kwargs)
        self._canvas.pack(fill=BOTH, expand=YES)
        self._init_board()
        self.pack(fill=BOTH, expand=YES)

        self.bind('<Configure>', self._on_configure)
        self._canvas.bind("<Button-1>", self._on_button_1)

        self.note_selected = lambda *a, **kw: None

    def _on_configure(self, event):
        wscale = float(event.width) / self._width
        hscale = float(event.height) / self._height
        self._width = event.width
        self._height = event.height
        self._padding *= wscale
        self._model.resize(self._width * self._factor)
        self._canvas.scale('all', 0, 0, wscale, hscale)

    def _on_button_1(self, event):
        fret = [i for i, distance in enumerate(self._model.Frets) if event.x < distance + self._padding][0]
        string = (event.y - self._padding) // ((self._height - self._padding * 2) / len(self._model.Strings))

        fret = int(min(max(0, fret), len(self._model.Frets) - 1))
        string = int(min(max(0, string), len(self._model.Strings) - 1))

        self.note_selected(string, fret)

    def _init_board(self):
        self._padding = self._height // 10

        self._canvas.create_line(
            self._padding // 2,
            0,
            self._padding,
            self._padding,
            width=8, fill='gray', capstyle=ROUND, joinstyle=ROUND)
        self._canvas.create_line(
            self._padding,
            self._height - self._padding,
            self._padding // 2,
            self._height,
            width=8, fill='gray', capstyle=ROUND, joinstyle=ROUND)

        for fret in range(0, len(self._model.Frets)):
            self._canvas.create_line(
                self._padding + self._model.Frets[fret],
                self._padding,
                self._padding + self._model.Frets[fret],
                self._height - self._padding,
                width=8, fill='gray', capstyle=ROUND, joinstyle=ROUND)

        space = (self._height - (self._padding * 2)) // len(self._model.Strings)
        for i, thickness in enumerate(self._model.Strings):
            self._canvas.create_line(
                0,
                self._padding + (i + .5) * space,
                self._width,
                self._padding + (i + .5) * space,
                width=thickness, capstyle=ROUND)
