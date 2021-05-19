<template>
  <modal :openModal="openModal">
    <template v-slot:title>Add Project</template>
    <template v-slot:content>
      * Project Name
      <v-text-field
        v-model="projectName"
        outlined
        required
        :error-messages="projectNameErrors"
        @input="$v.projectName.$touch()"
        @blur="$v.projectName.$touch()"
      ></v-text-field>

      * Project Leader
      <v-select
        v-model="projectLeaders"
        required
        dense
        chips
        multiple
        attach
        outlined
        :items="items"
        :error-messages="projectLeaderErrors"
        @change="$v.projectLeaders.$touch()"
        @blur="$v.projectLeaders.$touch()"
      >
        <template v-slot:selection="{ item }">
          <v-chip small class="ma-1" color="HummingBird">
            <span>{{ item }}</span>
          </v-chip>
        </template>
      </v-select>

      Project Crew(org,)
      <v-select :items="items" dense chips multiple attach outlined>
        <template v-slot:selection="{ item }">
          <v-chip small class="ma-1" color="HummingBird">
            <span>{{ item }}</span>
          </v-chip>
        </template>
      </v-select>

      Cross-org. Crew
      <!-- <v-text-field outlined></v-text-field> -->
      <v-combobox persistent-hint small-chips multiple outlined dense></v-combobox>
      Client Owner
      <v-text-field outlined></v-text-field>
      Client Contact
      <v-text-field outlined></v-text-field>
      Project Desc
      <v-text-field outlined></v-text-field>
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
      projectName: { required },
      projectLeaders: { required },
    },
    props: ["openModal"],
    data: () => {
      return {
        projectName: null,
        projectLeaders: [],
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
      projectNameErrors() {
        const errors = [];
        if (!this.$v.projectName.$dirty) return errors;
        !this.$v.projectName.required &&
          errors.push("Project Name is required.");
        return errors;
      },
      projectLeaderErrors() {
        const errors = [];
        if (!this.$v.projectLeaders.$dirty) return errors;
        !this.$v.projectLeaders.required &&
          errors.push("Project Leader is required");
        return errors;
      },
    },
    components: {
      modal: Modal,
    },
    methods: {
      submit() {
        this.$v.$touch();
        console.log(this.projectLeaderErrors);
        if (
          this.projectNameErrors.length !== 0 ||
          this.projectLeaderErrors.length !== 0
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
        this.projectName = null;
        this.projectLeaders = [];
      },
    },
  };
</script>
