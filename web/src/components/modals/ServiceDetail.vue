<template>
  <modal :openModal="openModal" @closeModal="closeDialog()">
    <template v-slot:title>Service Detail</template>
    <template v-slot:content>
      <span class="modal-span-title">Channel</span>
      <div class="mb-3">
          <v-chip small color="FountainBlue White--text">AOI-ch</v-chip>
      </div>

      <span class="modal-span-title">Issue Start Time</span>
      <div class="mb-3" style="color: #212529">2021-02-24 10:00:05</div>

      <span class="modal-span-title">Service Description</span>
      <div class="mb-3" style="color: #212529">descdescdescdesc</div>
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