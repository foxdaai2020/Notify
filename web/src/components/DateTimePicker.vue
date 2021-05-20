<template>
  <div class="datetimePicker">
    <!-- <span class="mr-2"><slot></slot></span> -->
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
      //   margin-right: 16px;
      .v-input__slot {
        margin-bottom: unset;
        border-color: rgba(0, 0, 0, 0.38);
        border-style: solid;
        border-width: 1px;
        border-radius: 4px;
        background-color: #ffffff;
        font-size: 12px;
        padding-right: 8px;
        padding-left: 8px;
        &:before {
          border-style: unset !important;
        }
        &:after {
          border-style: unset !important;
        }
        &:hover {
          border-color: black;
        }
      }

      input {
        max-height: 24px;
      }
    }
  }
</style>
