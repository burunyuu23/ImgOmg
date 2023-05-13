import Vue from 'vue'
import Keycloak from 'keycloak-js'

const initOptions = {
    url: process.env.VUE_APP_KEYCLOAK_URL,
    realm: 'list-keep',
    clientId: 'list-keep'
}

const keycloak = Keycloak(initOptions)

const KeycloakPlugin = {
    install: Vue => {
        Vue.$keycloak = keycloak
    }
}

Vue.use(KeycloakPlugin)

export default KeycloakPlugin