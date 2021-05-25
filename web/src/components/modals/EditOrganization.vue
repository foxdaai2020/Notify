<template>
  <modal :openModal="openModal">
    <template v-slot:title>Organization</template>
    <template v-slot:content>

      <v-radio-group
        class="mt-0 radiogroup small-radio"
        v-model="radioGroup"
        style="background: #E9F4F6"
      >
        <v-radio class="radio-title" label="Add Organization" value="radio-1" style="background:#E9F4F6">
        </v-radio>
        <div class="pb-3" v-show="radioGroup == 'radio-1'" style="background: #E9F4F6">
          <span class="modal-span-title">* New Organization Name</span>
          <v-text-field
            v-model="addNewOrganizationName"
            outlined
            required
            :error-messages="addNewOrganizationNameErrors"
          ></v-text-field>
          <span class="modal-span-title">Description</span>
          <v-text-field
            v-model="addDescription"
            outlined
            required
            :error-messages="addDescriptionErrors"
          ></v-text-field>
        </div>

        <v-radio class="radio-title" label="Edit Description" value="radio-2" style="background: #E9F4F6">
        </v-radio>
        <div class="pb-3" v-show="radioGroup == 'radio-2'" style="background: #E9F4F6">
          <span class="modal-span-title">* Select Organization</span>
          <v-select
            v-model="editSelectOrganization"
            required
            dense
            attach
            outlined
            :items="EditSelectOrganizationItems"
            :error-messages="editSelectOrganizationErrors"
            @change="$v.editSelectOrganization.$touch()"
            @blur="$v.editSelectOrganization.$touch()"
          >
          </v-select>
          <span class="modal-span-title">* New Organization Name</span>
          <v-text-field
            v-model="editNewOrganizationName"
            outlined
            required
            :error-messages="editNewOrganizationNameErrors"
          ></v-text-field>
          <span class="modal-span-title">Description</span>
          <v-text-field
            v-model="editDescription"
            outlined
            required
            :error-messages="editDescriptionErrors"
          ></v-text-field>
        </div>

        <v-radio class="radio-title" label="Delete Organization" value="radio-3" style="background: #E9F4F6">
        </v-radio>
        <div class="pb-3" v-show="radioGroup == 'radio-3'" style="background: #E9F4F6">
          <span class="modal-span-title">* Select Organization</span>
          <v-select
            v-model="deleteSelectOrganization"
            required
            dense
            attach
            outlined
            :items="DeleteSelectOrganizationItems"
            :error-messages="deleteSelectOrganizationErrors"
            @change="$v.deleteSelectOrganization.$touch()"
            @blur="$v.deleteSelectOrganization.$touch()"
          >
          </v-select>
        </div>
      </v-radio-group>

    </template>
    <template v-slot:actions>
      <div class="modal-button-group">
        <v-btn depressed @click="closeDialog" color="DarkGray White--text" class="mr-2"
          >取消</v-btn
        >
        <v-btn depressed @click="submit" color="FountainBlue White--text"
          >確定</v-btn
        >
      </div>
    </template>
  </modal>
</template>
<script>
  import { validationMixin } from "vuelidate";
  import { required } from "vuelidate/lib/validators";

  import Modal from "./Modal";
  export default {
    mixins: [validationMixin],
    validations: {
      editSelectOrganization: { required },
      deleteSelectOrganization: { required },
      role: { required },
      userName: { required },
      email: { required },
      password: { required },
    },
    props: ["openModal"],
    data: () => {
      return {
        radioGroup: 1,
        search: null,
        editSelectOrganization: null,
        deleteSelectOrganization: null,
        role: null,
        userName: null,
        addNewOrganizationName: null,
        addDescription: null,
        editNewOrganizationName: null,
        editDescription: null,
        projects: null,
        channels: null,
        chips: [],
        EditSelectOrganizationItems: ["org1", "org2", "org3"],
        DeleteSelectOrganizationItems: ["org1", "org2", "org3"],
        RoleItems: ["manager", "crew"],
        items: [
          "小廢物",
          "中廢物",
          "大廢物",
          "超級廢物",
          "臭廢物",
          "死廢物",
          "完全廢物",
          "究極廢物",
        ],
      };
    },
    computed: {
      addNewOrganizationNameErrors() {
        console.log("addNewOrganizationNameErrors")
        return [];
      },
      addDescriptionErrors() {
        console.log("addDescriptionErrors")
        return [];
      },
      editSelectOrganizationErrors() {
        const errors = [];
        if (!this.$v.editSelectOrganization.$dirty) return errors;
        !this.$v.editSelectOrganization.required &&
          errors.push("Organizations is required");
        return errors;
      },
      editNewOrganizationNameErrors() {
        console.log("editNewOrganizationNameErrors")
        return [];
      },
      editDescriptionErrors() {
        console.log("editDescriptionErrors")
        return [];
      },
      deleteSelectOrganizationErrors() {
        const errors = [];
        if (!this.$v.deleteSelectOrganization.$dirty) return errors;
        !this.$v.deleteSelectOrganization.required &&
          errors.push("Organizations is required");
        return errors;
      },
    },
    components: {
      modal: Modal,
    },
    methods: {
      validUserName(search) {
        if (search === "234") {
          this.search = "";
        }
      },
      submit() {
        this.$v.$touch();
        if (
          this.userNameErrors.length !== 0
        )
          return;
        this.clear();
        this.$emit("closeModal");
      },
      closeDialog() {
        this.clear();
        this.$emit("closeModal");
      },
      clear() {
        this.$v.$reset();
        this.userName = null;
        this.editSelectOrganizations = [];
        this.deleteSelectOrganizations = [];
        this.roles = [];
      },
      remove(item) {
        this.chips.splice(this.chips.indexOf(item), 1);
        this.chips = [...this.chips];
      },
    },
  };
</script>

<style>
/* .modal .v-navigation-drawer__content .v-card__text .v-input .v-input__slot {
  background: #E9F4F6 !important;
} */
/* .radiogroup .v-input--radio-group--column .v-radio:not(:last-child):not(:only-child) {
  padding-bottom: 8px;
  margin-bottom: 0px !important;
} */
.v-input--radio-group--column .v-radio:not(:last-child):not(:only-child) {
  padding-bottom: 8px !important;
  margin-bottom: 0px !important;
}

.radio-title .v-label {
  font-size: 14px !important;
}

.small-radio label {
  font-size: 14px;
  padding-left: 0px;
  margin-left: -4px;
}

.small-radio .v-icon {
  font-size: 14px !important;
}

.v-input--selection-controls__ripple {
  display: none;
}

</style>