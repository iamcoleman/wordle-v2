<template>
  <v-container id="board" style="background-color: seagreen" :style="{ width: boardWidth + 'px' }">
    <BoardRow></BoardRow>
    <BoardRow></BoardRow>
    <BoardRow></BoardRow>
    <BoardRow></BoardRow>
    <BoardRow></BoardRow>
    <BoardRow></BoardRow>
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

  data: () => ({
    windowHeight: window.innerHeight,
    windowWidth: window.innerWidth,
  }),

  computed: {
    boardWidth: function getBoardWidth() {
      // 0.77 is a good ratio for current setup
      const estBoardHeight = Math.floor(this.windowWidth / 0.77);
      const containerHeight = this.windowHeight - 290;

      if (estBoardHeight > containerHeight) {
        return Math.floor(containerHeight * 0.77);
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
