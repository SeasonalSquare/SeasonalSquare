import Vue from 'vue'
import VueRouter from 'vue-router'


// import Home from '../views/Home.vue'
import Main from "@/components/Main.vue"
import UserLogin from '@/components/user/UserLogin.vue'
import UserSignUp from '@/components/user/UserSignUp.vue'
import UserProfile from '@/components/user/UserProfile.vue'
import ProduceMore from '@/components/produce/ProduceMore.vue'
import RecipeDetail from '@/views/recipe/RecipeDetail.vue'
import RecipeList from '@/views/recipe/RecipeList.vue'
import RecipeCart from '@/views/cart/RecipeCart.vue'
import AllCart from '@/views/cart/AllCart.vue'

import Error from '@/views/error/Error.vue'

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
    path: '/produce/more',
    name: 'ProduceMore',
    component: ProduceMore
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
    path: '/cart/all',
    name: 'AllCart',
    component: AllCart,
  },
  {
    path: '/user/profile',
    name: 'UserProfile',
    component: UserProfile,
  },
  {
    path: "*",
    name: "Error",
    component: Error,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior () {
    return { x: 0, y: 0 };
  }
})

export default router
