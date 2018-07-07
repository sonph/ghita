import note


class SelectedRoot(object):
  def __init__(self):
    self.isCSelected = True
    self.isDSelected = False

  def selectNote(self, note):
    console.log('selected ' + note)
    if note == 'C':
      self.isCSelected = True
      self.isDSelected = False
    elif note == 'D':
      self.isCSelected = False
      self.isDSelected = True


class App(object):
  def __init__(self):
    self.selectedRoot = SelectedRoot()

  def getMajorScale(self, note):
    return note.scale('ionian').simple()

  def notesToStr(self, notes):
    return ' '.join(notes)

  def getMessage(self):
    message = ''
    for n in note.ALL_NOTES:
      message += self.notesToStr(self.getMajorScale(n)) + '\n'
    return message

  def start(self) -> None:
    console.log('python start()')
    self.initVue()

  def initVue(self) -> None:
    window.app = __new__(Vue({
      'el': '#app',
      'data': {
        'message': self.getMessage(),
        'selectedRoot': self.selectedRoot
      },
      'methods': {
        'selectNote': self.selectedRoot.selectNote,
      },
    }))

window.addEventListener('load', lambda: App().start())