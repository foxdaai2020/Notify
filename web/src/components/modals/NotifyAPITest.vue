<template>
  <modal :openModal="openModal">
    <template v-slot:title>Notify API Test</template>
    <template v-slot:content>
      <span>User ID</span>
      <v-text-field outlined></v-text-field>

      <span>Service ID</span>
      <v-text-field outlined></v-text-field>

      <span>Message</span>
      <v-textarea></v-textarea>


      <span>Post Test</span>
      <v-radio-group>
          <v-radio label="No: Execute Service"></v-radio>
          <v-radio label="Yes: Direct to Channels (Default)"></v-radio>
      </v-radio-group>
    </template>
    <template v-slot:actions>
      <v-btn depressed @click="closeDialog" color="DarkGray White--text"
        >取消</v-btn
      >
      <v-btn depressed @click="submit" color="FountainBlue White--text"
        >確定</v-btn
      >
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
      submit() {
        this.$emit("closeModal");
      },
      closeDialog() {
        this.$emit("closeModal");
      }
    },
  };
</script>
