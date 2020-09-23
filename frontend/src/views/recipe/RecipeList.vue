<template>
    <div>
        <div style="display: flex; margin: 1rem; justify-content: space-evenly;">
        <v-img src="https://health.chosun.com/site/data/img_dir/2020/05/07/2020050702573_0.jpg"
            max-width="300" max-height="200" style="border: 1px gray solid "/>
            <p>감자가 더 맛있어지는 법... 대충 설명...<br> 여기에 뭘뭘 넣지 뭔내용 넣을까아아ㅏ</p>
        </div>
        <br>
        <v-divider />
        <br>
        <div style="display: flex; flex-wrap: wrap; justify-content: space-evenly;">
            <recipe-card
                v-for="(recipe, index) in recipes" 
                :key="index" 
                :recipe="recipe"
                style="margin: 1rem;">
            </recipe-card>
        </div>
    </div>
</template>

<script>
import http from '@/util/http-common.js'
import RecipeCard from '@/components/recipe/RecipeCard.vue'

export default {
    components : {
        RecipeCard,
    },
    props: {
        grocery: {
            type: String,
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
            http.get(`/recipe/grocery/${this.grocery}`)
            .then(response => {
                this.recipes = response.data
            })
            .catch(err => {
                console.log(err)
            })
        }
    }
}
</script>

<style scoped>

</style>