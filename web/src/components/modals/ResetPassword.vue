<template>
  <modal :openModal="openModal" @closeModal="closeDialog()">
    <template v-slot:title>Reset Password</template>
    <template v-slot:content>

      <span class="modal-span-title">* New Password</span>
      <v-text-field
        outlined
        required
        :append-icon="valueNewPassword ? 'mdi-eye' : 'mdi-eye-off'"
        @click:append="() => (valueNewPassword = !valueNewPassword)"
        :type="valueNewPassword ? 'password' : 'text'"
        class="eye-peek"
      ></v-text-field>

      <span class="modal-span-title">* Confirm Password</span>
      <v-text-field
        outlined
        required
        :append-icon="valueConfirmPassword ? 'mdi-eye' : 'mdi-eye-off'"
        @click:append="() => (valueConfirmPassword = !valueConfirmPassword)"
        :type="valueConfirmPassword ? 'password' : 'text'"
        class="eye-peek"      ></v-text-field>
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
      organization: { required },
      role: { required },
      userName: { required },
      email: { required },
      password: { required },
    },
    props: ["openModal"],
    data: () => {
      return {
        valueNewPassword: String,
        valueConfirmPassword: String,
        search: null,
        organization: null,
        role: null,
        userName: null,
        email: null,
        password: null,
        projects: null,
        channels: null,
        chips: [],
        OrganizationItems: ["org1", "org2", "org3"],
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
          this.userNameErrors.length !== 0 ||
          this.organizationErrors.length !== 0 ||
          this.roleErrors.length !== 0 ||
          this.emailErrors.length != 0 ||
          this.passwordErrors.length != 0
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
        this.organizations = [];
        this.roles = [];
      },
      remove(item) {
        this.chips.splice(this.chips.indexOf(item), 1);
        this.chips = [...this.chips];
      },
    },
  };
</script>