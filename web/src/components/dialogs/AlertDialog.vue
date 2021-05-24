<template>
  <v-dialog v-model="openDialog" width="400px">
    <v-card>
      <v-card-text class="d-flex justify-center pt-4">
        <slot name="content" />
      </v-card-text>
      <v-card-actions class="justify-center">
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
