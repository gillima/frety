class Controller:
    def __init__(self, ui, model):
        self._ui = ui
        self._model = model
        self._ui.note_selected = self._on_note_selected
        self._expected = list()

    def setup(self, notes):
        self._expected = notes

    def _on_note_selected(self, string, fret):
        note = self._model.note(string, fret)
        print(f'On string {string}, fret {fret}: {note}')
        if (self._expected[0] == note):
            self._expected = self._expected[1:]
        if (not self._expected):
            print("You did it")


