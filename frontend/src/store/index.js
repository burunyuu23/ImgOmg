import {createStore} from 'vuex'
import axios from "axios";
import Cookies from 'js-cookie';

export default createStore({
    state: {
        isAuth: false,
        dialog: false
    },
    getters: {
    },
    actions: {
    },
    mutations: {
        start(state) {
            state.dialog = true;
        },
        exitDialog(state) {
            state.dialog = false;
        }
    },
    modules: {}
})
