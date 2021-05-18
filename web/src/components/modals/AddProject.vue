<template>
  <modal :openModal="openModal">
    <template v-slot:title>Add Project</template>
    <template v-slot:content>
      <v-text-field
        v-model="name"
        outlined
        label="* Project Name"
        required
        :error-messages="nameErrors"
        @input="$v.name.$touch()"
        @blur="$v.name.$touch()"
      ></v-text-field>
      <v-select
        dense
        chips
        multiple
        attach
        outlined
        :items="items"
        label="* Project Leader"
      >
        <template v-slot:selection="{ item }">
          <v-chip small class="ma-1" color="HummingBird">
            <span>{{ item }}</span>
          </v-chip>
        </template>
      </v-select>
      <v-select
        :items="items"
        dense
        chips
        multiple
        attach
        outlined
        label="Project Crew(org,)"
      >
        <template v-slot:selection="{ item }">
          <v-chip small class="ma-1" color="HummingBird">
            <span>{{ item }}</span>
          </v-chip>
        </template>
      </v-select>
      <v-text-field outlined label="Cross-org. Crew"></v-text-field>
      <v-text-field outlined label="Client Owner"></v-text-field>
      <v-text-field outlined label="Client Contact"></v-text-field>
      <v-text-field outlined label="Project Desc"></v-text-field>
    </template>
    <template v-slot:actions>
      <v-btn depressed @click="closeDialog">取消</v-btn>
      <v-btn depressed @click="submit" color="FountainBlue White--text">確定</v-btn>
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
      name: { required },
    },
    props: ["openModal"],
    data: () => {
      return {
        name: null,
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
      nameErrors() {
        const errors = [];
        if (!this.$v.name.$dirty) return errors;
        !this.$v.name.required && errors.push("Name is required.");
        return errors;
      },
    },
    components: {
      modal: Modal,
    },
    methods: {
      submit() {
        this.$v.$touch();
      },
      closeDialog() {
        this.clear();
        this.$emit("closeModal");
      },
      clear() {
        this.$v.$reset();
        this.name = null;
      },
    },
  };
</script>
