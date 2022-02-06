<template>
  <div id="keyboard">
<!--    <p>{{ keyboardAbsent }}</p>-->
<!--    <p>{{ keyboardPresent }}</p>-->
<!--    <p>{{ keyboardCorrect }}</p>-->

    <!--  TOP ROW  -->
    <div class="d-flex flex-row justify-center keyboard-row">
      <button
        ref="q"
        @click="onKeyboardClick('q')"
        class="fade"
        :class="letterClass('q')"
        v-on:keydown.enter.prevent
      >q</button>
      <button
        ref="w"
        @click="onKeyboardClick('w')"
        class="fade"
        :class="letterClass('w')"
        v-on:keydown.enter.prevent
      >w</button>
      <button
        ref="e"
        @click="onKeyboardClick('e')"
        class="fade"
        :class="letterClass('e')"
        v-on:keydown.enter.prevent
      >e</button>
      <button
        ref="r"
        @click="onKeyboardClick('r')"
        class="fade"
        :class="letterClass('r')"
        v-on:keydown.enter.prevent
      >r</button>
      <button
        ref="t"
        @click="onKeyboardClick('t')"
        class="fade"
        :class="letterClass('t')"
        v-on:keydown.enter.prevent
      >t</button>
      <button
        ref="y"
        @click="onKeyboardClick('y')"
        class="fade"
        :class="letterClass('y')"
        v-on:keydown.enter.prevent
      >y</button>
      <button
        ref="u"
        @click="onKeyboardClick('u')"
        class="fade"
        :class="letterClass('u')"
        v-on:keydown.enter.prevent
      >u</button>
      <button
        ref="i"
        @click="onKeyboardClick('i')"
        class="fade"
        :class="letterClass('i')"
        v-on:keydown.enter.prevent
      >i</button>
      <button
        ref="o"
        @click="onKeyboardClick('o')"
        class="fade"
        :class="letterClass('o')"
        v-on:keydown.enter.prevent
      >o</button>
      <button
        ref="p"
        @click="onKeyboardClick('p')"
        class="fade"
        :class="letterClass('p')"
        v-on:keydown.enter.prevent
      >p</button>
    </div>

    <!--  MIDDLE ROW  -->
    <div class="d-flex flex-row justify-center keyboard-row">
      <div class="half-spacer"></div>
      <button
        ref="a"
        @click="onKeyboardClick('a')"
        class="fade"
        :class="letterClass('a')"
        v-on:keydown.enter.prevent
      >a</button>
      <button
        ref="s"
        @click="onKeyboardClick('s')"
        class="fade"
        :class="letterClass('s')"
        v-on:keydown.enter.prevent
      >s</button>
      <button
        ref="d"
        @click="onKeyboardClick('d')"
        class="fade"
        :class="letterClass('d')"
        v-on:keydown.enter.prevent
      >d</button>
      <button
        ref="f"
        @click="onKeyboardClick('f')"
        class="fade"
        :class="letterClass('f')"
        v-on:keydown.enter.prevent
      >f</button>
      <button
        ref="g"
        @click="onKeyboardClick('g')"
        class="fade"
        :class="letterClass('g')"
        v-on:keydown.enter.prevent
      >g</button>
      <button
        ref="h"
        @click="onKeyboardClick('h')"
        class="fade"
        :class="letterClass('h')"
        v-on:keydown.enter.prevent
      >h</button>
      <button
        ref="j"
        @click="onKeyboardClick('j')"
        class="fade"
        :class="letterClass('j')"
        v-on:keydown.enter.prevent
      >j</button>
      <button
        ref="k"
        @click="onKeyboardClick('k')"
        class="fade"
        :class="letterClass('k')"
        v-on:keydown.enter.prevent
      >k</button>
      <button
        ref="l"
        @click="onKeyboardClick('l')"
        class="fade"
        :class="letterClass('l')"
        v-on:keydown.enter.prevent
      >l</button>
      <div class="half-spacer"></div>
    </div>

    <!--  BOTTOM ROW  -->
    <div class="d-flex flex-row justify-center keyboard-row">
      <button
        class="one-and-a-half"
        @click="onKeyboardClick('submit')"
        v-on:keydown.enter.prevent
      >
        <v-icon style="font-size: 16px;">fas fa-check</v-icon>
      </button>
      <button
        ref="z"
        @click="onKeyboardClick('z')"
        class="fade"
        :class="letterClass('z')"
        v-on:keydown.enter.prevent
      >z</button>
      <button
        ref="x"
        @click="onKeyboardClick('x')"
        class="fade"
        :class="letterClass('x')"
        v-on:keydown.enter.prevent
      >x</button>
      <button
        ref="c"
        @click="onKeyboardClick('c')"
        class="fade"
        :class="letterClass('c')"
        v-on:keydown.enter.prevent
      >c</button>
      <button
        ref="v"
        @click="onKeyboardClick('v')"
        class="fade"
        :class="letterClass('v')"
        v-on:keydown.enter.prevent
      >v</button>
      <button
        ref="b"
        @click="onKeyboardClick('b')"
        class="fade"
        :class="letterClass('b')"
        v-on:keydown.enter.prevent
      >b</button>
      <button
        ref="n"
        @click="onKeyboardClick('n')"
        class="fade"
        :class="letterClass('n')"
        v-on:keydown.enter.prevent
      >n</button>
      <button
        ref="m"
        @click="onKeyboardClick('m')"
        class="fade"
        :class="letterClass('m')"
        v-on:keydown.enter.prevent
      >m</button>
      <button
        class="one-and-a-half"
        @click="onKeyboardClick('delete')"
        v-on:keydown.enter.prevent
      >
        <v-icon style="font-size: 16px;">fas fa-backspace</v-icon>
      </button>
    </div>

  </div>
</template>

<script>
export default {
  name: 'Keyboard',

  props: {
    keyboardAbsent: Array,
    keyboardPresent: Array,
    keyboardCorrect: Array,
  },

  data: () => ({
    //
  }),

  methods: {
    onKeyboardClick(key) {
      this.$emit('keyInput', key);
    },

    letterClass(letter) {
      return {
        absent: this.keyboardAbsent.includes(letter),
        present: this.keyboardPresent.includes(letter),
        correct: this.keyboardCorrect.includes(letter),
      };
    },
  },
};
</script>

<style scoped lang="scss">
#keyboard {
  width: 100%;
}

.keyboard-row {
  margin: 0 auto 8px;
}

button {
  font-weight: bold;
  border: 0;
  padding: 0;
  margin: 0 6px 0 0;
  height: 58px;
  border-radius: 4px;
  cursor: pointer;
  user-select: none;
  background-color: $kb-bg-color;
  color: $kb-text-tbd-color;
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  text-transform: uppercase;
  -webkit-tap-highlight-color: rgba(0,0,0,0.3);

  &:last-of-type {
    margin: 0;
  }
}

.half-spacer {
  flex: 0.5;
}

.one-and-a-half {
  flex: 1.5;
}

.fade {
  transition: background-color 0.2s ease, color 0.2s ease;
}

.absent {
  background-color: $game-absent;
  color: $kb-text-color;
}

.present {
  background-color: $game-present;
  color: $kb-text-color;
}

.correct {
  background-color: $game-correct;
  color: $kb-text-color;
}
</style>
