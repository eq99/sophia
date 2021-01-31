<template>
  <v-container>
    <v-timeline dense>
      <v-timeline-item v-for="n in 2" :key="n">
        <span slot="opposite">Tus eu perfecto</span>
        <v-card class="elevation-2">
          <v-card-title class="headline"> Lorem ipsum </v-card-title>
          <v-card-text>
            Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet
            nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an
            vim zril disputando voluptatibus, vix an salutandi sententiae.
          </v-card-text>
        </v-card>
      </v-timeline-item>
    </v-timeline>
  </v-container>
</template>
