import {createApp} from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import {loadFonts} from './plugins/webfontloader'
import router from "./router.js"
import axios from 'axios'
import store from "./store/index.js";
import mixins from "./mixins/index.js";


loadFonts()

const app = createApp(App)

app.config.globalProperties.$axios = axios;

mixins.forEach(mixin => {
    app.mixin(mixin)
})

app
    .use(store)
    .use(vuetify)
    .use(router)
    .mount('#app')
