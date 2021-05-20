<template>
  <modal :openModal="openModal">
    <template v-slot:title>Edit Project</template>
    <template v-slot:content>
      <span>* Project Name</span>
      <v-text-field
        v-model="projectName"
        outlined
        required
        :error-messages="projectNameErrors"
        @input="$v.projectName.$touch()"
        @blur="$v.projectName.$touch()"
      ></v-text-field>

      <span>* Project Leader</span>
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

      <span>Project Crew(org,)</span>
      <v-select :items="items" dense chips multiple attach outlined>
        <template v-slot:selection="{ item }">
          <v-chip small class="ma-1" color="HummingBird">
            <span>{{ item }}</span>
          </v-chip>
        </template>
      </v-select>

      <span>Cross-org. Crew</span>
      <v-combobox
        v-model="chips"
        outlined
        multiple
        dense
        :search-input.sync="search"
        @keydown.enter="validUserName(search)"
        @blur="validUserName(search)"
      >
        <template v-slot:selection="{ attrs, item, selected }">
          <v-chip
            color="HummingBird"
            class="mt-1 mb-1"
            small
            :key="JSON.stringify(item)"
            v-bind="attrs"
            :input-value="selected"
            close
            @click:close="remove(item)"
          >
            {{ item }}
          </v-chip>
        </template>
      </v-combobox>

      <span>Client Owner</span>
      <v-text-field outlined></v-text-field>

      <span>Client Contact</span>
      <v-text-field outlined></v-text-field>

      <span>Project Desc</span>
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
        search: null,
        projectName: null,
        projectLeaders: [],
        chips: [],
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
      validUserName(search) {
        if (search === "234") {
          this.search = "";
        }
      },
      submit() {
        this.$v.$touch();
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
      remove(item) {
        this.chips.splice(this.chips.indexOf(item), 1);
        this.chips = [...this.chips];
      },
    },
  };
</script>
