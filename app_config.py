class AppConfig:
  def __init__(self):
    # If true, show simple constants.CHORDS only.
    # Otherwise show all available chords in Tonal.
    self.simple_chords = True  # type: bool

    # If true, settings panel is visible
    self.open_settings = False  # type: bool

    # Selected instrument. 'guitar' or 'ukulele'
    self.instrument = 'guitar'  # type: str

  def toggleSettings(self):
    self.open_settings = not self.open_settings
