import Vue from "vue";
import VueRouter from "vue-router";
import CourseRouter from "./course";
import AppRouter from "./app";
import UserRouter from "./user";
import ExploreRouter from "./explore";

Vue.use(VueRouter);

const routes = [...AppRouter, ...CourseRouter, ...UserRouter, ...ExploreRouter];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
