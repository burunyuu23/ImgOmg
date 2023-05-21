<script>
import DnlkkIcon from "./DnlkkIcon.vue";
import Cookies from 'js-cookie';

export default {
    name: "NavBar",
    components: {DnlkkIcon},
    mounted() {
      if (Cookies.get('jwt') !== undefined)
          this.$store.commit('auth');
    }
}
</script>

<template>
    <div class="main">
        <v-card rounded="0">
            <v-toolbar
                    class="toolbar"
                    density="compact"
                    dense>
                <dnlkk-icon/>
                <v-spacer/>
                <v-btn icon
                       v-if="!this.$store.state.isAuth">
                    <v-icon
                            @click="this.$store.commit('start');">
                        mdi-account-arrow-left
                    </v-icon>
                </v-btn>
                <div v-else>
                    <v-btn icon>
                        <v-icon
                                @click="$router.push('/lk')">
                            mdi-account-box
                        </v-icon>
                    </v-btn>
                    <v-btn icon>
                        <v-icon
                                @click="this.$store.commit('logout')">
                            mdi-export
                        </v-icon>
                    </v-btn>
                </div>
            </v-toolbar>
        </v-card>
    </div>
</template>

<style scoped>
.toolbar {
	background: linear-gradient(to right, var(--logo-c), var(--header-bgc));
}

.main dnlkk-icon {
	justify-content: start;
}
</style>