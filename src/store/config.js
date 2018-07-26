export default class {
  constructor() {
    this.simpleChords = true;
    this.openSettings = false;
    this.openReadme = false;
    this.instrument = 'guitar';
  }

  toggleSettings() {
    this.openSettings = !this.openSettings;
  }

  toggleReadme() {
    this.openReadme = !this.openReadme;
  }
}
