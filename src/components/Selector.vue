<template>
  <div>
    <h3>Selector</h3>
    <table>
      <tbody>
        <tr>
          <td colspan="3">Scale</td>
          <td colspan="3">Chord</td>
        </tr>
        <tr v-for="row in VUE_CONSTANTS.SCALE_SELECTORS">
          <td class="selectable clickable"
              v-if="row[0]"
              v-bind:class="{ selected: scale.root.note == row[0] }"
              v-on:click="scale.setRoot(row[0]); fretboard.showNotes(scale)">{{ row[0] }}
          </td>
          <td v-else />

            <td class="selectable clickable"
                v-if="row[1]"
                v-bind:class="{ selected: scale.scale == row[1] }"
                v-on:click="scale.setScale(row[1]); fretboard.showNotes(scale)">{{ row[1] }}
            </td>
            <td v-else />

              <td class="selectable clickable"
                  v-if="row[1]"
                  v-bind:class="{ selected: scale.scale == row[1] }"
                  v-on:click="scale.setScale(row[1]); fretboard.showNotes(scale)">{{ Tonal.Scale.intervals(row[1]).join(' ') }}
              </td>
              <td class="selectable clickable alternate"
                  v-if="row[0]"
                  v-bind:class="{ selected: chord.root.note == row[0] }"
                  v-on:click="chord.setRoot(row[0]); fretboard.showNotes(chord)">{{ row[0] }}
              </td>
              <td v-else />

                <td class="selectable clickable alternate"
                    v-if="row[2]"
                    v-bind:class="{ selected: chord.chord == row[2] }"
                    v-on:click="chord.setChord(row[2]); fretboard.showNotes(chord)">{{ row[2] }}
                </td>
                <td v-else />

                  <td class="selectable clickable alternate"
                      v-if="row[2]"
                      v-bind:class="{ selected: chord.chord == row[2] }"
                      v-on:click="chord.setChord(row[2]); fretboard.showNotes(chord)">{{ Tonal.Chord.intervals(row[2]).join(' ') }}
                  </td>
                  <td v-else />

        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { VUE_CONSTANTS } from '../constants';
import * as Tonal from 'tonal';
export default {
  name: 'Selector',
  props: ['scale', 'fretboard', 'chord'],
  data() {
    return {
      VUE_CONSTANTS,
      Tonal,
    };
  },
};
</script>

<style scoped>

td {
  padding-left: 1em;
  padding-right: 1em;
  white-space: nowrap;
  text-align: left;
}

</style>
