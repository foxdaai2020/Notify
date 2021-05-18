<template>
  <div>
    <v-navigation-drawer app disable-resize-watcher color="gradient" permanent>
      <template v-slot:prepend>
        <v-list-item-title>
          <p class="project-title">Notify Service</p>
        </v-list-item-title>
          <p class="project-user">admin
            <v-icon dense>mdi-account-circle</v-icon>
          </p>
      </template>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
          v-for="(item, index) of routers"
          :key="index"
          link
          :to="item.route"
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
  </div>
</template>

<script>
  export default {
    data: () => {
      return {
        routers: [
          { text: "Project", route: "project" },
          { text: "Channel", route: "channel" },
          { text: "Service", route: "service" },
          { text: "Management", route: "management" },
        ],
      };
    },
  };
</script>

<style scoped>
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
  font-size: 21px;
  padding: 24px 24px 6px 24px;
}

.project-user {
  font-size: 14px;
  padding-left: 24px;
}

.notify-item-title {
  font-size: 16px !important;
  padding: 8px 0 8px 28px;
  z-index: 2;
}

.v-application--is-ltr .v-list.v-sheet .v-list-item, .v-application--is-ltr .v-list.v-sheet .v-list-item::before, .v-application--is-ltr .v-list.v-sheet .v-list-item > .v-ripple__container {
  border-bottom-left-radius: 32px !important;
  border-top-left-radius: 32px !important;
}

.v-list-item--link:before {
  margin-left: 16px;
  background-color: white;
}

.theme--light.v-list-item:hover::before {
  opacity: 0.24;
}

.theme--light.v-list-item:focus::before {
  opacity: 0.62;
}

.theme--light.v-list-item--active:hover::before, .theme--light.v-list-item--active::before {
  opacity: 1;
}

.theme--light.v-list-item--active:focus::before {
  opacity: 1;
}

.theme--light.v-list-item.v-list-item--highlighted::before {
  opacity: 1;
}

.v-list-item:active {
  margin-left: 16px;
  background-color: white;
}
</style>
