<template>
  <div id='fretboard'>
  <h3> Fretboard </h3>
  <table v-bind:class="tableClass">
    <tbody>
      <tr>
        <td class="fretnumber"
            v-for="fret in fretboard.frets[0]">
          <span v-if="fret.marker">{{ fret.fretNumber }}</span>
        </td>
      </tr>
      <tr v-for="string in fretboard.frets">
        <td class="note"
            v-for="fret in string"
            v-bind:class="{ show: fret.note.selected, root: fret.note.interval_to_tonic == '1P', bluenote: fret.note.interval_to_tonic == '4A', fretmarker: fret.marker }">
          {{ fret.note.note }}
            <sub class="interval">{{ fret.note.intervalToTonic }}</sub>
        </td>
      </tr>
    </tbody>
  </table>
  </div>
</template>

<script>
export default {
  name: 'Fretboard',
  props: ['fretboard'],
  computed: {
    tableClass: function() {
      const keys = ['guitar', 'ukulele'];
      return keys.reduce((acc, key) => Object.assign({}, acc, {
          [key]: this.fretboard.config.instrument === key,
        }),
        {},
      );
    },
  }
};
</script>

<style scoped>

table {
  border-spacing: 0px 3px;
  table-layout: fixed;
}

table.guitar {
  width: 1600px;
}

table.ukulele {
  width: 900px;
}

td {
  border: none;
  text-align: center;
  white-space: nowrap;
}

td.fretnumber {
  border: none;
}

td.note {
  border-right: 1px solid #999;
  padding-top: 0.2em;
  padding-bottom: 0.2em;
  margin: 2px;
  color: #fff;
}

td sub.interval {
  font-size: 0.6em;
  color: #888;
}

.note.fretmarker {
  background-color: #f5f5f5;
  color: #f5f5f5;
}

/* Nut */
td.note:first-child {
  border-right: 3px solid #999;
}

/* Last fret */
td.note:last-child {
  border-right: none;
}

td.note.root.show {
  color: #6200EE;
  font-weight: bold;
}

td.note.bluenote.show {
  color: #018786;
}

td.note.show {
  color: #333;
}

</style>
