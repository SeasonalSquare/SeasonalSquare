<template>
<v-app>
  <v-container  > 
    <v-row align="center" class="text-center">
      <v-col cols="12" align="center">
        <food-carousel :foods="foods" ></food-carousel>
      </v-col>
    </v-row>
    <v-row  align="center" class="text-center"> 
      <category-main-food/>
    </v-row>


        <h1>다음은 API위한 테스트 인풋 박스입니다.</h1>
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
        </recipe-card> 
      
  </v-container>
</v-app>
</template>

<script>
  // import http from "@/util/http-common"
  import http from '@/util/http-common.js'
  import RecipeCard from '@/components/RecipeCard.vue'
  import FoodCarousel from '@/components/layout/FoodCarousel.vue'
  import CategoryMainFood from '@/components/layout/CategoryMainFood.vue'
  //const SERVER_URL = 'http://localhost:8301'


  export default {
    name: 'Main',
    components : {
      RecipeCard,
      FoodCarousel,
      CategoryMainFood,
    },
    data() {
      return {
        testInput: '',
        recipes: [],
        foods : null,
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
      http.get(`/recipe/grocery/감자`).then(res => {
        // console.log(res.data)
        this.foods=res.data
        this.foods.splice(7)
      }).catch(err => {
        console.log(err + "죽인다")
      })
    }
  }
</script>
