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
            background: #ffffff !important;
            min-height: 32px !important;
            input {
              height: 32px;
              font-size: 12px;
            }
          }
          .v-text-field__details {
            margin-bottom: 0;
          }
          flex: 0;

          .v-select__slot {
            min-height: 32px;
            .v-select__selections {
              font-size: 12px;
              min-height: 32px;
              input {
                height: 24px;
              }
            }
            .v-input__append-inner {
              margin-top: 0px;
              align-self: center;
            }
          }

          [role="combobox"] {
            .v-input__append-inner {
              display: none;
            }
          }
         }
      }
    }
  }
</style>
