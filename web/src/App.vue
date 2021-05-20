<template>
  <v-app>
    <router-view />
  </v-app>
</template>

<script>
  export default {
    name: "App",

    data: () => ({
      //
    }),
  };
</script>

<style>
  * {
    font-family: "Microsoft JhengHei" !important;
  }

  a {
    text-decoration: none;
  }

  .v-btn {
    letter-spacing: 0px !important;
    font-family: "Microsoft JhengHei";
    text-transform: none !important;
  }

  .v-card {
    font-family: "Microsoft JhengHei";
  }

  .v-dialog {
    border-radius: 10px !important;
  }

  .v-tab {
  text-transform: none !important;
  }

  .v-sheet {
    box-shadow: none !important;
  }

  .v-toolbar{
    box-shadow: none !important;
  }

  .v-input {
    font-size: 12px !important;
  }
</style>
