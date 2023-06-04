<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "LayerPhoto",
  props: ['photo_src', 'layer_num'],
  methods: {
    chooseLayer(){
      this.$emit('chooseLayer', this.layer_num)
    }
  }
})
</script>

<template>
  <div
      class="layer"
      @click="chooseLayer">
    <v-img
        :src="photo_src"
    />
    <div class="layer-text">
      <div
          style="font-size: 15px"
          v-if="layer_num === 0">
        Первоначальный слой
      </div>
      <div v-else>
        Слой {{ layer_num }}
      </div>
    </div>
  </div>
</template>

<style scoped>
.layer-text{
  position: absolute;
  text-shadow: 0 0 5px black;

  width: 100%;
  height: 100%;

  font-size: 20px;
  font-weight: 600;
  transform: translateY(20px);

  display: flex;
  justify-content: center;
  align-content: flex-end;
  align-items: flex-end;
}
.layer{
  background: black;
  display: flex;
  align-content: center;
  align-items: center;
  justify-content: center;

  position: relative;
}
</style>