<script>
import {defineComponent} from 'vue'
import {imageMixin} from "../../mixins/imageMixin.js";

export default defineComponent({
  name: "DnlkkCompress",
  mixins: [imageMixin],
  data: () => ({
    compress: false,
  }),
  computed: {
    image() {
      return this.$store.getters.getReqImage
    },
    src_image() {
      return this.$store.getters.getImage.src
    },
    compress_rate() {
      return this.$store.state.req.methods.compress
    }
  },
  mounted() {
    this.compress = this.compress ||
        this.$store.state.req.methods.compress < 101
  },
  watch: {
    compress_rate(newValue) {
      this.$store.commit('get_compress')
    },
    compress(newValue) {
      if (newValue === false) {
        this.$store.state.req.methods.compress = 101
      }
      else {
        this.$store.state.req.methods.compress = 100
      }
    }
  }
})
</script>

<template>
  <div>
  <v-container>
    <div class=" text-capitalize">Применить сжатие</div>
    <v-checkbox v-model="compress"/>
    <v-slider
        v-if="compress"
        v-model="$store.state.req.methods.compress"
        :step="1"
        thumb-label="always"/>
  </v-container>
  <div
      class="cont">
    Размер текущего файла:
    {{getFileSizeFromBase64(image)}}
  </div>
  <div
      class="cont">
    Размер сжатого файла:
    ~{{getFileSizeFromBase64(src_image)}}
  </div>
  </div>
</template>


<style scoped>

* {
  text-align: left;
  font-size: 30px;
}
.cont {
  display: flex;
  justify-content: center;
}
</style>