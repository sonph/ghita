import note


def join(sep, items):
  s = ''
  for item in items:
    s += sep + str(item)
  return s


class SelectedRoot(object):
  def __init__(self):
    self.selectedRoot = 'A'
    self.scale = self.getMajorScaleStr(self.selectedRoot)

  def selectRoot(self, rootNote: str):
    console.log('selected ' + rootNote)
    self.selectedRoot = rootNote
    self.scale = self.getMajorScaleStr(self.selectedRoot)

  @staticmethod
  def getMajorScaleStr(note) -> str:
    root = teoria.note(note)
    notes = root.scale('ionian').simple()
    return join(' ', notes)

class App(object):
  def __init__(self):
    self.selectedRoot = SelectedRoot()

  def start(self) -> None:
    console.log('python start()')
    self.initVue()

  def initVue(self) -> None:
    window.app = __new__(Vue({
      'el': '#app',
      'data': {
        'selectedRoot': self.selectedRoot
      },
    }))

window.addEventListener('load', lambda: App().start())