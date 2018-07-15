<template>
  <div id="app">
		<Fretboard />
		<Notes />
		<Selector />
		<Chords />
  </div>
</template>

<script>
import Fretboard from './components/Fretboard';
import Notes from './components/Notes';
import Selector from './components/Selector';
import Chords from './components/Chords';

export default {
  name: 'app',
	components: {
		Fretboard,
		Notes,
		Selector,
		Chords,
	},
};
</script>

<style{{#sass}} lang="scss"{{/sass}}>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
