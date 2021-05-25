<template>
  <modal :openModal="openModal">
    <template v-slot:title>Service Detail</template>
    <template v-slot:content>
      <span class="modal-span-title">Channel</span>
      <div>
          <v-chip>AOI-ch</v-chip>
      </div>

      <span class="modal-span-title">Service ID</span>
      <v-text-field outlined></v-text-field>

      <span class="modal-span-title">Message</span>
      <v-textarea outlined auto-grow rows="2"></v-textarea>

      <span class="modal-span-title">Post Test</span>
    </template>
    <template v-slot:actions>
      <div class="modal-button-group">
        <v-btn depressed @click="submit" color="DarkGray White--text"
          >關閉</v-btn
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
      },
    },
  };
</script>