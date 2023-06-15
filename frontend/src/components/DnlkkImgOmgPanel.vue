<script>
import {defineComponent} from 'vue'
import DnlkkSettingsPanel from "./DnlkkSettingsPanel.vue";
import {mapGetters} from "vuex";
import { saveAs } from 'file-saver';
import LayerPhoto from "./LayerPhoto.vue";
import {
  FontAwesomeIcon
} from "@fortawesome/vue-fontawesome";
import DnlkkRect from "./DnlkkRect.vue";

export default defineComponent({
  name: "DnlkkImgOmgPanel",
  components: {
    DnlkkRect,
    FontAwesomeIcon,
    LayerPhoto, DnlkkSettingsPanel},
  data: () => ({
    shouldRender: false,
    refresh: false,
    method: 'Цвет',
    methods: ['Цвет', 'Размер', 'Сжатие', 'Приколы'],
    baseRect: {
      width_l: 0,
      width_r: 1,
      height_t: 0,
      height_b: 1,
    },
    startRect: {
      startX: 0,
      startY: 0,
      startW: 0,
      startH: 0,
    },
    main_height: 0,
    id: 0,
    window_width: 1920,
    current_first_layer: 0,
  }),
  methods: {
    setMethod(data) {
      this.method = data;
    },
    myEventHandler(e) {
      this.window_width =
          document.body.getBoundingClientRect().width;
      this.startRect.startH =
          document.getElementsByClassName("image")[0].getBoundingClientRect().height;
      this.startRect.startY =
          document.getElementsByClassName("image")[0].getBoundingClientRect().y -
          document.getElementsByClassName("photo")[0].getBoundingClientRect().y - 20;

      this.startRect.startX =
          this.isWide ?
              0 :
              (document.getElementsByClassName("image")[0].getBoundingClientRect().width
                  - this.startRect.startH / this.getImage.height *
                  this.getImage.width) / 2;
      this.startRect.startW =
          this.isWide ?
              document.getElementsByClassName("image")[0].getBoundingClientRect().width :
              this.startRect.startH / this.getImage.height *
              this.getImage.width;


      this.main_height =
          document.getElementsByClassName("main_height")[0].getBoundingClientRect().height - 40;

      this.resize();
    },
    size(w, w2, h, h2) {
      this.baseRect.width_l = this.startRect.startX +
          w / this.getImage.width * this.startRect.startW

      this.baseRect.width_r = this.startRect.startW -
          this.baseRect.width_l +
          this.startRect.startX -
          (this.getImage.width - w2) /
          this.getImage.width * this.startRect.startW

      this.baseRect.height_t = this.startRect.startY +
          h / this.getImage.height * this.startRect.startH

      this.baseRect.height_b = this.startRect.startH - this.baseRect.height_t +
          this.startRect.startY -
          (this.getImage.height - h2) / this.getImage.height * this.startRect.startH

      this.$store.commit('setSize', [w, w2, h, h2]);
    },
    resize() {
      this.size(this.w, this.w2, this.h, this.h2);
    },
    upload() {
      this.shouldRender = true;
      this.$store.commit('upload', this.getImage.src);
      this.rerender();
    },
    rerender() {
      setTimeout(() => this.shouldRender = false, 100);
    },
    refreshing() {
      this.refresh = true;
      this.$store.commit('refresh');
      setTimeout(() => this.refresh = false, 1000);
    },
    save() {
      const byteCharacters =
          atob(this.$store.getters.getReqImage.split(',')[1]);
      const byteNumbers = new Array(byteCharacters.length);
      for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
      }
      const byteArray = new Uint8Array(byteNumbers);
      const blob = new Blob([byteArray], { type: 'image/jpeg' });
      saveAs(blob, 'ImageOMG.jpg');
    },
    chooseLayer(layer_num){
      this.shouldRender = true;
      this.current_first_layer = 0;
      this.$store.commit('chooseLayer', layer_num);
      this.rerender();
    }
  },
  computed: {
    ...mapGetters(['getImage', 'getSize', 'getColor']),
    isWide() {
      let image_aspect = this.getImage.width / this.getImage.height
      let photo_aspect =
          document.getElementsByClassName("main_height")[0].getBoundingClientRect().width /
          document.getElementsByClassName("main_height")[0].getBoundingClientRect().height

      return image_aspect >= photo_aspect
    },
    w() {
      return this.getSize[0]
    },
    w2() {
      return this.getSize[1]
    },
    h() {
      return this.getSize[2]
    },
    h2() {
      return this.getSize[3]
    },
  },
  mounted() {
    window.addEventListener("resize", this.myEventHandler);

    this.id = setInterval(() => {
          window.dispatchEvent(new
          Event('resize'));
        },
        100)
  },
  unmounted() {
    window.removeEventListener("resize", this.myEventHandler);
    clearInterval(this.id)
  },
})
</script>

<template>

  <div
      class="cont"
      v-if="!shouldRender">
    <div class="main main_height">
      <div class="photo-panel">
      <div class="photo"
           :style="window_width >
           945 ? `height: ${0.85*main_height}px` :
           `height: auto`">
        <div class="square">
          <dnlkk-rect v-if="w2 !== 0" class="red-square"
                      :refresh="refresh" :base-rect="baseRect"
                      />
          <dnlkk-rect v-if="w2 !== 0" class="red-square blurred"
                      :refresh="refresh" :base-rect="baseRect"
          />
          <dnlkk-rect class="non-blend-square"
                      :refresh="refresh" :base-rect="baseRect"
          />
          <div v-if="w2 !== 0"
               class="another-square"/>
        </div>
        <v-img :src="getImage"
               :style="
               (this.refresh ?
               `transition: filter 1s linear;`
               : 'transition: filter 0.1s linear;') +
               `filter: brightness(${getColor.brightness}%)
               saturate(${getColor.saturation}%)
               contrast(${getColor.contrast}%)
               grayscale(${getColor.grayscale}%)
                sepia(${getColor.sepia}%)
                invert(${getColor.invert}%);`"
               class="image"/>
        <div class="image image_gradient"
             :style="`
        margin-left: ${startRect.startX - 10}px;
        margin-right: ${startRect.startY - 10}px;
        width: ${startRect.startW + 20}px;
        height: ${startRect.startH + 20}px;`">
        </div>
      </div>
        <div class="layers_panel"
             :style="`height: ${0.15*main_height}px`">
      <div class="layers">
        <div v-if="$store.state.layers.length === 0">
          Пока что слоёв нет
          .
        </div>
        <div
            class="layer-photo"
            v-else>
          <div
              style="display: grid; align-items: center;
              justify-items: center"
            :style="`grid-template-columns: repeat(${Math.min($store.state.layers.length + 2, 5)}, 1fr);`">
          <font-awesome-icon
              v-if="$store.state.layers.length > 3 &&
                    current_first_layer > 0"
              @click="current_first_layer--"
              class="icon"
              icon="square-caret-left" />
            <div v-else/>
          <layer-photo v-for="(layer, index) in
          $store.state.layers.slice(current_first_layer,
          current_first_layer + 3)"
              @chooseLayer="chooseLayer"
              class="image layer-image"
              :style="`width: ${0.12*main_height}px;
              height: ${0.12*main_height}px;`"
              :photo_src="layer"
          :layer_num="current_first_layer+index"/>
          <font-awesome-icon
              v-show="$store.state.layers.length > 3 &&
                    current_first_layer <
                    $store.state.layers.length - 3"
              @click="current_first_layer++"
              class="icon"
              icon="square-caret-right" />
          </div>
        </div>
      </div>
          </div>
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
            @size="size"
            class="panel"/>
        <div class="btns">
          <v-btn class="lets_btn upload-btn"
                 @click="upload">
            Погнали!
          </v-btn>
          <v-btn class="lets_btn refresh-btn"
                 @click="refreshing()">
            Обнулить
          </v-btn>
          <v-btn class="lets_btn save-btn"
                 @click="save()">
            Сохранить
          </v-btn>
        </div>
      </div>
    </div>
  </div>
  <div
      class="cont"
      v-else>
    <div class="main main_height white_text">
      Чето делаем...
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

  flex-grow: 0;
}

.main {
  background: rgba(0, 0, 0, 0.55);

  height: 100%;
  width: 100%;

  display: grid;

  grid-template-columns: 2fr 1fr;
  padding: 20px;
  grid-column-gap: 20px;
  flex-grow: 0;
}

.photo-panel {
  grid-template-rows: 1fr 1fr;
}

.photo {
  background: black;
  box-shadow: 0 0 20px black;
  padding: 20px;
  display: flex;

  position: relative;
}

.image {
  display: flex;
  align-self: center;

  width: max-content;
  object-fit: fill;
}

.v-img__img--contain {
  object-fit: contain;
}


.settings {
  display: grid;

  grid-template-rows: auto 1fr auto;

  padding: 10px 5px 30px;
  background: var(--header-bgc);
  box-shadow: 0 0 20px var(--header-bgc);
}

.settings-choose {
  display: grid;
  grid-template-columns: auto auto auto auto;
}

.settings-choose a {
  background: var(--main-bgc);
  color: white;
  border-radius: 50% 50% 0 0;
}

.panel {
  height: 95%;
  background: var(--main-bgc);
}

.layers_panel {
  display: flex;
  text-align: center;
  align-content: center;
  justify-content: center;
  padding: 20px;

  background: linear-gradient(black,
  var(--header-bgc));

  box-shadow: 0 0 20px black;
}

.layer-photo {
  display: flex;
  align-items: center;
  font-weight: 900;
  justify-items: center;
  justify-content: center;
  justify-self: center;
}
.icon {
  font-size: 50px;
  color: white;
  cursor: pointer;
}
.layer-image {
  margin: 20px;
  border: 5px solid black;
  border-radius: 10%;
  cursor: pointer;
}
.layers {
  display: flex;
  align-items: center;

  color: white;
  text-shadow: 0 0 5px white;

  height: 100%;
}

.chosen {
  color: white;
  font-size: 40px;
  font-weight: 900;
  text-shadow: 0 0 20px white;
  transition: text-shadow 0.2s ease-in, color 0.2s ease-in, font-size 0.2s ease-in, margin 0.2s ease-in;
  margin: 0;
  z-index: 2;
}

.centered {
  display: flex;
  justify-content: center; /* Align horizontal */
  align-items: center; /* Align vertical */
  transition: font-size 0.1s ease-in, margin 0.2s ease-in;
  color: #aaaeb7;
}

.centered:hover {
  font-size: 20px;
  font-weight: 900;
  margin: 0 5px;
}

.red-square {
  position: absolute;
  width: 100%;
  height: 100%;
  z-index: 2;
}

.non-blend-square {
  position: absolute;
  width: 100%;
  height: 100%;
  z-index: 2;
  mix-blend-mode: overlay;
  background: white;
  filter: blur(12px);
}

.another-square {
  position: absolute;
  background: gray;
  width: calc(100% - 40px);
  height: calc(100% - 40px);
  z-index: 1;
  mix-blend-mode: multiply;
}

.red-square::before {
  content: "";
  display: block;
  width: 100%;
  height: 100%;
  border: 2px solid red;
  box-sizing: border-box;
  box-shadow: 0 0 20px black;

  border-image: conic-gradient(from var(--angle), red, yellow, lime, aqua, blue, magenta, red) 1;
  animation: 10s rotate ease infinite;
}

.image_gradient {
  position: absolute;
  z-index: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 18px;
  border-radius: 5px;
  box-shadow: inset 0 0 12px 12px black, inset 0 0 3px 2px white;

  border-image: conic-gradient(from var(--angle), red, yellow, lime, aqua, blue, magenta, red) 1;
  animation: 10s rotate ease infinite;
}

@keyframes rotate {
  to {
    --angle: 360deg;
  }
}

@property --angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.lets_btn {
  color: white;
  text-shadow: 0 0 5px white;
  background: var(--main-bgc);
  box-shadow: none;
}

.btns {
  display: grid;
  grid-template-areas: "one two"
                        "three three";
  column-gap: 20px;
  row-gap: 20px;
}
.upload-btn{
  grid-area: one;
}
.refresh-btn{
  grid-area: two;
}
.save-btn{
  grid-area: three;
}

.white_text {
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 50px;
}

.blurred {
  filter: blur(5px);
}

@media (max-width:1000px) {
  .main {
    grid-template-columns: 1fr;
    grid-template-rows: 1fr 1fr;
    padding: 10px;
    grid-row-gap: 20px;
  }
}

</style>