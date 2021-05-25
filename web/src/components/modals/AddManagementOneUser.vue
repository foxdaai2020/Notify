<template>
  <div>
    <modal :openModal="openModal">
      <template v-slot:title>Registration:One User</template>
      <template v-slot:content>

        <span class="modal-span-title">* Organization</span>
        <v-select
          v-model="organization"
          required
          dense
          attach
          outlined
          :items="OrganizationItems"
          :error-messages="organizationErrors"
          @change="$v.organization.$touch()"
          @blur="$v.organization.$touch()"
        >
        </v-select>

        <span class="modal-span-title">* Role</span>
        <v-select
          v-model="role"
          required
          dense
          attach
          outlined
          :items="RoleItems"
          :error-messages="roleErrors"
          @change="$v.role.$touch()"
          @blur="$v.role.$touch()"
        >
        </v-select>

        <span class="modal-span-title">* User Name</span>
        <v-text-field
          v-model="userName"
          outlined
          required
          :error-messages="userNameErrors"
          @input="$v.userName.$touch()"
          @blur="$v.userName.$touch()"
        ></v-text-field>

        <span class="modal-span-title">* Email</span>
        <v-text-field
          v-model="email"
          outlined
          required
          :error-messages="emailErrors"
          @input="$v.email.$touch()"
          @blur="$v.email.$touch()"
        ></v-text-field>

        <span class="modal-span-title">* Password</span>
        <v-text-field
          v-model="password"
          outlined
          required
          :error-messages="passwordErrors"
          @input="$v.password.$touch()"
          @blur="$v.password.$touch()"
        ></v-text-field>

        <span class="modal-span-title">Projects</span>
        <v-select
          v-model="projects"
          dense
          chips
          multiple
          attach
          outlined
          :items="items"
        >
          <template v-slot:selection="{ item }">
            <v-chip small class="ma-1" color="HummingBird">
              <span>{{ item }}</span>
            </v-chip>
          </template>
        </v-select>

        <span class="modal-span-title">Channels</span>
        <v-select
          v-model="channels"
          dense
          chips
          multiple
          attach
          outlined
          :items="items"
        >
          <template v-slot:selection="{ item }">
            <v-chip small class="ma-1" color="HummingBird">
              <span>{{ item }}</span>
            </v-chip>
          </template>
        </v-select>

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

    <alert-register-one-user-dialog
      :openDialog="openRegisterOneUserDialog"
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
    </alert-register-one-user-dialog>
  </div>
</template>
<script>
  import { validationMixin } from "vuelidate";
  import { required } from "vuelidate/lib/validators";
  import Modal from "./Modal";
  import AlertDialog from "@/components/dialogs/AlertDialog";
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
        search: null,
        organization: null,
        role: null,
        userName: null,
        email: null,
        password: null,
        projects: null,
        channels: null,
        openRegisterOneUserDialog: false,
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
      organizationErrors() {
        const errors = [];
        if (!this.$v.organization.$dirty) return errors;
        !this.$v.organization.required &&
          errors.push("Organizations is required");
        return errors;
      },
      roleErrors() {
        const errors = [];
        if (!this.$v.role.$dirty) return errors;
        !this.$v.role.required &&
          errors.push("Role is required");
        return errors;
      },
      userNameErrors() {
        const errors = [];
        if (!this.$v.userName.$dirty) return errors;
        !this.$v.userName.required &&
          errors.push("User Name is required.");
        return errors;
      },
      emailErrors() {
        const errors = [];
        if (!this.$v.email.$dirty) return errors;
        !this.$v.email.required &&
          errors.push("Email is required.");
        return errors;
      },
      passwordErrors() {
        const errors = [];
        if (!this.$v.password.$dirty) return errors;
        !this.$v.password.required &&
          errors.push("Password is required.");
        return errors;
      },
    },
    components: {
      modal: Modal,
      "alert-register-one-user-dialog": AlertDialog,
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
        console.log('hi')
        this.$emit("closeModal");
        this.openRegisterOneUserDialog = true
        //this.openDialog();
      },
      // openDialog() {
      //   console.log('hey')
      //   this.openRegisterOneUserDialog = true
      // },
      closeDialog() {
        this.clear();
        this.$emit("closeModal");
        this.openRegisterOneUserDialog = false
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