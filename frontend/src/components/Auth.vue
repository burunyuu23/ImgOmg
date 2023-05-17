<script>
import {defineComponent} from 'vue'

export default defineComponent({
    name: "Auth",
    data() {
        return {
            visible: false,
            login: '',
            password: '',
            rules: {
                required: value => !!value || 'Required.',
                email: value => {
                    const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                    return pattern.test(value) || 'Invalid e-mail.'
                },
            },
        }
    },
    methods: {
        hasEmptyFields(obj) {
            return Object.values(obj).some(val => !val)
        },
        auth() {
            let auth_data;
            if (this.rules.email(this.login) !==
                'Invalid e-mail.'){
                auth_data = {
                    "email": this.login,
                    "password": this.password
                }
            } else {
                auth_data = {
                    "login": this.login,
                    "password": this.password
                }
            }

            if (!this.hasEmptyFields(auth_data)) {
                this.$store.commit('login',
                    auth_data)
            }
        }
    }
})
</script>

<template>
    <v-card>
        <v-card-title class="title text-center">
            <div class="text-h3">Войти</div>
        </v-card-title>
        <v-card-text>
            <v-container>
                <v-row>
                    <v-col cols="12">
                        <v-text-field
                                label="Логин или почта"
                                v-model="login"
                                required
                        ></v-text-field>
                    </v-col>
                    <v-col cols="12">
                        <v-text-field
                                :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                                :type="visible ? 'text' : 'password'"
                                density="compact"
                                placeholder="Введите пароль"
                                prepend-inner-icon="mdi-lock-outline"
                                variant="outlined"
                                v-model="password"
                                @click:append-inner="visible = !visible"
                        ></v-text-field>
                    </v-col>
                </v-row>
            </v-container>
        </v-card-text>
        <v-card-actions>
            <v-spacer/>
            <v-btn
                    variant="text"
                    @click="this.$store.commit('exitDialog')"
            >
                Закрыть
            </v-btn>
            <v-btn
                    variant="text"
                    @click="auth"
            >
                Войти
            </v-btn>
            <v-btn
                    variant="text"
                    @click="this.$emit('sign_in')"
            >
                Зарегистрироваться
            </v-btn>
            <v-spacer/>
        </v-card-actions>
    </v-card>
</template>

<style scoped>

* {
	background: none;
}
</style>