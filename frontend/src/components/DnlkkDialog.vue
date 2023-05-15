<script>
import {defineComponent} from 'vue'
import Register from "./Register.vue";
import Auth from "./Auth.vue";

export default defineComponent({
    name: "DnlkkDialog",
    components: {Auth, Register},
    data() {
        return {
            isSignUp: true
        }
    },
    props: ['dialog'],
    methods: {
        sign_in() {
            this.isSignUp = !this.isSignUp
        },
    },
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
                <div class="video-container">
                    <video autoplay muted loop class="video-container">
                        <source src="../resources/test.mp4" type="video/mp4"/>
                    </video>
                </div>
                <register v-if="isSignUp" @sign_in="sign_in"/>
                <auth v-else @sign_in="sign_in"/>
                <div style="clear:both;"> </div>
            </v-dialog>
        </v-row>
    </template>
</template>

<style scoped>
*{
    color: white;
    text-shadow: 0 0 20px var(--header-bgc);
}
.dialog {
}
.video-container {
    position: absolute;
    margin: 0;
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    overflow: hidden;
    filter: blur(15px);
    box-shadow: 0 0 100px var(--logo-c);
}
video {
    object-fit: fill
}
</style>