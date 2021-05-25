<template>
  <v-navigation-drawer
    width="300px"
    v-model="openModal"
    :permanent="openModal"
    right
    temporary
    class="d-flex modal"
    fixed
  >
    <v-card color="PattensBlue" class="d-flex flex-column" style="flex: 1">
      <v-card-title><slot name="title"></slot></v-card-title>
      <v-divider></v-divider>
      <v-card-text class="d-flex flex-column" style="flex: 1">
        <slot name="content"></slot>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <slot name="actions"></slot>
      </v-card-actions>
    </v-card>
  </v-navigation-drawer>
</template>

<script>
  export default {
    props: ["openModal"],
  };
</script>

<style lang="scss">
  .modal {
    .v-navigation-drawer__content {
      display: flex;
      .v-card__text {
        overflow: scroll;
        background: var(--v-PattensBlue);
        .v-input {
          background: var(--v-PattensBlue);
          .v-input__slot {
            margin-bottom: 0 !important;
            background: #ffffff;
            min-height: 30px !important;
            input {
              height: 30px;
              font-size: 12px;
            }

            fieldset {
              border: 1px solid !important;
            }
          }
          .v-text-field__details {
            margin-bottom: 0;
          }
          flex: 0;
          .v-select__slot {
            min-height: 32px;
            .v-select__selections {
              padding: 0px;
              font-size: 12px;
              min-height: 30px;
              .v-select__selection--comma {
                margin: 0px 4px 3px 0px;
              }
              input {
                height: 12px;
              }
            }
            .v-input__append-inner {
              margin-top: 0px;
              align-self: center;
            }

            .v-text-field--outlined.v-input--is-focused fieldset,
            .v-text-field--outlined.v-input--has-state fieldset {
              border: 5px solid currentColor;
            }
          }

          [role="combobox"] {
            .v-input__append-inner {
              display: none;
            }
          }

          &.v-input--is-disabled {
            .v-input__slot { 
              background: #F4F4F4;
            }
          }
        }
      }
    }
  }

  .modal-span-title {
    color: #696969;
    font-size: 13px;
  }

  .modal-button-group {
    margin-right: 8px;
    margin-bottom: 8px;
  }
  .modal-selection.v-input--selection-controls {
    .v-input__slot {
      background: #e9f4f6!important;
      .v-icon {
        font-size: 16px;
      }
      label {
        color: #212529;
        font-size: 12px;
      }
    }
  }
</style>
