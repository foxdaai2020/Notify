<template>
  <error-frame>
    <template v-slot:title>
      404 Not Found
    </template>
    <template v-slot:content>
      <h3 class="mb-10" style="color: #212529">The URL you requested was not found.</h3>
      <v-btn outlined color="Genoa" class="error-btn-bgcolor" medium @click="backHome()">
        <router-link to="/">
          <v-icon left>
            mdi-logout-variant
          </v-icon>
          Back to Home Page
        </router-link></v-btn
      >
    </template>
  </error-frame>
</template>

<script>
  import ErrorFrame from "../components/ErrorFrame";

  export default {
    components: {
      "error-frame": ErrorFrame,
    },
    methods: {
      backHome() {
        this.$emit("backHome");
      }
    }
  }
</script>