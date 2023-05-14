import {createStore} from 'vuex'
import axios from "axios";
import Cookies from 'js-cookie';
import {BASE_URL} from "../baseUrl.js";

export default createStore({
    state: {
        isAuth: false,
        dialog: false,
        response: '',
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
        },
        async registration(state, data) {
            // state.dialog = false;
            console.log(data);
            await axios.post(`${BASE_URL}/user/signup`,
                data)
                .then(response => {
                    Cookies.set('jwt', `${response.data['access token']}`, {
                        expires: 7,
                        path: ''});
                    state.response = "Спасибо за регистрацию!";
                    state.dialog = false;
                    state.isAuth = true;
                })
                .catch(error => {
                    if (error.response.status === 403) {
                        state.response = error.response.data.detail;
                    } else {
                        state.response = "Возникла" +
                            " непредвиденная ошибка!" +
                            " Какой кошмар...";
                    }})
        },
        async login(state) {
            
        }

    },
    modules: {}
})
