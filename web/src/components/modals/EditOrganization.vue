<template>
  <modal :openModal="openModal">
    <template v-slot:title>Organization</template>
    <template v-slot:content>

    <!-- <v-container
      class="px-0"
      fluid
    >
      <v-radio-group v-model="radioGroup">
          <v-radio label="Radio 1" value="radio-1" v-model="x">
          </v-radio>
          <div v-show="x == 'radio-1'">hi</div>
          <v-radio label="Radio 2" value="radio-2" v-model="x">
          </v-radio>
          <div v-show="x == 'radio-2'">hello</div>
      </v-radio-group>
    </v-container> -->

  <input type="radio" v-model="x" value="radio-1">number1
  <div v-show="x == 'radio-1'">hi</div>
  <input type="radio" v-model="x" value="radio-2">numbwe2
  <div v-show="x == 'radio-2'">hello</div>


    </template>
    <template v-slot:actions>
      <v-btn depressed @click="closeDialog" color="DarkGray White--text"
        >取消</v-btn
      >
      <v-btn depressed @click="submit" color="FountainBlue White--text"
        >確定</v-btn
      >
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
        radioGroup: 1,
        x: 'radio-1',
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
      organizationErrors() {
        const errors = [];
        if (!this.$v.organization.$dirty) return errors;
        !this.$v.organization.required &&
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