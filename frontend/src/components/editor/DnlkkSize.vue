<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "DnlkkSize",
  data: () => ({
    width: 1,
    height: 1,
    aspect: 'Произвольная'
  }),
  watch: {
    width(newValue, oldValue) {
      if (newValue < 1) {
        this.width = oldValue;
      }
    },
    height(newValue, oldValue) {
      if (newValue < 1) {
        this.height = oldValue;
      }
    }
}
})
</script>

<template>
  <v-container class="cont">
    <div class=" text-capitalize">Ширина</div>
    <v-text-field
        v-model="width"
        hide-details
        single-line
        type="number"
    />
  </v-container>
  <v-container class="cont">
    <div class=" text-capitalize">Высота</div>
    <v-text-field
        v-model="height"
        hide-details
        single-line
        type="number"
    />
  </v-container>
  <v-container class="cont">
    <div class=" text-capitalize">Ориентация</div>
    <v-select
        :items="['Произвольная', '16:9', 'Квадратная',
        '9:16']"/>
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

.v-slider-thumb__label div {
  transform: rotateX(180deg);;
}
</style>