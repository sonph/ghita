from typing import Any, Dict, List, Optional, Callable

import app_config
import constants
import utils


__pragma__('skip')
# Hack to ignore static check errors on objects included at runtime.
__pragma__ = window = console = __new__ = object()  # type: Any
Tone = Tonal = Set = Vue = object()
__pragma__('noskip')

class Note:
  """Represents a note.

  Attributes:
      note: str, string representation
      interval_to_tonic: str, interval to tonic, if this note is in a scale
      selected: bool, this note is selected
  """
  def __init__(self,
      note: str,
      interval_to_tonic: str = None,
      selected: bool = False) -> None:
    self.note = self.normalize(note)
    self.interval_to_tonic = interval_to_tonic
    self.selected = selected
    self.update()

  def select(self, select: bool = True) -> Note:
    """Marks or unmarks this note as selected."""
    self.selected = select
    return self

  def interval(self, interval: str = None) -> Note:
    """Sets interval relative to tonic."""
    self.interval_to_tonic = interval
    return self

  def update(self) -> None:
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
      type: str, 'chord' or 'scale'
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

  def updateNotes(self):
    tonal_notes_str = self._getNotes()

    notes_str = []
    for note_str in tonal_notes_str:
      notes_str.append(Note.normalize(note_str))

    self.notes = []
    self.all_notes_sorted = []
    for index, note_str in enumerate(constants.NOTES):
      selected = notes_str.includes(note_str)
      interval = Tonal.Distance.interval(self.root.note, note_str)
      if selected:
        self.notes.append(Note(note_str, interval, selected))
      self.all_notes_sorted.append(Note(note_str, interval, selected))

      if note_str == self.root.note:
        root_index = index

    self.all_notes = utils.rotate(self.all_notes_sorted, root_index)


class Chord(NotesCollection):
  """Represents a chord.

  Attributes:
      root: Note, root note
      chord: str, chord type

    inherited from NotesCollection:
      type
      notes
      all_notes
      all_notes_sorted
  """
  TYPE = 'chord'

  def __init__(self,
      config: app_config.AppConfig,
      root: Note = Note('C', '1P', True),
      chord: str = 'M') -> None:
    self.type = self.TYPE
    self.config = config
    self.root = root
    self.chord = chord
    self.update()

  def setRoot(self, root: str) -> Chord:
    self.root = Note(root, '1P', True)
    self.update()
    return self

  def setChord(self, chord: str) -> Chord:
    self.chord = chord
    self.update()
    return self

  def setRootAndChord(self, root, chord):
    self.root = Note(root, '1P', True)
    self.chord = chord
    self.update()

  def _getNotes(self) -> List[str]:
    return Tonal.Chord.notes('{0} {1}'.format(self.root.note, self.chord))

  def contains(self, note_to_check: str) -> Optional[str]:
    """Checks if the chord contains the note.

    Returns:
        interval if True, None otherwise.
    """
    for note in self.notes:
      if note_to_check == note.note:
        return note.interval_to_tonic
    return None

  def update(self):
    """Updates all derived attributes, such as those used in Vue."""
    console.log('updating chord ' + self.root.note + ' ' + self.chord)
    self.updateNotes()


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
      type
      notes
      all_notes
      all_notes_sorted
  """
  TYPE = 'scale'

  def __init__(self,
      config: app_config.AppConfig,
      root: str = 'C',
      scale: str = 'ionian') -> None:
    self.type = self.TYPE
    self.config = config
    self.root = Note(root, '1P', True)
    self.scale = scale
    self.update()

  def setRoot(self, note: str) -> Scale:
    self.root = Note(note, '1P', True)
    self.update()
    return self

  def setScale(self, scale: str) -> Scale:
    self.scale = scale
    self.update()
    return self

  def setRootAndScale(self, root: str, scale: str) -> None:
    self.root = Note(root, '1P', True)
    self.scale = scale
    self.update()

  def contains(self, note_to_check: str) -> Optional[str]:
    """Checks if the scale contains the note.

    Returns:
        interval if True, None otherwise.
    """
    for note in self.notes:
      if note_to_check == note.note:
        return note.interval_to_tonic
    return None

  def _getNotes(self) -> List[str]:
    return Tonal.Scale.notes('{0} {1}'.format(self.root.note, self.scale))

  def update(self):
    """Updates all derived attributes."""
    console.log('updating scale ' + self.root.note + ' ' + self.scale)
    self.updateNotes()

    scaleNameStr = '{0} {1}'.format(self.root.note, self.scale)
    self.chords = Tonal.Scale.chords(scaleNameStr)

    self.all_chords = {}
    modes = Tonal.Scale.modeNames(scaleNameStr)
    # TODO: For blues, we only get 2 alternate modes.
    # TODO: It's possible to use Tonal.Detect.chords, but result is pretty fuzzy
    for mode in modes:
      rootNote = mode[0]
      chordsForNote = Tonal.Scale.chords(
          '{0} {1}'.format(rootNote, mode[1]))
      if self.config.simple_chords:
        chordsForNote = chordsForNote.filter(
            lambda c: constants.CHORDS_SET.has(c))
      self.all_chords[rootNote] = chordsForNote

    # Construct transposed array for available chords for each note in scale.
    arrays = []
    for note in self.all_notes:
      if note.note in self.all_chords:
        arrays.append(self.all_chords[note.note])
      else:
        # Empty list of chords for notes that are not in scale.
        arrays.append([])
    self.all_chords_transposed = utils.transpose(arrays)


class Fret:
  """Represents a fret.

  Attributes:
    note: Note, note
    marker: bool, if this has a fret marker
    fret_number: int, fret number
  """
  def __init__(self,
      note: Note,
      marker: bool,
      fret_number: int) -> None:
    self.note = note
    self.marker = marker
    self.fret_number = fret_number


class Fretboard:
  """Represents a fretboard.

  Attributes:
    instrument_config: Dict[str, Any], instrument config in constants module
    frets: Dict[int, Dict[int, Fret]], map [string][fret] to Note, representing
        all frets
    shown_frets: List[Fret], frets currently shown
  """
  def __init__(self, config: app_config.AppConfig) -> None:
    self.config = config
    self.update()

  def update(self):
    self.shown_frets = []  # type: List[Fret]
    self.frets = {}  # type: Dict[int, Dict[int, Fret]]

    if self.config.instrument == 'guitar':
      self.instrument_config = constants.GUITAR
    elif self.config.instrument == 'ukulele':
      self.instrument_config = constants.UKULELE

    for string, open_note in enumerate(self.instrument_config['OPEN_NOTES']):
      self.frets[string] = {}
      for fret in range(self.instrument_config['FRETS']):
        note = Note.normalize(Tonal.Distance.transpose(
            open_note, Tonal.Interval.fromSemitones(fret)))
        self.frets[string][fret] = Fret(
            Note(note), self.instrument_config['FRET_MARKERS'].has(fret), fret)

  def showNotes(self, notes_collection: NotesCollection):
    """Shows notes in this collection on the fretboard."""
    self.reset()

    notes_str = []
    for note in notes_collection.notes:
      notes_str.append(note.note)

    for string in range(len(self.instrument_config['OPEN_NOTES'])):
      for fret in range(self.instrument_config['FRETS']):
        # indexOf does not work for a List[Note] and Note
        index = notes_str.indexOf(self.frets[string][fret].note.note)
        if index != -1:
          self.frets[string][fret].note.select().interval(
              notes_collection.notes[index].interval_to_tonic)
          self.shown_frets.append(self.frets[string][fret])

  def reset(self):
    for fret in self.shown_frets:
      fret.note.select(False).interval(None)
    self.shown_frets = []


class QuickList:
  """Quick access list of scales, chords, etc.

  Attributes:
    visible: bool
    collections: List[List[str]]
    len: int, number of items in the list
  """
  def __init__(self) -> None:
    # TODO: Use some sort of ordered set instead.
    # TODO: Make Chord and Scale immutable, then we can simply store the
    # instances. Currently they're mutable so we have to store the strings.
    self.collections = []  # type: List[List[str]]
    self.update()

  def add(self, collection: List[str]) -> None:
    self.collections.append(collection)
    self.update()

  def remove(self, index: int) -> None:
    """Removes indexed collection."""
    self.collections.splice(index, 1)
    self.update()

  def clearAll(self) -> None:
    self.collections = []
    self.update()

  def update(self):
    """Updates derived attributes."""
    self.len = len(self.collections)
    self.visible = self.len > 0

  def displayStr(self, collection: List[str]) -> str:
    """Converts to a string for display in UI."""
    return '{0} {1} {2}'.format(collection[0], collection[1], collection[2])


class App(object):
  def __init__(self) -> None:
    self.config = app_config.AppConfig()
    self.scale = Scale(self.config)
    self.chord = Chord(self.config)
    self.fretboard = Fretboard(self.config)
    self.fretboard.showNotes(self.scale)
    self.quicklist = QuickList()

    # TODO: Refactor code. Prototype only.
    self.current_keyboard_notes = __new__(Set())
    # Because vue can only track changes to a property in an object.
    self.current_keyboard_chords = {'list': []}  # type: Dict[str, List[str]]

  def start(self) -> None:
    console.log('python start()')
    self.initVue()
    self.initKeyboard()

  def onChangeOptionSimpleChords(self):
    console.log('Simple chords: ' + self.config.simple_chords)
    self.scale.update()

  def onChangeOptionsInstrument(self):
    console.log('Selected instrument: ' + self.config.instrument)
    self.fretboard.update()
    self.fretboard.showNotes(self.scale)

  # TODO: prefer not to expose this function through 'methods'. Move this into
  # the quicklist object or something.
  def onQuicklistSelect(self, index: int) -> None:
    col = self.quicklist.collections[index]
    if col[0] == 'scale':
      self.scale.setRootAndScale(col[1], col[2])
      self.fretboard.showNotes(self.scale)
    elif col[0] == 'chord':
      self.chord.setRootAndChord(col[1], col[2])
      self.fretboard.showNotes(self.chord)


  def initKeyboard(self):
    max_num_voices = 6
    synth = __new__(Tone.PolySynth(max_num_voices, Tone.Synth));

    synth.set({
      # "oscillator" : {
      #   "type" : "amtriangle",
      #   "harmonicity" : 0.5,
      #   "modulationType" : "sine"
      # },
      "envelope" : {
        # "attackCurve" : 'exponential',
        "attack" : 0.005,
        "decay" : 0.05,
        "sustain" : 1.0,
        "release" : 1,
      },
      "portamento" : 0.05
    })

    synth.toMaster()

    keyboard = Interface.Keyboard()

    def keyDown(note):
      console.log('keyDown note ' + note)
      synth.triggerAttack(note)
      self.current_keyboard_notes.add(note)
      self.current_keyboard_chords.list = Tonal.Detect.chord(
          Array.js_from(self.current_keyboard_notes))

    def keyUp(note):
      console.log('keyUp note ' + note)
      synth.triggerRelease(note)
      self.current_keyboard_notes.delete(note)
      self.current_keyboard_chords.list = Tonal.Detect.chord(
          Array.js_from(self.current_keyboard_notes))

    keyboard.keyDown = keyDown
    keyboard.keyUp = keyUp
    window.keyboard = keyboard


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
          'config': self.config,
          'quicklist': self.quicklist,
          'current_keyboard_chords': self.current_keyboard_chords,
          'Tonal': Tonal,
          'VUE_CONSTANTS': constants.VUE_CONSTANTS,
        },
        # Watch for v-model's.
        'watch': {
          'config.simple_chords': self.onChangeOptionSimpleChords,
          'config.instrument': self.onChangeOptionsInstrument,
        },
        'methods': {
          # TODO: move these into quicklist or something
          'onQuicklistSelect': self.onQuicklistSelect,
        },
      }))

window.addEventListener('load', lambda: App().start())
