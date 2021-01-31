<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="12">
        <v-sheet min-height="70vh" rounded="lg">
          <section>
            <h1><a href="/courese/de">线性代数</a></h1>
            <p>在这面课程里面，你讲学习很多知识，例如矩阵，行列式。</p>
          </section>
          <section>
            <h1><a href="/courese/de">高等数学</a></h1>
            <p>
              你将在高等数学这门课里面学到极限，微分，导数，不定积分，定积分，特殊函数积分。
            </p>
          </section>
          <section>
            <h1><a href="/courese/de">离散数学</a></h1>
            <p>你将在《离散数学》这门课学习集合关系，逻辑分析，图论等知识。</p>
          </section>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import Markdown from "@/components/Markdown";

export default {
  name: "Introduction",
  components: {
    // Markdown,
  },
  data: () => ({
    readmeURL: "",
  }),
  computed: {
    computedReadmeURL() {
      let branch = branch || "master";
      return `/api/repos/${this.$route.params.courseid}/raw/${branch}/${this.$route.params.articleid}`;
    },
  },
};
</script>
