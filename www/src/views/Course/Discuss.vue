<template>
  <v-container>
    <v-toolbar color="green" dark dense>
      <v-text-field hide-details prepend-icon="mdi-magnify" single-line></v-text-field>
      <v-spacer></v-spacer>
      <!-- sort -->
      <v-select
        v-model="e1"
        :items="sortBy"
        menu-props="auto"
        label="Select"
        hide-details
        prepend-icon="mdi-sort"
        single-line
      ></v-select>
      <!-- sort -->

      <v-btn
        :loading="loading3"
        :disabled="loading3"
        color="blue-grey"
        class="ma-2 white--text"
        @click="loader = 'loading3'"
      >
        <v-icon left dark>mdi-pencil</v-icon>
        添加
      </v-btn>
    </v-toolbar>

    <v-list subheader two-line>
      <router-link to="/course/discuss/id">
        <v-list-item class="item" v-for="(topic, i) in topics" :key="i" color="green">
          <v-list-item-content>
            <v-list-item-title>{{ topic.title }}</v-list-item-title>
            <v-list-item-subtitle
              >{{ topic.time }} by {{ topic.author }}
            </v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action>
            <v-badge
              bordered
              :content="topic.replyNums"
              :value="topic.replyNums"
              color="green"
              overlap
            >
              <v-icon large> mdi-message </v-icon>
            </v-badge>
          </v-list-item-action>
        </v-list-item>
      </router-link>
    </v-list>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    sortBy: ["最近更新", "最多评论"],
    topics: [
      { title: "概率论为审美这么难？", replyNums: 5, time: "2020-30-23", author: "马云" },
      { title: "概率论为审美这么难？", replyNums: 5, time: "2020-30-23", author: "马云" },
    ],
  }),
};
</script>

<style lang="css" scoped>
.item {
  border-bottom: solid 1px;
  margin-top: 2px;
}
</style>
