class App:
  def __init__(self):
    pass

  def start(self) -> None:
    console.log('python start()')
    self.initVue()

  def getMessage(self) -> str:
    return '{0}'.format('Hello world!')

  def initVue(self) -> None:
    app = __new__(Vue({'el': '#app', 'data': {'message': self.getMessage()}}))

window.addEventListener('load', lambda: App().start())