<template>
  <v-dialog v-model="show" persistent max-width="500px">
    <v-card>
      <v-card-text>
        <p class="text-h6 text-center text--primary">SETTINGS</p>
        <v-btn icon class="close-button" @click="show=false">
          <v-icon>fas fa-times</v-icon>
        </v-btn>
        <!-- SETTINGS -->
        <v-container>
          <v-row justify="center" align="center">
            <v-col>
              <span class="settings text--primary">Dark Mode</span>
              <p style="margin: 0;">Coming Soon!</p>
            </v-col>
            <v-spacer></v-spacer>
            <v-col class="text-right">
              <v-switch inset disabled class="settings-switch"></v-switch>
            </v-col>
          </v-row>

          <v-divider></v-divider>

          <v-row justify="center" align="center">
            <v-col>
              <span class="settings text--primary">Feedback</span>
            </v-col>
            <v-spacer></v-spacer>
            <v-col class="text-right" style="margin: 13px 0;">
              <v-btn
                fab
                small
                elevation="4"
                color="#1DA1F2"
                @click="openTwitter"
                style="margin: 4px;"
              >
                <v-icon color="white">fab fa-twitter</v-icon>
              </v-btn>
              <v-btn
                fab
                small
                elevation="4"
                color="secondary"
                @click="openEmail"
                style="margin: 4px;"
              >
                <v-icon>fas fa-envelope</v-icon>
              </v-btn>
            </v-col>
          </v-row>

          <v-divider></v-divider>
        </v-container>

<!--        <v-divider></v-divider>-->

        <!-- INFO -->
        <v-container style="margin-top: 4rem;">
          <v-row dense>
            <v-col>
              <span class="small-details">
                Inspired by the original
                <a href="https://www.powerlanguage.co.uk/wordle/" target="_blank">Wordle</a>
              </span>
            </v-col>
          </v-row>
          <v-row dense>
            <v-col>
              <span class="small-details">Copyright 2022.</span>
            </v-col>
            <v-spacer></v-spacer>
            <v-col class="text-right">
              <span class="small-details">Day #{{ currDayOffset }}</span>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'DialogSettings',

  props: {
    value: Boolean,
    currDayOffset: Number,
  },

  data: () => ({}),

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

  methods: {
    openTwitter() {
      window.open('https://twitter.com/DrColeTheMan', '_blank');
    },

    openEmail() {
      window.location = 'mailto:wordski.feedback@gmail.com?subject=WordskiFeedback';
    },
  },
};
</script>

<style scoped lang="scss">
.close-button {
  position: absolute;
  top: 6px;
  right: 14px;
}

.settings {
  font-size: 1rem;
}

p {}

.v-card__text {
  padding: 8px 24px !important;
}

.small-details {
  font-size: 0.8rem;
  line-height: 0.8rem;
}
</style>
