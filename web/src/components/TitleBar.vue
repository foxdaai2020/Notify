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
    <div class="filter " style="display: flex;align-items: center;">
      <template v-if="serviceListFilter">
        <span class="mr-2">Project</span>
        <v-select
          hide-details
          dense
          class="mr-4"
          outlined
          multiple
          :items="items"
          attach
          v-model="projects"
        >
        </v-select>
        <v-btn small outlined color="Genoa White--text">Show</v-btn>
      </template>

      <template v-if="issueTackerFilter">
        <v-checkbox label="Open" class="mr-4" hide-details></v-checkbox>
        <v-checkbox label="Close" class="mr-4" hide-details></v-checkbox>
        <span class="mr-2">Start Time</span>
        <datetime-picker> </datetime-picker>

        <span class="mr-2">End Time</span>
        <datetime-picker></datetime-picker>
        <v-btn small outlined color="Genoa White--text">Show</v-btn>
      </template>

      <template v-if="messageListFilter">
        <v-checkbox label="Fail Post" class="mr-4" hide-details></v-checkbox>
        <v-checkbox label="Normal Post" class="mr-4" hide-details></v-checkbox>
        <span class="mr-2">Start Time</span>
        <datetime-picker> </datetime-picker>
        <span class="mr-2">End Time</span>
        <datetime-picker> </datetime-picker>
        <v-btn small outlined color="Genoa White--text">Show</v-btn>
      </template>
    </div>
  </div>
</template>
<script>
  import DateTimePicker from "./DateTimePicker";

  export default {
    data: () => {
      return {
        projects: [],
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
    .filter {
      font-size: 10px;
      color: var(--v-Cinder-base);
      label {
        font-size: 10px;
        color: var(--v-Cinder-base);
      }
      .v-input {
        height: 26px;
        .v-input__control {
          height: 26px;
          .v-input__slot {
            min-height: 26px !important;
            .v-select__slot {
              min-height: 26px !important;
              height: 26px;
              .v-select__selections {
                display: flex;
                align-items: center;
                min-height: 26px !important;
                height: 26px;
                padding: 0;
                input {
                  height: 0px !important;
                  display: none;
                }
                min-width: 100px;
              }
              .v-input__append-inner {
                margin-top: 0px;
                align-self: center;
              }
            }
          }
        }
      }
      .v-input--selection-controls {
        margin-top: 0;
        padding-top: 0;
      }
      button {
        height: 24px;
      }
      
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
