<template>
  <modal :openModal="openModal">
    <template v-slot:title>Add Channel</template>
    <template v-slot:content>
      <span class="modal-span-title">* Channel Name</span>
      <v-text-field
        v-model="channelName"
        outlined
        required
        :error-messages="channelNameErrors"
        @input="$v.channelName.$touch()"
        @blur="$v.channelName.$touch()"
      ></v-text-field>

      <span class="modal-span-title">Channel Description</span>
      <v-text-field outlined></v-text-field>

      <span class="modal-span-title">* Member@Org.</span>
      <v-select
        v-model="members"
        required
        dense
        chips
        multiple
        attach
        outlined
        :items="items"
        :error-messages="memberErrors"
        @change="$v.members.$touch()"
        @blur="$v.members.$touch()"
      >
        <template v-slot:selection="{ item }">
          <v-chip small class="ma-1" color="HummingBird">
            <span>{{ item }}</span>
          </v-chip>
        </template>
      </v-select>

      <span class="modal-span-title">Add by User Name (e.g. @Cross-Org.)</span>
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
      channelName: { required },
      members: { required },
    },
    props: ["openModal"],
    data: () => {
      return {
        search: null,
        channelName: null,
        members: [],
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
    components: {
      modal: Modal,
    },
    computed: {
      channelNameErrors() {
        const errors = [];
        if (!this.$v.channelName.$dirty) return errors;
        !this.$v.channelName.required &&
          errors.push("Channel Name is required.");
        return errors;
      },
      memberErrors() {
        const errors = [];
        if (!this.$v.members.$dirty) return errors;
        !this.$v.members.required && errors.push("Member is required");
        return errors;
      },
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
          this.channelNameErrors.length !== 0 ||
          this.memberErrors.length !== 0
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
        this.channelName = null;
        this.members = [];
      },
      remove(item) {
        this.chips.splice(this.chips.indexOf(item), 1);
        this.chips = [...this.chips];
      },
    },
  };
</script>
