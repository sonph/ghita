import Fretboard from './Fretboard';
import Scale from './Scale';
import Chord from './Chord';
import Config from './config';
import QuickList from './QuickList';

export default class {
  constructor() {
    this.config = new Config();
    this.scale = new Scale(this.config);
    this.chord = new Chord(this.config);
    this.fretboard = new Fretboard(this.config);
    this.fretboard.showNotes(this.scale);
    this.quicklist = new QuickList();
  }

  onQuicklistSelect(index) {
    const col = this.quicklist.collections[index];
    if (col[0] === 'scale') {
      this.scale.setRootAndScale(col[1], col[2]);
      this.fretboard.showNotes(this.scale);
    } else if (col[0] === 'chord') {
      this.chord.setRootAndChord(col[1], col[2]);
      this.fretboard.showNotes(this.chord);
    }
  }
};
