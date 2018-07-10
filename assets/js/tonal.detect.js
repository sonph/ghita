/* Manually created from https://github.com/danigb/tonal/blob/a105f292f423505e1731fb1c415b87f4a7ea889e/extensions/detect/index.js
since tonal-detect is 404 on npmjs.

TODO: browserify or something
*/

Tonal.Detect = {}

function detector(dictionary, defaultBuilder) {
  defaultBuilder = defaultBuilder || ((tonic, names) => [tonic, names]);
  return function(notes, builder) {
    builder = builder || defaultBuilder;
    notes = Tonal.Array.sort(notes.map(Tonal.Note.pc));
    return Tonal.PcSet.modes(notes)
      .map((mode, i) => {
        const tonic = Tonal.Note.name(notes[i]);
        const names = dictionary.names(mode);
        return names.length ? builder(tonic, names) : null;
      })
      .filter(x => x);
  };
}
Tonal.Detect.chord = detector(
  Tonal.Dictionary.chord,
  (tonic, names) => tonic + names[0]
);

Tonal.Detect.scale = detector(
  Tonal.Dictionary.scale,
  (tonic, names) => tonic + " " + names[0]
);

Tonal.Detect.pcset = detector(Tonal.Dictionary.pcset);
