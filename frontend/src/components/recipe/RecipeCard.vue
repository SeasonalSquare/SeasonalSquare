<template>
  <div>
    <v-hover v-slot:default="{ hover }">
      <v-card 
        class="d-inline-block mx-auto"
        :elevation="hover ? 12 : 2"
      >
        <v-container>
          <router-link :to="{name: 'RecipeDetail', params: {pk: recipe.pk, summary: recipe}}" tag="div">
            <div style="font-size: 1.5rem; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; text-align: center; max-width:250px; padding-left: 1rem; padding-right: 1rem;">
              {{ recipe.title }}
            </div>
            <RecipeImage
              :src="img"
              :max-width="250"
              :max-height="200"
              style="margin: 1rem;"
            />
            <v-btn
              color="#EC8852"
              text
            >
              레시피 바로 보기
            </v-btn>

            <v-btn
              color="#EC8852"
              text
              @click.prevent="moveToHome"
            >
              장 보러가기
            </v-btn>
          </router-link>
        </v-container>
      </v-card>
    </v-hover>
  </div>
</template>

<script>
import RecipeImage from '@/components/recipe/RecipeImage'

export default {
  name: 'RecipeCard',
  components: {
    RecipeImage
  },
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
      return this.recipe.image
    },
  },
  methods: {
    moveToHome() {
      alert("미구현");
      this.$router.push("/");
    }
  },
}
</script>

<style>

</style>