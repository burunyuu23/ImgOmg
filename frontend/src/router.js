import { createRouter, createWebHistory } from 'vue-router'
import HomePage from "./views/HomePage.vue";
import CabinetPage from "./views/CabinetPage.vue";
import TestPage from "./views/TestPage.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomePage
    },
    {
        path: '/lk',
        name: 'lk',
        component: CabinetPage
    },
    {
        path: '/test',
        name: 'test',
        component: TestPage
    }
]

const router = createRouter({
  history: createWebHistory(''),
  routes
})
export default router