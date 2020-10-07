<template>
<v-app>
  <v-container  fluid style="padding-top:0px"> 
    <v-row align="center" class="text-center">
      <v-col cols="12" align="center" style="padding-top:0px">
        <food-carousel :produces="produces" ></food-carousel>
      </v-col>
    </v-row>
    
    <category-main-food/>

      
  </v-container>
</v-app>
</template>

<script>
  // import http from '@/util/http-common.js'
  import httpPro from '@/util/http-produce.js'
  // import RecipeCard from '@/components/recipe/RecipeCard.vue'
  import FoodCarousel from '@/components/layout/FoodCarousel.vue'
  import CategoryMainFood from '@/components/layout/CategoryMainFood.vue'
  //const SERVER_URL = 'http://localhost:8301'


  export default {
    name: 'Main',
    components : {
      FoodCarousel,
      CategoryMainFood,
    },
    data() {
      return {
        testInput: '',
        recipes: [],
        produces : null,
      }
   },
   methods:{
   },
    created() {
      httpPro.get(`/todayProduce`).then(res => {
        this.produces=res.data
        this.produces.splice(7)
      }).catch(err => {
        console.log(err)
      })
    }
  }
</script>
