<template>
  <div class="error-bg-color">
    <div class="error-contnet-position">
      <h1 class="mb-10" style="color: #696969">
        <slot name="title">
        </slot>
      </h1>
      <div>
        <h3 class="mb-10" style="color: #212529">
          <slot name="content">
          </slot>
        </h3>
      </div>
      <div>
        <slot name="back-home-button">
          <v-btn outlined color="Genoa" class="error-btn-bgcolor" medium @click="backHome()">
          <v-icon left>
            mdi-logout-variant
          </v-icon>
            Back to Home Page
          </v-btn>
        </slot>
      </div>
    </div>
  </div>
</template>

<style>
.error-bg-color {
  height: 100%;
  background-color: #e9f4f6 !important;
}
.error-contnet-position {
  position: absolute;
  top: 50px;
  left: 50px;
}
.error-btn-bgcolor {
  background-color: white;
}
</style>

<script>
  export default {
    methods: {
      backHome() {
        this.$router.push('/');
      }
    }
  }
</script>