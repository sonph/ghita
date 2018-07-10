from typing import List, Any, Optional

import utils

NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
SCALES = ['ionian', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'aeolian',
    'locrian', 'blues', 'major pentatonic', 'minor pentatonic',
    'harmonic minor', 'melodic minor']

# TODO: Make a standard list of chord types, and possibly a text box
CHORDS = ['M', 'm', 'aug', 'dim',
          'minor7', 'maj7', 'aug7', 'dim7',
          '9', '11', '13']
FRET_MARKERS = [0, 3, 5, 7, 9, 12, 15, 17, 19]

SCALES_INTERVALS = []
for scale in SCALES:
  SCALES_INTERVALS.append(Tonal.Scale.intervals(scale).join(' '))

CHORDS_INTERVALS = []
for chord in CHORDS:
  CHORDS_INTERVALS.append(Tonal.Chord.intervals(chord).join(' '))

VUE_CONSTANTS = {
  'NOTES': NOTES,
  'SCALES': SCALES,
  'SCALE_SELECTORS': utils.transpose([NOTES, SCALES, SCALES_INTERVALS, CHORDS, CHORDS_INTERVALS]),
  'FRET_MARKERS': FRET_MARKERS,
}


class Note:
  """Represents a note.

  Attributes:
      note: str, string representation
      intervalToTonic: str, interval to tonic, if this note is in a scale
      selected: bool, this note is selected
  """
  def __init__(self,
      note: str,
      intervalToTonic: str = None,
      selected: bool = False) -> None:
    self.note = self.normalize(note)
    self.intervalToTonic = intervalToTonic
    self.selected = selected
    self._update()

  def select(self, select: bool = True) -> Note:
    """Marks or unmarks this note as selected."""
    self.selected = select
    return self

  def interval(self, interval: str = None) -> Note:
    """Sets interval relative to tonic."""
    self.intervalToTonic = interval
    return self

  def _update(self) -> None:
    """Updates all derived attributes, such as those used in Vue."""
    pass

  @classmethod
  def normalize(self, note: str) -> str:
    """Simplifies and normalizes flats to sharps."""
    note = Tonal.Note.simplify(note)
    if note.endswith('b'):
      note = Tonal.Note.enharmonic(note)
    return note


class NotesCollection:
  """Collection of notes.

  Attributes:
      notes: List[Note], list of notes
      all_notes_sorted: List[Note], 12 chromatic notes (some selected),
          starting from A
      all_notes: List[Note], similar to all_notes_sorted, but starting from root
  """
  def __init__(self):
    pass

  def _getNotes(self) -> List[str]:
    """Gets notes as strings in this particular collection."""
    raise NotImplementedError()

  def _updateNotes(self):
    tonal_notes_str = self._getNotes()

    notes_str = []
    for note_str in tonal_notes_str:
      notes_str.append(Note.normalize(note_str))

    self.notes = []
    self.all_notes_sorted = []
    for index, note_str in enumerate(NOTES):
      selected = notes_str.includes(note_str)
      interval = Tonal.Distance.interval(self.root.note, note_str)
      if selected:
        self.notes.append(Note(note_str, interval, selected))
      self.all_notes_sorted.append(Note(note_str, interval, selected))

      if note_str == self.root.note:
        root_index = index

    self.all_notes = utils.shift_cycle(self.all_notes_sorted, root_index)


class Chord(NotesCollection):
  """Represents a chord.

  Attributes:
      root: Note, root note
      chord: str, chord type

    inherited from NotesCollection:
      notes
      all_notes
      all_notes_sorted
  """
  def __init__(self,
      root: Note = Note('C', '1P', True),
      chord: str = 'M') -> None:
    self.root = root
    self.chord = chord
    self._update()

  def setRoot(self, root: str) -> Chord:
    self.root = Note(root, '1P', True)
    self._update()
    return self

  def setChord(self, chord: str) -> Chord:
    self.chord = chord
    self._update()
    return self

  def setRootAndChord(self, root, chord):
    self.root = Note(root, '1P', True)
    self.chord = chord
    self._update()

  def _getNotes(self) -> List[str]:
    return Tonal.Chord.notes('{0} {1}'.format(self.root.note, self.chord))

  def contains(self, note_to_check: str) -> Optional[str]:
    """Checks if the chord contains the note.

    Returns:
        interval if True, None otherwise.
    """
    for note in self.notes:
      if note_to_check == note.note:
        return note.intervalToTonic
    return None

  def _update(self):
    """Updates all derived attributes, such as those used in Vue."""
    console.log('updating chord ' + self.root.note + ' ' + self.chord)
    self._updateNotes()


class Scale(NotesCollection):
  """Represents a scale.

  Attributes:
      root: Note, root note
      scale: str, scale type

      chords: [str], possible chords with current root, for suggestion in
          selector UI
      all_chords: Dict[str, List[str]], map of notes in scale to possible
          chords, used to look at chord progressions
      all_chords_transposed: List[List[str]], transposed all_chords, used for UI

    inherited from NotesCollection:
      notes
      all_notes
      all_notes_sorted
  """
  def __init__(self,
      root: str = 'C',
      scale: str = 'ionian') -> None:
    self.root = Note(root, '1P', True)
    self.scale = scale
    self._update()

  def setRoot(self, note: str) -> Scale:
    self.root = Note(note, '1P', True)
    self._update()
    return self

  def setScale(self, scale: str) -> Scale:
    self.scale = scale
    self._update()
    return self

  def setRootAndScale(self, root: str, scale: str) -> None:
    self.root = Note(root, '1P', True)
    self.scale = scale
    self._update()

  def contains(self, note_to_check: str) -> Optional[str]:
    """Checks if the scale contains the note.

    Returns:
        interval if True, None otherwise.
    """
    for note in self.notes:
      if note_to_check == note.note:
        return note.intervalToTonic
    return None

  def _getNotes(self) -> List[str]:
    return Tonal.Scale.notes('{0} {1}'.format(self.root.note, self.scale))

  def _update(self):
    """Updates all derived attributes."""
    console.log('updating scale ' + self.root.note + ' ' + self.scale)
    self._updateNotes()

    scaleNameStr = '{0} {1}'.format(self.root.note, self.scale)
    self.chords = Tonal.Scale.chords(scaleNameStr)

    self.all_chords = {}
    modes = Tonal.Scale.modeNames(scaleNameStr)
    # TODO: For blues, we only get 2 alternate modes.
    # TODO: It's possible to use Tonal.Detect.chords, but result is pretty fuzzy
    for mode in modes:
      rootNote = mode[0]
      self.all_chords[rootNote] = Tonal.Scale.chords(
          '{0} {1}'.format(rootNote, mode[1]))

    arrays = []
    for note in NOTES:
      if note in self.all_chords:
        arrays.append(self.all_chords[note])
      else:
        # Empty list of chords for notes that are not in scale.
        arrays.append([])
    self.all_chords_transposed = utils.transpose(arrays)


class Fret:
  """Represents a fret.

  Attributes:
    note: Note, note
    marker: bool, if this has a fret marker
    fretStr: str, string to show on fretboard
    fretNumber: int, fret number
  """
  def __init__(self,
      note: Note,
      marker: bool,
      fretNumber: int) -> None:
    self.note = note
    self.marker = marker
    self.fretNumber = fretNumber


class Fretboard:
  """Represents a fretboard.

  Attributes:
    frets: map [string: int][fret: int] -> Note, all frets
    shownFrets: [Fret], frets currently shown
  """
  def __init__(self):
    self.shownFrets = []
    self.frets = {}
    openNotes = ['E', 'B', 'G', 'D', 'A', 'E']
    for string, openNote in enumerate(openNotes):
      self.frets[string] = {}
      for fret in range(22):
        note = Note.normalize(Tonal.Distance.transpose(
            openNote, Tonal.Interval.fromSemitones(fret)))
        self.frets[string][fret] = Fret(
            Note(note), FRET_MARKERS.indexOf(fret) != -1, fret)

  def showScale(self, scale: Scale):
    """Shows notes in this scale on the fretboard."""
    self.reset()

    notes = scale.notes
    notes_str = []
    for note in scale.notes:
      notes_str.append(note.note)

    for string in range(6):
      for fret in range(22):
        # Testing a string in a list of strings.
        # Try testing a Note object in a list of Notes instead.
        index = notes_str.indexOf(self.frets[string][fret].note.note)
        if index != -1:
          self.frets[string][fret].note.select().interval(
              scale.notes[index].intervalToTonic)
          self.shownFrets.append(self.frets[string][fret])

  def reset(self):
    for fret in self.shownFrets:
      fret.note.select(False).interval(None)
    self.shownFrets = []


class App(object):
  def __init__(self):
    self.scale = Scale()
    self.chord = Chord()
    self.fretboard = Fretboard()
    self.fretboard.showScale(self.scale)

    # For debugging
    window.s = self.scale
    window.fb = self.fretboard
    window.chord = self.chord

  def start(self) -> None:
    console.log('python start()')
    self.initVue()

  def initVue(self) -> None:
    # (#15) Workaround.
    if not window.vue_loaded:
      window.vue_loaded = True
      window.app = __new__(Vue({
        'el': '#app',
        'data': {
          'scale': self.scale,
          'chord': self.chord,
          'fretboard': self.fretboard,
          'VUE_CONSTANTS': VUE_CONSTANTS,
        },
      }))

window.addEventListener('load', lambda: App().start())