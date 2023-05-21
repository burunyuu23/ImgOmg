<script>
import {defineComponent} from 'vue'
import DnlkkColor from "./editor/DnlkkColor.vue";
import DnlkkSize from "./editor/DnlkkSize.vue";
import DnlkkCompress from "./editor/DnlkkCompress.vue";
import DnlkkPrikols from "./editor/DnlkkPrikols.vue";

export default defineComponent({
  name: "DnlkkSettingsPanel",
  components: {
    DnlkkPrikols,
    DnlkkCompress, DnlkkSize, DnlkkColor},
  props: ['method'],
})
</script>

<template>
  <v-container>
    <dnlkk-color v-if="method === 'Цвет'"/>
    <dnlkk-size v-else-if="method === 'Размер'" />
    <dnlkk-compress v-else-if="method === 'Сжатие'"/>
    <dnlkk-prikols v-else/>
  </v-container>
</template>


<style scoped>

</style>