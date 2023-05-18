<template>
    <v-app app class="app">
        <nav-bar/>
        <v-main class="main">
            <video autoplay muted loop class="video-container">
                <source src="../src/resources/test.mp4" type="video/mp4"/>
            </video>
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
.video-container {
    background: url('../src/resources/test.mp4') no-repeat center center fixed;
    position: absolute;
    background-size: auto;
    object-fit: cover;
    pointer-events: none;
    width: 100vw;
    height: calc(100vh - 48px);
    top: 48px;

    opacity: 100%;
}

.main {
    background: var(--main-bgc);
}
</style>
