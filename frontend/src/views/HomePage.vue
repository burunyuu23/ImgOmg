<script>
import DnlkkDialog from "../components/DnlkkDialog.vue";
import axios from "axios";
import {EDIT_URL} from "../baseUrl.js";
import DnlkkHomeButton
  from "../components/DnlkkHomeButton.vue";
import DnlkkImgOmgPanel
  from "../components/DnlkkImgOmgPanel.vue";

export default {
  components: {
    DnlkkImgOmgPanel,
    DnlkkHomeButton, DnlkkDialog},
}
</script>

<template>
  <TransitionGroup>
    <dnlkk-home-button
        v-if="!this.$store.state.isLoaded"/>

    <dnlkk-img-omg-panel
        v-else/>
  </TransitionGroup>
</template>

<style scoped>
.v-enter-active, v-leave-active {
  transition: opacity 0.5s ease;
}

v-enter-from, v-leave-to {
  opacity: 0;
}

</style>