<template>
  <modal :openModal="openModal">
    <template v-slot:title>Edit Issue</template>
    <template v-slot:content>
      <span>Message ID</span>
      <v-text-field outlined></v-text-field>

      <span>Update time</span>
      <v-text-field outlined></v-text-field>

      <span>Status</span>
      <v-select dense attach outlined :items="items"> </v-select>

      <v-checkbox
        label="Apply to previous message  ({message cnt})"
      ></v-checkbox>
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
    data: () => {
      return {
        search: null,
        channelName: null,
        members: [],
        chips: [],
        items: ["Open", "Close"],
      };
    },
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
