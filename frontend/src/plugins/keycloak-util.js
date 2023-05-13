import Vue from 'vue'

const TOKEN_MIN_VALIDITY_SECONDS = 70

export async function updateToken  () {
    await Vue.$keycloak.updateToken(TOKEN_MIN_VALIDITY_SECONDS)
    return Vue.$keycloak.token
}