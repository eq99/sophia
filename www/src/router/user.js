export default [
  {
    path: "/account/:userid",
    component: () => import("@/views/User/User.vue"),
    children:[
      {
      path:"/",
      component: () =>import("@/views/User/Account.vue")
    },
    {
      path:"assets",
      component: () =>import("@/views/User/Assets.vue")
    }
  ]
  },
];
