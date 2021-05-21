<template>
  <div>
    <title-bar>Member Auth.</title-bar>
    <div class="d-flex align-center ma-2">
      <v-btn class="mr-2" outlined color="Genoa" small>
        <v-icon left>
          mdi-download
        </v-icon>
        Template</v-btn
      >
      <v-btn class="mr-2" outlined color="Genoa" small>
        <v-icon left>
          mdi-upload
        </v-icon>
        Ｕsers</v-btn
      >
      <v-btn class="mr-2" outlined color="Genoa" small @click="openAddManagementOneUserModal = true">
        <v-icon left>
          mdi-plus-circle-outline
        </v-icon>
        User</v-btn
      >
      <v-btn class="mr-2" outlined color="Genoa" small @click="openEditOrganizationModal = true">
        <v-icon left>
          mdi-square-edit-outline
        </v-icon>
        Org.</v-btn
      >
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        label="Search"
        single-line
        hide-details
        outlined
        style="max-width:150px"
      ></v-text-field>
    </div>
    <v-data-table
      :headers="headers"
      :items="desserts"
      :search="search"
    ></v-data-table>
    <add-management-one-user-modal
      :openModal="openAddManagementOneUserModal"
      @closeModal="openAddManagementOneUserModal = false"
    ></add-management-one-user-modal>
    <edit-organization-modal
      :openModal="openEditOrganizationModal"
      @closeModal="openEditOrganizationModal = false"
    ></edit-organization-modal>
    <update-user-info-modal
      :openModal="openUpdateUserInfoModal"
      @closeModal="openUpdateUserInfoModal = false"
    ></update-user-info-modal>
  </div>
</template>

<script>
  import TitleBar from "../components/TitleBar";
  import AddManagementOneUserModal from "../components/modals/AddManagementOneUser";
  import EditOrganizationModal from "../components/modals/EditOrganization";
  import UpdateUserInfoModal from '../components/modals/UpdateUserInfo.vue';
  export default {
    data: () => {
      return {
        openAddManagementOneUserModal: false,
        openEditOrganizationModal: false,
        openUpdateUserInfoModal: false,
        search: "",
        headers: [
          {
            text: "Dessert (100g serving)",
            align: "start",
            value: "name",
          },
          { text: "Calories", filterable: false, value: "calories" },
          { text: "Fat (g)", value: "fat" },
          { text: "Carbs (g)", value: "carbs" },
          { text: "Protein (g)", value: "protein" },
          { text: "Iron (%)", value: "iron" },
        ],
        desserts: [
          {
            name: "Frozen Yogurt",
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: "1%",
          },
          {
            name: "Ice cream sandwich",
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: "1%",
          },
          {
            name: "Eclair",
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: "7%",
          },
          {
            name: "Cupcake",
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: "8%",
          },
          {
            name: "Gingerbread",
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: "16%",
          },
          {
            name: "Jelly bean",
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: "0%",
          },
          {
            name: "Lollipop",
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: "2%",
          },
          {
            name: "Honeycomb",
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: "45%",
          },
          {
            name: "Donut",
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: "22%",
          },
          {
            name: "KitKat",
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: "6%",
          },
        ],
      };
    },
    components: {
      "title-bar": TitleBar,
      "add-management-one-user-modal": AddManagementOneUserModal,
      "edit-organization-modal": EditOrganizationModal,
      "update-user-info-modal": UpdateUserInfoModal,
    },
  };
</script>

<style lang="scss">
  .v-text-field.v-text-field--outlined {
    .v-label {
      top: unset;
    }

    background: var(--v-White-base);
    .v-input__control .v-input__slot {
      min-height: 20px;
    }
  }
</style>