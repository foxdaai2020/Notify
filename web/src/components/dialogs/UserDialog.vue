<template>
  <v-dialog
    v-model="openUserDialog"
    persistent
    width="350px"
  >

    <v-card height="500px">
      <v-toolbar>
          <v-icon color="DarkRed" class="mr-2">mdi-comment-account</v-icon>
          <v-toolbar-title style="font-size: 16px; color: #696969;">User Setting</v-toolbar-title>
          <span style="position: absolute; height: 0px; left: 0px; right: 0px; top: 53px; border: 0.5px solid #D3D3D3;"></span>
        <!-- <v-spacer></v-spacer> -->
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
            <p>
              Sed mollis, eros et ultrices tempus, mauris ipsum aliquam libero, non adipiscing dolor urna a orci. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Nunc sed turpis.
            </p>

            <p class="mb-0">
              Donec venenatis vulputate lorem. Aenean viverra rhoncus pede. In dui magna, posuere eget, vestibulum et, tempor auctor, justo. Fusce commodo aliquam arcu. Suspendisse enim turpis, dictum sed, iaculis a, condimentum nec, nisi.
            </p>
          </v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-text>
            <p>
              Fusce a quam. Phasellus nec sem in justo pellentesque facilisis. Nam eget dui. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In dui magna, posuere eget, vestibulum et, tempor auctor, justo.
            </p>

            <p class="mb-0">
              Cras sagittis. Phasellus nec sem in justo pellentesque facilisis. Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nam at tortor in tellus interdum sagittis.
            </p>
          </v-card-text>
        </v-card>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="closeDialog"
          >
            I accept
          </v-btn>
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
    }
  }
</script>

<style>
.v-slide-group__prev {
  display: none !important;
}

.card-outline {
  top: 10px;
  width: 313px;
  height: 368px;
  margin: auto;
  border: 1px solid Lightgray;
}

.custom-tab-space {
  padding: 0px;
  padding-top: 10px;
}

.v-tab--active {
  border: 1px solid Lightgray;
  border-radius: 4px 4px 0 0;
}

.v-tab--active:hover {
  border: 1px solid Lightgray;
  border-radius: 4px 4px 0 0;
}

.v-tab:before {
  border-radius: 4px 4px 0 0;
}

</style>