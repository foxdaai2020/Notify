<template>
<div class="login">
  <div class="login-content" :style="{'background-image': 'url(' + require('@/assets/login-page.png') + ')'}">
    <div class="login-dialog">
      <p class="login-title">Notify Service</p>
      <p class="login-info">請輸入帳號資訊</p>
      <div class="login-input">
        <v-text-field
          outlined
          label="User Name"
          hide-details="auto"
          :style="{'min-height': '20px'}"
          class="mb-6"
        ></v-text-field>
        <v-text-field
          outlined
          label="Password"
          hide-details="auto"
          :style="{'min-height': '20px'}"
          class="mb-6"
        >
        </v-text-field>
      </div>
      <v-btn
        color="FountainBlue White--text"
        width="186px"
        height="38px"
        depressed
      >登入</v-btn>
    </div>
  </div>
</div>
</template>

<style lang="scss">
html, body {
  overflow-y: hidden;
}

.login {
  font-family: "Microsoft JhengHei";
  width: 100%;
  height: 100%;
}

.login-content {
  width: 100%;
  height: 100%;
  background-size: cover;
}

.login-dialog {
  position: absolute;
  top: 135px;
  left: 160px;
  width: 258px;
  height: 332px;
  background-color: WhiteSmoke;
  border-radius: 15px;
  text-align: center;
}

.login-title {
  font-size: 27px;
  font-weight:bold;
  margin-top: 30px;
}

.login-info {
  font-size: 14px;
  text-align: left;
  margin-left: 38px;
  padding-bottom: 6px;
}

.login-input {
  margin: auto;
  width: 186px;
  .v-text-field--outlined .v-label {
    top: unset;
  }
  .v-text-field {
    background: var(--v-White-base);
    .v-input__control .v-input__slot {
      min-height: 40px;
    }
  } 
}

</style>