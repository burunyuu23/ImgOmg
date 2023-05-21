<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "DnlkkPrikols",
  data: () => ({

  })
})
</script>

<template>

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