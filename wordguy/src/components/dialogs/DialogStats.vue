<template>
  <v-dialog v-model="show" max-width="500px">
    <v-card @click.stop="show=false" style="cursor: default;">
      <v-card-text>
        <p class="text-h6 text-center text--primary">STATISTICS</p>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'DialogStats',

  props: {
    value: Boolean,
  },

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
