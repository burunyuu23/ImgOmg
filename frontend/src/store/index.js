import {createStore} from 'vuex'
import axios from "axios";
import Cookies from 'js-cookie';
import {AUTH_URL, EDIT_URL} from "../baseUrl.js";
import {profileMixin} from "../mixins/profileMixin.js";
export default createStore({
    mixins: [profileMixin],
    state: {
        isLoaded: false,
        isAuth: false,
        dialog: false,
        response: '',
        image: new Image(),
        save_image: new Image(),
        profile: {
            login: '',
            fullname: '',
            email: '',
            birthdate: '',
            category: '',
        },
        req: {
            image: new Image(),
            methods: {
                color: {
                    brightness: 100,
                    saturation: 100,
                    contrast: 100,
                    sepia: 0,
                    grayscale: 0,
                    invert: 0
                },
                size: [0, 0, 0, 0],
                compress: 102,
                prikols: {
                    prikol: '',
                    file: ''
                }
            }
        },
        layers: [],
    },
    getters: {
        getImage(state){
            return state.image
        },
        getReqImage(state){
            return state.req.image
        },
        getProfile(state){
            return state.profile
        },
        getSize(state) {
            return state.req.methods.size
        },
        getColor(state) {
            return state.req.methods.color
        }
    },
    actions: {
    },
    mutations: {
        setSize(state, arr){
          state.req.methods.size = arr
        },
        start(state) {
            state.dialog = true;
        },
        exitDialog(state) {
            state.dialog = false;
        },
        async registration(state, data) {
            // state.dialog = false;
            // console.log(data);
            await axios.post(`${AUTH_URL}/user/signup`,
                data)
                .then(response => {
                    Cookies.set('jwt', `${response.data['access token']}`, {
                        expires: 7,
                        path: ''
                    });
                    // console.log(response)
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
            // console.log(data);
            await axios.post(`${AUTH_URL}/user/login`,
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

            // console.log(state.profile)
        },
        async logout(state) {
            axios.get(`${AUTH_URL}/user/logout`)
                .then(response => {
                    state.profile = response.data
                    Cookies.remove('jwt');
                })
                .catch(error => {
                    return Promise.reject(error)
                })

            state.isAuth = false
            state.isLoaded = false;
        },
        async auth(state) {
            await axios.get(`${AUTH_URL}/user/profile`,
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
        },
        async upload(state, image) {
            state.isLoaded = true;
            state.req.image = image
            // console.log(image)

            await axios.post(`${EDIT_URL}/upload`,
                {login: state.profile.login, req: state.req})
                .then(resp => {
                    // console.log('SUCCESS!!');
                    if (state.req.methods.compress !== 102)
                        state.req.image = resp.data.image

                    state.save_image = state.image
                    state.image = new Image()
                    state.image.src = resp.data.image
                    state.layers.push(state.image)
                    state.req.methods.size = [0, state.image.naturalWidth, 0, state.image.naturalHeight]
                })
                .catch(err => {
                    // console.log('FAILURE!!');
                    // console.log(err);
                });
            this.commit('refresh')
        },
        async get_compress(state) {
            await axios.post(`${EDIT_URL}/compress_size`,
                {login: state.profile.login, rate: state.req.methods.compress})
                .then(resp => {
                    // console.log('SUCCESS!!');

                    state.save_image = state.image
                    state.image = new Image()
                    state.image.src = resp.data.image
                })
                .catch(err => {
                    // console.log('FAILURE!!');
                    // console.log(err);
                });
            state.req.methods.prikols = {
                prikol: '',
                file: ''
            }
        },
        async get_prikol(state) {
            await axios.post(`${EDIT_URL}/pre_prikol`,
                {login: state.profile.login, prikol: state.req.methods.prikols})
                .then(resp => {
                    // console.log('SUCCESS!!');

                    state.save_image = state.image
                    state.image = new Image()
                    state.image.src = resp.data.image

                    state.req.methods.prikols.file = resp.data.file
                })
                .catch(err => {
                    // console.log('FAILURE!!');
                    // console.log(err);
                });
            state.req.methods.compress = state.req.methods.compress === 102 ? 102 : 101
        },
        refreshing(state){
            state.image = state.save_image
        },
        refresh(state){
            state.req.methods.color = {
                brightness: 100,
                saturation: 100,
                contrast: 100,
                sepia: 0,
                grayscale: 0,
                invert: 0}
            state.req.methods.compress = state.req.methods.compress === 102 ? 102 : 101
            state.req.methods.size = [0, state.image.naturalWidth, 0, state.image.naturalHeight]
            state.req.methods.prikols = {
                prikol: '',
                file: ''
            }
        },
        chooseLayer(state, num){
            state.image = state.layers[num];
            state.save_image = state.layers[num];
            state.req.image = state.image.src
            this.commit('refresh');
            this.commit('upload', state.image.src)
            state.layers = state.layers.slice(0, num);
        }
    },
    modules: {}
})
