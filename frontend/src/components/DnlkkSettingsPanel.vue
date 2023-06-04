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
  methods: {
    size(w, w2, h, h2){
      this.$emit('size', w, w2, h, h2)
    }
  }
})
</script>

<template>
  <v-container style="display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin: 0 0 10px 0;">
    <dnlkk-color v-if="method === 'Цвет'"/>
    <dnlkk-size
        @size="size"
        v-else-if="method === 'Размер'" />
    <dnlkk-compress v-else-if="method === 'Сжатие'"/>
    <dnlkk-prikols v-else/>
  </v-container>
</template>


<style scoped>

</style>