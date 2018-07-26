import * as TonalChord from 'tonal-chord';
import NotesCollection from './NotesCollection';
import Note from './Note';
import Config from './config';

class Chord extends NotesCollection {
  constructor(
    config,
    root = new Note('C', '1P', true),
    chord = 'M',
  ) {
    super();

    this.type = Chord.type;
    this.config = config;
    this.root = root;
    this.chord = chord;
    this.update();
  }

  setRoot(root) {
    this.root = new Note(root, '1P', true);
    this.update();
    return this;
  }

  setChord(chord) {
    this.chord = chord;
    this.update();
    return this;
  }

  setRootAndChord(root, chord) {
    this.root = new Note(root, '1P', true);
    this.chord = chord;
    this.update();
  }

  _getNotes() {
    return TonalChord.notes(`${this.root.note} ${this.chord}`);
  }

  contains(noteToCheck) {
    this.notes.forEach(function(note) {
      if (noteToCheck === note.note) {
        return note.intervalToTonic;
      };
    });

    return null;
  }

  update() {
    this.updateNotes();
  }
}

Chord.type = 'CHORD';

export default Chord;
