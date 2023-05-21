<script>
import {defineComponent} from 'vue'
import VueDatePicker from "@vuepic/vue-datepicker";
import {profileMixin} from "../mixins/profileMixin.js";
export default defineComponent({
    name: "Register",
  mixins: [profileMixin],
  components: {VueDatePicker},
    data() {
        return {
            items: ['Обыватель', 'Студент', 'Дизайнер'],
            visible: false,
            rules: {
                required: value => !!value || 'Required.',
                email: value => {
                    const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                    return pattern.test(value) || 'Invalid e-mail.'
                },
            },
            login: '',
            password: '',
            repeat_password: '',
            name: '',
            surname: '',
            patronymic: '',
            email: '',
            birthdate: new Date(),
            category: 'Обыватель',
            categoryIndex: 1,
        }
    },
    computed: {
      date() {
        return this.formatDate(this.birthdate.toISOString().split('T')[0], false);
      },
        passwords_incorrect() {
            return this.password !== this.repeat_password
        },
        not_secure_password() {
            return this.password === 'not a secure password'
        },
        can_reg() {
            let reg_data = {
                "login": this.login,
                "name": this.name,
                "surname": this.surname,
                "email": this.email,
                "birthdate": this.birthdate,
                "category": this.categoryIndex
            }

            return this.rules.email(this.email) !== 'Invalid e-mail.' &&
                !(this.not_secure_password ||
                    this.passwords_incorrect ||
                    this.hasEmptyFields(reg_data))

        }
    },
    methods: {
        hasEmptyFields(obj) {
            return Object.values(obj).some(val => !val)
        },
        reg() {
            let reg_data = {
                "login": this.login,
                "password": this.password,
                "name": this.name,
                "surname": this.surname,
                "patronymic": this.patronymic,
                "email": this.email,
                "birthdate": this.birthdate,
                "category": this.categoryIndex
            }

            if (this.can_reg) {
                this.$store.commit('registration',
                    reg_data)
            }
        }
        ,
        onPasswordChange(value) {
            if (value.target.value.length > 6)
                this.password = value.target.value
            else
                this.password = 'not a secure password'
        }
    },
    watch: {
        category(newValue) {
            this.categoryIndex = this.items.findIndex(
                (item) => item === newValue) + 1;
        }
    }
})
</script>

<template>
    <v-card>
        <v-card-title class="title">
            <div class="text-h3">Зарегистрируйтесь для
                начала
            </div>
        </v-card-title>
        <v-card-text>
            <div class="text-h5 text-center"
                 v-if="!can_reg">Не
                оставляйте
                обязательные поля
                незаполненными!
            </div>
            <div class="text-h5 text-center"
                 v-else-if="this.$store.state.response.length >
             0">
                {{ this.$store.state.response }}
            </div>
            <v-container>
                <v-row>
                    <v-col
                            cols="12"
                            sm="12"
                            md="3"
                    >
                        <v-text-field
                                label="Логин*"
                                v-model="login"
                                required
                        ></v-text-field>
                    </v-col>

                    <v-col
                            cols="12"
                            sm="4"
                            md="3"
                    >
                        <v-text-field
                                label="Фамилия*"
                                v-model="surname"
                                required
                        ></v-text-field>
                    </v-col>

                    <v-col
                            cols="12"
                            sm="4"
                            md="3"
                    >
                        <v-text-field
                                label="Имя*"
                                v-model="name"
                                required
                        ></v-text-field>
                    </v-col>

                    <v-col
                            cols="12"
                            sm="4"
                            md="3"
                    >
                        <v-text-field
                                label="Отчество"
                                v-model="patronymic"
                                hint="Если есть"
                                persistent-hint
                        ></v-text-field>
                    </v-col>

                    <v-col cols="12">
                        <v-text-field
                                v-model="email"
                                :rules="[rules.required, rules.email]"
                                label="Почта*"
                        ></v-text-field>
                    </v-col>


                    <v-col cols="6">
                        <v-text-field
                                :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                                :type="visible ? 'text' : 'password'"
                                density="compact"
                                placeholder="Введите пароль*"
                                prepend-inner-icon="mdi-lock-outline"
                                variant="outlined"
                                @change="onPasswordChange"
                                @click:append-inner="visible = !visible"
                        ></v-text-field>
                        <div
                                class="hint"
                                v-if="not_secure_password">
                            Пароль меньше 7 символов
                        </div>
                    </v-col>

                    <v-col cols="6">
                        <v-text-field
                                :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                                :type="visible ? 'text' : 'password'"
                                density="compact"
                                placeholder="Повторите пароль*"
                                v-model="repeat_password"
                                prepend-inner-icon="mdi-lock-outline"
                                variant="outlined"
                                @click:append-inner="visible = !visible"
                        ></v-text-field>
                        <div
                                class="hint"
                                v-if="passwords_incorrect">
                            Пароли не совпадают
                        </div>
                    </v-col>

                    <v-col
                            cols="12"
                    >
                      <vue-date-picker
                          class="dp__theme_light"

                          :max-date="new Date()"
                          :enable-time-picker="false"
                          auto-apply
                          v-model="birthdate"
                          :format="date" >
                      </vue-date-picker>
                    </v-col>
                    <v-col
                            cols="12"
                    >
                        <v-autocomplete
                                :items="items"
                                label="Ваша категория*"
                                v-model="category"
                        ></v-autocomplete>
                    </v-col>
                </v-row>
            </v-container>
            <small>* &mdash; Показывает, что данные
                необходимы</small>
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
                    @click="reg"
            >
                Зарегистрироваться
            </v-btn>
            <v-btn
                variant="text"
                @click="this.$emit('sign_in')"
            >
                Войти
            </v-btn>
            <v-spacer/>
        </v-card-actions>
    </v-card>
</template>

<style scoped>
* {
	background: none;
}

.title {
	display: grid;
	justify-items: center;
	align-items: center;
}

.hint {
	color: transparent;
	text-shadow: 0 0 1px black;
}

.dp__theme_light {
  --dp-background-color: none;
  --dp-text-color: white;
  --dp-hover-color: #f3f3f3;
  --dp-hover-text-color: #212121;
  --dp-hover-icon-color: #959595;
  --dp-primary-color: #1976d2;
  --dp-primary-text-color: #f8f5f5;
  --dp-secondary-color: #c0c4cc;
  --dp-border-color: rgba(233, 233, 233, 0.55);
  --dp-menu-border-color: #ddd;
  --dp-border-color-hover: #aaaeb7;
  --dp-disabled-color: #f6f6f6;
  --dp-scroll-bar-background: #f3f3f3;
  --dp-scroll-bar-color: #959595;
  --dp-success-color: #76d275;
  --dp-success-color-disabled: #a3d9b1;
  --dp-icon-color: #959595;
  --dp-danger-color: #ff6f60;
  --dp-highlight-color: rgba(25, 118, 210, 0.1);
}
</style>

<style>

.dp__theme_light {
  --dp-primary-color: var(--header-bgc);
}
</style>