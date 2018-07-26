import * as Tonal from 'tonal';

/** Class represents a note. **/
class Note {
  constructor(note, intervalToTonic, selected) {
    this.note = Note.normalize(note);
    this.intervalToTonic = intervalToTonic;
    this.selected = selected;
    this.update();
  }

  /**
   * Marks or unmarks this note as selected.
   * @param {boolean} select
   *
   * @return {Note}
   */
  select(select) {
    this.selected = select;
    return this;
  }

  /**
   * Sets interval relative to tonic.
   * @param {string} interval
   *
   * @return {Note}
   */
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

  /**
   * Updates all derived attributes, such as those used in Vue.
   */
  update() {
    // TODO: Implement
  }
}

export default Note;
