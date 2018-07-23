import * as Tonal from 'tonal';
import NotesCollection from './NotesCollection';
import Note from './Note';
import { transpose } from '../utils';
import * as constants from '../constants';

/** Class represents a scale. **/

class Scale extends NotesCollection {
  constructor(config, root = 'C', scale ='ionian') {
    super();

    this.type = this.TYPE;
    this.config = config;
    this.root = new Note(root, '1P', true);
    this.scale = scale;
    this.update();
  }

  setRoot(note) {
    this.root = new Note(note, '1P', true);
    this.update();
    return this;
  }

  setScale(scale) {
    this.scale = scale;
    this.update();
    return this;
  }

  setRootAndScale(root, scale) {
    this.root = new Note(root, '1P', true);
    this.scale = scale;
    this.update();
  }

  contains(noteToCheck) {
    for (let i = 0; i < this.notes.length; i += 1) {
      if (this.notes[i].note === noteToCheck) {
        return this.notes[i].intervalToTonic;
      }
    }

    return null;
  }

  update() {
    this.updateNotes();

    const scaleNameStr = `${this.root.note} ${this.scale}`;
    this.chords = Tonal.Scale.chords(scaleNameStr);

    this.allChords = {};
    const modes = Tonal.Scale.modeNames(scaleNameStr);
    //TODO: For blues, we only get 2 alternate modes.
    //TODO: It's possible to use Tonal.Detect.chords, but result is pretty fuzzy
    modes.forEach((mode) => {
      const rootNote = mode[0];
      let chordsForNote = Tonal.Scale.chords(`${rootNote} ${mode[1]}`);

      if (this.config.simpleChords) {
        chordsForNote = chordsForNote.filter(function(c) {
          return constants.CHORDS_SET.has(c);
        });
      }

      this.allChords[rootNote] = chordsForNote;
    });

    const arrays = [];
    // Construct transposed array for available chords for each note in scale.
    this.allNotes.forEach((note) => {
      if (note.note in this.allChords) {
        arrays.push(this.allChords[note.note]);
      } else {
        // Empty list of chords for notes that are not in scale.
        arrays.push([]);
      }
    });

    this.allChordsTranposed = transpose(arrays);
  }

  _getNotes() {
    return Tonal.Scale.notes(`${this.root.note} ${this.scale}`);
  }
}

Scale.type = 'Scale';

export default Scale;
