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
              class="d-flex transition-fast-in-fast-out white darken-2 v-card--reveal display-3"
              style="height: 100%; opacity: 0.7;"
            >
              <v-btn
                text
                @click.prevent="moveToRecipeDetail"
                color="#EC8852"
                style="height: 100%; width: 50%; font-size: 0.9rem; font-weight: 800;"
              >
                <div>
                  <v-row>
                    <v-avatar
                      color="#EC8852"
                      size="4rem"
                    >
                      <v-icon x-large color="black">mdi-chef-hat</v-icon>
                    </v-avatar>
                  </v-row>
                  <v-row>
                    <br>
                    레시피
                    <br>
                    바로 보기
                  </v-row>
                </div>
              </v-btn>
              <v-btn
                text
                @click.prevent="moveToRecipeCart"
                style="height: 100%; width: 50%; font-size: 0.9rem; font-weight: 800;"
              >
                <div style="width: 50%;">
                  <v-row>
                    <v-avatar
                      color="black"
                      size="4rem"
                    >
                      <v-icon x-large color="white">mdi-cart-variant</v-icon>
                    </v-avatar>
                  </v-row>
                  <v-row>
                    <br>
                    장바구니
                    <br>
                    담기
                  </v-row>
                </div>
              </v-btn>
            </div>
          </v-expand-transition>
        </v-img>
        <v-card-text>
          <div
            class="card-title"
          >
              {{ recipe.title }}
              <div v-if="recipe.writer" style="font-size: 0.8rem; font-weight: 500">
                <v-icon small color="#FEAA6E">mdi-lead-pencil</v-icon>
                {{ recipe.writer }}
              </div>
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
      this.$store.commit('setSummary', this.recipe);
      this.$router.push({name: 'RecipeDetail'}).catch(() => {});
      this.scrollToTop();
    },
    moveToRecipeCart() {
      this.$store.commit('setSummary', this.recipe);
      this.$router.push({name: 'RecipeCart'}).catch(() => {});
      this.scrollToTop();
    },
    scrollToTop() {
      window.scrollTo(0,0);
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
  font-weight: 700;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  max-width: 210px;
  text-align: center;
}
</style>