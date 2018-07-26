<template>
  <div>
    <span class="selectable clickable" v-on:click='config.toggleSettings()'>Settings</span>
    <span class="spacing"></span>
    <span class="selectable clickable" v-on:click="config.toggleReadme()">Readme</span>

    <div v-if="config.openSettings">
      <h3> Options </h3>
      <div>
        <input type="checkbox" v-model="config.simpleChords" />
        <label for="checkbox"> Show simple chords only </label>
      </div>

      <div>
        <fieldset>
          Legend Instrument
          <div v-for="instrument in VUE_CONSTANTS.INSTRUMENTS">
            <input
               type="radio"
               v-bind:id='"instrumentSelect" + instrument.value'
               v-model="config.instrument"
               v-bind:value='instrument.value'
               />
            <label v-bind:for='"instrumentSelect" + instrument.value'>
              {{ instrument.text }}
            </label>
          </div>
        </fieldset>
      </div>

    </div>

    <div v-if="config.openReadme">
      <h3>Readme</h3>
      <div>TODO: add instructions here</div>
    </div>
  </div>
</template>

<script>
import { VUE_CONSTANTS } from '../constants';
  export default {
    name: 'settings',
    props: ['config'],
    data: function() {
      return { VUE_CONSTANTS };
    }
  }
</script>
