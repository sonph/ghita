import Fretboard from './Fretboard';
import Scale from './Scale';
import Config from './config';

export default class {
  constructor() {
    this.config = new Config();
    this.scale = new Scale(this.config);
    this.fretboard = new Fretboard(this.config);
    this.fretboard.showNotes(this.scale);
  }
};
