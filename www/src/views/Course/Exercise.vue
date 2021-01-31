<template>
  <v-container>
    <v-list two-line dense>
      <router-link to="/course/exercise/id" v-for="(problem, i) in problems" :key="i">
        <v-list-item>
          <v-list-item-icon>
            <v-iocn v-text="problem.score"></v-iocn>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ problem.title }} </v-list-item-title>
            <v-list-item-subtitle>{{ problem.answers }} 回答 </v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action>
            <v-icon v-text="problem.status"> </v-icon>
          </v-list-item-action>
        </v-list-item>
      </router-link>
    </v-list>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    problems: [
      { title: "多维随机变量求解", answers: 5, score: 10, status: "mdi-star" },
      { title: "多维随机变量求解", answers: 5, score: 10, status: "mdi-check" },
      { title: "多维随机变量求解", answers: 5, score: 10, status: "mdi-clock" },
    ],
  }),
};
</script>
