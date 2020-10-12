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
                <div class="emphasize-text" style="margin: 1rem;"> 
                    {{ summary.title }}
                </div>
            </v-col>

            <v-col
                style="flex: 1 1 60%; padding-top: 2rem;"
            >
                <v-row>
                    <div style="font-size: 0.9rem; color: black; margin-start: 1rem">
                        <v-icon color="#FEAA6E">mdi-hand-pointing-right</v-icon>
                        없는 재료를 장바구니에 담아 장을 볼 때 활용하세요!
                    </div>
                </v-row>
                <v-row>
                    <v-col>
                        <v-container>
                            <v-chip
                                color="#BEDDBF"
                                class="emphasize-text"
                            >
                                재료
                            </v-chip>
                            <div
                                v-for="(main_ingredient, i) in main_ingredients"
                                :key = i
                                class="d-flex"
                            >
                                <div style="flex: 1 1 40%;">
                                    <v-checkbox
                                        color="#EC8852"
                                        :value="main_ingredient.ingredient_name"
                                        :label="main_ingredient.ingredient_name + ' ' + main_ingredient.amount"
                                        v-model="main_checkbox"
                                    >
                                    </v-checkbox>
                                </div>
                            </div>
                        </v-container>
                    </v-col>
                    <v-col 
                        v-if="source_ingredients.length"
                    >
                        <v-container>
                            <v-chip
                                color="#BEDDBF"
                                class="emphasize-text"
                            >
                                양념 재료
                            </v-chip>
                            <div
                                v-for="(source_ingredient, j) in source_ingredients"
                                :key = j
                                class="d-flex"
                            >
                                <div style="flex: 1 1 40%;">
                                    <v-checkbox
                                        color="#EC8852"
                                        :value="source_ingredient.source_name"
                                        :label="source_ingredient.source_name + ' ' + source_ingredient.amount"
                                        v-model="source_checkbox"
                                    >
                                        <!-- <template #label :class="checkClass"> {{ source_ingredient.source_name }}</template> -->
                                    </v-checkbox>
                                </div>
                            </div>
                        </v-container>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col style="margin-left: 1rem; margin-right: 1rem;">
                        <v-btn block x-large color="#5C5749" @click.prevent="addToCart">
                            <v-icon v-if="!isInCart" color="white">mdi-cart-outline</v-icon>
                            <v-icon v-else color="#EC8852">mdi-cart</v-icon>
                        </v-btn>
                    </v-col>
                </v-row>
            </v-col>
        </div>

        <br>
        <v-divider></v-divider>
        <br>
        <div class="sub-title"> 만드는 법 </div>
        <br>
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
            </v-col>
        </div>
        <br>
    </v-container>
</template>

<script>
import { mapState } from 'vuex'
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
    computed: {
        ...mapState(['token']),
    },
    data() {
        return {
            main_ingredients : [],
            source_ingredients: [],
            recipe : [],
            isInCart : false,
            full_main_ingredients_name : [],
            full_source_ingredients_name : [],
            main_checkbox : [],
            source_checkbox : [],
            shoppinglist: [],
        }
    },
    async created() {
        await this.fetchRecipe();
        this.fetchShoppingCart();
    },
    methods: {
        async fetchRecipe() {
            http.get(`/recipe/${this.summary.pk}/`)
            .then(response => {
                this.main_ingredients = response.data.ingredient_data.main_ingredients
                this.source_ingredients = response.data.ingredient_data.source_ingredients
                this.recipe = response.data.recipe

                this.full_main_ingredients_name = this.main_ingredients.map((main) => {
                    return main.ingredient_name
                })
                this.full_source_ingredients_name = this.source_ingredients.map((source) => {
                    return source.source_name
                })
            })
            .catch(() => {
                this.$dialog.notify.error('레시피를 불러올 수 없습니다.', {
                    position: 'top-right',
                    timeout: 2000
                })
            })
        },
        fetchShoppingCart() {
            http.get(`/accounts/shoppingcart/`, {
                headers: {
                    "Authorization": this.token,
                }
            }).then(response => {
                this.shoppinglist = response.data
            }).catch(() => {
                if(this.token) {                    
                    this.$dialog.notify.error('장바구니를 불러올 수 없습니다.', {
                        position: 'top-right',
                        timeout: 2000
                    })
                }
            })
        },
        addToCart() {
            if(this.isInCart) {
                this.$dialog.notify.warning('이미 장바구니에 담긴 레시피입니다.', {
                    position: 'top-right',
                    timeout: 1000
                })
                return;
            }

            let cart = this.full_main_ingredients_name.filter((word) => !this.main_checkbox.includes(word));
            let fullcart = cart.concat(this.full_source_ingredients_name.filter((word) => !this.source_checkbox.includes(word)));
            
            if(this.shoppinglist){
                this.putShoppingCart(fullcart);
            }else{
                this.postShoppingCart(fullcart);
            }
        },
        postShoppingCart(fullcart) {
            http.post(`/accounts/shoppingcart/`, {
                shoppinglist: [{
                    pk: this.summary.pk,
                    title: this.summary.title,
                    image: this.summary.image,
                    ingredients: fullcart,
                }]
            }, {
                headers: { 
                    "Authorization": this.token,
                }
            }).then(() => {
                this.isInCart = true
                this.$dialog.notify.success('장바구니에 담겼습니다.', {
                    position: 'top-right',
                    timeout: 1000
                })
            }).catch(() => {
                let message = '장바구니 담기에 실패했습니다.'
                if(!this.token) message = '로그인을 해주세요.'
                this.$dialog.notify.error(message, {
                    position: 'top-right',
                    timeout: 2000
                })
            })
        },
        putShoppingCart(fullcart) {
            http.put(`/accounts/shoppingcart/`, {
                shoppinglist: [{
                    pk: this.summary.pk,
                    title: this.summary.title,
                    image: this.summary.image,
                    ingredients: fullcart,
                }]
            }, {
                headers: { 
                    "Authorization": this.token,
                }
            }).then(() => {
                this.isInCart = true
                this.$dialog.notify.success('장바구니에 담겼습니다.', {
                    position: 'top-right',
                    timeout: 1000
                })
            }).catch(() => {
                let message = '장바구니 담기에 실패했습니다.'
                if(!this.token) message = '로그인을 해주세요.'
                this.$dialog.notify.error(message, {
                    position: 'top-right',
                    timeout: 2000
                })
            })
        }
    },
}
</script>

<style scoped>
.sub-title {
    font-weight: 700;
    font-size: 1.5rem;
    line-height: 32px;
    letter-spacing: -0.3px;
    text-align: center;
    padding: 0.5rem;
}
.emphasize-text {
    font-size: 1.1rem;
    font-weight: 600;
    color: #5C5749;
}
.v-input--is-label-active >>> label {
    text-decoration-color: #EC8852;
    text-decoration-line: line-through;
}
</style>
