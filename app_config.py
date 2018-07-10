class AppConfig:
  def __init__(self):
    # If true, show all available chords. Otherwise show CHORDS only.
    self.all_chords = False

    # If true, settings panel is visible
    self.open_settings = False

  def toggleSettings(self):
    self.open_settings = not self.open_settings

  def test(self):
    console.log(self.all_chords)