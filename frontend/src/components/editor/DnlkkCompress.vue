<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "DnlkkCompress",
  data: () => ({
    compress: false,
    compress_rate: 100
  })
})
</script>

<template>
  <v-container class="cont">
    <div class=" text-capitalize">Применить сжатие</div>
    <v-checkbox v-model="compress"/>
    <v-slider
        v-if="compress"
        v-model="compress_rate"
        :step="1"
        thumb-label="always"/>
  </v-container>
</template>


<style scoped>

* {
  text-align: left;
  font-size: 30px;
}
.cont {
}
</style>