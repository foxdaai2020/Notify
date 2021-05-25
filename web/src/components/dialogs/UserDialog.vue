<template>
  <v-dialog
    v-model="openUserDialog"
    persistent
    width="350px"
  >

    <v-card height="560px">
      <v-toolbar>
          <v-icon color="DarkRed" class="mr-2">mdi-comment-account</v-icon>
          <v-toolbar-title style="font-size: 16px; color: #696969;">User Setting</v-toolbar-title>
          <span style="position: absolute; height: 0px; left: 0px; right: 0px; top: 54px; border: 0.5px solid #F4F4F4;"></span>
        <v-spacer></v-spacer>
          <v-btn
            color="transparent"
            @click="closeDialog"
            depressed
            :ripple="false"
            style="min-width:20px;padding:0px;"
          >
            <v-icon color="DarkGray" style="font-size: 20px">mdi-close</v-icon>
          </v-btn>
        <template v-slot:extension>
          <v-tabs
            v-model="tab"
            class="custom-tab-space"
            style="margin:2px;"
            flat
            depressed
          >
            <!-- <v-tabs-slider color="pink"></v-tabs-slider> -->
            <v-tab
              v-for="item in items"
              :key="item"
              style="padding:15px;"
            >
              {{ item }}
            </v-tab>
          </v-tabs>
        </template>
      </v-toolbar>

    <v-tabs-items v-model="tab" class="card-outline">
      <v-tab-item>
        <v-card flat>
          <v-card-text>

            <span class="tab-userinfo-title">User ID</span>
            <v-text-field
              filled
              outlined
              disabled
              value="John Doe"
              hide-details
              class="mb-2"
            ></v-text-field>
            <span class="tab-userinfo-title">User Key</span>
            <v-text-field
              filled
              outlined
              disabled
              value="John Doe"
              hide-details
              class="mb-2"
            ></v-text-field>
            <span class="tab-userinfo-title">User Name</span>
            <v-text-field
              filled
              outlined
              disabled
              value="John Doe"
              hide-details
              class="mb-2"
            ></v-text-field>
            <span class="tab-userinfo-title">Nickname</span>
            <v-text-field
              filled
              outlined
              disabled
              value="John Doe"
              hide-details
              class="mb-2"
            ></v-text-field>
            <span class="tab-userinfo-title">E-mail</span>
            <v-text-field
              filled
              outlined
              disabled
              value="John Doe"
              hide-details
              class="mb-2"
            ></v-text-field>
            <span class="tab-userinfo-title">Role</span>
            <v-text-field
              filled
              outlined
              disabled
              value="John Doe"
              hide-details
              class="mb-2"
            ></v-text-field>

          </v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card class="reset-forms">
          <v-card-text>

            <span>Old Password</span>
            <v-text-field
            outlined
            required
            :append-icon="valueOldPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="() => (valueOldPassword = !valueOldPassword)"
            :type="valueOldPassword ? 'password' : 'text'"
            class="eye-peek"
            ></v-text-field>
            <span>New Password</span>
            <v-text-field
            outlined
            required
            :append-icon="valueNewPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="() => (valueNewPassword = !valueNewPassword)"
            :type="valueNewPassword ? 'password' : 'text'"
            class="eye-peek"
            ></v-text-field>
            <span>Confirm Password</span>
            <v-text-field
            outlined
            required
            :append-icon="valueConfirmPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="() => (valueConfirmPassword = !valueConfirmPassword)"
            :type="valueConfirmPassword ? 'password' : 'text'"
            class="eye-peek"
            ></v-text-field>

          </v-card-text>
        </v-card>

        <!-- <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="closeDialog"
          >
            I accept
          </v-btn>
        </v-card-actions> -->
        <v-card-actions class="user-setting-reset-btns">
          <v-btn depressed @click="closeDialog" color="DarkGray White--text"
            >取消</v-btn
          >
          <v-btn depressed @click="closeDialog" color="FountainBlue White--text"
            >確定</v-btn
          >
        </v-card-actions>

      </v-tab-item>
    </v-tabs-items>

    </v-card>

  </v-dialog>
</template>

<script>
  export default {
    props: ["openUserDialog"],
    data () {
      return {
        //resetmountes: false,
        valueOldPassword: String,
        valueNewPassword: String,
        valueConfirmPassword: String,
        tab: null,
        items: [
          'User Information', 'Reset Password',
        ],
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
          //openUserDialog: false,
      }
    },
    methods: {
      closeDialog() {
        this.$emit("closeUserDialog");
      },
    },
    // mounted() {
    //   this.resetmountes = true;
    // }
  }
</script>

<style>
.v-slide-group__prev {
  display: none !important;
}

.card-outline {
  top: 10px;
  width: 313px;
  height: 408px;
  margin: auto;
  border: 1px solid Lightgray;
}

.custom-tab-space {
  padding: 0px;
  padding-top: 10px;
}

.custom-tab-space .v-tab--active {
  border: 1px solid Lightgray;
  border-radius: 4px 4px 0 0;
}

.custom-tab-space .v-tab--active:hover {
  border: 1px solid Lightgray;
  border-radius: 4px 4px 0 0;
}

.custom-tab-space .v-tab:before {
  border-radius: 4px 4px 0 0;
}

.v-btn:before {
  opacity: 0 !important;
}

.v-ripple__container {
  opacity: 0 !important;
}

/* .v-text-field__details {
  margin: 0px !important;
  padding: 0px !important;
} */

.tab-userinfo-title {
  font-size: 14px;
}

.reset-forms {
  height: 340px;
}

.user-setting-reset-btns {
  margin-left: 150px;
}

.eye-peek .v-input__append-inner {
  margin-top: 4px !important;
}
</style>