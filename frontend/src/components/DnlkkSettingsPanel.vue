<script>
import {defineComponent} from 'vue'
import DnlkkColor from "./editor/DnlkkColor.vue";

export default defineComponent({
  name: "DnlkkSettingsPanel",
  components: {DnlkkColor},
  props: ['method'],
})
</script>

<template>
  <v-container>
    <dnlkk-color/>
  </v-container>
</template>


<style scoped>

</style>