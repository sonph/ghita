class App:
  def __init__(self):
    pass

  def start(self):
    console.log('python start()')
    self.initVue()

  def initVue(self):
    app = __new__(Vue({'el': '#app', 'data': {'message': 'Hello world!'}}))

window.addEventListener('load', lambda: App().start())