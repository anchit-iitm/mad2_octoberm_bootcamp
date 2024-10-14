import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import TestView from '../views/test.vue'
import LoginView from '../views/LoginView.vue'
import searchView from '../views/search.vue'

const routes = [
  // {
  //   path: '/',
  //   name: 'home',
  //   component: HomeView
  // },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // },
  {
    // component: () => import('@/views/test.vue'),
    component: TestView,
    path: '/testsjdvbnskjv',
    name: 'test'
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('@/views/register.vue')
  },
  {
    path: '/create',
    name: 'create',
    component: () => import('@/views/create.vue')
  },
  {
    path: '/update/:id', // /api/category/<int:id>
    name: 'update',
    component: () => import('@/views/update.vue'),
  },
  {
    path: '/search',
    name: 'search',
    component: searchView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
