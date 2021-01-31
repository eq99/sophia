<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="12">
        <v-sheet min-height="70vh" rounded="lg">
          <Markdown :url="computedReadmeURL" />
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Markdown from "@/components/Markdown";

export default {
  name: "Introduction",
  components: {
    Markdown,
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
