<script>
import {defineComponent} from 'vue'
import {mapGetters} from "vuex";

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
    getSize(newValue) {
      this.width_l = newValue[0]
      this.width_r = newValue[1]
      this.height_t = newValue[2]
      this.height_b = newValue[3]
    },
    width_l(newValue, oldValue) {
      if (newValue < 0) {
        this.width_l = oldValue;
      }
      if ((newValue >= this.width_r))
        this.width_l = this.width_r - 1;

      this.$emit('size', this.width_l, this.width_r,
          this.height_t, this.height_b)
    },
    width_r(newValue, oldValue) {
      if (newValue < 0) {
        this.width_r = oldValue;
      }
      if ((newValue <= this.width_l))
        this.width_r = this.width_l + 1;
      if (newValue > this.getImage.width)
        this.width_r = this.getImage.width

      this.$emit('size', this.width_l, this.width_r,
          this.height_t, this.height_b)
    },

    height_t(newValue, oldValue) {
      if (newValue < 0) {
        this.height_t = oldValue;
      }
      if ((newValue >= this.height_b))
        this.height_t = this.height_b - 1;

      this.$emit('size', this.width_l, this.width_r,
          this.height_t, this.height_b)
    },
    height_b(newValue, oldValue) {
      if (newValue < 0) {
        this.height_b = oldValue;
      }
      if ((newValue <= this.height_t))
        this.height_b = this.height_t + 1;
      if (newValue > this.getImage.height)
        this.height_b = this.getImage.height

      this.$emit('size', this.width_l, this.width_r,
          this.height_t, this.height_b)
    },
  },
  computed: {
    ...mapGetters(['getSize', 'getImage'])
  },
  mounted() {
    this.width_l =
        this.getSize[0]
    this.width_r =
        this.getSize[1]
    this.height_t =
        this.getSize[2]
    this.height_b =
        this.getSize[3]
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
            :max="this.$store.state.image.width"
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
            :max="this.$store.state.image.width"
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
            :max="this.$store.state.image.height"
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
            :max="this.$store.state.image.height"
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