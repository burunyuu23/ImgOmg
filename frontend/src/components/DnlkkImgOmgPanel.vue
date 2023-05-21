<script>
import {defineComponent} from 'vue'
import DnlkkSettingsPanel from "./DnlkkSettingsPanel.vue";

export default defineComponent({
  name: "DnlkkImgOmgPanel",
  components: {DnlkkSettingsPanel},
  data: () => ({
    method: 'Цвет',
    methods: ['Цвет', 'Размер', 'Сжатие', 'Приколы'],
  }),
  methods: {
    setMethod(data){
      this.method = data;
    }
  }
})
</script>

<template>
  <div class="cont">
    <div class="main">
      <div class="photo">

      </div>
      <div class="settings">
        <div class="settings-choose">
          <a v-for="meth in methods"
             :class="method === meth ? 'chosen' :
             'centered'"
             @click="setMethod(meth);">
            {{ meth }}
          </a>
        </div>
        <dnlkk-settings-panel
            :method="method"
            class="panel"/>
      </div>
    </div>
  </div>
</template>

<style scoped>
* {
  text-align: center;
}
a {
  cursor: pointer;
}

.cont {
  position: relative;
  box-shadow: 0 0 500px black;

  margin: 20px 0;
  height: 90vh;
}
.main {
  background: rgba(0, 0, 0, 0.55);

  height: 100%;

  display: grid;

  grid-template-columns: 2fr 1fr;
  padding: 20px;
  grid-column-gap: 20px;
}

.photo {
  background: black;
  box-shadow: 0 0 20px black;
}

.settings {
  padding: 10px 5px;
  background: var(--header-bgc);
  box-shadow: 0 0 20px var(--header-bgc);
}

.settings-choose {
  display: grid;

  grid-template-columns: auto auto auto auto;
}

.settings-choose a{
  background: var(--main-bgc);
  color: white;
  margin: 0 5px;
  border-radius: 50% 50% 0 0;
  padding: 0 5px;
}
.panel {
  height: 95%;
  background: var(--main-bgc);
}
.chosen {
  color: white;
  font-size: 30px;
  font-weight: 900;
  text-shadow: 0 0 20px white;
  transition: text-shadow 0.2s ease-in, color 0.2s
  ease-in, font-size 0.2s ease-in;
}
.centered {
  display: flex;
  justify-content: center; /* Align horizontal */
  align-items: center; /* Align vertical */
  transition: font-size 0.1s ease-in;
  color: #aaaeb7;
}
.centered:hover {
  font-size: 20px;
  font-weight: 900;
}
</style>