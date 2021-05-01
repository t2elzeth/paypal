import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/buy-premium',
    name: 'BuyPremium',
    component: () => import('../views/BuyPremium')
  },
  {
    path: '/payment-done',
    name: 'PaymentDone',
    component: () => import('../views/PaymentDone')
  },
  {
    path: '/payment-cancelled',
    name: 'PaymendCancelled',
    component: () => import('../views/PaymentCancelled')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
