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
    # Simplify flats to sharps.
    self.notes = [Tonal.Note.enharmonic(note) if note.endsWith('b') else note for note in notes]
    window.notes = self.notes
    console.log('notes ' + self.notes)


class App(object):
  def __init__(self):
    self.scale = Scale()

  def start(self) -> None:
    console.log('python start()')
    self.initVue()

  def initVue(self) -> None:
    window.app = __new__(Vue({
      'el': '#app',
      'data': {
        'scale': self.scale
      },
    }))

window.addEventListener('load', lambda: App().start())