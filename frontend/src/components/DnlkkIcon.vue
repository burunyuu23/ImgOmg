<script>
import {defineComponent} from 'vue'

export default defineComponent({
    name: "DnlkkIcon"
})
</script>

<template>
    <div class="imgomg ml-5">
        <div>
            <video autoplay muted loop class="video-container">
                <source src="../resources/test.mp4" type="video/mp4"/>
            </video>
            <a
                    class="imgomg__text font-weight-medium"
                    href="/">
                ImgOmg
            </a>
        </div>
        <div class="wrapper">
            <div class="">&nbsp;∧,,,∧</div>
            <div class="">( ̳• · • ̳)</div>
            <div class="">/ づ♡</div>
        </div>
    </div>
</template>

<style scoped>
.imgomg {
    display: grid;
    grid-template-columns: max-content max-content;
    grid-template-rows: max-content;

    align-items: center;
    width: 255px;

    background-color: var(--main-bgc);
    border-radius: 100px 100px 0 0;
    color: white;

    box-shadow: 0 0 0 black;
    transition: 1s linear;
}
.imgomg:hover {
    box-shadow: 0 0 20px black;
}
.imgomg:active {
    color: var(--header-bgc);
}


.imgomg__text {
    text-decoration: none;
    color: white;

    display: flex;

    margin-left: 50px;
    justify-self: end;
    justify-content: end;
    justify-items: end;

    font-size: 32px;
    transition: 1s linear;
}
.imgomg__text:hover {
    color: black;
    transition: 1s linear;
}
.imgomg__text:active {
    color: var(--header-bgc);
}

.wrapper {
    font-size: 12px;
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr 1fr 1fr;
}

.video-container {
    border-radius: 50px 50px 0 0;
    position: absolute;
    background-size: auto;
    object-fit: cover;
    pointer-events: none;
    width: 255px;
    opacity: 50%;
    display: grid;
    grid-template-columns: max-content max-content;
    grid-template-rows: max-content;

    align-items: center;
    transition: 1s linear;
}

@media screen and (max-width: 380px) {
    .imgomg {
        width: 196px;
    }

    .imgomg__text {
        font-size: 16px;
    }

    .video-container {
        width: 196px;
        top:0;
    }
}
</style>