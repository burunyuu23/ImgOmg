<script setup>

import DnlkkIcon from "./DnlkkIcon.vue";
</script>

<template>
    <v-card
            color="#2ec587"
            flat
            rounded="0"
    >
        <v-toolbar density="compact"
                   color="#2ec587">

            <dnlkk-icon/>

            <v-spacer></v-spacer>

            <v-btn icon v-if="!this.$store.state.isAuth">
                <v-icon>mdi-account-arrow-left</v-icon>
            </v-btn>
            <div v-else>
                <v-btn icon>
                    <v-icon>mdi-account-box</v-icon>
                </v-btn>
                <v-btn icon>
                    <v-icon>mdi-export</v-icon>
                </v-btn>
            </div>
        </v-toolbar>
    </v-card>
</template>

<style scoped>
* {
    background: var(--header-bgc);
}

.main {
    display: grid;
    grid-template-columns: auto auto auto auto;
    grid-template-rows: auto;

    align-self: center;
    align-items: center;
    align-content: center;

    justify-content: start;

    margin: 0;
}

.main dnlkk-icon {
    justify-content: start;
}
</style>