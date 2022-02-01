<template>
  <v-row ref="row">
    <BoardTile
      v-bind:letter="letters[0].letter"
      v-bind:status="letters[0].status"
      v-bind:pos="0"
      v-bind:win="win"
      v-bind:shake="shake"
    ></BoardTile>
    <BoardTile
      v-bind:letter="letters[1].letter"
      v-bind:status="letters[1].status"
      v-bind:pos="1"
      v-bind:win="win"
      v-bind:shake="shake"
    ></BoardTile>
    <BoardTile
      v-bind:letter="letters[2].letter"
      v-bind:status="letters[2].status"
      v-bind:pos="2"
      v-bind:win="win"
      v-bind:shake="shake"
    ></BoardTile>
    <BoardTile
      v-bind:letter="letters[3].letter"
      v-bind:status="letters[3].status"
      v-bind:pos="3"
      v-bind:win="win"
      v-bind:shake="shake"
    ></BoardTile>
    <BoardTile
      v-bind:letter="letters[4].letter"
      v-bind:status="letters[4].status"
      v-bind:pos="4"
      v-bind:win="win"
      v-bind:shake="shake"
    ></BoardTile>
    <BoardTile
      v-bind:letter="letters[5].letter"
      v-bind:status="letters[5].status"
      v-bind:pos="5"
      v-bind:win="win"
      v-bind:shake="shake"
    ></BoardTile>
  </v-row>
</template>

<script>
import BoardTile from '@/components/BoardTile.vue';

export default {
  name: 'BoardRow',

  components: {
    BoardTile,
  },

  props: {
    letters: Array,
    win: Boolean,
    shake: Boolean,
  },
};
</script>

<style scoped lang="scss">

</style>
