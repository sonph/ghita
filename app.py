import note

class App:
  def __init__(self):
    pass

  def start(self) -> None:
    console.log('python start()')
    self.initVue()

  def getMajorScale(self, note):
    return note.scale('ionian').simple()

  def notesToStr(self, notes):
    return ' '.join(notes)

  def initVue(self) -> None:
    message = ''
    for n in note.ALL_NOTES:
      message += self.notesToStr(self.getMajorScale(n)) + '\n'
    app = __new__(Vue({'el': '#app', 'data': {'message': message}}))

window.addEventListener('load', lambda: App().start())