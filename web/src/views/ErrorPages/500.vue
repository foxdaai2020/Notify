<template>
  <error-frame>
    <template v-slot:title>
      500 Error
    </template>
    <template v-slot:content>
      <h3 class="mb-10" style="color: #212529">Internal Server Error</h3>
      <v-btn outlined color="Genoa" class="error-btn-bgcolor" medium @click="backHome()">
      <v-icon left>
        mdi-logout-variant
      </v-icon>
        Back to Home Page
      </v-btn>
    </template>
  </error-frame>
</template>

<script>
  import ErrorFrame from "@/components/ErrorFrame";

  export default {
    components: {
      "error-frame": ErrorFrame,
    },
    methods: {
      backHome() {
        this.$router.push('/');
      }
    }
  }
</script>