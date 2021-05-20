<template>
  <modal :openModal="openModal">
    <template v-slot:title>Add Service</template>
    <template v-slot:content>
      <span>* Project</span>
      <v-select
        v-model="project"
        required
        dense
        attach
        outlined
        :items="items"
        :error-messages="projectErrors"
        @change="$v.project.$touch()"
        @blur="$v.project.$touch()"
      >
      </v-select>

      <span>Tag</span>
      <v-select
        v-model="tags"
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

      <span>Service ID</span>
      <v-text-field outlined></v-text-field>

      <span>* Owner</span>
      <v-text-field outlined disabled></v-text-field>

      <span>* Enabled (Deafult: True)</span>
      <v-select
        v-model="enabled"
        required
        dense
        attach
        outlined
        :items="booleanItems"
        :error-messages="enabledErrors"
        @change="$v.enabled.$touch()"
        @blur="$v.enabled.$touch()"
      >
      </v-select>

      <span>* Issue tracker (Default: False)</span>
      <v-select
        v-model="issueTracker"
        required
        dense
        attach
        outlined
        :items="booleanItems"
        :error-messages="issueTrackerErrors"
        @change="$v.issueTracker.$touch()"
        @blur="$v.issueTracker.$touch()"
      >
      </v-select>

      <span>Service Description</span>
      <v-text-field outlined></v-text-field>

      <span>* Service type</span>
      <v-select
        v-model="serviceType"
        required
        dense
        attach
        outlined
        :items="ServiceTypeItems"
        :error-messages="serviceTypeErrors"
        @change="$v.serviceType.$touch()"
        @blur="$v.serviceType.$touch()"
      >
      </v-select>

      <span>Interval start time</span>
      <datetime-picker style="margin-bottom:14px;"></datetime-picker>

      <span>Interval second</span>
      <v-text-field outlined></v-text-field>
      <span>Message body</span>
      <v-text-field outlined></v-text-field>
      <span>* Channels</span>
      <v-select
        v-model="channels"
        required
        dense
        chips
        multiple
        attach
        outlined
        :items="items"
        :error-messages="channelErrors"
        @change="$v.channels.$touch()"
        @blur="$v.channels.$touch()"
      >
        <template v-slot:selection="{ item }">
          <v-chip small class="ma-1" color="HummingBird">
            <span>{{ item }}</span>
          </v-chip>
        </template>
      </v-select>

      <v-btn>Generate your notify-request sample</v-btn>
      <v-btn>Generate your reg-request sample</v-btn>
    </template>
    <template v-slot:actions>
      <v-btn @click="closeDialog"></v-btn>
      <v-btn @click="closeDialog"></v-btn>
    </template>
  </modal>
</template>
<script>
  import { validationMixin } from "vuelidate";
  import { required } from "vuelidate/lib/validators";

  import DateTimePicker from "../DateTimePicker";
  import Modal from "./Modal";
  export default {
    mixins: [validationMixin],
    validations: {
      project: { required },
      enabled: { required },
      issueTracker: { required },
      serviceType: { required },
      channels: { required },
    },
    data: () => {
      return {
        project: null,
        tags: [],
        enabled: true,
        issueTracker: false,
        serviceDescription: null,
        intervalStartTime: null,
        intervalSecond: null,
        messageBody: null,
        serviceType: null,
        channels: [],
        booleanItems: [true, false],
        ServiceTypeItems: ["delay forward", "dead notice", "direct forward"],
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
    props: ["openModal"],
    computed: {
      projectErrors() {
        const errors = [];
        if (!this.$v.project.$dirty) return errors;
        !this.$v.project.required && errors.push("Project is required.");
        return errors;
      },
      enabledErrors() {
        const errors = [];
        if (!this.$v.enabled.$dirty) return errors;
        !this.$v.enabled.required && errors.push("Enabled is required");
        return errors;
      },
      issueTrackerErrors() {
        const errors = [];
        if (!this.$v.issueTracker.$dirty) return errors;
        !this.$v.issueTracker.required &&
          errors.push("Issue Tracker is required");
        return errors;
      },
      serviceTypeErrors() {
        const errors = [];
        if (!this.$v.serviceType.$dirty) return errors;
        !this.$v.serviceType.required &&
          errors.push("Service Type is required");
        return errors;
      },
      channelErrors() {
        const errors = [];
        if (!this.$v.channels.$dirty) return errors;
        !this.$v.channels.required && errors.push("Channel is required");
        return errors;
      },
    },
    components: {
      modal: Modal,
      "datetime-picker": DateTimePicker,
    },
    methods: {
      closeDialog() {
        this.$emit("closeModal");
      },
    },
  };
</script>
