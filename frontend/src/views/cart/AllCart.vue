<template>
    <v-container
        style="min-height: 100%; max-width: 800px"
    >
        <h2 class="title-position">장바구니</h2>
        <p style="border-bottom:1px solid black; font-size:12px; padding: 1rem 0 1rem" />

        <div v-if="token">
            <div v-if="!shoppinglist.length"
                class="title-position"
                style="font-weight: 700; font-size: 1.2rem"
            >
                <v-icon x-large color="#FFE1A2">mdi-alert-circle</v-icon>
                <br>
                장바구니가 비었습니다.
            </div>
            <div v-else>
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
                <div>
                    <v-btn
                        block
                        large
                        color="#EC8852"
                        @click.prevent="deleteCart"
                        style="margin-top: 1rem"
                    >
                        장바구니 전체 삭제
                    </v-btn>
                </div>
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
                this.shoppinglist = response.data
            }).catch(() => {
                this.$dialog.notify.error('장바구니를 불러올 수 없습니다.', {
                    position: 'top-right',
                    timeout: 2000
                })
            })
        },
        deleteCart() {
            http.delete(`/accounts/shoppingcart/`, {
                headers: {
                    "Authorization": this.token,
                }
            }).then(() => {
                this.shoppinglist = []
                this.$dialog.notify.success('삭제 완료되었습니다.', {
                    position: 'top-right',
                    timeout: 2000
                })
            }).catch(() => {
                this.$dialog.notify.error('삭제에 실패했습니다.', {
                    position: 'top-right',
                    timeout: 2000
                })
            })
        }
    },
}
</script>

<style scoped>
.title-position {
    text-align: center;
    margin-top: 2rem;
}
</style>
