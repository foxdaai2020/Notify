import Vue from "vue";
import VueRouter from "vue-router";
import MainLayout from "./layouts/MainLayout";
import Login from "./views/Login";
import Project from "./views/Project";
import Channel from "./views/Channel";
import Service from "./views/Service";
import Management from "./views/Management";

Vue.use(VueRouter);

const routes = [
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/",
    name: "main-layout",
    component: MainLayout,
    children: [
      { path: "/", component: Project, alias: "/project" },
      { path: "/channel", component: Channel },
      { path: "/service", component: Service },
      { path: "/management", component: Management },
    ],
  },
  {
    path: '/404',
    alias: '*',
    name: 'notFound',
    component: () => import(/* webpackChunkName: "notFound" */ '@/views/404.vue')
  }
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
