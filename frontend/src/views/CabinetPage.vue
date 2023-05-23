<script>
import {mapGetters} from "vuex";

export default {
  computed: {
    ...mapGetters(['getProfile'])
  }
}
</script>

<template>
  <div class="cont" :class="!this.$store.state.isAuth ?
  'notification' : ''">
    <v-container class="main">
      <div v-if="this.$store.state.isAuth">
        <h1>{{ getProfile.login }}</h1>
        <v-img src="../../public/vite.svg"/>
        <div class="info">
          <h3>ФИО: {{ getProfile.fullname }}</h3>
          <h5>Почта: {{ getProfile.email }}</h5>
          <div>День рождения: {{ getProfile.birthdate }}
          </div>
          <h5>{{ getProfile.category }}</h5>
        </div>
      </div>
      <div v-else>
        <h2>Извините, но, кажется, вы не авторизованы.</h2>
        <div class="text">
          <h3>Тыкнете</h3>
          <h3
              class="click"
              @click="this.$store.commit('start');">
              &nbsp;сюды
          </h3>
          <h3>, чтобы решить это недоразумение.</h3>
        </div>
      </div>
    </v-container>
  </div>
</template>

<style scoped>
.cont {
  position: absolute;
  width: 100%;
  padding: 20px;
  height: 100%;
}

.notification {
  top: calc(50% - 20px - 48px);
}
.main {
  display: flex;
  justify-content: center;
  justify-items: center;
  justify-self: center;

  font-size: 30px;
  color: white;
  text-shadow: 0 0 7px white;

  text-align: center;
  background: rgba(44, 44, 44, 0.2);
}
.text {
  display: flex;
  justify-content: center;
}

.click {
  cursor: pointer;
  text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
  color: white;
  animation: color 3s infinite alternate;
}

@keyframes color {
  50% {
    color: var(--header-bgc);
  }
}

</style>