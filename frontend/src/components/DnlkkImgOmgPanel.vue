<script>
import {defineComponent} from 'vue'
import DnlkkSettingsPanel from "./DnlkkSettingsPanel.vue";
import {mapGetters} from "vuex";

export default defineComponent({
  name: "DnlkkImgOmgPanel",
  components: {DnlkkSettingsPanel},
  data: () => ({
    method: 'Цвет',
    methods: ['Цвет', 'Размер', 'Сжатие', 'Приколы'],
    width_l: 0,
    width_r: 1,
    height_t: 0,
    height_b: 1,
    aspect: 1,
    w: 0,
    w2: 0,
    h: 0,
    h2: 0,
    startX: 0,
    startY: 0,
    startW: 0,
    startH: 0,
    main_height: 0,
  }),
  methods: {
    setMethod(data) {
      this.method = data;
    },
    myEventHandler(e) {
      this.startH =
          document.getElementsByClassName("image")[0].getBoundingClientRect().height;
      this.startY =
          document.getElementsByClassName("image")[0].getBoundingClientRect().y -
          document.getElementsByClassName("photo")[0].getBoundingClientRect().y - 20;

      this.startX =
          this.isWide ?
              0 :
              (document.getElementsByClassName("image")[0].getBoundingClientRect().width
                  - this.startH / this.getImage.height *
                  this.getImage.width) / 2 ;
      this.startW =
          this.isWide ?
              document.getElementsByClassName("image")[0].getBoundingClientRect().width :
              this.startH / this.getImage.height *
              this.getImage.width;


      this.main_height =
          document.getElementsByClassName("main_height")[0].getBoundingClientRect().height - 40;

      this.resize();
    },
    size(w, w2, h, h2) {
      this.w = w
      this.w2 = w2
      this.h = h
      this.h2 = h2

      this.width_l = this.startX +
          w/this.getImage.width * this.startW

      this.width_r = this.startW - this.width_l +
          this.startX -
          (this.getImage.width - w2)/this.getImage.width * this.startW

      this.height_t = this.startY +
          h/this.getImage.height * this.startH

      this.height_b = this.startH - this.height_t +
          this.startY -
          (this.getImage.height - h2)/this.getImage.height * this.startH

      console.log(this.width_l);
      console.log(this.width_r);
      console.log(this.height_t);
      console.log(this.height_b);
    },
    resize() {
      this.size(this.w, this.w2, this.h, this.h2);
    },
  },
  computed: {
    ...mapGetters(['getImage']),
    isWide(){
      return this.getImage.width/this.getImage.height >= 1
    }
  },
  mounted() {
    window.addEventListener("resize", this.myEventHandler);

    const id = setInterval(() => {
          this.aspect =
              this.getImage.width / this.getImage.height;

          window.dispatchEvent(new
          Event('resize'));
        },
        100)
  },
  destroyed() {
    window.removeEventListener("resize", this.myEventHandler);
  },
})
</script>

<template>

  <div class="cont">
    <div class="main main_height">
      <div class="photo"
           :style="`height: ${main_height}px`">
        <div class="square">
          <div class="red-square"
               :style="` margin-top: ${height_t}px;
              margin-left: ${width_l}px;
              width: ${width_r}px;
              height: ${height_b}px;`"
          />
          <div class="non-blend-square"
               :style="` margin-top: ${height_t}px;
              margin-left: ${width_l}px;
              width: ${width_r}px;
              height: ${height_b}px;`"
          />
          <div class="another-square"/>
        </div>
        <v-img :src="getImage"
               class="image"/>
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
  height: max-content;
}

.v-img__img--contain {
  object-fit: contain;
}


.settings {
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

.chosen {
  color: white;
  font-size: 40px;
  font-weight: 900;
  text-shadow: 0 0 20px white;
  transition: text-shadow 0.2s ease-in, color 0.2s ease-in, font-size 0.2s ease-in, margin 0.2s ease-in;
  margin: 0;
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
  filter: blur(10px);
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
  border: 1px solid red;
  box-sizing: border-box;
  box-shadow: 0 0 20px red;
}
</style>