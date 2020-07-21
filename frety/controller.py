import itertools
import random

from frety.abcplus import AbcPlus


class Controller:
    def __init__(self, ui, model):
        self._ui = ui
        self._model = model
        self._abcplus = AbcPlus(self._model.string_notes, self._model.fret_count)
        self._ui.note_selected += self._on_note_selected
        self._note_selection = list()
        self._next_note = ''
        self.learn_all()

    def learn_all(self):
        self._note_selection = list(set(itertools.chain.from_iterable(s[:-1] for s in self._abcplus.strings)))
        self.next()

    def learn_0_5(self):
        self._note_selection = list()
        for f in [0, 4]:
            self._note_selection.extend(self._abcplus.note(s, f if f != 5 or s != 2 else 4) for s in range(6))
        self.next()

    def next(self):
        current = self._next_note
        while current == self._next_note:
            self._next_note = random.choice(self._note_selection)
        self._ui.ask_for_note(self._next_note)

    def _on_note_selected(self, string, fret):
        note = self._abcplus.note(string, fret)
        print(f'On string {string}, fret {fret}: {note}')
        if note == self._next_note:
            print(f'Correct')
            self.next()


