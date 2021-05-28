<template>
  <modal :openModal="openModal" @closeModal="closeDialog()">
    <template v-slot:title>Service Detail</template>
    <template v-slot:content>
      <span class="modal-span-title">Channel</span>
      <div class="mb-2">
          <v-chip class="mr-1 mb-1" v-for="(item, index) of 10" :key="index" small color="DimGray White--text">AOI-ch</v-chip>
      </div>

      <span class="modal-span-title">Issue Start Time</span>
      <v-text-field disabled outlined></v-text-field>

      <span class="modal-span-title">Service Description</span>
      <v-text-field disabled outlined></v-text-field>

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