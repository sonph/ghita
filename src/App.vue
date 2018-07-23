<template>
  <div id="app">
    <QuickList v-bind="{ scale, quicklist, chord }" :handle-select="onQuicklistSelect"/>
    <Settings v-bind="{ config }" />
    <Fretboard v-bind="{ fretboard }"/>
    <Notes v-bind="{ chord, scale, quicklist }" />
    <Selector v-bind="{ scale, fretboard, chord }" />
    <Chords v-bind="{ scale, chord } "/>
  </div> </template>

<script>
import Fretboard from './components/Fretboard';
  import Notes from './components/Notes';
  import Selector from './components/Selector';
  import Chords from './components/Chords';
  import QuickList from './components/QuickList';
  import Settings from './components/Settings';
  import Store from './store';
  const store = new Store();

  export default {
    name: 'app',
    components: {
      Fretboard,
      Notes,
      Selector,
      Chords,
      QuickList,
      Settings,
    },
    data: function() {
      return {
        fretboard: store.fretboard,
        scale: store.scale,
        config: store.config,
        quicklist: store.quicklist,
        chord: store.chord,
      }
    },
    watch: {
      'config.simpleChords': function() {
        console.log(`Simple chords: ${this.config.instrument}`);
        this.scale.update();
      },
      'config.instrument': function() {
        console.log(`Selected instrument: ${this.config.instrument}`);
        this.fretboard.update();
        this.fretboard.showNotes(this.scale);
      },
    },
    methods: {
      onQuicklistSelect: store.onQuicklistSelect,
    },
  }
</script>

<style lang="css">
@font-face {
  font-family: 'LCD Solid';
  src: url('./assets/fonts/LCD_Solid.ttf') format('truetype');
}

body {
  font-family: monospace;
  font-size: 15px;
  padding: 2em;
}

/* Basically means the element can be `selected` (enabled/highlighted) or
not. */
.selectable {
  color: #ddd;
}
.selectable.selected, .clickable.selected:hover {
  color: #6200EE;
}

/* Rename to something else. We have highlight 1 for scale, and 2 for chord */
.selectable.alternate.selected, .clickable.alternate.selected:hover {
  color: #03DAC6;
}

/* Elements that have hover/click bindings. */
.clickable:hover {
  color: #999;
  cursor: pointer;
  text-decoration: underline;
}

.right {
  text-align: right;
}

span.spacing:before {
  content: "\00a0 \00a0 ";
}

</style>
