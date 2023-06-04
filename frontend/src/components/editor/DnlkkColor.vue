<script>
import {defineComponent} from 'vue'
import {mapGetters} from "vuex";

export default defineComponent({
  name: "DnlkkColor",
  data: (() => ({
    page: 1
}))
})
</script>

<template>
  <div style="justify-content: center">
    <div v-if="page === 1">
      <v-container class="cont">
        <div class=" text-capitalize">Яркость</div>
        <v-slider
            max="200"
            min="0"
            :step="1"
            v-model="$store.state.req.methods.color.brightness"
            thumb-label="always"/>
      </v-container>
      <v-container class="cont">
        <div class=" text-capitalize">Насыщенность</div>
        <v-slider
            class=""
            max="200"
            min="0"
            :step="1"
            v-model="$store.state.req.methods.color.saturation"
            thumb-label="always"/>
      </v-container>
      <v-container class="cont">
        <div class=" text-capitalize">Контрастность</div>
        <v-slider
            class=""
            max="200"
            min="0"
            :step="1"
            v-model="$store.state.req.methods.color.contrast"
            thumb-label="always"
            aria-label="down"/>
      </v-container>
      <v-container class="cont">
        <div class=" text-capitalize">Сепия</div>
        <v-slider
            class=""
            max="100"
            min="0"
            :step="1"
            v-model="$store.state.req.methods.color.sepia"
            thumb-label="always"
            aria-label="down"/>
      </v-container>

    </div>
    <div v-if="page === 2">
      <v-container class="cont">
        <div class=" text-capitalize">Серость...</div>
        <v-slider
            class=""
            max="100"
            min="0"
            :step="1"
            v-model="$store.state.req.methods.color.grayscale"
            thumb-label="always"
            aria-label="down"/>
      </v-container>
      <v-container class="cont">
        <div class=" text-capitalize">Инверсия</div>
        <v-slider
            class=""
            max="100"
            min="0"
            :step="1"
            v-model="$store.state.req.methods.color.invert"
            thumb-label="always"
            aria-label="down"/>
      </v-container>
    </div>

  </div>

  <v-pagination
      class="spacer"
      v-model="page"
      :length="2"
      rounded="circle"
  ></v-pagination>
</template>


<style scoped>

* {
  text-align: left;
  font-size: 30px;
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