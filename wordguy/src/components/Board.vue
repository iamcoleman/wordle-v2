<template>
  <v-container id="board" :style="{ width: boardWidth + 'px' }">
    <BoardRow
      v-bind:letters="boardData[0]"
      v-bind:win="winAnimation[0]"
      v-bind:shake="shakeAnimation[0]"
    ></BoardRow>
    <BoardRow
      v-bind:letters="boardData[1]"
      v-bind:win="winAnimation[1]"
      v-bind:shake="shakeAnimation[1]"
    ></BoardRow>
    <BoardRow
      v-bind:letters="boardData[2]"
      v-bind:win="winAnimation[2]"
      v-bind:shake="shakeAnimation[2]"
    ></BoardRow>
    <BoardRow
      v-bind:letters="boardData[3]"
      v-bind:win="winAnimation[3]"
      v-bind:shake="shakeAnimation[3]"
    ></BoardRow>
    <BoardRow
      v-bind:letters="boardData[4]"
      v-bind:win="winAnimation[4]"
      v-bind:shake="shakeAnimation[4]"
    ></BoardRow>
    <BoardRow
      v-bind:letters="boardData[5]"
      v-bind:win="winAnimation[5]"
      v-bind:shake="shakeAnimation[5]"
    ></BoardRow>
<!--    {{ boardWidth }}-->
<!--    {{ shakeAnimation }}-->
<!--    {{ winAnimation }}-->
  </v-container>
</template>

<script>
import BoardRow from '@/components/BoardRow.vue';

export default {
  name: 'Board',

  components: {
    BoardRow,
  },

  props: {
    controlHeight: Number,
    boardData: Array,
    winAnimation: Array,
    shakeAnimation: Array,
  },

  data: () => ({}),

  computed: {
    boardWidth: function getBoardWidth() {
      if (this.controlHeight < 500) {
        if (this.controlHeight < 275) {
          return Math.floor(this.controlHeight * 0.9);
        }
        return Math.floor(this.controlHeight * 0.95);
      }

      return 500;
    },
  },

  methods: {},

};
</script>

<style scoped lang="scss">
</style>
