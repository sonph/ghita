<template>
  <div>
    <h3> Notes </h3>
    <div>Scale
      <span class="spacing" />
        <span class="selectable clickable"
              v-on:click="quicklist.add(['scale', scale.root.note, scale.scale])"
              title="Add scale to quick access list">save
        </span>
        <table>
          <tbody>
            <tr>
              <td class="selectable"
                  v-for="note in scale.allNotes"
                  v-bind:class="{ selected: note.selected }">{{ note.note }}
              </td>
            </tr>
            <tr>
              <td class="selectable"
                  v-for="note in scale.allNotes"
                  v-bind:class="{ selected: note.selected }">{{ note.intervalToTonic}}
              </td>
            </tr>
          </tbody>
        </table>
    </div>
    <br>

    <div>Chord
      <span class="spacing" />

        <span class="selectable clickable"
              v-on:click="quicklist.add(['chord', chord.root.note, chord.chord])"
              title="Add chord to quick access list">save
        </span>
        <table>
          <tbody>
            <tr>
              <td class="selectable alternate"
                  v-for="note in chord.allNotes"
                  v-bind:class="{ selected: note.selected }">{{ note.note }}
              </td>
            </tr>
            <tr>
              <td class="selectable alternate"
                  v-for="note in chord.allNotes"
                  v-bind:class="{ selected: note.selected }">{{ note.intervalToTonic}}
              </td>
            </tr>
          </tbody>
        </table>
    </div>
  </div>
</template>

<script>
export default {
  props: ['scale', 'quicklist', 'chord'],
  name: 'Notes',
  data() {
    return {
      title: 'Notes',
    };
  },
};
</script>

<style scoped>
td {
  padding-right: 1em;
  text-align: center;
}
</style>
