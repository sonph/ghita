class AppConfig:
  def __init__(self):
    # If true, show simple constants.CHORDS only.
    # Otherwise show all available chords in Tonal.
    self.simple_chords = True

    # If true, settings panel is visible
    self.open_settings = False

  def toggleSettings(self):
    self.open_settings = not self.open_settings
