<template>
  <div>
    <img :src="img">
    <p>{{ recipe.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'RecipeCard',
  props : {
    recipe: {
      type: Object,
    }
  },
  data() {
    return {
      name: ''
    }
  },
  computed: {
    img() {
      console.log(this.recipe)
      return this.recipe.image
    }
    
    
  }
  
}
</script>

<style>

</style>