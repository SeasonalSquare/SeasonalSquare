<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
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
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  // import http from "@/util/http-common"
  import axios from 'axios'
  import RecipeCard from '@/components/RecipeCard.vue'
  const SERVER_URL = 'http://localhost:8301'


  export default {
    name: 'HelloWorld',
    components : {
      RecipeCard,
    },
    data() {
      return {
        testInput: '',
        recipes: [],
      }
   },
   methods:{
     textInput() {
       console.log(this.testInput)
       axios.get(`${SERVER_URL}/api/recipe/grocery/${this.testInput}`)
       .then(response => {
        this.recipes = response.data
       })

     }
   }
  }
</script>
