ALL_NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

from typing import List, Any

class Note:
  """Represents a note.

  Attributes:
      note: str, string representation
      intervalToTonic: str, interval to tonic, if this note is in a scale
      selected: bool, this note is selected
      fretStr: str, string to show on fretboard
  """
  def __init__(self,
      note: str,
      intervalToTonic: str = None,
      selected: bool = False) -> None:
    self.note = self.normalize(note)
    self.intervalToTonic = intervalToTonic
    self.selected = selected
    self.update()

  def select(self, select: bool = True) -> Note:
    """Marks or unmarks this note as selected."""
    self.selected = select
    return self

  def interval(self, interval: str = None) -> Note:
    """Sets interval relative to tonic."""
    self.intervalToTonic = interval
    return self

  def update(self) -> None:
    """Updates all derived attributes, such as those used in Vue."""
    self.fretStr = sprintf('  %-2s  ', self.note)

  @classmethod
  def normalize(self, note: str) -> str:
    """Simplifies and normalizes flats to sharps."""
    note = Tonal.Note.simplify(note)
    if note.endswith('b'):
      note = Tonal.Note.enharmonic(note)
    return note


class Scale:
  """Represents a scale.

  Attributes:
      root: Note, root note
      scale: str, scale type
      notes: [Note], list of notes
      all_notes: [Note], 12 chromatic notes (some selected), used for UI
  """
  def __init__(self,
      root: Note = Note('C', '1P', True),
      scale: str = 'ionian') -> None:
    self.root = root
    self.scale = scale
    self.update()

  def setRoot(self, note: str) -> Scale:
    """Sets root note."""
    self.root = Note(note, '1P', True)
    self.update()
    return self

  def setScale(self, scale: str) -> Scale:
    """Sets scale type."""
    self.scale = scale
    self.update()
    return self

  def update(self):
    """Updates all derived attributes."""
    tonal_notes_str = Tonal.Scale.notes('{0} {1}'.format(self.root.note, self.scale))
    notes_str = []
    for note_str in tonal_notes_str:
      notes_str.append(Note.normalize(note_str))

    self.notes = []
    self.all_notes = []
    for note_str in ALL_NOTES:
      selected = notes_str.includes(note_str)
      interval = Tonal.Distance.interval(self.root.note, note_str)
      if selected:
        self.notes.append(Note(note_str, interval, selected))
      self.all_notes.append(Note(note_str, interval, selected))


class Fretboard(object):
  """Represents a fretboard.

  Attributes:
    frets: map [string: int][fret: int] -> Note, all frets
  """
  def __init__(self):
    self.frets = {}
    openNotes = ['E', 'B', 'G', 'D', 'A', 'E']
    for string, openNote in enumerate(openNotes):
      self.frets[string] = {}
      for fret in range(22):
        note = Note.normalize(Tonal.Distance.transpose(
            openNote, Tonal.Interval.fromSemitones(fret)))
        self.frets[string][fret] = Note(note)

  def showScale(self, scale: Scale):
    """Shows notes in this scale on the fretboard."""
    notes = scale.notes
    notes_str = []
    for note in scale.notes:
      notes_str.append(note.note)

    for string in range(6):
      for fret in range(22):
        # Testing a string in a list of strings.
        # Try testing a Note object in a list of Notes instead.
        index = notes_str.indexOf(self.frets[string][fret].note)
        if index != -1:
          self.frets[string][fret].select().interval(
              scale.notes[index].intervalToTonic)
        else:
          self.frets[string][fret].select(False).interval(None)


class App(object):
  def __init__(self):
    self.scale = Scale()
    self.fretboard = Fretboard()
    self.fretboard.showScale(self.scale)

    # For debugging
    window.s = self.scale
    window.fb = self.fretboard

  def start(self) -> None:
    console.log('python start()')
    self.initVue()

  def initVue(self) -> None:
    window.app = __new__(Vue({
      'el': '#app',
      'data': {
        'scale': self.scale,
        'fretboard': self.fretboard,
      },
    }))

window.addEventListener('load', lambda: App().start())