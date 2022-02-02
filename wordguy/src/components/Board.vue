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
<!--    {{ windowHeight }}-->
<!--    {{ windowWidth }}-->
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
    boardData: Array,
    winAnimation: Array,
    shakeAnimation: Array,
  },

  data: () => ({
    windowHeight: window.innerHeight,
    windowWidth: window.innerWidth,
  }),

  computed: {
    boardWidth: function getBoardWidth() {
      // 0.96 is a good ratio for current setup
      const estBoardHeight = Math.floor(this.windowWidth / 0.96);
      // 290px == height of bar and keyboard
      const containerHeight = this.windowHeight - 290;

      if (estBoardHeight > containerHeight) {
        return Math.floor(containerHeight * 0.96);
      }

      return 500;
    },
  },

  mounted() {
    this.$nextTick(() => {
      window.addEventListener('resize', this.onResize);
    });
  },

  beforeDestroy() {
    window.removeEventListener('resize', this.onResize);
  },

  methods: {
    onResize() {
      this.windowHeight = window.innerHeight;
      this.windowWidth = window.innerWidth;
    },
  },

};
</script>

<style scoped lang="scss">
</style>
