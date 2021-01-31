<template>
  <v-container>
    <v-list>
      <v-list-item>
        <v-list-item-avatar>
          <v-img :src="user.avatarURL"></v-img>
        </v-list-item-avatar>
        <v-list-content>
          <v-list-item-title class="title"> {{ user.name }} </v-list-item-title>
          <p class="mb-0">{{ user.bibo }}</p>
          <p class="font-weight-bold">
            <v-icon>mdi-tag</v-icon>
            {{ user.subject }}
          </p>
        </v-list-content>
      </v-list-item>
      <v-divider class="my-6"></v-divider>
    </v-list>
    <v-simple-table>
      <tbody>
        <tr v-for="(setting, i) in settings" :key="i">
          <td>{{ setting.name }}</td>
          <td>{{ setting.value }}</td>
          <td>
            <v-btn dense>{{ setting.op }} </v-btn>
          </td>
        </tr>
      </tbody>
    </v-simple-table>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    user: {
      avatarURL: "https://cdn.vuetifyjs.com/images/john.png",
      name: "一只特立独行的猪",
      bibo: "要么痛快的死去，要么坚强的活着",
      subject: "计算机",
    },
    settings: [
      { name: "手机", value: "18620411149", op: "更换手机" },
      { name: "邮箱", value: "18620411149@11.com", op: "验证邮箱" },
    ],
  }),
  mounted() {
    this.axios
      .get("/api/repos/")
      .then((res) => {
        this.repos = res.data;
      })
      .catch((err) => console.log(err));
  },
};
</script>
