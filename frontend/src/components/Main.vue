<template>
<v-app>
  <v-container  fluid style="padding-top:0px"> 
    <v-row align="center" class="text-center">
      <v-col cols="12" align="center" style="padding-top:0px">
        <food-carousel :produces="produces" ></food-carousel>
      </v-col>
    </v-row>
    
    <category-main-food/>


        <!-- <h1>다음은 API위한 테스트 인풋 박스입니다.</h1>
        <v-text-field 
          label="농수산물"
          solo
          v-model="testInput"
          @keypress.enter="textInput"
        >
        </v-text-field>
        <recipe-card  
          v-for="(recipe, index) in recipes" 
          :key="index" 
          :recipe="recipe">
        </recipe-card>  -->
      
  </v-container>
</v-app>
</template>

<script>
  // import http from "@/util/http-common"
  import http from '@/util/http-common.js'
  import httpPro from '@/util/http-produce.js'
  // import RecipeCard from '@/components/recipe/RecipeCard.vue'
  import FoodCarousel from '@/components/layout/FoodCarousel.vue'
  import CategoryMainFood from '@/components/layout/CategoryMainFood.vue'
  //const SERVER_URL = 'http://localhost:8301'


  export default {
    name: 'Main',
    components : {
      // RecipeCard,
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
     textInput() {
       console.log(this.testInput)
       http.get(`/recipe/grocery/${this.testInput}`)
       .then(response => {
        this.recipes = response.data
       })
       .catch(err => {
        console.log(err + "죽인다")
       })
     }
   },
    created() {
      httpPro.get(`/todayProduce`).then(res => {
        // console.log(res.data)
        this.produces=res.data
        this.produces.splice(7)
      }).catch(err => {
        console.log("[Main Cretated] " + err)
      })
    }
  }
</script>
