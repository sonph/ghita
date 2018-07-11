import utils

NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
NOTES_SET = __new__(Set(NOTES))

SCALES = ['ionian', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'aeolian',
    'locrian', 'blues', 'major pentatonic', 'minor pentatonic',
    'harmonic minor', 'melodic minor']
SCALES_SET = __new__(Set(SCALES))

# TODO(#24): This is also used to check for "simple chords", so the names have
# to be exactly as appear in names(aliases=False), since Scale.chords returns
# canonical chord names. We need some way to check for aliases.
CHORDS = [
    'M',  # major
    'm',  # minor
    '7',  # 7
    'm7',  # minor7
    'Maj7',  # maj7
    'Madd9', # major add9
    'Maj9', # major9
    'o',  # dim
    'o7',  # dim7
    # 'aug', 
    'Msus2',  # sus2
    'Msus4',  # sus4
]
CHORDS_SET = __new__(Set(CHORDS))

FRET_MARKERS = [0, 3, 5, 7, 9, 12, 15, 17, 19]
FRET_MARKERS_SET = __new__(Set(FRET_MARKERS))

VUE_CONSTANTS = {
  'NOTES': NOTES,
  'NOTES_SET': NOTES_SET,
  'SCALES': SCALES,
  'SCALES_SET': SCALES_SET,
  'FRET_MARKERS': FRET_MARKERS,
  'FRET_MARKERS_SET': FRET_MARKERS_SET,
  'SCALE_SELECTORS': utils.transpose([NOTES, SCALES, CHORDS]),
}


