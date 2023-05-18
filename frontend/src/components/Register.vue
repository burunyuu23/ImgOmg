<script>
import {defineComponent} from 'vue'
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

export default defineComponent({
  components: { VueDatePicker },
  name: "Register",
  data() {
    return {
      items: ['Обыватель', 'Студент', 'Дизайнер'],
      visible: false,
      emailRules: {
        required: value => !!value ||
            'Необходимо!',
        email: value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(value) ||
              'Неверный адрес электронной почты!'
        },
        check: (v) => this.emailRules.required(v) ===
            true && this.emailRules.email(v) === true
      },
      login: '',
      password: '',
      repeat_password: '',
      name: '',
      surname: '',
      patronymic: '',
      email: '',
      date: new Date(),
      category: 'Обыватель',
      categoryIndex: 1,
    }
  },
  computed: {
    passwords_incorrect() {
      return this.password !== this.repeat_password
    },
    not_secure_password() {
      return this.password === 'Небезопасный пароль'
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

      return this.emailRules.check(this.email) &&
          !(this.not_secure_password ||
              this.passwords_incorrect ||
              this.hasEmptyFields(reg_data))
    },
    birthdate(){
      return this.date.toISOString().split('T')[0]
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
    },
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
    },
}})
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
                :rules="[emailRules.required, emailRules.email]"
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
            />
            <div
                class="hint"
                v-if="passwords_incorrect">
              Пароли не совпадают
            </div>
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
          <v-col
              cols="12"
          >
            &mdash; Дата рождения*
            <vue-date-picker
                :enable-time-picker="false"
                :flow="['year', 'month', 'calendar']"
                v-model="date"
                :max-date="new Date()"
                :clearable="false"
                auto-apply
                required/>
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
  --dp-primary-color: var(--header-bgc);
  --dp-background-color: rgba(255, 255, 255, 0.04);
  --dp-text-color: white;
  --dp-border-color: rgba(255, 255, 255, 0.33);
  --dp-icon-color: rgba(255, 255, 255, 0.6);
  --dp-border-radius: 4px;

}
</style>

<style>

.dp__theme_light {
  --dp-primary-color: var(--header-bgc);
//--dp-background-color: rgba(255, 255, 255, 0.99);
  --dp-border-radius: 4px;

  position: relative;
}
</style>