import {createStore} from 'vuex'
import axios from "axios";
import Cookies from 'js-cookie';
import {BASE_URL} from "../baseUrl.js";
import {profileMixin} from "../mixins/profileMixin.js";
export default createStore({
    mixins: [profileMixin],
    state: {
        isAuth: false,
        dialog: false,
        response: '',
        profile: {
            login: '',
            fullname: '',
            email: '',
            birthdate: '',
            category: '',
        }
    },
    getters: {},
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
                        path: ''
                    });
                    console.log(response)
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
                    }
                })
        },
        async login(state, data) {
            console.log(data);
            await axios.post(`${BASE_URL}/user/login`,
                data)
                .then(response => {
                    Cookies.set('jwt', `${response.data['access token']}`, {
                        expires: 7,
                        path: ''
                    });
                })
                .catch(error => {
                    if (error.response.status === 403) {
                        state.response = error.response.data.detail;
                    } else {
                        state.response = "Возникла" +
                            " непредвиденная ошибка!" +
                            " Какой кошмар...";
                    }
                })
                .finally(() => {
                    this.commit('auth');
                })

            console.log(state.profile)
        },
        async logout(state) {
            axios.get(`${BASE_URL}/user/logout`)
                .then(response => {
                    state.profile = response.data
                    Cookies.remove('jwt');
                })
                .catch(error => {
                    return Promise.reject(error)
                })

            state.isAuth = false
        },
        async auth(state) {
            await axios.get(`${BASE_URL}/user/profile`,
                {
                    headers: {
                        'Authorization':
                            'Bearer ' +
                            Cookies.get('jwt')
                    }
                })
                .then(response => {
                    let data = response.data

                    state.profile = {
                        login: data.login,
                        fullname: profileMixin.methods.fullName(data.name, data.surname, data.patronymic),
                        email: data.email,
                        birthdate: profileMixin.methods.formatDate(data.birthdate),
                        category: data.category,
                    }
                    state.isAuth = true

                    state.response = ''
                    state.dialog = false
                })
                .catch(error => {
                    console.error(error)
                })
        }

    },
    modules: {}
})
