<template>
  <div>
    <v-tooltip bottom  v-for="(recipe, index) in recipes" :key="index" >
      <template v-slot:activator="{ on, attrs }">
        <v-avatar  v-bind="attrs" v-on="on" style="margin-right:30px;margin-bottom:10px"
            size="95">
            <img :src="recipe.image"  @click="goRecipe(recipe)" >
        </v-avatar>
      </template>
      <span>{{recipe.title}}</span>
    </v-tooltip>
  </div>
</template>

<script>
import http from '@/util/http-common.js'

export default {
  name: 'RecipeMain',
  props : ['food'],
  data() {
    return {
      name: '',
      recipes: [],
    }
  },
  created() {
    http.get(`/recipe/grocery/${this.food}`)
      .then(response => {
      this.recipes = response.data
      this.recipes.splice(6)
      })
      .catch(err => {
      console.log(err)
      })
  },
  methods: {
    goRecipe(recipe){
        this.$router.push({name: 'RecipeDetail', params: {pk: recipe.pk, summary: recipe}});
    }
  }
  
}
</script>

<style>

</style>