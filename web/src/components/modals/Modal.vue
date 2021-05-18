<template>
  <v-navigation-drawer
    absolute
    v-model="openModal"
    :permanent="openModal"
    right
    temporary
    class="d-flex modal"
    style="height: 100vh;"
  >
    <v-card class="d-flex flex-column" style="flex: 1">
      <v-card-title><slot name="title"></slot></v-card-title>
      <v-divider class="mb-4"></v-divider>
      <v-card-text class="d-flex flex-column" style="flex: 1">
        <slot name="content"></slot>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <slot name="actions"></slot>
      </v-card-actions>
    </v-card>
  </v-navigation-drawer>
</template>

<script>
  export default {
    props: ["openModal"]
  };
</script>

<style lang="scss">
  .modal .v-navigation-drawer__content {
    display: flex;

    .v-card__text {
      overflow: scroll;
      .v-input {
        flex: 0;
      }
    }
  }
</style>
