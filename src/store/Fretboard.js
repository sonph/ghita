import { Interval, Distance } from 'tonal';
import * as constants from '../constants';
import Note from './Note';
import Fret from './Fret';

/** Class represents a fretboard. */
class Fretboard {
  constructor(config) {
    this.config = config;
    this.update();
  }

  update() {
    this.shownFrets = [];
    this.frets = {};

    if (this.config.instrument === 'guitar') {
      this.instrumentConfig = constants.GUITAR;
    } else if (this.config.instrument === 'ukulele') {
      this.instrumentConfig = constants.UKULELE;
    }

    this.instrumentConfig['OPEN_NOTES'].forEach((openNote, string) => {
      this.frets[string] = {};
      for (let fret = 0; fret < this.instrumentConfig['FRETS']; fret += 1) {
        const note = Note.normalize(
          Distance.transpose(
            openNote, Interval.fromSemitones(fret),
          ),
        );

        this.frets[string][fret] = new Fret(
          new Note(note),
          this.instrumentConfig['FRET_MARKERS'].has(fret),
          fret,
        );
      }
    });
  }

  showNotes(notesCollection) {
    this.reset();

    const notesStr = notesCollection.notes.map(function(each) {
      return each.note;
    });

    for (let string = 0; string < this.instrumentConfig['OPEN_NOTES'].length; string += 1) {
      for (let fret = 0; fret < this.instrumentConfig['FRETS']; fret += 1) {
        const currentFret = this.frets[string][fret];
        const index = notesStr.indexOf(currentFret.note.note);
        if (index !== -1) {
          currentFret.note.select(true).interval(
            notesCollection.notes[index].intervalToTonic
          );
          this.shownFrets.push(currentFret);
        }
      }
    }
  }

  reset() {
    this.shownFrets.forEach(function(fret) {
      fret.note.select(false).interval(null);
    });
    this.shownFrets = [];
  }
};

export default Fretboard;
