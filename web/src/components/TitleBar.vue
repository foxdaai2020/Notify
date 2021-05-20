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
        width="50px"
        hide-details
        dense
        class="mr-4"
        outlined
        chips
        multiple
        :items="items"
        attach
      >
        <template v-slot:selection="{ item }">
          <v-chip small>
            <span>{{ item }}</span>
          </v-chip>
          <!-- <span v-if="index === 1" class="grey--text caption">
            (+{{ value.length - 1 }} others)
          </span> -->
        </template>
      </v-select>
      <v-btn small outlined>Show</v-btn>
    </template>

    <template v-if="issueTackerFilter">
      <v-checkbox label="Open" class="mr-4"></v-checkbox>
      <v-checkbox label="Close" class="mr-4"></v-checkbox>
      <span class="mr-2">Start Time</span>
      <datetime-picker> </datetime-picker>

      <span class="mr-2">End Time</span>
      <datetime-picker></datetime-picker>
      <v-btn small outlined>Show</v-btn>
    </template>

    <template v-if="messageListFilter">
      <v-checkbox label="Fail Post" class="mr-4"></v-checkbox>
      <v-checkbox label="Normal Post" class="mr-4"></v-checkbox>
      <span class="mr-2">Start Time</span>
      <datetime-picker> </datetime-picker>
      <span class="mr-2">End Time</span>
      <datetime-picker> </datetime-picker>
      <v-btn small outlined>Show</v-btn>
    </template>
  </div>
</template>
<script>
  import DateTimePicker from "./DateTimePicker";

  export default {
    data: () => {
      return {
        items: ["11111", "21111", "31111", "313111", "3111ㄉ1", "311211"],
      };
    },
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
