	(function () {
		var app_config = {};
		var constants = {};
		var utils = {};
		var __name__ = '__main__';
		var Any = __init__ (__world__.typing).Any;
		var Dict = __init__ (__world__.typing).Dict;
		var List = __init__ (__world__.typing).List;
		var Optional = __init__ (__world__.typing).Optional;
		var Callable = __init__ (__world__.typing).Callable;
		__nest__ (app_config, '', __init__ (__world__.app_config));
		__nest__ (constants, '', __init__ (__world__.constants));
		__nest__ (utils, '', __init__ (__world__.utils));
		var Note = __class__ ('Note', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self, note, interval_to_tonic, selected) {
				if (typeof interval_to_tonic == 'undefined' || (interval_to_tonic != null && interval_to_tonic .hasOwnProperty ("__kwargtrans__"))) {;
					var interval_to_tonic = null;
				};
				if (typeof selected == 'undefined' || (selected != null && selected .hasOwnProperty ("__kwargtrans__"))) {;
					var selected = false;
				};
				self.note = self.normalize (note);
				self.interval_to_tonic = interval_to_tonic;
				self.selected = selected;
				self.py_update ();
			});},
			get select () {return __get__ (this, function (self, select) {
				if (typeof select == 'undefined' || (select != null && select .hasOwnProperty ("__kwargtrans__"))) {;
					var select = true;
				};
				self.selected = select;
				return self;
			});},
			get interval () {return __get__ (this, function (self, interval) {
				if (typeof interval == 'undefined' || (interval != null && interval .hasOwnProperty ("__kwargtrans__"))) {;
					var interval = null;
				};
				self.interval_to_tonic = interval;
				return self;
			});},
			get py_update () {return __get__ (this, function (self) {
				// pass;
			});},
			get normalize () {return __getcm__ (this, function (self, note) {
				var note = Tonal.Note.simplify (note);
				if (note.endswith ('b')) {
					var note = Tonal.Note.enharmonic (note);
				}
				return note;
			});}
		});
		var NotesCollection = __class__ ('NotesCollection', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self) {
				// pass;
			});},
			get _getNotes () {return __get__ (this, function (self) {
				var __except0__ = NotImplementedError ();
				__except0__.__cause__ = null;
				throw __except0__;
			});},
			get updateNotes () {return __get__ (this, function (self) {
				var tonal_notes_str = self._getNotes ();
				var notes_str = list ([]);
				var __iterable0__ = tonal_notes_str;
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var note_str = __iterable0__ [__index0__];
					notes_str.append (Note.normalize (note_str));
				}
				self.notes = list ([]);
				self.all_notes_sorted = list ([]);
				var __iterable0__ = enumerate (constants.NOTES);
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var __left0__ = __iterable0__ [__index0__];
					var index = __left0__ [0];
					var note_str = __left0__ [1];
					var selected = notes_str.includes (note_str);
					var interval = Tonal.Distance.interval (self.root.note, note_str);
					if (selected) {
						self.notes.append (Note (note_str, interval, selected));
					}
					self.all_notes_sorted.append (Note (note_str, interval, selected));
					if (note_str == self.root.note) {
						var root_index = index;
					}
				}
				self.all_notes = utils.rotate (self.all_notes_sorted, root_index);
			});}
		});
		var Chord = __class__ ('Chord', [NotesCollection], {
			__module__: __name__,
			TYPE: 'chord',
			get __init__ () {return __get__ (this, function (self, config, root, chord) {
				if (typeof root == 'undefined' || (root != null && root .hasOwnProperty ("__kwargtrans__"))) {;
					var root = Note ('C', '1P', true);
				};
				if (typeof chord == 'undefined' || (chord != null && chord .hasOwnProperty ("__kwargtrans__"))) {;
					var chord = 'M';
				};
				self.py_metatype = self.TYPE;
				self.config = config;
				self.root = root;
				self.chord = chord;
				self.py_update ();
			});},
			get setRoot () {return __get__ (this, function (self, root) {
				self.root = Note (root, '1P', true);
				self.py_update ();
				return self;
			});},
			get setChord () {return __get__ (this, function (self, chord) {
				self.chord = chord;
				self.py_update ();
				return self;
			});},
			get setRootAndChord () {return __get__ (this, function (self, root, chord) {
				self.root = Note (root, '1P', true);
				self.chord = chord;
				self.py_update ();
			});},
			get _getNotes () {return __get__ (this, function (self) {
				return Tonal.Chord.notes ('{0} {1}'.format (self.root.note, self.chord));
			});},
			get contains () {return __get__ (this, function (self, note_to_check) {
				var __iterable0__ = self.notes;
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var note = __iterable0__ [__index0__];
					if (note_to_check == note.note) {
						return note.interval_to_tonic;
					}
				}
				return null;
			});},
			get py_update () {return __get__ (this, function (self) {
				console.log ((('updating chord ' + self.root.note) + ' ') + self.chord);
				self.updateNotes ();
			});}
		});
		var Scale = __class__ ('Scale', [NotesCollection], {
			__module__: __name__,
			TYPE: 'scale',
			get __init__ () {return __get__ (this, function (self, config, root, scale) {
				if (typeof root == 'undefined' || (root != null && root .hasOwnProperty ("__kwargtrans__"))) {;
					var root = 'C';
				};
				if (typeof scale == 'undefined' || (scale != null && scale .hasOwnProperty ("__kwargtrans__"))) {;
					var scale = 'ionian';
				};
				self.py_metatype = self.TYPE;
				self.config = config;
				self.root = Note (root, '1P', true);
				self.scale = scale;
				self.py_update ();
			});},
			get setRoot () {return __get__ (this, function (self, note) {
				self.root = Note (note, '1P', true);
				self.py_update ();
				return self;
			});},
			get setScale () {return __get__ (this, function (self, scale) {
				self.scale = scale;
				self.py_update ();
				return self;
			});},
			get setRootAndScale () {return __get__ (this, function (self, root, scale) {
				self.root = Note (root, '1P', true);
				self.scale = scale;
				self.py_update ();
			});},
			get contains () {return __get__ (this, function (self, note_to_check) {
				var __iterable0__ = self.notes;
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var note = __iterable0__ [__index0__];
					if (note_to_check == note.note) {
						return note.interval_to_tonic;
					}
				}
				return null;
			});},
			get _getNotes () {return __get__ (this, function (self) {
				return Tonal.Scale.notes ('{0} {1}'.format (self.root.note, self.scale));
			});},
			get py_update () {return __get__ (this, function (self) {
				console.log ((('updating scale ' + self.root.note) + ' ') + self.scale);
				self.updateNotes ();
				var scaleNameStr = '{0} {1}'.format (self.root.note, self.scale);
				self.chords = Tonal.Scale.chords (scaleNameStr);
				self.all_chords = dict ({});
				var modes = Tonal.Scale.modeNames (scaleNameStr);
				var __iterable0__ = modes;
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var mode = __iterable0__ [__index0__];
					var rootNote = mode [0];
					var chordsForNote = Tonal.Scale.chords ('{0} {1}'.format (rootNote, mode [1]));
					if (self.config.simple_chords) {
						var chordsForNote = chordsForNote.filter ((function __lambda__ (c) {
							return constants.CHORDS_SET.has (c);
						}));
					}
					self.all_chords [rootNote] = chordsForNote;
				}
				var arrays = list ([]);
				var __iterable0__ = self.all_notes;
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var note = __iterable0__ [__index0__];
					if (__in__ (note.note, self.all_chords)) {
						arrays.append (self.all_chords [note.note]);
					}
					else {
						arrays.append (list ([]));
					}
				}
				self.all_chords_transposed = utils.transpose (arrays);
			});}
		});
		var Fret = __class__ ('Fret', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self, note, marker, fret_number) {
				self.note = note;
				self.marker = marker;
				self.fret_number = fret_number;
			});}
		});
		var Fretboard = __class__ ('Fretboard', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self, config) {
				self.config = config;
				self.py_update ();
			});},
			get py_update () {return __get__ (this, function (self) {
				self.shown_frets = list ([]);
				self.frets = dict ({});
				if (self.config.instrument == 'guitar') {
					self.instrument_config = constants.GUITAR;
				}
				else if (self.config.instrument == 'ukulele') {
					self.instrument_config = constants.UKULELE;
				}
				var __iterable0__ = enumerate (self.instrument_config ['OPEN_NOTES']);
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var __left0__ = __iterable0__ [__index0__];
					var string = __left0__ [0];
					var open_note = __left0__ [1];
					self.frets [string] = dict ({});
					for (var fret = 0; fret < self.instrument_config ['FRETS']; fret++) {
						var note = Note.normalize (Tonal.Distance.transpose (open_note, Tonal.Interval.fromSemitones (fret)));
						self.frets [string] [fret] = Fret (Note (note), self.instrument_config ['FRET_MARKERS'].has (fret), fret);
					}
				}
			});},
			get showNotes () {return __get__ (this, function (self, notes_collection) {
				self.reset ();
				var notes_str = list ([]);
				var __iterable0__ = notes_collection.notes;
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var note = __iterable0__ [__index0__];
					notes_str.append (note.note);
				}
				for (var string = 0; string < len (self.instrument_config ['OPEN_NOTES']); string++) {
					for (var fret = 0; fret < self.instrument_config ['FRETS']; fret++) {
						var index = notes_str.indexOf (self.frets [string] [fret].note.note);
						if (index != -(1)) {
							self.frets [string] [fret].note.select ().interval (notes_collection.notes [index].interval_to_tonic);
							self.shown_frets.append (self.frets [string] [fret]);
						}
					}
				}
			});},
			get reset () {return __get__ (this, function (self) {
				var __iterable0__ = self.shown_frets;
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var fret = __iterable0__ [__index0__];
					fret.note.select (false).interval (null);
				}
				self.shown_frets = list ([]);
			});}
		});
		var QuickList = __class__ ('QuickList', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self) {
				self.collections = list ([]);
				self.py_update ();
			});},
			get add () {return __get__ (this, function (self, collection) {
				self.collections.append (collection);
				self.py_update ();
			});},
			get remove () {return __get__ (this, function (self, index) {
				self.collections.splice (index, 1);
				self.py_update ();
			});},
			get clearAll () {return __get__ (this, function (self) {
				self.collections = list ([]);
				self.py_update ();
			});},
			get py_update () {return __get__ (this, function (self) {
				self.len = len (self.collections);
				self.visible = self.len > 0;
			});},
			get displayStr () {return __get__ (this, function (self, collection) {
				return '{0} {1} {2}'.format (collection [0], collection [1], collection [2]);
			});}
		});
		var App = __class__ ('App', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self) {
				self.config = app_config.AppConfig ();
				self.scale = Scale (self.config);
				self.chord = Chord (self.config);
				self.fretboard = Fretboard (self.config);
				self.fretboard.showNotes (self.scale);
				self.quicklist = QuickList ();
			});},
			get start () {return __get__ (this, function (self) {
				console.log ('python start()');
				self.initVue ();
			});},
			get onChangeOptionSimpleChords () {return __get__ (this, function (self) {
				console.log ('Simple chords: ' + self.config.simple_chords);
				self.scale.py_update ();
			});},
			get onChangeOptionsInstrument () {return __get__ (this, function (self) {
				console.log ('Selected instrument: ' + self.config.instrument);
				self.fretboard.py_update ();
				self.fretboard.showNotes (self.scale);
			});},
			get onQuicklistSelect () {return __get__ (this, function (self, index) {
				var col = self.quicklist.collections [index];
				if (col [0] == 'scale') {
					self.scale.setRootAndScale (col [1], col [2]);
					self.fretboard.showNotes (self.scale);
				}
				else if (col [0] == 'chord') {
					self.chord.setRootAndChord (col [1], col [2]);
					self.fretboard.showNotes (self.chord);
				}
			});},
			get initVue () {return __get__ (this, function (self) {
				if (!(window.vue_loaded)) {
					window.vue_loaded = true;
					window.app = new Vue (dict ({'el': '#app', 'data': dict ({'scale': self.scale, 'chord': self.chord, 'fretboard': self.fretboard, 'config': self.config, 'quicklist': self.quicklist, 'Tonal': Tonal, 'VUE_CONSTANTS': constants.VUE_CONSTANTS}), 'watch': dict ({'config.simple_chords': self.onChangeOptionSimpleChords, 'config.instrument': self.onChangeOptionsInstrument}), 'methods': dict ({'onQuicklistSelect': self.onQuicklistSelect})}));
				}
			});}
		});
		window.addEventListener ('load', (function __lambda__ () {
			return App ().start ();
		}));
		__pragma__ ('<use>' +
			'app_config' +
			'constants' +
			'typing' +
			'utils' +
		'</use>')
		__pragma__ ('<all>')
			__all__.Any = Any;
			__all__.App = App;
			__all__.Callable = Callable;
			__all__.Chord = Chord;
			__all__.Dict = Dict;
			__all__.Fret = Fret;
			__all__.Fretboard = Fretboard;
			__all__.List = List;
			__all__.Note = Note;
			__all__.NotesCollection = NotesCollection;
			__all__.Optional = Optional;
			__all__.QuickList = QuickList;
			__all__.Scale = Scale;
			__all__.__name__ = __name__;
		__pragma__ ('</all>')
	}) ();
