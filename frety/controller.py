import itertools
import random

from frety.abcplus import AbcPlus


class Controller:
    def __init__(self, ui, model):
        self._ui = ui
        self._model = model
        self._abcplus = AbcPlus(self._model.string_notes, self._model.fret_count)
        self._ui.note_selected = self._on_note_selected
        self._all_notes = list(set(itertools.chain.from_iterable(s[:-1] for s in self._abcplus.strings)))
        self._next_note = ''

    def next(self):
        self._next_note = random.choice(self._all_notes)
        self._ui.ask_for_note(self._next_note)

    def _on_note_selected(self, string, fret):
        note = self._abcplus.note(string, fret)
        print(f'On string {string}, fret {fret}: {note}')
        if note == self._next_note:
            print(f'Correct')
            self.next()


