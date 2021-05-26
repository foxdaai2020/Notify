<template>
  <v-dialog
    v-model="openRegistrationDialog"
    persistent
    width="350px"
  >

    <v-card height="560px">
      <v-toolbar>
          <v-icon color="DarkRed" class="mr-2">mdi-comment-account</v-icon>
          <v-toolbar-title style="font-size: 16px; color: #696969;">Registration: Users</v-toolbar-title>
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
          <v-btn
            outlined
            color="FountainBlue White--text"
            class="mb-2"
            >Download Failed Users</v-btn
          >

          <div style="position:absolute; top:50px; height: 380px; overflow: scroll;">
            <table>
              <thead>
                <tr>
                  <th>user name</th>
                  <th >result</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>user01</td>
                  <td>email failed</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>org. change</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>email failed</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>org. change</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>email failed</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>org. change</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>email failed</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>org. change</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>email failed</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>org. change</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>email failed</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>org. change</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>email failed</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>org. change</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>email failed</td>
                </tr>
                <tr>
                  <td>user01</td>
                  <td>org. change</td>
                </tr>
              </tbody>
            </table>
          </div>

        </template>
      </v-toolbar>

        <v-card-actions class="reset-btns">
          <v-btn depressed @click="closeDialog" color="DarkGray White--text"
            >取消</v-btn
          >
          <v-btn depressed @click="closeDialog" color="FountainBlue White--text"
            >確定</v-btn
          >
        </v-card-actions>


    </v-card>

  </v-dialog>
</template>

<script>
  export default {
    props: ["openRegistrationDialog"],
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
        text: 'Lorerud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      }
    },
    methods: {
      closeDialog() {
        this.$emit("closeRegistrationDialog");
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

.reset-btns {
  margin-top: 380px;
  margin-left: 176px;
}

.eye-peek .v-input__append-inner {
  margin-top: 4px !important;
}

table, th, td {
  border: 1px solid Lightgray;
}

table {
  border-collapse: collapse;
  width: 316px;
  text-align: center;
}

</style>