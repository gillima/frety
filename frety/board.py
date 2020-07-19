class Board:
    NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    def __init__(self, count=12, length=628, strings=None):
        self._fret_count = count
        self._mansur = length
        self._strings = strings or [('E', 1), ('B', 2), ('G', 3), ('D', 4), ('A', 5), ('E', 6)]
        self._positions = None
        self.resize(length)

    @property
    def Frets(self):
        return self._positions

    @property
    def Strings(self):
        return [thickness for note, thickness in self._strings]

    @property
    def Mansur(self):
        return self._mansur

    def resize(self, length):
        self._positions = list(self._calculate_frets(length))


    def note(self, string, fret):
        note_pos = Board.NOTES.index(self._strings[string][0])
        note_pos = (note_pos + fret) % len(Board.NOTES)
        return Board.NOTES[note_pos]

    def _calculate_frets(self, length):
        position = 0
        yield position
        for i in range(self._fret_count):
            distance = length / 17.817
            position += distance
            yield position
            length -= distance