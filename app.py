def join(sep, items):
  s = ''
  for item in items:
    s += sep + str(item)
  return s


class Scale(object):
  def __init__(self):
    self.selectedRoot = 'C'
    self.selectedType = 'ionian'
    self.notes = self.getNotesStr(self.selectedRoot, self.selectedType)

  def selectRoot(self, rootNote: str):
    console.log('selected root ' + rootNote)
    self.selectedRoot = rootNote
    self.notes = self.getNotesStr(self.selectedRoot, self.selectedType)

  def selectType(self, scaleType: str):
    console.log('selected scale type ' + scaleType)
    self.selectedType = scaleType
    self.notes = self.getNotesStr(self.selectedRoot, self.selectedType)

  @staticmethod
  def getNotesStr(root, scaleType) -> str:
    root = teoria.note(root)
    notes = root.scale(scaleType).simple()
    return join(' ', notes)

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