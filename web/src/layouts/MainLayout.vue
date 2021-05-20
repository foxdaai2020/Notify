<template>
  <div>
    <v-navigation-drawer app disable-resize-watcher color="gradient" permanent>
      <template v-slot:prepend>
        <v-list-item-title>
          <p class="project-title">Notify Service</p>
        </v-list-item-title>

        <div class="project-user">
          <v-menu offset-y style="width: 160px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="transparent"
                v-bind="attrs"
                v-on="on"
                small
                depressed
                :ripple="false"
              >
                <p>admin
                  <v-icon dense>mdi-account-circle</v-icon>
                  <v-icon small>mdi-chevron-down</v-icon>
                </p>
              </v-btn>

            </template>
            <v-list>
              <v-list-item
                v-for="(item, index) in items"
                :key="index"
                @click="action(item.title)"
              >
                <v-list-item-title>
                  <v-icon dense :color="item.color" style="padding-right:6px;">{{ item.icon }}</v-icon>
                  {{ item.title }}
                </v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </div>
      </template>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
          v-for="(item, index) of routers"
          :key="index"
          link
          :to="item.route"
          :ripple="false"
        >
          <v-list-item-content>
            <v-list-item-title class="notify-item-title">{{ item.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <v-container fluid>
        <router-view />
      </v-container>
    </v-main>
    <user-dialog
    :openUserDialog="openUserDialog"
    @closeUserDialog="openUserDialog = false"
    ></user-dialog>
  </div>
</template>

<script>
  import UserDialog from "../components/dialogs/UserDialog";
  export default {
    data: () => {
      return {
        openUserDialog: false,
        items: [
          { title: "admin", icon: "mdi-account", color: "Genoa" },
          { title: "User Setting", icon: "mdi-cog-outline", color: "ChelseaCucumber" },
          { title: "Log Out", icon: "mdi-logout-variant", color: "DarkRed" },
        ],
        routers: [
          { text: "Project", route: "project" },
          { text: "Channel", route: "channel" },
          { text: "Service", route: "service" },
          { text: "Management", route: "management" },
        ],
      };
    },
    components: {
      "user-dialog": UserDialog,
    },
    methods: {
      action(title) {
        if (title == "User Setting") {
          console.log('user')
          this.openUserDialog = true
        } else if(title == "Log Out") {
          this.$router.push({ path: '/login' })
        }
      },
      closeUserDialog() {
        this.openUserDialog = false
      }
    }
  };
</script>

<style scoped lang="scss">
.v-navigation-drawer {
  width: 180px !important;
}

.v-application .gradient{
  background: linear-gradient(180deg, #BCE6D7 0%, rgba(255, 255, 255, 0) 100%), #3DBEBE !important;
}

.v-main {
  padding: 0 0 0 180px !important;
}

.project-title {
  font-weight: 400;
  font-size: 21px;
  padding: 24px 24px 6px 24px;
}

.project-user {
  padding-left: 16px;
  font-size: 14px;
  width: 160px;
}

.notify-item-title {
  font-size: 16px !important;
  padding: 8px 0 8px 24px;
  z-index: 2;
  font-weight: 400 !important;
}

.v-list-item--link:before {
  margin-left: 16px;
  background-color: white;
}

// .v-application--is-ltr .v-list.v-sheet .v-list-item, .v-application--is-ltr .v-list.v-sheet .v-list-item::before, .v-application--is-ltr .v-list.v-sheet .v-list-item > .v-ripple__container {
//   border-bottom-left-radius: 32px !important;
//   border-top-left-radius: 32px !important;
// }

// .theme--light.v-list-item:focus::before {
//   opacity: 0.62;
// }

// .theme--light.v-list-item--active:hover::before,
// .theme--light.v-list-item--active::before {
//   opacity: 1;
// }

.v-btn:before {
  opacity: 0 !important;
}

.v-ripple__container {
  opacity: 0 !important;
}

.v-application--is-ltr .v-list.v-sheet .v-list-item {
  &:before {
    border-bottom-left-radius: 32px !important;
    border-top-left-radius: 32px !important;
  }
  .v-ripple__container {
    border-bottom-left-radius: 32px !important;
    border-top-left-radius: 32px !important;
  }
}

.theme--light.v-list-item:focus::before {
  opacity: 0.62;
}

.theme--light.v-list-item--active {
  &:before {
    opacity: 1;
  }
  &:hover {
    &:before {
      opacity: 1;
    }
  }
}
</style>
