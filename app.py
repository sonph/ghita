def normalizeNote(note):
  note = Tonal.Note.simplify(note)
  if note.endswith('b'):
    return Tonal.Note.enharmonic(note)
  return note


class Scale(object):
  def __init__(self):
    self.selectedRoot = 'A'
    self.selectedType = 'lydian'
    self.notes = []
    self.update()

  def selectRoot(self, rootNote: str):
    console.log('selected root ' + rootNote)
    self.selectedRoot = rootNote
    self.update()

  def selectType(self, scaleType: str):
    console.log('selected scale type ' + scaleType)
    self.selectedType = scaleType
    self.update()

  def update(self):
    console.log('update')
    notes = Tonal.Scale.notes(self.selectedRoot + ' ' + self.selectedType)
    self.notes = []
    # Convert flats to sharps and simplify.
    for note in notes:
      note = Tonal.Note.simplify(note)
      self.notes.append(
        Tonal.Note.enharmonic(note) if note.endsWith('b') else note)


class Fret(object):
  def __init__(self, displayStr, note):
    self.displayStr = displayStr
    self.note = note
    self.show = False
    self.isRoot = False

class Fretboard(object):
  def __init__(self):
    self.fb = {}
    openNotes = ['E', 'B', 'G', 'D', 'A', 'E']
    for string in range(6):
      openNote = openNotes[string]
      self.fb[string] = {}
      for fret in range(22):
        note = normalizeNote(Tonal.Distance.transpose(
            openNote, Tonal.Interval.fromSemitones(fret)))
        self.fb[string][fret] = Fret(sprintf('  %-2s  ', note), note)
    console.log(self.fb)
    window.fb = self.fb

  def showScale(self, scale: Scale):
    notes = scale.notes
    for string in range(6):
      for fret in range(22):
        index = notes.indexOf(self.fb[string][fret].note)
        self.fb[string][fret].show = (index != -1)
        self.fb[string][fret].isRoot = (index == 0)

class App(object):
  def __init__(self):
    self.scale = Scale()
    self.fretboard = Fretboard()

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