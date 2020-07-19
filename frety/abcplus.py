class AbcPlus:
    """
    This class is used to convert a note using the ABCPLus notation into
    the list of string/fret combinations who represent the note.

    For more info about ABCPLus see: http://penzeng.de/Geige/Abc.htm
    """

    def __init__(self, open_notes=None, frets=14):
        open_notes = open_notes or ("e", "b", "G", "D,", "A,", "E,,")
        self._strings = [list(self.get_notes(note, frets)) for note in open_notes]

    @property
    def strings(self):
        return self._strings

    def note(self, string, fret):
        return self._strings[string][fret]

    @staticmethod
    def get_notes(start, count):
        yield start

        is_upper = start[0] == start[0].upper()
        modifiers = start.count(',') if is_upper else start.count("'")
        for i in range(count):
            start = start.replace("'", '').replace(',', '')

            if start.upper() in 'ACDFG':
                start += "#"
            else:
                start = chr(ord(start[0]) + 1)

            if start[0].upper() == 'H':
                start = 'A'
                if modifiers == 0:
                    if not is_upper:
                        modifiers += 1
                    else:
                        is_upper = False
                else:
                    modifiers += -1 if is_upper else 1

            start = start.upper() if is_upper else start.lower()
            start += (',' if is_upper else "'") * modifiers
            yield start
