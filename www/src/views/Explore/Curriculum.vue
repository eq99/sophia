<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="12">
        <v-sheet min-height="70vh" rounded="lg">
          <h1>计算机</h1>
          <ol>
            <li><a href="/curriculum/Basic">计算机基础 </a></li>
            <li><a href="/curriculum/Basic"> 机器学习 </a></li>
            <li><a href="/curriculum/Basic">计算机基础 </a></li>
          </ol>
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
