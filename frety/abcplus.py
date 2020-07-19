class AbcPlus:
    """
    This class is used to convert a note using the ABCPLus notation into
    the list of string/fret combinations who represent the note.

    For more info about ABCPLus see: http://penzeng.de/Geige/Abc.htm
    """

    def __init__(self, open_notes=None, frets=14):
        open_notes = open_notes or ("e", "b", "G", "D,", "A,", "E,,")
        self._strings = [list(self._init_string(note, frets)) for note in open_notes]

    def note(self, string, fret):
        return self._strings[string][fret]

    @staticmethod
    def _init_string(note, frets):
        yield note

        is_upper = note[0] == note[0].upper()
        modifiers = note.count(',') if is_upper else note.count("'")
        for i in range(frets):
            note = note.replace("'", '').replace(',', '')

            if note.upper() in 'ACDFG':
                note += "#"
            else:
                note = chr(ord(note[0]) + 1)

            if note[0].upper() == 'H':
                note = 'A'
                if modifiers == 0:
                    if not is_upper:
                        modifiers += 1
                    else:
                        is_upper = False
                else:
                    modifiers += -1 if is_upper else 1

            note = note.upper() if is_upper else note.lower()
            note += (',' if is_upper else "'") * modifiers
            yield note
