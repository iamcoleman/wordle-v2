<template>
  <v-app>
    <v-app-bar
      app
      color="white"
      flat
    >
      <v-container class="py-0 fill-height top-nav app-container">
        <v-spacer></v-spacer>
        <h1>Wordle v2</h1>
        <v-spacer></v-spacer>
        <v-btn @click="changeKeyboardStatus()">click</v-btn>
      </v-container>
    </v-app-bar>

    <v-main>
      <v-container
        ref="board-container"
        id="board-container"
        class="top-nav app-container fill-height"
      >
<!--        <router-view/>-->
        <Board></Board>
      </v-container>
    </v-main>

    <v-footer app color="white">
      <v-container class="top-nav app-container fill-height">
        <Keyboard
          v-bind:keyboard-absent="keyboardStatus.absent"
          v-bind:keyboard-present="keyboardStatus.present"
          v-bind:keyboard-correct="keyboardStatus.correct"
        ></Keyboard>
      </v-container>
    </v-footer>
  </v-app>
</template>

<script>
import Keyboard from '@/components/Keyboard.vue';
import Board from '@/components/Board.vue';

export default {
  name: 'App',

  components: {
    Board,
    Keyboard,
  },

  data: () => ({
    keyboardStatus: {
      absent: ['a', 'z'],
      present: ['t', 'y'],
      correct: ['w'],
    },
  }),

  methods: {
    changeKeyboardStatus() {
      this.keyboardStatus.absent.push('q');
      this.keyboardStatus.correct.push('t');
    },
  },
};
</script>

<style lang="scss">
$new-color: red;

.top-nav {
  background-color: $new-color;
}
</style>
