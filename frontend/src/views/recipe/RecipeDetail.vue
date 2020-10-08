<template>
    <v-container>
        <div class="title-text"> 
            {{ summary.title }}
        </div>
        <div style="font-weight: 700; margin-start: 1rem">
            <v-icon color="#FEAA6E">mdi-lead-pencil</v-icon>
            작성자
            {{ summary.writer }}
        </div>
        <div
            class="d-flex"
        >
            <v-col
                style="flex: 1 1 40%; padding-top: 2rem;"
            >
                <RecipeImage
                    :src="summary.image"
                    :max-width="450"
                    :max-height="400"
                    style="margin: auto;"
                />
            </v-col>

            <v-col
                style="flex: 1 1 40%;"
            >
                <v-list
                    disabled
                >
                    <v-subheader>
                        <v-chip
                            color="#BEDDBF"
                            style="font-weight: 600"
                        >
                            재료
                        </v-chip>
                    </v-subheader>
                    <v-list-item-group>
                        <v-list-item
                            v-for="(main_ingredient, i) in main_ingredients"
                            :key = i
                        >
                        <v-list-item-content>
                            <div class="d-flex">
                                <div style="flex: 1 1 40%;">
                                    {{ main_ingredient.ingredient_name }}
                                </div>
                                <div style="flex: 1 1 40%;">
                                    {{ main_ingredient.amount }}
                                </div>
                            </div>
                        </v-list-item-content>
                        </v-list-item>
                    </v-list-item-group>
                </v-list>

                <v-list
                    disabled
                    v-if="source_ingredients.length"
                >
                    <v-subheader>
                        <v-chip
                            color="#BEDDBF"
                            style="font-weight: 600"
                        >
                            양념 재료
                        </v-chip>
                    </v-subheader>
                    <v-list-item-group>
                        <v-list-item
                            v-for="(source_ingredient, j) in source_ingredients"
                            :key = j
                        >
                        <v-list-item-content>
                            <div class="d-flex">
                                <div style="flex: 1 1 40%;">
                                    {{ source_ingredient.source_name }}
                                </div>
                                <div style="flex: 1 1 40%;">
                                    {{ source_ingredient.amount }}
                                </div>
                            </div>
                        </v-list-item-content>
                        </v-list-item>
                    </v-list-item-group>
                </v-list>
            </v-col>
        </div>
        <br>
        <v-divider></v-divider>
        <br>
        <div class="title-text">만드는 법</div>
        <div
            class="d-flex"
                v-for="(step, index) in recipe"
                :key = index
            >
            <v-col
                style="flex: 1 1 10%; text-align: center;"
            >
                <v-avatar
                    size="2.5rem"
                    color="#FFE1A2"
                >
                    {{ step.step }}
                </v-avatar>
            </v-col>
            <v-col
                style="flex: 1 1 30%;"
            >
                <RecipeImage
                    :src="step.image"
                    :max-width="300"
                    :max-height="250"
                />
            </v-col>
            <v-col
                style="flex: 1 1 50%;"
            >
                {{ step.explain }}
            </v-col>
        </div>

        <v-divider></v-divider>
        <div class="title-text">연관 추천 레시피</div>
        <v-container style="display: flex; flex-wrap: wrap; justify-content: space-evenly;">
            <recipe-card
                v-for="(recipe, index) in rel_recipes" 
                :key="index" 
                :recipe="recipe"
                style="margin: 1rem;">
            </recipe-card>
        </v-container>

        <div class="title-text">색다른 추천 레시피</div>
        <v-container style="display: flex; flex-wrap: wrap; justify-content: space-evenly;">
            <recipe-card
                v-for="(recipe, index) in unrel_recipes" 
                :key="index" 
                :recipe="recipe"
                style="margin: 1rem;">
            </recipe-card>
        </v-container>
        <scroll-top/>
    </v-container>
</template>

<script>
import { mapState } from 'vuex'

import http from '@/util/http-common.js'
import RecipeImage from '@/components/recipe/RecipeImage'
import RecipeCard from '@/components/recipe/RecipeCard'
import ScrollTop from '@/components/layout/ScrollTop.vue'

export default {
    components: {
        RecipeImage,
        RecipeCard,
        ScrollTop,
    },
    props: {
        summary: {
            type: Object,
            required: true,
        },
    },
    computed: {
        ...mapState(['token']),
    },
    watch: {
        summary: {
            deep: true,
            handler : function () {
                this.fetchRecipe();
            }
        }
    },
    data() {
        return {
            main_ingredients : [],
            source_ingredients: [],
            recipe : [],
            rel_recipes: [],
            unrel_recipes: [],
        }
    },
    async created() {
        await this.fetchRecipe();
    },
    methods: {
        async fetchRecipe() {
            http.get(`/recipe/${this.summary.pk}/`,{
                headers: {
                    "Authorization": this.token,
                }
            })
            .then(response => {
                this.main_ingredients = response.data.ingredient_data.main_ingredients
                this.source_ingredients = response.data.ingredient_data.source_ingredients
                this.recipe = response.data.recipe
                this.rel_recipes = response.data.recommend.rel_recipes
                this.unrel_recipes = response.data.recommend.unrel_recipes
            })
            .catch(() => {
                this.$dialog.notify.error('레시피를 불러올 수 없습니다.', {
                    position: 'top-right',
                    timeout: 2000
                })
            })
        }
    },
}
</script>

<style scoped>
.title-text {
    font-size: 1.7rem;
    font-weight: 700;
    margin: 1rem;
    color: #5C5749;
}
</style>