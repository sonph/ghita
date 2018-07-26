export default class {
  constructor() {
    this.simpleChords = true;
    this.openOptions = false;
    this.openReadme = false;
    this.instrument = 'guitar';
  }

  toggleOptions() {
    this.openOptions = !this.openOptions;
  }

  toggleReadme() {
    this.openReadme = !this.openReadme;
  }
}
