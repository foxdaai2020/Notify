<template>
  <div>
    <title-bar>Member Auth.</title-bar>
    <div class="d-flex align-center table-action">
      <v-btn class="mr-2" outlined color="Genoa" small>
        <v-icon left>
          mdi-download
        </v-icon>
        Template</v-btn
      >
      <v-btn class="mr-2" outlined color="Genoa" small @click="action()">
        <v-icon left>
          mdi-upload
        </v-icon>
        Ｕsers</v-btn
      >
      <v-btn
        class="mr-2"
        outlined
        color="Genoa"
        small
        @click="openAddManagementOneUserModal = true"
      >
        <v-icon left>
          mdi-plus-circle-outline
        </v-icon>
        User</v-btn
      >
      <v-btn
        class="mr-2"
        outlined
        color="Genoa"
        small
        @click="openEditOrganizationModal = true"
      >
        <v-icon left>
          mdi-square-edit-outline
        </v-icon>
        Org.</v-btn
      >
      <v-spacer></v-spacer>
      <span class="mr-2 search-text">篩選</span>
      <v-text-field
        v-model="search"
        single-line
        hide-details
        outlined
        style="max-width:150px"
      ></v-text-field>
    </div>
    <v-data-table :headers="headers" :items="managementData" :search="search">
      <template v-slot:item.edit>
        <v-icon small @click="openUpdateUserInfoModal = true">
          mdi-square-edit-outline
        </v-icon>
      </template>
      <template v-slot:item.resetpassword>
        <v-icon small @click="openResetPasswordModal = true">
          mdi-lock-reset
        </v-icon>
      </template>
    </v-data-table>
    <registration-dialog
      :openRegistrationDialog="openRegistrationDialog"
      @closeRegistrationDialog="openRegistrationDialog = false"
    ></registration-dialog>
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
    <reset-password-modal
      :openModal="openResetPasswordModal"
      @closeModal="openResetPasswordModal = false"
    ></reset-password-modal>
    <!-- <alert-dialog
      :openDialog="openConfirmDeleteDialog"
      @closeDialog="openConfirmDeleteDialog = false"
    >
      <template slot="content">Delete Service successfully.</template>
      <template slot="action">
        <v-btn
          depressed
          color="FountainBlue White--text"
          @click="openConfirmDeleteDialog = false"
          >確定</v-btn
        >
      </template>
    </alert-dialog> -->
    <!-- <alert-register-one-user-dialog
      :openDialog="openRegisterOneUserDialog"
      @closeDialog="openRegisterOneUserDialog = false"
    >
      <template slot="content">Register one user successfully.</template>
      <template slot="action">
        <v-btn
          depressed
          color="FountainBlue White--text"
          @click="openRegisterOneUserDialog = false"
          >確定</v-btn
        >
      </template>
    </alert-register-one-user-dialog> -->
  </div>
</template>

<script>
  import TitleBar from "../components/TitleBar";
  import AddManagementOneUserModal from "../components/modals/AddManagementOneUser";
  import EditOrganizationModal from "../components/modals/EditOrganization";
  import UpdateUserInfoModal from "../components/modals/UpdateUserInfo.vue";
  import ResetPasswordModal from "../components/modals/ResetPassword.vue";
  import RegistrationDialog from "../components/dialogs/RegistrationDialog.vue";
  export default {
    data: () => {
      return {
        openAddManagementOneUserModal: false,
        openEditOrganizationModal: false,
        openUpdateUserInfoModal: false,
        openResetPasswordModal: false,
        openRegistrationDialog: false,
        openRegisterOneUserDialog: false,
        search: "",
        headers: [
          { text: "User Name", align: "center", value: "userName" },
          { text: "Nickname", align: "center", value: "nickName" },
          { text: "Org.", align: "center", value: "org" },
          { text: "Role", align: "center", value: "role" },
          { text: "Project Leader", align: "center", value: "projectLeader" },
          { text: "Default Ch.", align: "center", value: "defaultCh" },
          {
            text: "Registration Time.",
            align: "center",
            value: "registrationTime",
          },
          { text: "Activate", align: "center", value: "activate" },
          { text: "Edit", align: "center", value: "edit", filterable: false },
          {
            text: "Reset Password",
            align: "center",
            value: "resetpassword",
            filterable: false,
          },
        ],
        managementData: [
          {
            userName: "AT0123",
            nickName: "Superman",
            org: "DAAI",
            role: "manager",
            projectLeader: "AI-project",
            defaultCh: "AOI-ch",
            registrationTime: "2021-05-01",
            activate: "v",
            edit: "edit",
            resetPassword: "resetpassword",
          },
        ],
      };
    },
    components: {
      "title-bar": TitleBar,
      "add-management-one-user-modal": AddManagementOneUserModal,
      "edit-organization-modal": EditOrganizationModal,
      "update-user-info-modal": UpdateUserInfoModal,
      "reset-password-modal": ResetPasswordModal,
      "registration-dialog": RegistrationDialog,
    },
    methods: {
      action() {
        this.openRegistrationDialog = true;
      },
      closeRegistrationDialog() {
        this.openRegistrationDialog = false;
      },
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
