<template>
  <v-container id="board" :style="{ width: boardWidth + 'px' }">
    <BoardRow v-bind:letters="boardData[0]"></BoardRow>
    <BoardRow v-bind:letters="boardData[1]"></BoardRow>
    <BoardRow v-bind:letters="boardData[2]"></BoardRow>
    <BoardRow v-bind:letters="boardData[3]"></BoardRow>
    <BoardRow v-bind:letters="boardData[4]"></BoardRow>
    <BoardRow v-bind:letters="boardData[5]"></BoardRow>
<!--    {{ windowHeight }}-->
<!--    {{ windowWidth }}-->
<!--    {{ boardWidth }}-->
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
  },

  data: () => ({
    windowHeight: window.innerHeight,
    windowWidth: window.innerWidth,
  }),

  computed: {
    boardWidth: function getBoardWidth() {
      // 0.84 is a good ratio for current setup
      const estBoardHeight = Math.floor(this.windowWidth / 0.84);
      const containerHeight = this.windowHeight - 290;

      if (estBoardHeight > containerHeight) {
        return Math.floor(containerHeight * 0.84);
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
