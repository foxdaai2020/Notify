<template>
  <div class="bg-color">
    <div class="notfound-contnet-position">
      <h1 class="mb-10" style="color: #696969">404 Not Found</h1>
      <h3 class="mb-10" style="color: #212529">The URL you requested was not found.</h3>
      <v-btn outlined color="Genoa" class="notfound-btn-bgcolor" medium @click="backHome()">
        <router-link to="/">
          <v-icon left>
            mdi-logout-variant
          </v-icon>
          Back to Home Page
        </router-link></v-btn
      >
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    backHome() {
      this.$emit("closeModal");
    }
  }
}
</script>

<style scoped>
.bg-color {
  height: 100%;
  background-color: #e9f4f6 !important;
}
.notfound-contnet-position {
  position: absolute;
  top: 50px;
  left: 50px;
}
.notfound-btn-bgcolor {
  background-color: white;
}
</style>