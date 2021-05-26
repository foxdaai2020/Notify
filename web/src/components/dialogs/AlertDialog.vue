<template>
  <v-dialog v-model="openDialog" width="400px">
    <v-card height="200px">
      <v-card-text class="dialog-content d-flex justify-center pt-4">
        <slot name="content" />
      </v-card-text>
      <v-card-actions class="dialog-click-btn justify-center">
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
.dialog-content {
  position: absolute;
  top: 40px;
}

.dialog-click-btn {
  position: relative;
  top: 110px;
}
</style>
