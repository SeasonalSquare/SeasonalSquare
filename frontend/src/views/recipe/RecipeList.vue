<template>
    <div>
        <v-container style="display: flex; margin: 1rem; justify-content: space-evenly;">
            <v-row>
                <v-col>
                    <RecipeImage
                        :src="'http://j3a503.p.ssafy.io:8000/produceImg?name='+produce.fullname"
                        :max-width="300"
                        :max-height="200"
                        style="margin: 0 auto;"
                    />
                </v-col>
                <v-col style="padding: 1rem;">
                    <h2 style="margin-bottom: 1rem; color: #5C5749">
                        ‘<span style="color: #EC8852">{{ produce.name }}</span>’ 더 맛있어지는 법
                        <i class="fas fa-exclamation"></i>
                    </h2>
                    <div class="description-text">
                        이름 : {{ produce.fullname }}
                    </div>
                    <div class="description-text">
                        칼로리 : {{ produce.kcal }}
                    </div>
                    <div class="description-text">
                        제철 : {{ formatMonths(produce.months) }}
                    </div>
                    <div class="description-text">
                        가격 : {{ produce.price }}원 ({{ produce.unit }})
                    </div>
                </v-col>
            </v-row>
        </v-container>

        <v-divider />
        <br>
        <v-container style="display: flex; flex-wrap: wrap; justify-content: space-evenly;">
            <recipe-card
                v-for="(recipe, index) in recipes" 
                :key="index" 
                :recipe="recipe"
                style="margin: 1rem;">
            </recipe-card>
        </v-container>
        <scroll-top/>
    </div>
</template>

<script>
import http from '@/util/http-common.js'
import RecipeCard from '@/components/recipe/RecipeCard.vue'
import RecipeImage from '@/components/recipe/RecipeImage.vue'
import ScrollTop from '@/components/layout/ScrollTop.vue'

export default {
    components : {
        RecipeCard,
        RecipeImage,
        ScrollTop,
    },
    props: {
        produce: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            recipes: [],
        }
    },
    created() {
        this.findRecipeByFoodName();
    },
    methods:{
        findRecipeByFoodName() {
            http.get(`/recipe/grocery/${this.produce.name}/`)
            .then(response => {
                this.recipes = response.data
            })
            .catch(() => {
                this.$dialog.notify.error('레시피를 불러올 수 없습니다.', {
                    position: 'top-right',
                    timeout: 2000
                })
            })
        },
        formatMonths(months){
            if(months === '-') return '없음'
            else return months.replaceAll(" ", ", ") + '월'
        },
    }
}
</script>

<style scoped>
.description-text {
    font-weight: 700;
    margin-bottom: 0.5rem;
    color: #5C5749
}
</style>