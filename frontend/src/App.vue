<template>
    <v-app app>
        <nav-bar/>
        <v-main class="main">
            <router-view/>
        </v-main>
    </v-app>
</template>

<script>

import NavBar from "./components/NavBar.vue";

export default {
    name: 'App',
    components: {NavBar},
}
</script>

<style scoped>
.main{
    background: var(--main-bgc);
}
</style>
