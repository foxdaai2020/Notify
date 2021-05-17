<template>
  <div>
    <v-navigation-drawer app disable-resize-watcher color="HummingBird">
      <template v-slot:prepend>
        <v-list-item two-line>
          <v-list-item-avatar>
            <img src="https://randomuser.me/api/portraits/women/81.jpg" />
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>Jane Smith</v-list-item-title>
            <v-list-item-subtitle>Logged In</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>

      <v-divider></v-divider>

      <v-list dense shaped>
        <v-list-item
          v-for="(item, index) of routers"
          :key="index"
          link
          :to="item.route"
        >
          <v-list-item-content>
            <v-list-item-title>{{ item.text }}</v-list-item-title>
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
          { text: "Management", route: "management" },
          { text: "Service", route: "service" },
        ],
      };
    },
  };
</script>
