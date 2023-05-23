<script>
import {defineComponent} from 'vue'
import axios from "axios";
import {EDIT_URL} from "../baseUrl.js";
import {mapGetters} from "vuex";

export default defineComponent({
  name: "DnlkkHomeButton",
  data: () => ({
    image: {}
  }),
  methods: {
    handleImage(e) {
      const image = e.target.files[0];
      console.log(image);
      this.base64_image(image)
    },
    base64_image(image) {
      const reader = new FileReader();

      reader.onload = (e) => {
        this.image = e.target.result;
        this.uploadImage()
      }

      reader.readAsDataURL(image);
    },
    async uploadImage() {
      const {image} = this;

      this.$store.commit('upload', image);
    },
    imgClick() {
      if (this.$store.state.isAuth)
        this.$refs.inputUpload.click();
      else
        this.$store.commit('start');
    }
  },
})
</script>

<template>
  <div>
    <input v-show="false"
           ref="inputUpload"
           type="file"
           @change="handleImage"/>
    <v-img
        @click="imgClick"
        :aspect-ratio="1/1"
        class="img"
        cover
        src="..\src\resources\MainMenuLogo.jpg"
    >
      <div class="main">
        <div class="catty_logo_container">
          <a class="catty_input_logo">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;／＞　
            フ</a>
          <a class="catty_input_logo">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
            　_　_|</a>
          <a class="catty_input_logo">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;／`
            ミ＿xノ</a>
          <a class="catty_input_logo">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/　　　　
            |</a>
          <a class="catty_input_logo">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/　
            ヽ　　 ﾉ</a>
          <a class="catty_input_logo">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│　　|　|　|</a>
          <a class="catty_input_logo">&nbsp;／￣|　　 |　|　|</a>
          <a class="catty_input_logo">(￣ヽ＿_ヽ_)__)</a>
          <a class="catty_input_logo">&nbsp;＼二)</a>
          <p>LET'S EDIT</p>
        </div>
      </div>
    </v-img>
  </div>
</template>

<style scoped>

.img {
  width: var(--width2);

  transform: translate(calc(50vw - var(--width2) / 2), 0);
  margin-top: 20px;
  border: 5px solid black;

  align-items: center;
}

.main {
  display: flex;
  justify-content: center;
  justify-items: center;
}

.main p {
  display: flex;
  justify-content: center;
}

.img {
  box-shadow: 0 0 0 var(--header-bgc);
  transition: box-shadow 1s linear;
}

.img:hover {
  box-shadow: 0 0 calc(var(--width2) / 3) #4acb86;
  transition: box-shadow 1s linear;
  cursor: pointer;
}


.catty_logo_container {
  display: flex;
  flex-direction: column;
}
</style>