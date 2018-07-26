import * as Tonal from 'tonal';
import * as constants from '../constants';
import Note from './Note';
import { rotate } from '../utils';

/** Class represents a collection of notes. **/

class NotesCollection {
  _getNotes() {
    throw new Error('Not impleted');
  }

  updateNotes() {
    const tonalNotesStr = this._getNotes();
    const notesStr = tonalNotesStr.map(function(each) {
      return Note.normalize(each);
    });

    let rootIndex = -1;

    this.notes = [];
    this.allNotesSorted = [];

    constants.NOTES.forEach((noteStr, index) => {
      const selected = notesStr.includes(noteStr);
      const interval = Tonal.Distance.interval(this.root.note, noteStr);

      if (selected) {
        this.notes.push(new Note(noteStr, interval, selected));
      }

      this.allNotesSorted.push(new Note(noteStr, interval, selected));

      if (noteStr === this.root.note) {
        rootIndex = index;
      }
    });

    this.allNotes = rotate(this.allNotesSorted, rootIndex);
  }
}

export default NotesCollection;
