<template>
  <v-card>
    <v-simple-table>
      <thead>
        <tr>
          <th>科目</th>
          <th>时间</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(asset, i) in assets" :key="i">
          <td>{{ asset.name }}</td>
          <td>{{ asset.time }}</td>
        </tr>
      </tbody>
    </v-simple-table>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    assets: [
      { name: "概率论", time: "2020 - 12 - 12" },
      { name: "概率论", time: "2020 - 12 - 12" },
      { name: "概率论", time: "2020 - 12 - 12" },
      { name: "概率论", time: 2020 - 12 - 12 },
    ],
  }),
};
</script>
