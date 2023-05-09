<script>
import {defineComponent} from 'vue'

export default defineComponent({
    name: "Register",
    data() {
        return{
            visible: false,
            email: '',
            rules: {
                required: value => !!value || 'Required.',
                email: value => {
                    const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                    return pattern.test(value) || 'Invalid e-mail.'
                },
            },
        }
    }
})
</script>

<template>
    <v-card>

        <v-card-title class="title">
          <div class="text-h5">Зарегистрируйтесь для начала</div>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                cols="12"
                sm="12"
                md="3"
              >
                <v-text-field
                  label="Логин*"
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
                          @click:append-inner="visible = !visible"
                  ></v-text-field>
              </v-col>

                <v-col cols="6">
                    <v-text-field
                            :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                            :type="visible ? 'text' : 'password'"
                            density="compact"
                            placeholder="Повторите пароль*"
                            prepend-inner-icon="mdi-lock-outline"
                            variant="outlined"
                            @click:append-inner="visible = !visible"
                    ></v-text-field>
                </v-col>

              <v-col
                cols="12"
                sm="6"
              >
                <v-text-field
                  type="date"
                  label="Дата рождения*"
                  required
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
              >
                <v-autocomplete
                  :items="['Обыватель', 'Студент', 'Дизайнер']"
                  label="Ваша категория*"
                ></v-autocomplete>
              </v-col>
            </v-row>
          </v-container>
          <small>* &mdash; Показывает, что данные необходимы</small>
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
            @click="this.$store.commit('exitDialog')"
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

.title {
    display: grid;
    justify-items: center;
    align-items: center;
}


</style>