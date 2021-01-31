<template>
  <v-app>
    <!-- <nav class="fixed-nav">
      <ul>
        <li><a href="/account/:userid">登录</a></li>
      </ul>

      <button>菜单</button>
    </nav> -->
    <v-navigation-drawer v-model="drawer" absolute bottom temporary right>
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item>
            <v-list-item-title>Foo</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Bar</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Fizz</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Buzz</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <v-btn
      fab
      fixed
      right
      bottom
      color="indigo"
      style="z-index: 100"
      @click="drawer = !drawer"
    >
      <v-icon>mdi-plus</v-icon>
    </v-btn>
    <main>
      <router-view></router-view>
    </main>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    drawer: false,
    group: null,
  }),
  watch: {
    group() {
      this.drawer = false;
    },
  },
};
</script>

<style lang="css"></style>
