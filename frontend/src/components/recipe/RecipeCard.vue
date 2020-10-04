<template>
  <div>
    <v-hover v-slot:default="{ hover }">
      <v-card
        class="mx-auto"
        color="grey lighten-4"
        max-width="600"
      >
        <v-img 
          :src="img"
          max-width="250"
          max-height="200">
          <v-expand-transition>
            <div
              v-if="hover"
              class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal display-3"
              style="height: 100%;"
            >
              <v-btn
                text
                @click.prevent="moveToRecipeDetail"
                color="black"
                style="height: 100%; font-size: 1.3rem; font-weight: 600;"
              >
                레시피
                <br>
                바로 보기
              </v-btn>
              <v-btn
                text
                @click.prevent="moveToRecipeCart"
                style="height: 100%; font-size: 1.3rem; font-weight: 600;"
              >
                장 보러
                <br>
                가기
              </v-btn>
            </div>
          </v-expand-transition>
        </v-img>
        <v-card-text>
          <div
            class="card-title"
          >
            {{ recipe.title }}
          </div>
        </v-card-text>
      </v-card>
    </v-hover>
  </div>
</template>

<script>
export default {
  name: 'RecipeCard',
  props : {
    recipe: {
      type: Object,
      required: true,
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
    moveToRecipeDetail() {
      this.$router.push({name: 'RecipeDetail', params: {pk: this.recipe.pk, summary: this.recipe}});
    },
    moveToRecipeCart() {
      this.$router.push({name: 'RecipeCart', params: {pk: this.recipe.pk, summary: this.recipe}});
    }
  },
}
</script>

<style scoped>
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: .5;
  position: absolute;
  width: 100%;
}
.card-title {
  color: #5C5749;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  max-width: 210px;
  text-align: center;
}
</style>