<template>
  <div class="datetimePicker d-flex">
    <span class="mr-2"><slot></slot></span>
    <v-datetime-picker outlined hide-details>
      <template slot="dateIcon">
        <v-icon>mdi-calendar</v-icon>
      </template>
      <template slot="timeIcon">
        <v-icon>mdi-clock-outline</v-icon>
      </template>
    </v-datetime-picker>
    <!-- <v-icon style="border-left: 1px solid black;padding: 2px">mdi-clock-outline</v-icon> -->
  </div>
</template>
<style lang="scss">
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
</style>
