export default [
  {
    path: "/curriculum/",
    component: () => import("@/views/Explore/Curriculum"),
  },
  {
    path: "/curriculum/:roadmap",
    component: () => import("@/views/Explore/Roadmap"),
  },
];
