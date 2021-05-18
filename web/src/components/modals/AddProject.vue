<template>
  <modal :openModal="openModal">
    <template v-slot:title>Add Project</template>
    <template v-slot:content>
      <v-text-field outlined label="* Project Name"></v-text-field>
      <v-text-field outlined label="* Project Name"></v-text-field>
      <v-text-field outlined label="* Project Name"></v-text-field>
      <v-text-field outlined label="* Project Name"></v-text-field>
      <v-text-field outlined label="* Project Name"></v-text-field>
      <v-text-field outlined label="* Project Name"></v-text-field>
      <v-select outlined label="* Project Name"></v-select>
      <v-select outlined label="* Project Name"></v-select>
      <v-select outlined label="* Project Name"></v-select>
      <v-select outlined label="* Project Name"></v-select>
      <v-select outlined label="* Project Name"></v-select>
    </template>
    <template v-slot:actions>
      <v-btn @click="closeDialog"></v-btn>
      <v-btn @click="closeDialog"></v-btn>
    </template>
  </modal>
</template>
<script>
  import Modal from "./Modal";
  export default {
    props: ["openModal"],
    components: {
      modal: Modal,
    },
    methods: {
      closeDialog() {
        this.$emit("closeModal");
      },
    },
  };
</script>
