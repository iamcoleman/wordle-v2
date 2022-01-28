<template>

  <v-col>
    <v-responsive :aspect-ratio="1" class="tile" ref="tile">
      <p v-if="displayLetter">{{ letter }}</p>
    </v-responsive>
  </v-col>

</template>

<script>
export default {
  name: 'BoardTile',

  data: () => ({
    displayLetter: false,
  }),

  props: {
    letter: String,
    status: String,
    pos: Number,
  },

  computed: {
    flipInClass: function computeFlipInClass() {
      return `anim-flip-in-${this.pos}`;
    },
  },

  watch: {
    letter: {
      handler: function watchLetter(newVal, oldVal) {
        console.log('New:', newVal, '- Old:', oldVal);
        this.$nextTick(() => {
          if (oldVal === undefined && !!newVal && this.status !== 'tbd') {
            // initializing the board on refresh
            this.$refs.tile.$el.classList.add(this.flipInClass);
          } else if (!oldVal && !!newVal) {
            // a new letter is typed in
            this.displayLetter = true;
            this.$refs.tile.$el.classList.add('anim-pop');
          } else if (!!oldVal && !newVal) {
            // a letter is deleted
            this.displayLetter = false;
            this.$refs.tile.$el.classList.remove('tile-tbd');
          }
        });
      },
      immediate: true,
    },

    status: {
      handler: function watchStatus(newVal, oldVal) {
        this.$nextTick(() => {
          if (oldVal === 'tbd' && !!newVal) {
            this.$refs.tile.$el.classList.add(this.flipInClass);
          }
        });
      },
    },
  },

  mounted() {
    this.$nextTick(() => {
      this.$refs.tile.$el.addEventListener('animationend', this.onAnimationEnd);
    });
  },

  beforeDestroy() {
    this.$refs.tile.$el.removeEventListener('animationend', this.onAnimationEnd);
  },

  methods: {
    onAnimationEnd(val) {
      // console.log(val);
      if (val.srcElement.classList.contains(this.flipInClass)) {
        console.log('FlipIn');
        this.displayLetter = true;
        this.$refs.tile.$el.classList.remove(this.flipInClass);
        this.$refs.tile.$el.classList.add('anim-flip-out');
        this.$refs.tile.$el.classList.add(this.statusClass());
        // remove 'tile-tbd' class when transitioning from 'tbd' to any other status
        if (this.$refs.tile.$el.classList.contains('tile-tbd')) {
          this.$refs.tile.$el.classList.remove('tile-tbd');
        }
      } else if (val.srcElement.classList.contains('anim-flip-out')) {
        console.log('FlipOut');
        this.$refs.tile.$el.classList.remove('anim-flip-out');
      } else if (val.srcElement.classList.contains('anim-pop')) {
        console.log('Pop');
        this.$refs.tile.$el.classList.remove('anim-pop');
        this.$refs.tile.$el.classList.add(this.statusClass());
      }
    },

    statusClass() {
      switch (this.status) {
        case 'tbd':
          return 'tile-tbd';
        case 'absent':
          return 'tile-absent';
        case 'present':
          return 'tile-present';
        case 'correct':
          return 'tile-correct';
        default:
          return null;
      }
    },
  },
};
</script>

<style scoped lang="scss">
.col {
  margin-right: 5px;
  margin-bottom: 5px;
  padding: 0;

  &:last-of-type {
    margin: 0 0 5px 0;
  }
}

.tile {
  align-items: center;
  font-size: 2rem;
  line-height: 2rem;
  font-weight: bold;
  text-transform: uppercase;
  background-color: $white;
  color: $tile-text-tbd-color;
  //border: 4px solid $tile-border-empty;
  border-width: 4px;
  border-style: solid;
  border-color: $tile-border-empty;

  p {
    text-align: center;
    margin: 0;
  }

  &-tbd {
    border-color: $tile-border-tbd;
  }

  &-absent {
    border-width: 0 !important;
    background-color: $game-absent;
    color: $tile-text-color;
  }

  &-present {
    border-width: 0 !important;
    background-color: $game-present;
    color: $tile-text-color;
  }

  &-correct {
    border-width: 0 !important;
    background-color: $game-correct;
    color: $tile-text-color;
  }
}

@media (max-height: 650px) {
  .tile {
    font-size: 1rem !important;
    line-height: 1rem !important;
    border-width: 2px;
  }
}

// Animations
@keyframes PopIn {
  from {
    transform: scale(0.8);
    opacity: 0;
  }
  40% {
    transform: scale(1.1);
    opacity: 1;
  }
}
.anim-pop {
  animation-name: PopIn;
  animation-duration: 100ms;
}

@keyframes FlipIn {
  0% {
    transform: rotateX(0);
  }
  100% {
    transform: rotateX(-90deg);
  }
}
.anim-flip-in {
  &-0 {
    animation-name: FlipIn;
    animation-duration: 250ms;
    animation-timing-function: ease-in;
  }
  &-1 {
    animation-delay: 100ms;
    animation-name: FlipIn;
    animation-duration: 250ms;
    animation-timing-function: ease-in;
  }
  &-2 {
    animation-delay: 200ms;
    animation-name: FlipIn;
    animation-duration: 250ms;
    animation-timing-function: ease-in;
  }
  &-3 {
    animation-delay: 300ms;
    animation-name: FlipIn;
    animation-duration: 250ms;
    animation-timing-function: ease-in;
  }
  &-4 {
    animation-delay: 400ms;
    animation-name: FlipIn;
    animation-duration: 250ms;
    animation-timing-function: ease-in;
  }
  &-5 {
    animation-delay: 500ms;
    animation-name: FlipIn;
    animation-duration: 250ms;
    animation-timing-function: ease-in;
  }
}

@keyframes FlipOut {
  0% {
    transform: rotateX(-90deg);
  }
  100% {
    transform: rotateX(0);
  }
}
.anim-flip-out {
  animation-name: FlipOut;
  animation-duration: 250ms;
  animation-timing-function: ease-in;
}
</style>
