<template>
  <v-dialog v-model="openDialog" width="500px">
    <v-card>
      <v-card-title>
        <slot name="title-icon"></slot>
        <slot name="title-text"></slot>
      </v-card-title>
      <v-divider></v-divider>
      <v-card-text>
        <slot name="content" />
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
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
