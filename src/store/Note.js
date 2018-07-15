import * as Tonal from 'tonal';
/** Class represents a note. **/

class Note {
  constructor(note, intervalToTonic, selected) {
    this.note = Note.normalize(note);
    this.intervalToTonic = intervalToTonic;
    this.selected = selected;
    this.update();
  }

  select(select) {
    this.selected = select;
    return this;
  }

  interval(interval) {
    this.intervalToTonic = interval;
    return this;
  }

  /**
   * Simplifies and normalizes flats to sharps.
   * @param {string} note
   *
   * @return {string} simplified note
   */
  static normalize(note) {
    note = Tonal.Note.simplify(note);
    if (note.endsWith('b')) {
      return Tonal.Note.enharmonic(note);
    }
    return note;
  }

  /**
   * Sets interval relative to tonic
   * @param {string} interval
   *
   * @return {void}
   */
  inverval(interval) {
    this.intervalToTonic = interval;
    return this;
  }

  update() {
  }
}

export default Note;
