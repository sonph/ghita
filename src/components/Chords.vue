<template>
  <div>
    <h3>Chords in scale</h3>
    <div>
      <table>
        <tbody>
          <tr>
            <td class="selectable"
                v-for="note in scale.allNotes"
                v-bind:class="{ selected: note.selected }">{{ note.note }}
            </td>
          </tr>
          <tr v-for="chordNames in scale.allChordsTranposed">
            <td class="selectable clickable alternate"
                v-for="(chordName, index) in chordNames"
                v-bind:class="{ selected: chord.root.note == scale.allNotes[index].note && chord.chord == chordName }"
                v-on:click="chord
                .setRoot(scale.allNotes[index].note)
                .setChord(chordName)">{{ chordName }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import * as Tonal from 'tonal';

export default {
  name: 'Chords',
  props: ['scale', 'chord'],
  data: function() {
    return {
      Tonal,
    };
  },
};
</script>

<style lang="scss" scope>
td {
  padding-right: 1em;
  text-align: center;
}
</style>
