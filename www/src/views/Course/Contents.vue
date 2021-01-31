<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="10">
        <v-sheet min-height="70vh" rounded="lg">
          <v-list dense>
            <v-list-item
              v-for="(content, i) in contents"
              :key="i"
              :href="prefixLink(content.path)"
            >
              <v-list-item-icon>
                <v-icon v-text="i"></v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title v-text="content.name"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "ChapterList",
  data: () => ({
    selectedItem: 1,
    contents: [],
  }),
  computed: {
    prefixLink() {
      return (link) => `/course/${this.$route.params.courseid}/article/${link}`;
    },
  },
  mounted() {
    let url = `/api/repos/${this.$route.params.courseid}/contents/`;
    this.axios
      .get(url)
      .then((res) => {
        const mdReg = /(\.md$)/;
        this.contents = res.data.filter(
          (item) => mdReg.test(item.path) && item.type === "file"
        );
      })
      .catch((err) => console.log(err));
  },
};
</script>
