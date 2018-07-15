<template>
  <div id="app">
    <Fretboard v-bind:fretboard="fretboard"/>
    <Notes v-bind:scale="scale" v-bind:quicklist="quicklist"/>
    <Selector v-bind:scale="scale" v-bind:fretboard="fretboard" v-bind:chord="chord"/>
    <Chords v-bind:scale="scale" v-bind:chord="chord"/>
  </div> </template>

<script>
import Fretboard from './components/Fretboard';
  import Notes from './components/Notes';
  import Selector from './components/Selector';
  import Chords from './components/Chords';
  import Store from './store';
  const store = new Store();

  export default {
    name: 'app',
    components: {
      Fretboard,
      Notes,
      Selector,
      Chords,
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
  }
</script>

<style{{#sass}} lang="scss"{{/sass}}>

@font-face {
  font-family: 'LCD Solid';
  src: url('../../assets/fonts/LCD_Solid.ttf') format('truetype');
}

body {
  font-family: 'monospace';
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

</style>
