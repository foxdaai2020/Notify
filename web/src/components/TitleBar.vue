<template>
  <div
    id="titleBar"
    class="d-flex pr-5"
    style="white-space:nowrap; align-items: center;"
  >
    <div class="text">
      <slot name="title"></slot>
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
    <template>
      <v-checkbox label="Fail Post" class="mr-4"></v-checkbox>
      <v-checkbox label="Normal Post" class="mr-4"></v-checkbox>
      <v-datetime-picker label="Select Datetime">
        <template slot="dateIcon">
          <v-icon>mdi-calendar</v-icon>
        </template>
        <template slot="timeIcon">
          <v-icon>mdi-clock-outline</v-icon>
        </template>
      </v-datetime-picker>
      <v-datetime-picker label="Select Datetime">
        <template slot="dateIcon">
          <v-icon>mdi-calendar</v-icon>
        </template>
        <template slot="timeIcon">
          <v-icon>mdi-clock-outline</v-icon>
        </template>
      </v-datetime-picker>
      <v-btn small outlined>Show</v-btn>
    </template>
  </div>
</template>
<script>
  export default {
    props: ["serviceListFilter", "issueTackerFilter", "messageListFilter"],
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
  }
  //   .test.v-text-field .v-input__control .v-input__slot {
  //     min-height: 40px;
  //   }
</style>
