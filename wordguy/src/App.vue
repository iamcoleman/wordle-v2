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
        <v-btn @click="changeBoardData()">click</v-btn>
      </v-container>
    </v-app-bar>

    <v-main>
      <v-container
        ref="board-container"
        id="board-container"
        class="app-container fill-height"
      >
<!--        <router-view/>-->
        <Board v-bind:board-data="boardData"></Board>
      </v-container>
    </v-main>

    <v-footer app color="white">
      <v-container class="top-nav app-container fill-height">
        <Keyboard
          v-bind:keyboard-absent="keyboardStatus.absent"
          v-bind:keyboard-present="keyboardStatus.present"
          v-bind:keyboard-correct="keyboardStatus.correct"
          @keyInput="onKeyInput"
        ></Keyboard>
      </v-container>
    </v-footer>
  </v-app>
</template>

<script>
import Keyboard from '@/components/Keyboard.vue';
import Board from '@/components/Board.vue';
import Vue from 'vue';

export default {
  name: 'App',

  components: {
    Board,
    Keyboard,
  },

  data: () => ({
    wordList: ['apples', 'grapes', 'stinky', 'pisser', 'johnny'],
    startingDate: new Date(2022, 0, 1, 0, 0, 0, 0),
    currentDate: new Date(),

    keyboardStatus: {
      absent: ['a', 'z'],
      present: ['t', 'y'],
      correct: ['w'],
    },

    currentRowIndex: 2,
    currentRowLetters: ['t', 'r'],

    boardData: [
      [
        {
          letter: 'a',
          status: 'absent',
        },
        {
          letter: 'p',
          status: 'present',
        },
        {
          letter: 'p',
          status: 'present',
        },
        {
          letter: 'l',
          status: 'absent',
        },
        {
          letter: 'e',
          status: 'correct',
        },
        {
          letter: 's',
          status: 'absent',
        },
      ],
      [
        {
          letter: 'b',
          status: 'present',
        },
        {
          letter: 'r',
          status: 'absent',
        },
        {
          letter: 'a',
          status: 'correct',
        },
        {
          letter: 'k',
          status: 'absent',
        },
        {
          letter: 'e',
          status: 'correct',
        },
        {
          letter: 's',
          status: 'absent',
        },
      ],
      [
        {
          letter: 't',
          status: 'tbd',
        },
        {
          letter: 'r',
          status: 'tbd',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
      ],
      [
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
      ],
      [
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
      ],
      [
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
        {
          letter: '',
          status: '',
        },
      ],
    ],
  }),

  computed: {
    currentRowData: function computeCurrentRowData() {
      return [
        {
          letter: this.currentRowLetters[0] ? this.currentRowLetters[0] : '',
          status: this.currentRowLetters[0] ? 'tbd' : '',
        },
        {
          letter: this.currentRowLetters[1] ? this.currentRowLetters[1] : '',
          status: this.currentRowLetters[1] ? 'tbd' : '',
        },
        {
          letter: this.currentRowLetters[2] ? this.currentRowLetters[2] : '',
          status: this.currentRowLetters[2] ? 'tbd' : '',
        },
        {
          letter: this.currentRowLetters[3] ? this.currentRowLetters[3] : '',
          status: this.currentRowLetters[3] ? 'tbd' : '',
        },
        {
          letter: this.currentRowLetters[4] ? this.currentRowLetters[4] : '',
          status: this.currentRowLetters[4] ? 'tbd' : '',
        },
        {
          letter: this.currentRowLetters[5] ? this.currentRowLetters[5] : '',
          status: this.currentRowLetters[5] ? 'tbd' : '',
        },
      ];
    },
  },

  methods: {
    onKeyInput(key) {
      console.log('App:', key);
      if (key === 'delete') {
        this.deleteLetter();
      } else if (key === 'submit') {
        //
      } else {
        this.addLetter(key);
      }
    },

    addLetter(letter) {
      if (this.currentRowLetters.length < 6) {
        this.currentRowLetters.push(letter);
        Vue.set(this.boardData, this.currentRowIndex, this.currentRowData);
      }
    },

    deleteLetter() {
      if (this.currentRowLetters.length > 0) {
        this.currentRowLetters.pop();
        Vue.set(this.boardData, this.currentRowIndex, this.currentRowData);
      }
    },

    changeKeyboardStatus() {
      this.keyboardStatus.absent.push('q');
      this.keyboardStatus.correct.push('t');
    },

    changeBoardData() {
      // this.boardData[2][2].char = 'i';
      // this.boardData[2][2].status = 'tbd';
      // Vue.set(this.boardData[2], 2, { letter: 'i', status: 'tbd' });
      Vue.set(this.boardData[2], 1, { letter: '', status: '' });
      Vue.set(this.boardData[2], 0, { letter: 't', status: 'correct' });
      // console.log(Math.round((this.startingDate - this.currentDate) / 864e5));
      // console.log(Math.round((this.startingDate - this.currentDate)));
      const diffTime = Math.abs(this.currentDate.setHours(0, 0, 0, 0)
        - this.startingDate.setHours(0, 0, 0, 0));
      const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
      console.log('diffDays:', diffDays);
      console.log(this.currentDate.toLocaleString());
      console.log(this.startingDate.toLocaleString());
      // console.log((this.startingDate - this.currentDate) % this.wordList.length);
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
