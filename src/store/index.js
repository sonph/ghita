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
};
