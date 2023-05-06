<script>
import {defineComponent} from 'vue'

export default defineComponent({
    name: "DnlkkIcon"
})
</script>

<template>
    <div class="imgomg ml-5">
        <div>
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
}

.imgomg__text {
    text-decoration: none;
    color: var(--logo-c);

    display: flex;

    font-size: 32px;

    margin-left: 50px;
    justify-self: end;
    justify-content: end;
    justify-items: end;
}

.wrapper {
    font-size: 12px;
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr 1fr 1fr;
}


@media screen and (max-width: 380px) {

.imgomg {
    width: 196px;
}
    .imgomg__text {
        font-size: 16px;
    }
}
</style>