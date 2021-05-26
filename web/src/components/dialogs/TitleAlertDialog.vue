<template>
  <v-dialog v-model="openDialog" width="500px">
    <v-card>
      <v-card-title>
        <v-icon class="mr-2"><slot name="title-icon"></slot></v-icon>
        <slot name="title-text"></slot>
      </v-card-title>
      <v-divider></v-divider>
      <v-card-text class="mt-5">
        <slot name="content" />
      </v-card-text>
      <v-card-actions class="pb-6 title-dialog-click-btn">

        <slot name="action" />
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
  export default {
    props: ["openDialog"],
  };
</script>
<style>
.title-dialog-click-btn {
  position: relative;
  left: 320px;
}
</style>
