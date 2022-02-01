<template>
  <v-app>
    <!-- Dialogs -->
    <DialogNewGame v-model="showNewGameDialog"></DialogNewGame>
    <DialogStats v-model="showStatsDialog"></DialogStats>

    <v-app-bar
      app
      color="white"
      flat
    >
      <v-container class="py-0 fill-height top-nav app-container">
        <v-spacer></v-spacer>
        <h1>Wordle v2</h1>
        <v-spacer></v-spacer>
        <v-btn @click="test()">test</v-btn>
      </v-container>
    </v-app-bar>

    <v-main>
      <v-container
        ref="board-container"
        id="board-container"
        class="app-container fill-height"
      >
<!--        <router-view/>-->
        <Board
          v-bind:board-data="boardData"
          v-bind:win-animation="winAnimation"
          v-bind:shake-animation="shakeAnimation"
        ></Board>
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
import Vue from 'vue';
import Keyboard from '@/components/Keyboard.vue';
import Board from '@/components/Board.vue';
import DialogNewGame from '@/components/dialogs/DialogNewGame.vue';
import DialogStats from '@/components/dialogs/DialogStats.vue';
import wordList from '@/store/wordlist';

export default {
  name: 'App',

  components: {
    Board,
    Keyboard,
    DialogNewGame,
    DialogStats,
  },

  data: () => ({
    wordList,
    startingDate: new Date(2022, 0, 1, 0, 0, 0, 0),
    currentDate: new Date(),

    solution: null,
    lastCompletedTs: null,
    gameStatus: 'IN_PROGRESS',
    winAnimation: [false, false, false, false, false, false],
    shakeAnimation: [false, false, false, false, false, false],

    // dialogs
    showNewGameDialog: false,
    showStatsDialog: false,

    newGameState: {
      boardData: [
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
      gameStatus: 'IN_PROGRESS',
      lastCompletedTs: null,
      lastPlayedTs: null,
      rowIndex: 0,
      solution: null,
    },

    keyboardStatus: {
      absent: [],
      present: [],
      correct: [],
    },

    currentRowIndex: 0,
    currentRowLetters: [],

    boardData: [
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

  mounted() {
    if (localStorage.gameState) {
      console.log('gameState exists');
      // load the gameState
      this.loadGameFromStorage();
    } else {
      // create new game
      this.createNewGame();
    }
  },

  methods: {
    getTodaysSolution() {
      let day = Math.abs(this.currentDate.setHours(0, 0, 0, 0)
        - this.startingDate.setHours(0, 0, 0, 0));
      day = Math.ceil(day / (1000 * 60 * 60 * 24));

      return this.wordList[day];
    },

    onKeyInput(key) {
      if (this.gameStatus === 'IN_PROGRESS') {
        if (key === 'delete') {
          this.deleteLetter();
        } else if (key === 'submit') {
          this.submitRow();
        } else {
          this.addLetter(key);
        }
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

    submitRow() {
      // not 6 letters in row
      if (this.currentRowLetters.length !== 6) {
        console.error('Row does not have 6 characters...');
        this.shakeRow();
        return;
      }

      // not in wordlist
      if (!this.wordList.includes(this.currentRowLetters.join(''))) {
        console.error('Word not in wordlist...');
        this.shakeRow();
        return;
      }

      // update Keyboard and BoardData
      this.updateKeyboardStatus(this.currentRowLetters.join(''));
      this.updateBoardData();

      // check for `WIN`
      if (this.currentRowLetters.join('') === this.solution) {
        // update `gameStatus`
        this.gameStatus = 'WIN';
        // update `lastCompletedTs`
        this.lastCompletedTs = new Date().getTime();
        // update `winAnimation`
        Vue.set(this.winAnimation, this.currentRowIndex, true);
        // save `WIN` to storage
        this.saveGameToStorage('WIN');
        return;
      }

      // check for `FAIL`
      if ((this.currentRowIndex + 1) > 5) {
        // update `gameStatus`
        this.gameStatus = 'FAIL';
        // update `lastCompletedTs`
        this.lastCompletedTs = new Date().getTime();
        // save `FAIL` to storage
        this.saveGameToStorage('FAIL');
        return;
      }

      // continue the game if no `WIN` or `FAIL`
      this.nextTurn();
      this.saveGameToStorage('IN_PROGRESS');
    },

    updateKeyboardStatus(rowString) {
      let solutionCopy = this.solution;

      // handle all 'correct' first and remove correct chars from `solutionCopy`
      for (let i = 0; i < rowString.length; i += 1) {
        if (rowString[i] === solutionCopy[i]) {
          // add character to 'correct' if it does not already exist
          if (!this.keyboardStatus.correct.includes(rowString[i])) {
            this.keyboardStatus.correct.push(rowString[i]);
          }
          // set character to '0' in `solutionCopy` bc it has been accounted for
          solutionCopy = this.setCharAt(solutionCopy, i, '0');
          // remove character from 'present' if it exists
          this.keyboardStatus.present = this.keyboardStatus.present
            .filter((char) => char !== rowString[i]);
        }
      }

      // handle 'present' and 'absent' after correct
      for (let i = 0; i < rowString.length; i += 1) {
        const charIndex = solutionCopy.indexOf(rowString[i]);
        if (charIndex > -1) {
          // the character is 'present'
          if (!this.keyboardStatus.present.includes(rowString[i])) {
            this.keyboardStatus.present.push(rowString[i]);
          }
          // set character to '0' in `solutionCopy` bc it has been accounted for
          solutionCopy = this.setCharAt(solutionCopy, charIndex, '0');
        } else {
          // the character is 'absent'
          /* eslint-disable-next-line */
          if (!this.keyboardStatus.absent.includes(rowString[i])) {
            this.keyboardStatus.absent.push(rowString[i]);
          }
        }
      }
    },

    updateBoardData() {
      const rowData = [null, null, null, null, null, null];
      let solutionCopy = this.solution;

      // handle all 'correct' first and remove correct chars from `solutionCopy`
      for (let i = 0; i < this.currentRowLetters.length; i += 1) {
        const currLetter = this.currentRowLetters[i];
        const charIndex = solutionCopy.indexOf(currLetter);

        if (charIndex === i) {
          // the character is 'correct'
          rowData[i] = {
            letter: currLetter,
            status: 'correct',
          };
          // remove character from `solutionCopy` bc it has been accounted for
          solutionCopy = this.setCharAt(solutionCopy, charIndex, '0');
        }
      }

      // handle all 'present' next and remove present chars from `solutionCopy`
      for (let i = 0; i < this.currentRowLetters.length; i += 1) {
        const currLetter = this.currentRowLetters[i];
        const charIndex = solutionCopy.indexOf(currLetter);

        if (charIndex > -1) {
          // the character is 'present'
          rowData[i] = {
            letter: currLetter,
            status: 'present',
          };
          // remove character from `solutionCopy` bc it has been accounted for
          solutionCopy = this.setCharAt(solutionCopy, charIndex, '0');
        }
      }

      // handle all 'absent' last
      for (let i = 0; i < this.currentRowLetters.length; i += 1) {
        const currLetter = this.currentRowLetters[i];

        if (rowData[i] === null) {
          rowData[i] = {
            letter: currLetter,
            status: 'absent',
          };
        }
      }

      // update the `boardData` with `rowData`
      Vue.set(this.boardData, this.currentRowIndex, rowData);
    },

    nextTurn() {
      this.currentRowIndex += 1;
      this.currentRowLetters = [];
    },

    shakeRow() {
      Vue.set(this.shakeAnimation, this.currentRowIndex, true);
      // 600ms is the length of the Shake animation
      setTimeout(() => {
        Vue.set(this.shakeAnimation, this.currentRowIndex, false);
      }, 600);
    },

    endGame(victory) {
      console.log(victory);
    },

    loadGameFromStorage() {
      if (!localStorage.gameState) {
        console.error('gameState does not exist in LocalStorage');
      }

      const gameState = JSON.parse(localStorage.getItem('gameState'));
      console.log(gameState);

      // set `solution`
      this.solution = gameState.solution;
      // set `gameStatus`
      this.gameStatus = gameState.gameStatus;
      // set `lastCompletedTs`
      this.lastCompletedTs = gameState.lastCompletedTs;
      // set `boardData`
      this.boardData = gameState.boardData;
      // set `currentRowIndex`
      this.currentRowIndex = gameState.rowIndex;

      // update keyboard
      for (let i = 0; i < this.boardData.length; i += 1) {
        const rowLetterArray = [];
        for (let j = 0; j < this.boardData[i].length; j += 1) {
          rowLetterArray.push(this.boardData[i][j].letter);
        }
        this.updateKeyboardStatus(rowLetterArray.join(''));
      }
    },

    saveGameToStorage() {
      const savedBoardData = [];
      for (let i = 0; i < this.boardData.length; i += 1) {
        if (this.boardData[i][0].letter !== '') {
          savedBoardData.push(this.boardData[i]);
        } else {
          savedBoardData.push(this.newGameState.boardData[0]);
        }
      }

      const gameState = {
        boardData: savedBoardData,
        lastCompletedTs: this.lastCompletedTs,
        lastPlayedTs: new Date().getTime(),
        rowIndex: this.currentRowIndex,
        gameStatus: this.gameStatus,
        solution: this.solution,
      };

      const parsedGameState = JSON.stringify(gameState);
      localStorage.setItem('gameState', parsedGameState);
    },

    createNewGame() {
      // set `solution` to today's solution
      this.solution = this.getTodaysSolution();

      const gameState = {
        boardData: this.newGameState.boardData,
        lastCompletedTs: this.newGameState.lastCompletedTs,
        lastPlayedTs: this.newGameState.lastPlayedTs,
        gameStatus: this.newGameState.gameStatus,
        rowIndex: this.newGameState.rowIndex,
        solution: this.solution,
      };

      const parsedGameState = JSON.stringify(gameState);
      localStorage.setItem('gameState', parsedGameState);

      // TODO: Launch the 'instruction/new game' dialog
    },

    test() {
      // const lastCompletedTs = new Date(1643393863747);
      // const lastPlayedTs = new Date(1643656200631);
      // console.log(lastCompletedTs);
      // console.log(lastPlayedTs);
      // const newGuy = new Date();
      // console.log(newGuy.getTime());
      // console.log(newGuy);

      // let solutionCopy = this.solution;
      // console.log(solutionCopy);
      // console.log(this.solution);
      // solutionCopy = this.setCharAt(solutionCopy, 2, 'X');
      // console.log(solutionCopy);
      // console.log(this.solution);
      // solutionCopy = this.setCharAt(solutionCopy, 4, 'X');
      // console.log(solutionCopy);
      // console.log(this.solution);

      this.showNewGameDialog = true;
      // this.showStatsDialog = true;
    },

    /* Replaces the character at `index` with `char` in string `str` */
    setCharAt(str, index, char) {
      if (index > (str.length - 1)) {
        return str;
      }

      return str.substr(0, index) + char + str.substr(index + 1);
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
