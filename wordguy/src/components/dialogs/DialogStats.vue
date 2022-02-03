<template>
  <v-dialog v-model="show" max-width="500px">
    <v-card @click.stop="show=false" style="cursor: default;" v-ripple="false">
      <v-card-text>
        <!-- STATISTICS -->
        <p class="text-h6 text-center text--primary">STATISTICS</p>
        <v-container style="padding: 0;">
          <v-row class="text-center flex-nowrap">
            <v-col>
              <p class="text--primary stat-value">{{ gamesPlayed }}</p>
              <p class="stat-desc">Games Played</p>
            </v-col>
            <v-col>
              <p class="text--primary stat-value">{{ winPercentage }}%</p>
              <p class="stat-desc">Win %</p>
            </v-col>
            <v-col>
              <p class="text--primary stat-value">{{ currentStreak }}</p>
              <p class="stat-desc">Current Streak</p>
            </v-col>
            <v-col>
              <p class="text--primary stat-value">{{ maxStreak }}</p>
              <p class="stat-desc">Max Streak</p>
            </v-col>
          </v-row>
        </v-container>

        <!-- GUESS HISTORY -->
        <p class="text-h6 text-center text--primary" style="margin-bottom: 0;">GUESS HISTORY</p>
        <p class="text-center" style="margin: 0;">
          Average Guesses: {{ Math.round(averageGuesses * 100) / 100 }}
        </p>
        <GuessesChart :chart-data="guessesChartData" :styles="chartStyles"></GuessesChart>

        <!-- NEXT GAME & SHARE -->
        <v-container v-if="showShare">
          <v-row class="text-center align-center flex-nowrap">
            <v-col>
              <p class="text-h6 text-center text--primary" style="margin: 0;">
                NEXT WORDSKI
              </p>
              <p class="text-h4 text--primary">
                <countdown :time="ms" :transform="transform">
                  <template slot-scope="props">
                    {{ props.hours }}:{{ props.minutes }}:{{ props.seconds }}
                  </template>
                </countdown>
              </p>
            </v-col>
            <v-divider vertical></v-divider>
            <v-col>
              <div v-if="webShareApiSupported">
                <!-- Large Share Button -->
                <v-btn
                  large
                  color="green"
                  class="share-button white--text"
                  v-if="!useSmallButton"
                  @click.stop="shareViaWebShare"
                >
                  Share&nbsp;&nbsp;<v-icon>fas fa-share-alt</v-icon>
                </v-btn>
                <!-- Small Share Button -->
                <v-btn
                  fab
                  color="green"
                  class="white--text"
                  v-if="useSmallButton"
                  @click.stop="shareViaWebShare"
                >
                  <v-icon>fas fa-share-alt</v-icon>
                </v-btn>
              </div>
              <div v-if="!webShareApiSupported">
                <v-textarea
                  name="copyAndPaste"
                  label=""
                  :value="generateShareText()"
                  outlined
                  auto-grow
                  @click.stop
                ></v-textarea>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import GuessesChart from '@/components/dialogs/GuessesChart.vue';

export default {
  name: 'DialogStats',
  components: {
    GuessesChart,
  },

  props: {
    value: Boolean,
    msNewGame: Number,
    currGameStatus: String,
  },

  data: () => ({
    averageGuesses: 0,
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

    ms: 0,
    showShare: false,
    shareText: '',

    windowWidth: window.innerWidth,
  }),

  computed: {
    show: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit('input', value);
      },
    },

    chartStyles: function computeChartStyles() {
      return {
        height: '220px',
      };
    },

    guessesChartData: function computeChartData() {
      return {
        // axis: 'y',
        labels: ['1', '2', '3', '4', '5', '6', 'Fail'],
        datasets: [
          {
            label: 'Guesses',
            data: [
              this.guesses['1'],
              this.guesses['2'],
              this.guesses['3'],
              this.guesses['4'],
              this.guesses['5'],
              this.guesses['6'],
              this.guesses.fail,
            ],
            backgroundColor: 'rgba(134, 136, 138, 1)',
            categoryPercentage: 0.85,
            barPercentage: 1.0,
            datalabels: {
              align: 'left',
              anchor: 'end',
            },
            minBarLength: 22,
          },
        ],
      };
    },

    webShareApiSupported: function computeWebShareApiSupported() {
      return !!navigator.share;
    },

    useSmallButton: function computeUseSmallButton() {
      return this.windowWidth <= 400;
    },
  },

  watch: {
    show: function watchShow(val) {
      if (val) {
        this.loadStats();
        this.shareText = this.generateShareText();
      }
    },

    msNewGame: {
      handler: function watchLetter(val) {
        this.ms = val;
      },
      immediate: true,
    },

    currGameStatus: {
      handler: function watchCurrGameStatus(val) {
        this.showShare = val !== 'IN_PROGRESS';
      },
      immediate: true,
    },
  },

  mounted() {
    this.loadStats();

    this.$nextTick(() => {
      window.addEventListener('resize', this.onResize);
    });
  },

  beforeDestroy() {
    window.removeEventListener('resize', this.onResize);
  },

  methods: {
    loadStats() {
      let stats = localStorage.getItem('statistics');
      if (stats) {
        stats = JSON.parse(stats);
        this.averageGuesses = stats.averageGuesses;
        this.currentStreak = stats.currentStreak;
        this.gamesPlayed = stats.gamesPlayed;
        this.gamesWon = stats.gamesWon;
        this.maxStreak = stats.maxStreak;
        this.winPercentage = stats.winPercentage;
        this.guesses = stats.guesses;
      }
    },

    shareViaWebShare() {
      console.log(this.shareText);
      navigator.share({
        text: this.shareText,
      });
    },

    generateShareText() {
      let gameState = localStorage.getItem('gameState');
      let text = '';
      if (gameState) {
        gameState = JSON.parse(gameState);
        // set Wordski number
        text += `Wordski ${gameState.dayOffset}`;
        // set X/6
        text += gameState.gameStatus === 'FAIL' ? ' F/6' : ` ${gameState.rowIndex + 1}/6`;
        text += '\n\n';
        // create board text
        text += this.createBoardText(gameState.boardData);
      }

      return text;
    },

    createBoardText(boardData) {
      let boardText = '';
      for (let row = 0; row < boardData.length; row += 1) {
        if (boardData[row][0].letter === '') {
          break;
        }
        for (let col = 0; col < boardData[row].length; col += 1) {
          switch (boardData[row][col].status) {
            case 'present':
              boardText += '🟨';
              break;
            case 'correct':
              boardText += '🟩';
              break;
            default:
              boardText += '⬛️';
              break;
          }
        }
        boardText += '\n';
      }

      return boardText;
    },

    transform(props) {
      Object.entries(props).forEach(([key, value]) => {
        // add leading zero
        const digits = value < 10 ? `0${value}` : value;

        /* eslint-disable-next-line */
        props[key] = `${digits}`;
      });

      return props;
    },

    onResize() {
      this.windowWidth = window.innerWidth;
    },
  },
};
</script>

<style scoped lang="scss">
p {
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.v-card__text {
  padding: 8px 24px !important;
}

.stat-value {
  margin-bottom: 0 !important;

  @media screen and (max-width: 350px) {
    font-size: 1.25rem;
    line-height: 1.25rem;
  }
  @media screen and (min-width: 350px) and (max-width: 400px) {
    font-size: 1.7rem;
    line-height: 1.7rem;
  }
  @media screen and (min-width: 400px) {
    font-size: 2rem;
    line-height: 2rem;
  }
}

.stat-desc {
  margin-top: 0 !important;
  font-size: 12px;
  line-height: 12px;
}

.share-button {
  font-size: 20px !important;
}

.v-btn__content {
  color: white;
}
</style>
