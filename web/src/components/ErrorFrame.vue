<template>
  <div class="error-bg-color">
    <div class="error-contnet-position">
      <h1 class="mb-10" style="color: #696969">
        <slot name="title">
        <!-- 404 Not Found -->
        </slot>
      </h1>
      <div>
        <slot name="content">
          <!-- <h3 class="mb-10" style="color: #212529">The URL you requested was not found.</h3>
          <v-btn outlined color="Genoa" class="error-btn-bgcolor" medium @click="backHome()">
            <router-link to="/">
              <v-icon left>
                mdi-logout-variant
              </v-icon>
              Back to Home Page
            </router-link></v-btn
          > -->
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