<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "DnlkkSize",
  data: () => ({
    width_l: 0,
    width_r: 0,
    height_t: 0,
    height_b: 0,
    aspect: 'Произвольная'
  }),
  methods: {},
  watch: {
    width_l(newValue, oldValue) {
      if (newValue < 0) {
        this.width_l = oldValue;
      }
      this.$emit('size', this.width_l, this.width_r,
          this.height_t, this.height_b)
    },
    width_r(newValue, oldValue) {
      if (newValue < 0) {
        this.width_r = oldValue;
      }
      this.$emit('size', this.width_l, this.width_r,
          this.height_t, this.height_b)
    },
    height_t(newValue, oldValue) {
      if (newValue < 0) {
        this.height_t = oldValue;
      }
      this.$emit('size', this.width_l, this.width_r,
          this.height_t, this.height_b)
    },
    height_b(newValue, oldValue) {
      if (newValue < 0) {
        this.height_b = oldValue;
      }
      this.$emit('size', this.width_l, this.width_r,
          this.height_t, this.height_b)
    },
  }
})
</script>

<template>
  <v-container class="cont">
    <div class=" text-capitalize">Ширина</div>
    <v-row>
      <v-col cols="6">
        <v-text-field
            v-model="width_l"
            hide-details
            single-line
            type="number"
        />
        <v-slider
            max="1920"
            min="0"
            :step="1"
            v-model="width_l"
            thumb-label="always"/>
      </v-col>
      <v-col cols="6">
        <v-text-field
            v-model="width_r"
            hide-details
            single-line
            type="number"
        />
        <v-slider
            max="1920"
            min="0"
            :step="1"
            v-model="width_r"
            thumb-label="always"/>
      </v-col>
    </v-row>
  </v-container>
    <v-container class="cont">
      <div class=" text-capitalize">Высота</div>
      <v-row>
      <v-col cols="6">
        <v-text-field
            v-model="height_t"
            hide-details
            single-line
            type="number"
        />
        <v-slider
            max="769"
            min="0"
            :step="1"
            v-model="height_t"
            thumb-label="always"/>
      </v-col>
      <v-col cols="6">
        <v-text-field
            v-model="height_b"
            hide-details
            single-line
            type="number"
        />
        <v-slider
            max="769"
            min="0"
            :step="1"
            v-model="height_b"
            thumb-label="always"/>
      </v-col>
  </v-row>
  </v-container>
  <v-container class="cont">
    <div class=" text-capitalize">Ориентация</div>
    <v-select
        v-model="aspect"
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