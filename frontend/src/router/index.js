import Vue from 'vue'
import VueRouter from 'vue-router'


// import Home from '../views/Home.vue'
import Main from "@/components/Main.vue"
import UserLogin from '@/components/user/UserLogin.vue'
import UserSignUp from '@/components/user/UserSignUp.vue'
// Login Pingpong Test
import TempLogin from '../views/TempLogin.vue'
import RecipeDetail from '@/views/recipe/RecipeDetail.vue'
import RecipeList from '@/views/recipe/RecipeList.vue'
import RecipeCart from '@/views/cart/RecipeCart.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },  
  {
    path: '/user/login',
    name: 'UserLogin',
    component: UserLogin
  },
  {
    path: '/user/signup',
    name: 'UserSignUp',
    component: UserSignUp
  },
  {
    path: '/login',
    name: 'TempLogin',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: TempLogin
  },
  {
    path: '/recipe/detail/:pk',
    name: 'RecipeDetail',
    props: ({params}) => ({pk: Number.parseInt(params.pk, 10) || 0 , summary: params.summary}),
    component: RecipeDetail,
  },
  {
    path: '/recipe/list',
    name: 'RecipeList',
    props: ({params}) => ({produce: params.produce}),
    component: RecipeList,
  },
  {
    path: '/cart/recipe',
    name: 'RecipeCart',
    props: ({params}) => ({pk: Number.parseInt(params.pk, 10) || 0 , summary: params.summary}),
    component: RecipeCart,
  },
  {
    path: "*",
    name: "Error",
    component: RecipeCart,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
