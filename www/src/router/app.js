export default [
  {
    path: "/",
    name: "Home",
    component: () => import("@/views/Home.vue"),
  },
  {
    path:"/login",
    component: () =>import("@/views/User/Login.vue")
  },
];
