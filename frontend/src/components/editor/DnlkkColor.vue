<script>
import {defineComponent} from 'vue'
import {mapGetters} from "vuex";

export default defineComponent({
  name: "DnlkkColor",
})
</script>

<template>
  <v-row>
    <v-col cols="6">
      <v-container class="cont">
        <div class=" text-capitalize">Яркость</div>
        <v-slider
            max="200"
            min="0"
            :step="1"
            v-model="$store.state.req.methods.color.brightness"
            thumb-label="always"/>
      </v-container>
    </v-col>
    <v-col cols="6">
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
    </v-col>
  </v-row>

  <v-row>
    <v-col cols="6">
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
    </v-col>
    <v-col cols="6">
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
    </v-col>
  </v-row>

  <v-row>
    <v-col cols="6">
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
    </v-col>
    <v-col cols="6">
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
    </v-col>
  </v-row>

  <v-row>
    <v-col cols="6">

    </v-col>
    <v-col cols="6">

    </v-col>
  </v-row>


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