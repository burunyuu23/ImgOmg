<template>
    <v-app app class="app">
        <nav-bar/>
        <v-main class="main">
            <video autoplay muted loop class="video-container">
                <source src="../src/resources/test.mp4" type="video/mp4"/>
            </video>
            <router-view/>
        </v-main>
    </v-app>
</template>

<script>

import NavBar from "./components/NavBar.vue";
import axios from "axios";
import {updateToken} from "./plugins/keycloak-util.js";
import Vue from "vue";

export default Vue.extend({
    name: 'App',
    components: {NavBar},
    created: function () {
    axios.interceptors.request.use(async config => {
      // Обновляем токен
      const token = await updateToken()
      // Добавляем токен в каждый запрос
      config.headers.common[AUTHORIZATION_HEADER] = `Bearer ${token}`
      return config
    })

    axios.interceptors.response.use( (response) => {
      return response
    }, error => {
      return new Promise((resolve, reject) => {
        // Если от API получена ошибка - отправляем на страницу /error
        this.$router.push('/error')
        reject(error)
      })
    })
  },
  // Обновляем токен при навигации
  watch: {
    $route() {
      updateToken()
    }
  }
})
</script>

<style scoped>
.video-container {
    background: url('../src/resources/test.mp4') no-repeat center center fixed;
    position: absolute;
    background-size: auto;
    object-fit: cover;
    pointer-events: none;
    width: 100vw;
    height: calc(100vh - 48px);
    top: 48px;

    opacity: 100%;
}

.main {
    background: var(--main-bgc);
}
</style>
