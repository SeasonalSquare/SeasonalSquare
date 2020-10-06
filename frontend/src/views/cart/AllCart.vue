<template>
    <v-container
        style="min-height: 100%;"
    >
        <h2 class="title-position">장바구니</h2>
        <p style="border-bottom:1px solid black; font-size:12px; padding: 1rem 0 1rem" />

        <div v-if="token">
            <div
                v-for="(item, i) in shoppinglist" 
                :key="i"
            >
                <CartItem 
                    :pk="item.pk"
                    :title="item.title"
                    :image="item.image"
                    :ingredients="item.ingredients"
                    style="margin: 1rem;"
                />
            </div>
        </div>
        <div v-else
            class="title-position"
        >
            <v-icon x-large color="red" style="margin-bottom: 1rem">mdi-alert-circle</v-icon>
            <h2 >로그인 해주세요.</h2>
        </div>
    </v-container>
</template>

<script>
import { mapState } from 'vuex'
import http from '@/util/http-common.js'
import CartItem from '@/components/cart/CartItem'

export default {
    components: {
        CartItem,
    },
    computed: {
        ...mapState(['token']),
    },
    data() {
        return {
            shoppinglist: []
        }
    },
    async created() {
        await this.fetchShoppingCart()
    },
    methods: {
        async fetchShoppingCart() {
            http.get(`/accounts/shoppingcart/`, {
                headers: {
                    "Authorization": this.token,
                }
            }).then(response => {
                console.log(response.data)
                this.shoppinglist = response.data
            }).catch(error => {
                console.log(error)
            })
        },
    },
}
</script>

<style scoped>
.title-position {
    text-align: center;
    margin-top: 2rem;
}
</style>
