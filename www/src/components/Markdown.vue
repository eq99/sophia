<template>
  <article v-html="md2html" v-hljs></article>
</template>

<script>
import markdownIt from "markdown-it";
import hljsPlug from "@/plugins/highlight";
import hljs from "highlight.js";
import Vue from "vue";

Vue.directive("hljs", function (el) {
  let blocks = el.querySelectorAll("pre code");
  blocks.forEach((block) => {
    hljs.highlightBlock(block);
  });
});

let md = markdownIt({
  html: true,
  langPrefix: "language-", // CSS language prefix for fenced blocks. Can be
  // useful for external highlighters.
  linkify: false,
}).use(hljsPlug);

export default {
  name: "Markdown",
  props: {
    url: String,
  },
  data: () => ({
    markRaw: "# loading...",
  }),
  computed: {
    md2html() {
      return md.render(this.markRaw);
    },
  },
  mounted() {
    this.axios
      .get(this.url)
      .then((res) => {
        this.markRaw = res.data;
      })
      .catch((err) => console.log(err));
  },
};
</script>
