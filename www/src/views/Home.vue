<template>
  <v-container>
    <h1>主页</h1>
    <a href="/curriculum">课程中心</a>
    <a href="/login">注册登录</a>

    <section>
      <h1>我的课程</h1>
      <ul>
        <li><a href="/courese/gaoshu">高等数学</a></li>
        <li><a href="/courese/gaoshu">高等数学</a></li>
        <li><a href="/courese/gaoshu">高等数学</a></li>
        <li><a href="/courese/gaoshu">高等数学</a></li>
      </ul>
    </section>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    linkTocCourse: "",
    repos: [],
  }),
  computed: {
    convertLink() {
      return (link) => `course/${link}`;
    },
  },
  mounted() {
    this.axios
      .get("/api/repos/")
      .then((res) => {
        this.repos = res.data;
      })
      .catch((err) => console.log(err));
  },
};
</script>

<style lang="css" scoped>
a {
  text-decoration: none;
}
</style>
