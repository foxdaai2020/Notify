<template>
  <modal :openModal="openModal">
    <template v-slot:title>Notify API Test</template>
    <template v-slot:content>
      <span class="modal-span-title">User ID</span>
      <v-text-field outlined></v-text-field>

      <span class="modal-span-title">Service ID</span>
      <v-text-field outlined></v-text-field>

      <span class="modal-span-title">Message</span>
      <v-textarea></v-textarea>


      <span class="modal-span-title">Post Test</span>
      <v-radio-group>
          <v-radio label="No: Execute Service"></v-radio>
          <v-radio label="Yes: Direct to Channels (Default)"></v-radio>
      </v-radio-group>
    </template>
    <template v-slot:actions>
      <div class="modal-button-group">
        <v-btn depressed @click="closeDialog" color="DarkGray White--text" class="mr-2"
          >取消</v-btn
        >
        <v-btn depressed @click="submit" color="FountainBlue White--text"
          >確定</v-btn
        >
      </div>
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
