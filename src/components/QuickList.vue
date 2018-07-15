<template>
  <div id="quicklist" v-if="!quicklist.visible">
    <div class="right">Quick access list</div>
    <ul>
      <li v-for="(col, index) in quicklist.collections">
        <span>{{ index + 1 }}</span>
        <span class="spacing" />

          <span class="selectable clickable"
                v-on:click="onQuicklistSelect(index)"
                v-bind:class="{ selected: (chord.root.note == col[1] && chord.chord == col[2]) || (scale.root.note == col[1] && scale.scale == col[2]), alternate: chord.root.note == col[1] && chord.chord == col[2] }">{{ quicklist.displayStr(col) }}
          </span>
          <span class="spacing" />

            <span class="selectable clickable"
                  v-on:click="quicklist.remove(index)"
                  v-bind:title="'Remove ' + col[0]">(rm)
            </span>
      </li>
      <span class="right selectable clickable"
            v-on:click="quicklist.clearAll()"
            title="Clear list">clear
      </span>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'quicklist',
  props: ['quicklist', 'scale'],
}
</script>

<style lang="scss" scope>

#quicklist {
  position: fixed;
  right: 1em;
  bottom: 1em;
  background-color: #0000000a;
}

ul {
  list-style-type: none;
}
</style>
