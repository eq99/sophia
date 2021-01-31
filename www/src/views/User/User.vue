<template>
  <v-container>
    <v-row>
      <v-col cols="2">
        <v-sheet rounded="lg">
          <v-list color="transparent">
            <v-list-item
              v-for="(link, i) in links"
              :key="i"
              :href="prefixLink(link.name)"
            >
              <v-list-item-content>
                <v-list-item-title> {{ link.title }} </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-sheet>
      </v-col>

      <v-col>
        <router-view></router-view>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    links: [
      { name: "", title: "账户设置" },
      { name: "assets", title: "我的资产" },
    ],
  }),

  computed: {
    prefixLink() {
      return (link) => `/userid/${link}`;
    },
  },
};
</script>
