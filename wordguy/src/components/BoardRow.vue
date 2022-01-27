<template>
  <v-row>
    <v-col style="background-color: white">
      <v-responsive :aspect-ratio="1">W</v-responsive>
    </v-col>
    <v-col style="background-color: white">
      <v-responsive :aspect-ratio="1">W</v-responsive>
    </v-col>
    <v-col style="background-color: white">
      <v-responsive :aspect-ratio="1">W</v-responsive>
    </v-col>
    <v-col style="background-color: white">
      <v-responsive :aspect-ratio="1">W</v-responsive>
    </v-col>
    <v-col style="background-color: white">
      <v-responsive :aspect-ratio="1">W</v-responsive>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'BoardRow',
};
</script>

<style scoped lang="scss">
//.row {
//  margin-bottom: 5px;
//}

.col {
  margin-right: 5px;
  margin-bottom: 5px;
  padding: 0;

  &:last-of-type {
    margin: 0 0 5px 0;
  }
}
</style>
