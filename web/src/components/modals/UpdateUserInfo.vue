<template>
  <modal :openModal="openModal">
    <template v-slot:title>Update User</template>
    <template v-slot:content>
    <div v-if="isShow">
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

      <span class="modal-span-title">User ID</span>
      <v-text-field
        filled
        outlined
        disabled
        value="John Doe"
        hide-details
        class="mb-2"
      ></v-text-field>

      <span class="modal-span-title">User Key</span>
      <v-text-field
        filled
        outlined
        disabled
        value="John Doe"
        hide-details
        class="mb-2"
      ></v-text-field>

      <span class="modal-span-title">User Name</span>
      <v-text-field
        filled
        outlined
        disabled
        value="John Doe"
        hide-details
        class="mb-2"
      ></v-text-field>

      <span class="modal-span-title">E-mail</span>
      <v-text-field
        filled
        outlined
        disabled
        value="John Doe"
        hide-details
        class="mb-2"
      ></v-text-field>

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

      <span class="modal-span-title">* Activate</span>
      <v-select
        v-model="activate"
        required
        dense
        attach
        outlined
        :items="ActivateItems"
        :error-messages="activateErrors"
        @change="$v.activate.$touch()"
        @blur="$v.activate.$touch()"
      >
      </v-select>
    </div>

    <div v-else>
      <div class="short-input">
        <span class="modal-span-title">User Name</span>
        <v-text-field
          filled
          outlined
          disabled
          value="John"
          hide-details
          class="mb-2"
        ></v-text-field>

        <span class="modal-span-title">Role</span>
        <v-text-field
          filled
          outlined
          disabled
          value="John"
          hide-details
          class="mb-2"
        ></v-text-field>

        <span class="modal-span-title">Activate</span>
        <v-text-field
          filled
          outlined
          disabled
          value="John"
          hide-details
          class="mb-2"
        ></v-text-field>
      </div>

      <span class="modal-span-title">Project Leader</span>
      <v-icon>mdi-information</v-icon>
      <v-btn x-small>
        Show All
      </v-btn>
      <v-divider></v-divider>
      <span>Project1</span>
      <v-btn x-small>
        D
      </v-btn>
      <v-btn x-small>
        L
      </v-btn>
      <v-select
        v-model="project1"
        required
        dense
        attach
        outlined
        :items="Project1Items"
        @change="$v.project1.$touch()"
        @blur="$v.project1.$touch()"
      >
      </v-select>
      <span class="modal-span-title">Project2</span>
      <v-btn x-small>
        D
      </v-btn>
      <v-btn x-small>
        L
      </v-btn>
      <v-select
        v-model="project2"
        required
        dense
        attach
        outlined
        :items="Project2Items"
        @change="$v.project2.$touch()"
        @blur="$v.project2.$touch()"
      >
      </v-select>

      <span class="modal-span-title">Default Channels</span>
      <v-icon>mdi-information</v-icon>
      <v-btn x-small>
        Show All
      </v-btn>
      <v-divider></v-divider>
      <span class="modal-span-title">Channel1</span>
      <v-btn x-small>
        D
      </v-btn>
      <v-btn x-small>
        L
      </v-btn>
      <v-select
        v-model="channel1"
        required
        dense
        attach
        outlined
        :items="Channel1Items"
        @change="$v.channel1.$touch()"
        @blur="$v.channel1.$touch()"
      >
      </v-select>
      <span class="modal-span-title">Channel2</span>
      <v-btn x-small>
        D
      </v-btn>
      <v-btn x-small>
        L
      </v-btn>
      <v-select
        v-model="channel2"
        required
        dense
        attach
        outlined
        :items="Channel2Items"
        @change="$v.channel2.$touch()"
        @blur="$v.channel2.$touch()"
      >
      </v-select>

    </div>
    </template>
    <template v-slot:actions>
      <div v-if="isShow" class="modal-button-group">
        <v-btn depressed @click="closeDialog" color="DarkGray White--text" class="mr-2"
          >取消</v-btn
        >
        <v-btn depressed @click="nextDialog" color="FountainBlue White--text"
          >下一步</v-btn
        >
      </div>
      <div v-else class="modal-button-group">
        <v-btn depressed @click="previousDialog" color="DarkGray White--text" class="mr-2"
          >返回</v-btn
        >
        <v-btn depressed @click="closeDialog" color="FountainBlue White--text"
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
      activate: { required },
    },
    props: ["openModal"],
    data: () => {
      return {
        isShow: true,
        organization: null,
        role: null,
        activate: null,
        project1: null,
        project2: null,
        channel1: null,
        channel2: null,
        OrganizationItems: ["org1", "org2", "org3"],
        RoleItems: ["manager", "crew"],
        ActivateItems: ["true", "false"],
        Project1Items: ["project1","project2"],
        Project2Items: ["project1","project2"],
        Channel1Items: ["channel1","channel2"],
        Channel2Items: ["channel1","channel2"],
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
      activateErrors() {
        const errors = [];
        if (!this.$v.activate.$dirty) return errors;
        !this.$v.activate.required && errors.push("Name is required.");
        return errors;
      },
    },
    components: {
      modal: Modal,
    },
    methods: {
      submit() {
        this.$v.$touch();
        if (
          this.activateErrors.length !== 0 ||
          this.organizationErrors.length !== 0 ||
          this.roleErrors.length !== 0
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
        this.name = null;
      },
      nextDialog() {
        this.isShow = false;
      },
      previousDialog() {
        this.isShow = true;
      }
    },
  };
</script>
<style scoped>
.short-input {
  width: 30px !important;
  display: inline;
}
</style>