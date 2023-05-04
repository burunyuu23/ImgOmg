import { createRouter, createWebHistory } from 'vue-router'
import HomePage from "./views/HomePage.vue";
import EditorPage from "./views/EditorPage.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomePage
    },
    {
        path: '/editor',
        name: 'editor',
        component: EditorPage
    }
]

const router = createRouter({
  history: createWebHistory(''),
  routes
})
export default router