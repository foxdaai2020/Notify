<template>
  <div
    id="titleBar"
    class="d-flex pr-5"
    style="white-space:nowrap; align-items: center;"
  >
    <div class="text">
      <span><slot></slot></span>
    </div>
    <v-spacer></v-spacer>

    <template v-if="serviceListFilter">
      <v-select
        heigth="20px"
        style="max-width:150px"
        width="50px"
        hide-details
        dense
        class="mr-4"
        outlined
      ></v-select>
      <v-btn small outlined>Show</v-btn>
    </template>

    <template v-if="issueTackerFilter">
      <v-checkbox label="Open" class="mr-4"></v-checkbox>
      <v-checkbox label="Close" class="mr-4"></v-checkbox>
      <v-btn small outlined>Show</v-btn>
    </template>

    <template v-if="messageListFilter">
      <v-checkbox label="Fail Post" class="mr-4"></v-checkbox>
      <v-checkbox label="Normal Post" class="mr-4"></v-checkbox>
      <datetime-picker>
        Start Time
      </datetime-picker>
      <datetime-picker>
        End Time
      </datetime-picker>
      <v-btn small outlined>Show</v-btn>
    </template>
  </div>
</template>
<script>
  import DateTimePicker from "./DateTimePicker";

  export default {
    props: ["serviceListFilter", "issueTackerFilter", "messageListFilter"],
    components: {
      "datetime-picker": DateTimePicker,
    },
  };
</script>
<style lang="scss">
  #titleBar {
    height: 36px;
    background: var(--v-WhiteIce-base);
    height: 36px;
    border-radius: 20px;
    .text {
      background: var(--v-HummingBird-base);
      border-radius: 20px;
      height: 36px;
      display: inline-flex;
      align-items: center;
      flex: 0;
      padding: 16px;
    }

    .datetimePicker {
      .v-text-field {
        padding-top: unset;
        margin-top: unset;

        .v-text-field__details {
          display: none;
        }

        margin-right: 16px;
        .v-input__slot {
          margin-bottom: unset;
        }
        input {
          max-height: 24px;
        }
      }
    }
  }
</style>
