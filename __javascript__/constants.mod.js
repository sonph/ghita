	__nest__ (
		__all__,
		'constants', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var utils = {};
					var __name__ = 'constants';
					var Any = __init__ (__world__.typing).Any;
					__nest__ (utils, '', __init__ (__world__.utils));
					var NOTES = list (['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']);
					var NOTES_SET = new Set (NOTES);
					var SCALES = list (['ionian', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'aeolian', 'locrian', 'blues', 'major pentatonic', 'minor pentatonic', 'harmonic minor', 'melodic minor']);
					var SCALES_SET = new Set (SCALES);
					var CHORDS = list (['M', 'm', '7', 'm7', 'Maj7', 'Madd9', 'Maj9', 'o', 'o7', 'Msus2', 'Msus4']);
					var CHORDS_SET = new Set (CHORDS);
					var GUITAR = dict ({'FRETS': 23, 'OPEN_NOTES': list (['E', 'B', 'G', 'D', 'A', 'E']), 'FRET_MARKERS': new Set (list ([0, 3, 5, 7, 9, 12, 15, 17, 19]))});
					var UKULELE = dict ({'FRETS': 13, 'OPEN_NOTES': list (['A', 'E', 'C', 'G']), 'FRET_MARKERS': new Set (list ([0, 3, 5, 7, 10, 12]))});
					var INSTRUMENTS = list ([dict ({'value': 'guitar', 'text': 'Guitar (EADGBE)'}), dict ({'value': 'ukulele', 'text': 'Ukulele (GCEA)'})]);
					var VUE_CONSTANTS = dict ({'NOTES': NOTES, 'NOTES_SET': NOTES_SET, 'SCALES': SCALES, 'SCALES_SET': SCALES_SET, 'SCALE_SELECTORS': utils.transpose (list ([NOTES, SCALES, CHORDS])), 'INSTRUMENTS': INSTRUMENTS});
					__pragma__ ('<use>' +
						'typing' +
						'utils' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Any = Any;
						__all__.CHORDS = CHORDS;
						__all__.CHORDS_SET = CHORDS_SET;
						__all__.GUITAR = GUITAR;
						__all__.INSTRUMENTS = INSTRUMENTS;
						__all__.NOTES = NOTES;
						__all__.NOTES_SET = NOTES_SET;
						__all__.SCALES = SCALES;
						__all__.SCALES_SET = SCALES_SET;
						__all__.UKULELE = UKULELE;
						__all__.VUE_CONSTANTS = VUE_CONSTANTS;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
