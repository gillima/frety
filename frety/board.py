class Board:
    NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    def __init__(self, frets=13, length=628, strings=None):
        self._fret_count = frets
        self._mansur = length
        self._strings = strings or [('e', 1), ('b', 2), ('G', 3), ('D', 4), ('A,', 5), ('E,,', 6)]
        self._positions = None
        self.resize(length)

    @property
    def fret_count(self):
        return self._fret_count

    @property
    def fret_positions(self):
        return self._positions

    @property
    def string_thickness(self):
        return [thickness for note, thickness in self._strings]

    @property
    def string_notes(self):
        return [note for note, thickness in self._strings]

    @property
    def mansur(self):
        return self._mansur

    def resize(self, length):
        self._positions = list(self._calculate_frets(length))

    def _calculate_frets(self, length):
        position = 0
        yield position
        for i in range(self._fret_count):
            distance = length / 17.817
            position += distance
            yield position
            length -= distance