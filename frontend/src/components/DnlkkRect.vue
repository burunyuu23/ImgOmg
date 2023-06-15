<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "DnlkkRect",
  props: ['refresh', 'baseRect']
})
</script>

<template>
  <div :style="
                (this.refresh ?
               `transition: margin 0.5s ease,
               width 0.5s ease, height 0.5s ease;`
               : 'transition: margin 0.1s ease,' +
                'width 0.1s ease, height 0.1s ease;')
                +`margin-top: ${baseRect.height_t}px;
              margin-left: ${baseRect.width_l}px;
              width: ${baseRect.width_r}px;
              height: ${baseRect.height_b}px;`"
  />
</template>

<style scoped>

</style>