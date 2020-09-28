<template>
    <v-container>
        <div
            class="d-flex"
        >
            <v-col
                style="flex: 1 1 20%; padding-top: 2rem;"
            >
                <RecipeImage
                    :src="summary.image"
                    :max-width="450"
                    :max-height="400"
                    style="margin: auto;"
                />
                <div style="font-size: 1rem; margin: 1rem; color: #5C5749;"> 
                    {{ summary.title }}
                </div>
            </v-col>

            <v-col
                style="flex: 1 1 60%;"
            >
            <div class="sub-title">
                재료
            </div>
                <div
                    v-for="(main_ingredient, i) in main_ingredients"
                    :key = i
                    class="d-flex"
                >
                    <div style="flex: 1 1 40%; margin-top: 16px; padding-top: 4px; text-align: center;">
                        가격 xxxx원
                    </div>
                    <div style="flex: 1 1 40%;">
                        <v-checkbox
                            color="#EC8852"
                            :value="main_ingredient.ingredient_name"
                            :label="main_ingredient.ingredient_name + main_ingredient.amount"
                        >
                        </v-checkbox>
                    </div>
                </div>

                <div v-if="source_ingredients.length">
                    <div
                        v-for="(source_ingredient, j) in source_ingredients"
                        :key = j
                        class="d-flex"
                    >
                        <div style="flex: 1 1 40%; margin-top: 16px; padding-top: 4px; text-align: center;">
                            가격 xxxx원
                        </div>
                        <div style="flex: 1 1 40%;">
                            <v-checkbox
                                color="#EC8852"
                                :value="source_ingredient.source_name"
                                :label="source_ingredient.source_name + source_ingredient.amount"
                            >
                                <!-- <template #label :class="checkClass"> {{ source_ingredient.source_name }}</template> -->
                            </v-checkbox>
                        </div>
                    </div>
                </div>
                
                <v-divider></v-divider>
                <v-col class="d-flex">
                    <div style="flex: 1 1 40%; text-align: center; align-self: center;">
                        예상가격 xxxx원
                    </div>
                    <div style="flex: 1 1 40%;">
                        <v-btn icon x-large @click.once="addToCart">
                            <v-icon v-if="!isInCart">mdi-cart-outline</v-icon>
                            <v-icon v-else color="#EC8852">mdi-cart</v-icon>
                        </v-btn>
                    </div>
                </v-col>
            </v-col>
        </div>

        <v-divider></v-divider>
        <br>
        <div class="sub-title"> 만드는 법 </div>
        <div
            class="d-flex"
            v-for="(step, index) in recipe"
            :key = index
        >
            <v-col
                style="text-align: end;"
            >
                <v-avatar
                    size="2rem"
                    color="#FFE1A2"
                >
                    {{ step.step }}
                </v-avatar>
            </v-col>
            <v-col
                style="flex: 1 1 70%;"
            >
                {{ step.explain }}
                <v-divider></v-divider>
            </v-col>
        </div>
    </v-container>
</template>

<script>
import http from '@/util/http-common.js'
import RecipeImage from '@/components/recipe/RecipeImage'

export default {
    components: {
        RecipeImage,
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
            isInCart : false,
            notHaveIngredients : [],
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
            .catch(err => {
                console.log(err)
            })
        },
        addToCart() {
            this.isInCart = true
            alert("담길 예정이에요")
        },
        check(event) {
            console.log("check 함수 " + event)
            // if(!event) this.notHaveIngredients.push(event);
            // console.log(this.notHaveIngredients)
            // if(event) return 'checked-label'
            // else return 'unchecked-label'
            this.checkClass(event);
        },
        checkClass(event) {
            console.log("checkClass " + event)
            if(event) return 'checked-label'
            else return 'unchecked-label'
        },
    },
}
</script>

<style scoped>
.v-input--is-label-active label {
  text-decoration: line-through !important;
}
.text-green input {
    color: green !important;
}
.sub-title{
    font-weight: 700;
    font-size: 1.5rem;
    line-height: 32px;
    letter-spacing: -0.3px;
    text-align: center;
    padding: 0.5rem;
}
</style>