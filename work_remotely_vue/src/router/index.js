

import { createRouter, createWebHistory } from 'vue-router'

// Home
import HomeView from '../views/HomeView.vue'

// Home
import AboutView from '../views/AboutView.vue'

// Authentication
import LoginView from '../views/Authentication/LoginView.vue'

// Account
import ProfileView from '../views/Account/ProfileView.vue'

// 404 catchall Page Not Found
import PageNotFound from "@/components/PageNotFound/PageNotFound.vue";



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView,
    },
    // 404 Catchall Page Not Found
    {
      path: "/:catchAll(.*)",
      name: "PageNotFound",
      component: PageNotFound
    },
    // Authentication [ Login ]
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    // Account [ Profile ]
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView,
      meta: {
        requireLogin: true
      }
    },

    // Redirect to login if not authenticated

  ],
})

export default router
