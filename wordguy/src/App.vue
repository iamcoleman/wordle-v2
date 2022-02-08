<template>
  <v-app>
    <!-- Dialogs -->
    <DialogNewGame v-model="showNewGameDialog"></DialogNewGame>
    <DialogStats
      v-model="showStatsDialog"
      v-bind:msNewGame="msUntilNewGameAvailable"
      v-bind:curr-game-status="gameStatus"
      @next-game="loadNextGame(lastCompletedTs)"
    ></DialogStats>
    <DialogSettings
      v-model="showSettingsDialog"
      :curr-day-offset="dayOffset"
    ></DialogSettings>

    <v-app-bar
      app
      color="white"
      flat
      outlined
      style="height: 56px;"
    >
      <v-container class="py-0 fill-height app-container">
        <v-btn icon @click="openNewGame(0)" class="bar-buttons">
          <v-icon>fas fa-info</v-icon>
        </v-btn>
        <v-spacer></v-spacer>
        <h1>WORDSKI</h1>
        <v-spacer></v-spacer>
        <v-btn icon @click="openStats(0)" class="bar-buttons">
          <v-icon>far fa-chart-bar</v-icon>
        </v-btn>
        <v-btn icon @click="openSettings(0)" class="bar-buttons">
          <v-icon>fas fa-cog</v-icon>
        </v-btn>
<!--        <v-btn @click="test()">test</v-btn>-->
      </v-container>
    </v-app-bar>

    <v-main class="main-override">
      <v-divider style="max-width: 500px; margin: 0 auto;"></v-divider>
      <v-container
        ref="board-container"
        id="board-container"
        class="app-container fill-height"
      >
<!--        <router-view/>-->
        <Board
          v-bind:control-height="controlHeight"
          v-bind:board-data="boardData"
          v-bind:win-animation="winAnimation"
          v-bind:shake-animation="shakeAnimation"
        ></Board>
      </v-container>
    </v-main>

    <v-footer app color="white" class="disable-dbl-tap-zoom" style="height: 210px;">
      <v-container class="app-container fill-height" style="padding: 0;">
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
import DialogSettings from '@/components/dialogs/DialogSettings.vue';
import { acceptableGuesses, wordList } from '@/store/wordlist';

export default {
  name: 'App',

  components: {
    Board,
    Keyboard,
    DialogNewGame,
    DialogStats,
    DialogSettings,
  },

  data: () => ({
    controlHeight: 0,

    wordList,
    acceptableGuesses,
    startingDate: new Date(2022, 0, 1, 0, 0, 0, 0),
    currentDate: new Date(),

    solution: null,
    dayOffset: null,
    lastCompletedTs: null,
    gameStatus: 'IN_PROGRESS',
    winAnimation: [false, false, false, false, false, false],
    shakeAnimation: [false, false, false, false, false, false],

    // dialogs
    showNewGameDialog: false,
    showStatsDialog: false,
    msUntilNewGameAvailable: 0,
    showSettingsDialog: false,

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
      dayOffset: null,
    },
    newStatistics: {
      averageGuesses: null,
      currentStreak: 0,
      gamesPlayed: 0,
      gamesWon: 0,
      maxStreak: 0,
      winPercentage: 0,
      guesses: {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        fail: 0,
      },
    },

    keyboardStatus: {
      absent: [],
      present: [],
      correct: [],
    },
    newKeyboardStatus: {
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

    newGameAvailable: function computeNewGameAvailable() {
      if (this.dayOffset) {
        return this.dayOffset < this.getDayOffset();
      }

      return false;
    },
  },

  mounted() {
    if (localStorage.gameState) {
      // load the gameState
      this.loadGameFromStorage();
    } else {
      // create new game
      this.createNewGame();
    }

    // control-height
    this.$nextTick(() => {
      window.addEventListener('resize', this.controlHeightResize);
      this.controlHeightResize();
    });

    // keyboard input
    this.$nextTick(() => {
      window.addEventListener('keydown', this.keyboardInput);
    });
  },

  beforeDestroy() {
    window.removeEventListener('resize', this.controlHeightResize);
    window.removeEventListener('keydown', this.keyboardInput);
  },

  methods: {
    controlHeightResize() {
      this.controlHeight = this.$refs['board-container'].clientHeight;
    },

    getTodaysSolution() {
      let day = Math.abs(new Date().setHours(0, 0, 0, 0)
        - this.startingDate.setHours(0, 0, 0, 0));
      day = Math.ceil(day / (1000 * 60 * 60 * 24));

      return this.wordList[day];
    },

    getDayOffset() {
      const dayOffset = Math.abs(new Date().setHours(0, 0, 0, 0)
        - this.startingDate.setHours(0, 0, 0, 0));

      return Math.ceil(dayOffset / (1000 * 60 * 60 * 24));
    },

    keyboardInput(key) {
      if (key.keyCode === 8) {
        this.onKeyInput('delete');
      } else if (key.keyCode === 13) {
        this.onKeyInput('submit');
      } else if (key.keyCode >= 65 && key.keyCode <= 90) {
        this.onKeyInput(key.key.toLowerCase());
      }
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
        this.shakeRow();
        this.$toast.warning('Row does not have 6 characters');
        return;
      }

      // not in acceptable guesses
      if (!this.acceptableGuesses.includes(this.currentRowLetters.join(''))) {
        this.shakeRow();
        /* eslint-disable-next-line */
        this.$toast.warning(`${this.currentRowLetters.join('').toUpperCase()} is not in the word list`);
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
        // reset `winAnimation` (1000ms for flips, 1700ms for bounce)
        setTimeout(() => {
          Vue.set(this.winAnimation, this.currentRowIndex, false);
        }, 2700);
        // save `WIN` to storage
        this.saveGameToStorage('WIN');
        // generate statistics
        this.generateStats();
        // open WIN toast
        this.$toast.success(`${this.solution.toUpperCase()} is correct!`);
        // open statistics dialog (1000ms for flips, 1700ms for bounce)
        this.openStats(1000 + 1700);
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
        // generate statistics
        this.generateStats();
        // open FAIL toast
        this.$toast.error(`${this.solution.toUpperCase()} was the solution...`, {
          timeout: false,
        });
        // open statistics dialog (1000ms for flips)
        this.openStats(1000);
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

        if (currLetter === solutionCopy[i]) {
          // the character is 'correct'
          rowData[i] = {
            letter: currLetter,
            status: 'correct',
          };
          // remove character from `solutionCopy` bc it has been accounted for
          solutionCopy = this.setCharAt(solutionCopy, i, '0');
        }
      }

      // handle all 'present' next and remove present chars from `solutionCopy`
      for (let i = 0; i < this.currentRowLetters.length; i += 1) {
        // skip all `rowData` indexes that have already been populated with 'correct'
        if (!rowData[i]) {
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
      }

      // handle all 'absent' last
      for (let i = 0; i < this.currentRowLetters.length; i += 1) {
        // skip all `rowData` indexes that have already been populated with 'correct' | 'absent'
        if (!rowData[i]) {
          const currLetter = this.currentRowLetters[i];

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

    generateStats() {
      let prevStats = null;
      if (!localStorage.statistics) {
        console.log('No statistics found in LocalStorage...');
        prevStats = this.newStatistics;
      } else {
        prevStats = JSON.parse(localStorage.getItem('statistics'));
      }

      const newStats = JSON.parse(JSON.stringify(prevStats)); // deep copy

      // update `currentStreak`, `gamesPlayed`, and `gamesWon`
      if (this.gameStatus === 'WIN') {
        newStats.currentStreak += 1;
        newStats.gamesPlayed += 1;
        newStats.gamesWon += 1;
      } else {
        newStats.currentStreak = 0;
        newStats.gamesPlayed += 1;
      }

      // update `maxStreak`
      newStats.maxStreak = Math.max(newStats.currentStreak, newStats.maxStreak);

      // update `winPercentage`
      newStats.winPercentage = Math.round((newStats.gamesWon / newStats.gamesPlayed) * 100);

      // update `guesses`
      let numOfGuesses = null;
      if (this.gameStatus === 'WIN') {
        numOfGuesses = (this.currentRowIndex + 1).toString();
      } else {
        numOfGuesses = 'fail';
      }
      newStats.guesses[numOfGuesses] += 1;

      // update `averageGuesses`
      let totalGuesses = 0;
      totalGuesses += newStats.guesses['1'];
      totalGuesses += (newStats.guesses['2'] * 2);
      totalGuesses += (newStats.guesses['3'] * 3);
      totalGuesses += (newStats.guesses['4'] * 4);
      totalGuesses += (newStats.guesses['5'] * 5);
      totalGuesses += (newStats.guesses['6'] * 6);
      totalGuesses += (newStats.guesses.fail * 6); // fail counts as 6 guesses
      newStats.averageGuesses = (totalGuesses / newStats.gamesPlayed);

      // save `newStats` to LocalStorage
      const parsedNewStats = JSON.stringify(newStats);
      localStorage.setItem('statistics', parsedNewStats);
    },

    loadNextGame(lastPlayedTs) {
      // set `solution` to today's solution
      this.solution = this.getTodaysSolution();
      // set `dayOffset` to today's offset
      this.dayOffset = this.getDayOffset();
      // set `gameStatus` to 'IN_PROGRESS'
      this.gameStatus = this.newGameState.gameStatus;
      // set `boardData` to default
      this.boardData = this.newGameState.boardData;
      // set `keyboardStatus` to default
      this.keyboardStatus = this.newKeyboardStatus;
      // set `currentRowLetters` to default
      this.currentRowLetters = [];
      // set `currentRowIndex` to 0
      this.currentRowIndex = this.newGameState.rowIndex;

      // make the gameState
      const gameState = {
        boardData: this.boardData,
        lastCompletedTs: this.lastCompletedTs,
        lastPlayedTs,
        gameStatus: this.gameStatus,
        rowIndex: this.currentRowIndex,
        solution: this.solution,
        dayOffset: this.dayOffset,
      };

      // save to LocalStorage
      const parsedGameState = JSON.stringify(gameState);
      localStorage.setItem('gameState', parsedGameState);
    },

    loadGameFromStorage() {
      if (!localStorage.gameState) {
        console.error('gameState does not exist in LocalStorage');
      }

      const gameState = JSON.parse(localStorage.getItem('gameState'));

      // set `lastCompletedTs` before gameStatus check because `newGameAvailable` requires it
      this.lastCompletedTs = gameState.lastCompletedTs;
      // set `dayOffset` before gameStatus check because `newGameAvailable` requires it
      this.dayOffset = gameState.dayOffset;

      // check if gameState from LocalStorage is in completed state
      if (gameState.gameStatus === 'WIN' || gameState.gameStatus === 'FAIL') {
        // then, check if new game is available
        if (this.newGameAvailable) {
          this.loadNextGame(gameState.lastPlayedTs);
          return;
        }
      }

      // if gameState from LocalStorage is not in completed state, then load it in

      // set `solution`
      this.solution = gameState.solution;
      // set `dayOffset`
      this.dayOffset = gameState.dayOffset;
      // set `gameStatus`
      this.gameStatus = gameState.gameStatus;
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
      const gameState = {
        boardData: this.boardData,
        lastCompletedTs: this.lastCompletedTs,
        lastPlayedTs: new Date().getTime(),
        rowIndex: this.currentRowIndex,
        gameStatus: this.gameStatus,
        solution: this.solution,
        dayOffset: this.dayOffset,
      };

      const parsedGameState = JSON.stringify(gameState);
      localStorage.setItem('gameState', parsedGameState);
    },

    createNewGame() {
      // set `solution` to today's solution
      this.solution = this.getTodaysSolution();
      // set `dayOffset` to today's offset
      this.dayOffset = this.getDayOffset();

      const gameState = {
        boardData: this.newGameState.boardData,
        lastCompletedTs: this.newGameState.lastCompletedTs,
        lastPlayedTs: this.newGameState.lastPlayedTs,
        gameStatus: this.newGameState.gameStatus,
        rowIndex: this.newGameState.rowIndex,
        solution: this.solution,
        dayOffset: this.dayOffset,
      };

      const parsedGameState = JSON.stringify(gameState);
      localStorage.setItem('gameState', parsedGameState);

      this.openNewGame();
    },

    updateMsUntilNewGameAvailable() {
      if (!this.newGameAvailable) {
        const currDateTime = new Date();

        this.msUntilNewGameAvailable = (24 * 60 * 60 * 1000) - Math.abs(
          new Date().setHours(0, 0, 0, 0) - currDateTime.getTime(),
        );
      } else {
        this.msUntilNewGameAvailable = 0;
      }
    },

    openStats(delay = 0) {
      setTimeout(() => {
        this.updateMsUntilNewGameAvailable();
        this.showStatsDialog = true;
      }, delay);
    },

    openNewGame(delay = 0) {
      setTimeout(() => {
        this.showNewGameDialog = true;
      }, delay);
    },

    openSettings(delay = 0) {
      setTimeout(() => {
        this.showSettingsDialog = true;
      }, delay);
    },

    /* Replaces the character at `index` with `char` in string `str` */
    setCharAt(str, index, char) {
      if (index > (str.length - 1)) {
        return str;
      }

      return str.substr(0, index) + char + str.substr(index + 1);
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

      // this.showNewGameDialog = true;
      // this.showStatsDialog = true;
      // this.openNewGame();
      this.openStats();

      // console.log(new Date().setHours(0, 0, 0, 0));

      // console.log(this.boardData);
    },
  },
};
</script>

<style lang="scss">
.main-override {
  padding: 0 !important;
  position: fixed !important;
  top: 56px !important;
  bottom: 210px !important;
  left: 0 !important;
  right: 0 !important;
}

.bar-buttons {
  @media screen and (max-width: 310px) {
    height: 28px !important;
    width: 28px !important;
  }
  @media screen and (min-width: 310px) and (max-width: 350px) {
    height: 36px !important;
    width: 36px !important;
  }
  @media screen and (min-width: 350px) {
    height: 48px !important;
    width: 48px !important;
  }
}
</style>
