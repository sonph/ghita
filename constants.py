import utils

NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
SCALES = ['ionian', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'aeolian',
    'locrian', 'blues', 'major pentatonic', 'minor pentatonic',
    'harmonic minor', 'melodic minor']

CHORDS = ['M', 'm', 'aug', 'dim',
          'minor7', 'maj7', 'aug7', 'dim7',
          '9', '11', '13']
FRET_MARKERS = [0, 3, 5, 7, 9, 12, 15, 17, 19]

SCALES_INTERVALS = []
for scale in SCALES:
  SCALES_INTERVALS.append(Tonal.Scale.intervals(scale).join(' '))

CHORDS_INTERVALS = []
for chord in CHORDS:
  CHORDS_INTERVALS.append(Tonal.Chord.intervals(chord).join(' '))

VUE_CONSTANTS = {
  'NOTES': NOTES,
  'SCALES': SCALES,
  'SCALE_SELECTORS': utils.transpose([NOTES, SCALES, SCALES_INTERVALS, CHORDS, CHORDS_INTERVALS]),
  'FRET_MARKERS': FRET_MARKERS,
}


