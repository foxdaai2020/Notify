import Vue from "vue";
import Vuex from "vuex";

import faceMask from "./modules/faceMask";

Vue.use(Vuex);

/**
 * CreateStore - Function to create store.
 *
 * @returns {Object}  Description.
 */
export function createStore() {
  return new Vuex.Store({
    modules: {
      faceMask,
    },
  });
}
