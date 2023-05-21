import {createApp} from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import {loadFonts} from './plugins/webfontloader'
import router from "./router.js"
import axios from 'axios'
import store from "./store/index.js";
import mixins from "./mixins/index.js";
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

loadFonts()

const app = createApp(App)

app.config.globalProperties.$axios = axios;

mixins.forEach(mixin => {
    app.mixin(mixin)
})

app
    .component('VueDatePicker', VueDatePicker)
    .use(store)
    .use(vuetify)
    .use(router)
    .mount('#app')
