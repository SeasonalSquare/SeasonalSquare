<template>
    <v-container>
        <div class="title-text"> 
            {{ summary.title }}
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
        <scroll-top/>
    </v-container>
</template>

<script>
import http from '@/util/http-common.js'
import RecipeImage from '@/components/recipe/RecipeImage'
import ScrollTop from '@/components/layout/ScrollTop.vue'
export default {
    components: {
        RecipeImage,
         ScrollTop,
    },
    props: {
        summary: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            main_ingredients : [],
            source_ingredients: [],
            recipe : [],
        }
    },
    async created() {
        await this.fetchRecipe();
    },
    methods: {
        async fetchRecipe() {
            http.get(`/recipe/${this.summary.pk}/`)
            .then(response => {
                this.main_ingredients = response.data.ingredient_data.main_ingredients
                this.source_ingredients = response.data.ingredient_data.source_ingredients
                this.recipe = response.data.recipe
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