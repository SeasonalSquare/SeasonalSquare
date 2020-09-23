import Vue from 'vue'
import VueRouter from 'vue-router'


// import Home from '../views/Home.vue'
import Main from "@/components/Main.vue"
// Login Pingpong Test
import TempLogin from '../views/TempLogin.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/login',
    name: 'TempLogin',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: TempLogin
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
