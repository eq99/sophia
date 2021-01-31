<template>
  <v-card>
    <v-toolbar color="cyan" dark flat>
      <v-toolbar-title>概率论</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="blue lighten-1 ml-3">
        <v-icon color="red">mdi-heart</v-icon>
        <span>打赏</span>
      </v-btn>
      <v-btn color="blue lighten-1 ml-3">
        <v-icon color="yellow">mdi-star</v-icon>
        <span>1234</span>
      </v-btn>
    </v-toolbar>
    <v-container>
      <v-btn><router-link :to="convertLink('')">简介</router-link></v-btn>
      <v-btn><router-link :to="convertLink('contents')">目录</router-link></v-btn>
      <v-btn><router-link :to="convertLink('discuss')">讨论</router-link></v-btn>
      <v-btn><router-link :to="convertLink('exercise')">练习</router-link></v-btn>
      <v-btn><router-link :to="convertLink('manage')">管理</router-link></v-btn>
    </v-container>
    <router-view></router-view>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      tab: null, // tab control
    };
  },
  computed: {
    convertLink() {
      return (link) => `/course/${this.$route.params.courseid}/${link}`;
    },
  },
};
</script>
