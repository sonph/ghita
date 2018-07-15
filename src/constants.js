import { transpose } from './utils';

export const NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'];

export const SCALES = ['ionian', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'aeolian',
    'locrian', 'blues', 'major pentatonic', 'minor pentatonic',
  'harmonic minor', 'melodic minor'];

export const SCALES_SET = new Set(SCALES);

//TODO(#24): This is also used to check for "simple chords", so the names have
//to be exactly as appear in names(aliases=False), since Scale.chords returns
//canonical chord names. We need some way to check for aliases.
export const CHORDS = [
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
];

export const CHORDS_SET = new Set(CHORDS);

export const GUITAR = {
  'FRETS': 23,  // +1 for open fret
  'OPEN_NOTES': ['E', 'B', 'G', 'D', 'A', 'E'],
  'FRET_MARKERS': new Set([0, 3, 5, 7, 9, 12, 15, 17, 19]),
};

export const UKULELE = {
  'FRETS': 13,  // +1 for open fret
  'OPEN_NOTES': ['A', 'E', 'C', 'G'],
  'FRET_MARKERS': __new__(Set([0, 3, 5, 7, 10, 12]))
};

export const INSTRUMENTS = [
  {'value': 'guitar',
  'text': 'Guitar (EADGBE)'},
  {'value': 'ukulele',
  'text': 'Ukulele (GCEA)'},
];

export const VUE_CONSTANTS = {
  'NOTES': NOTES,
  'NOTES_SET': NOTES_SET,
  'SCALES': SCALES,
  'SCALES_SET': SCALES_SET,
  'SCALE_SELECTORS': transpose([NOTES, SCALES, CHORDS]),
  'INSTRUMENTS': INSTRUMENTS,
};


