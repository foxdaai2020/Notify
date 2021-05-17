import Vue from "vue";
import App from "./App.vue";
import router from './router.js';
import { createStore } from './store';
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false;
const store = createStore();


new Vue({
  store,
  router,
  vuetify,
  render: (h) => h(App)
}).$mount("#app");
