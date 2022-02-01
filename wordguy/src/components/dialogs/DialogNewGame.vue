<template>
  <v-dialog v-model="show" max-width="500px">
    <v-card @click.stop="show=false" style="cursor: default;">
      <v-card-text>
        <p class="text--primary">Guess the <strong>WORDLE</strong> in 6 tries.</p>
        <p class="text--primary">
          Each guess must be a valid 6 letter word. Press the submit key (bottom left) to submit
          your guess.
        </p>
        <p class="text--primary">
          After each guess, the color of the tiles will change to show how close your guess was to
          the correct word.
        </p>

        <v-divider></v-divider>

        <p class="text--primary"><strong>Examples</strong></p>

        <v-container style="width: 80%; margin: 0;">
          <BoardRow :letters="example1"></BoardRow>
        </v-container>
        <p class="text--primary">
          The letter <strong>E</strong> is in the word and in the correct spot.
        </p>

        <v-container style="width: 80%; margin: 0;">
          <BoardRow :letters="example2"></BoardRow>
        </v-container>
        <p class="text--primary">
          The letters <strong>W</strong> and <strong>K</strong> are in the word, but both are in the
          wrong spot.
        </p>

        <v-container style="width: 80%; margin: 0;">
          <BoardRow :letters="example3"></BoardRow>
        </v-container>
        <p class="text--primary">
          The letter <strong>E</strong> is not in the word in any spot.
        </p>

        <v-divider></v-divider>

        <p class="text--primary">
          <strong>
            A new WORDLE will be available each day!
          </strong>
        </p>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import BoardRow from '@/components/BoardRow.vue';

export default {
  name: 'DialogNewGame',

  components: {
    BoardRow,
  },

  props: {
    value: Boolean,
  },

  data: () => ({
    example1: [
      {
        letter: 'r',
        status: 'tbd',
      },
      {
        letter: 'e',
        status: 'correct',
      },
      {
        letter: 'c',
        status: 'tbd',
      },
      {
        letter: 'k',
        status: 'tbd',
      },
      {
        letter: 'o',
        status: 'tbd',
      },
      {
        letter: 'n',
        status: 'tbd',
      },
    ],
    example2: [
      {
        letter: 'w',
        status: 'present',
      },
      {
        letter: 'o',
        status: 'tbd',
      },
      {
        letter: 'r',
        status: 'tbd',
      },
      {
        letter: 'k',
        status: 'present',
      },
      {
        letter: 'e',
        status: 'tbd',
      },
      {
        letter: 'r',
        status: 'tbd',
      },
    ],
    example3: [
      {
        letter: 'n',
        status: 'tbd',
      },
      {
        letter: 'o',
        status: 'tbd',
      },
      {
        letter: 'v',
        status: 'tbd',
      },
      {
        letter: 'i',
        status: 'tbd',
      },
      {
        letter: 'c',
        status: 'tbd',
      },
      {
        letter: 'e',
        status: 'absent',
      },
    ],
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
</style>
