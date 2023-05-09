<script>
import {defineComponent} from 'vue'
import Register from "./Register.vue";

export default defineComponent({
    name: "DnlkkDialog",
    components: {Register},
    props: ['dialog']
})
</script>

<template>
    <template>
        <v-row justify="center">
            <v-dialog
                class="dialog"
                    v-model="dialog"
                    persistent
                    width="1024"
            >
                <template v-slot:activator="{ props }">
                    <v-btn
                            color="primary"
                            v-bind="props"
                    >
                        Open Dialog
                    </v-btn>
                </template>
                <div>
                    <video autoplay muted loop class="video-container">
                        <source src="../resources/test.mp4" type="video/mp4"/>
                    </video>
                </div>
                <register/>
            </v-dialog>
        </v-row>
    </template>
</template>

<style scoped>
*{
    color: white;
    text-shadow: 0 0 20px var(--header-bgc);
}
.video-container {
    position: absolute;
    margin: 0;
    height: 100%;
    width: 100%;
    overflow: hidden;
    filter: blur(15px);
    box-shadow: 0 0 100px var(--logo-c);
}
</style>