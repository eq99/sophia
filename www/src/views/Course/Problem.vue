<template>
  <v-card :loading="loading" class="mx-auto my-0" max-width="720">
    <!-- <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template> -->

    <v-card-title> {{ problem.title }} </v-card-title>

    <v-card-text>
      <v-row align="center" class="mx-0">
        <div class="mr-4">作者：{{ problem.author }}</div>
        <div>评分：</div>
        <v-rating
          :value="problem.rates"
          color="amber"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>

        <div class="grey--text">{{ problem.rates }}</div>
      </v-row>
      <v-row>
        <v-chip-group
          v-model="selection"
          active-class="deep-purple accent-2 white--text"
          column
          v-for="(tag, i) in problem.tags"
          :key="i"
        >
          <v-chip>{{ tag }} </v-chip>
        </v-chip-group>
      </v-row>
      <v-divider class="mx-4"></v-divider>
      <div>
        {{ problem.description }}
      </div>
    </v-card-text>

    <v-card-actions>
      <v-btn color="deep-purple lighten-2" text @click="reserve"> 回答 </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    problem: {
      title: "非常难的问题",
      description: "这是已给法拉法肯计划安抚安抚",
      author: "千森",
      rates: 5.0,
      tags: ["ha好啊", "淮安抗癌"],
    },
  }),
};
</script>
