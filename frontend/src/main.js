import Vue, {createApp} from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import {loadFonts} from './plugins/webfontloader'
import router from "./router.js"
import axios from 'axios'
import store from "./store/index.js";
import i18n from '@/plugins/i18n'
import '@/plugins/keycloak'
import {updateToken} from '@/plugins/keycloak-util'

loadFonts()


const app = createApp(App)

app.config.productionTip = false
app.config.globalProperties.$axios = axios;

app.$keycloak.init({onLoad: 'login-required'}).then((auth) => {
    if (!auth) {
        window.location.reload();
    } else {
        new Vue({
            vuetify,
            router,
            i18n,
            store,
            render: h => h(App)
        }).$mount('#app')

        window.onfocus = () => {
            updateToken()
        }
    }
})