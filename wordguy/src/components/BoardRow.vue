<template>
  <v-row>

<!--    <v-col-->
<!--      v-for="(letter, index) in letters"-->
<!--      :key="index"-->
<!--      :ref="'letter-' + index"-->
<!--      class="anim-pop"-->
<!--    >-->
<!--      <v-responsive :aspect-ratio="1" class="tile" :class="tileClass(letter)">-->
<!--        <p>{{ letter.char }}</p>-->
<!--      </v-responsive>-->
<!--    </v-col>-->

    <BoardTile
      v-bind:letter="letters[0].letter"
      v-bind:status="letters[0].status"
      v-bind:pos="0"
    ></BoardTile>
    <BoardTile
      v-bind:letter="letters[1].letter"
      v-bind:status="letters[1].status"
      v-bind:pos="1"
    ></BoardTile>
    <BoardTile
      v-bind:letter="letters[2].letter"
      v-bind:status="letters[2].status"
      v-bind:pos="2"
    ></BoardTile>
    <BoardTile
      v-bind:letter="letters[3].letter"
      v-bind:status="letters[3].status"
      v-bind:pos="3"
    ></BoardTile>
    <BoardTile
      v-bind:letter="letters[4].letter"
      v-bind:status="letters[4].status"
      v-bind:pos="4"
    ></BoardTile>
    <BoardTile
      v-bind:letter="letters[5].letter"
      v-bind:status="letters[5].status"
      v-bind:pos="5"
    ></BoardTile>

<!--    <v-col>-->
<!--      <v-responsive :aspect-ratio="1" class="tile">-->
<!--        <p>W</p>-->
<!--      </v-responsive>-->
<!--    </v-col>-->
<!--    <v-col>-->
<!--      <v-responsive :aspect-ratio="1" class="tile">-->
<!--        <p>W</p>-->
<!--      </v-responsive>-->
<!--    </v-col>-->
<!--    <v-col>-->
<!--      <v-responsive :aspect-ratio="1" class="tile">-->
<!--        <p>W</p>-->
<!--      </v-responsive>-->
<!--    </v-col>-->
<!--    <v-col>-->
<!--      <v-responsive :aspect-ratio="1" class="tile">-->
<!--        <p>W</p>-->
<!--      </v-responsive>-->
<!--    </v-col>-->
<!--    <v-col>-->
<!--      <v-responsive :aspect-ratio="1" class="tile">-->
<!--        <p>W</p>-->
<!--      </v-responsive>-->
<!--    </v-col>-->
<!--    <v-col>-->
<!--      <v-responsive :aspect-ratio="1" class="tile">-->
<!--        <p>W</p>-->
<!--      </v-responsive>-->
<!--    </v-col>-->

  </v-row>
</template>

<script>
import BoardTile from '@/components/BoardTile.vue';

export default {
  name: 'BoardRow',

  components: {
    BoardTile,
  },

  props: {
    letters: Array,
  },

  mounted() {
    // console.log(this.$refs['letter-5']);
  },

  watch: {
    // letters: {
    //   deep: true,
    //   immediate: true,
    //   handler: function watchLetters(newVal, oldVal) {
    //     console.log(newVal[2].char, oldVal[2].char);
    //   },
    // },
  },

  methods: {
    tileClass(letter) {
      return {
        'tile-tbd': letter.status === 'tbd',
        'tile-absent': letter.status === 'absent',
        'tile-present': letter.status === 'present',
        'tile-correct': letter.status === 'correct',
      };
    },
  },
};
</script>

<style scoped lang="scss">

</style>
