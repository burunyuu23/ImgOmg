<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "DnlkkColor",
  data: () => ({
    brightness: 0,
    saturation: 0,
    contrast: 0,
  })
})
</script>

<template>
  <v-container class="cont">
    <div class=" text-capitalize">Яркость</div>
    <v-slider
        max="100"
        min="-100"
        :step="1"
        v-model="brightness"
        thumb-label="always"/>
  </v-container>
  <v-container class="cont">
    <div class=" text-capitalize">Насыщенность</div>
    <v-slider
        class=""
        max="100"
        min="-100"
        :step="1"
        v-model="saturation"
        thumb-label="always"/>
  </v-container>
  <v-container class="cont">
    <div class=" text-capitalize">Контрастность</div>
    <v-slider
        class=""
        max="100"
        min="-100"
        :step="1"
        v-model="contrast"
        thumb-label="always"
        aria-label="down"/>
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

<style>

.v-slider-thumb__label {
  background: var(--header-bgc);
  border-radius: 50%;
  color: var(--main-bgc);
  font-weight: 900;

}
.v-slider-thumb__label::before {
  color: var(--header-bgc);
}
.v-slider.v-input--horizontal
.v-slider-thumb__label.v-locale--is-ltr,
.v-locale--is-ltr .v-slider.v-input--horizontal .v-slider-thumb__label {
  transform: translate(-18px, 65px) rotateX(180deg);
}

.v-slider-thumb__label div{
  transform: rotateX(180deg);;
}
</style>