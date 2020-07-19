from frety.abcplus import AbcPlus


class Controller:
    def __init__(self, ui, model):
        self._ui = ui
        self._model = model
        self._abcplus = AbcPlus(self._model.string_notes, self._model.fret_count)
        self._ui.note_selected = self._on_note_selected

    def prepare(self):
        pass

    def _on_note_selected(self, string, fret):
        note = self._abcplus.note(string, fret)
        print(f'On string {string}, fret {fret}: {note}')


