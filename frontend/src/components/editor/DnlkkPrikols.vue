<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "DnlkkPrikols",
  data: () => ({
    prikols:
        ['D̸̦̘̾͊͜͝R̵̠͕͛̐͜͝A̵̡̞̟͛̕͝I̵͍͓͓͊̓͘N̵͉̙̈́̈́͊͜ S̵̡͉͔͑̈́̒T̴̻̟̙̈́͠͠Ý̸̼̼͆̀͜L̸̡͕͚͒̽͝E̴͔͕͙͐͆́',
        '𝕖𝕝𝕖𝕘𝕒𝕟𝕥',
        'sudo rm -fr /background --no-preserve-root'],
  })
})
</script>

<template>
  <v-container class="cont">
    <div>Выберите прикол:</div>
    <v-select
        v-model="$store.state.req.methods.prikols"
        :items="prikols"/>
    <div
        class="grid"
        v-if="$store.state.req.methods.prikols !== ''">
      <div>Выбран прикол:</div>
      <div> {{ $store.state.req.methods.prikols }}</div>

      <hr class="black"/>
      <v-btn
          class="btn"
          @click="$store.state.req.methods.prikols = ''">
        Мне не нужны приколы
      </v-btn>
      <hr class="black"/>
    </div>
  </v-container>
</template>


<style scoped>

* {
  text-align: center;
  font-size: 30px;
}

.btn {
  background: transparent;
  color: black;
  box-shadow: none;
  margin: 0;
}

.black {
  display: block;
  height: 1px;
  border: 0;
  margin: 1em 0;
  padding: 0;
  border-top: 1px solid black;
  -webkit-tap-highlight-color: black;
}

.grid {
  display: grid;
  grid-template-rows: 1fr 1fr;

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