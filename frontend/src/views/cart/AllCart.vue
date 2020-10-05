<template>
    <v-container>
        <h2 style="text-align: center; margin-top: 2rem;">장바구니</h2>
        <p style="border-bottom:1px solid black; font-size:12px; padding: 1rem 0 1rem" />

        <div 
            v-for="(dump, i) in dumps" 
            :key="i"
        >
            <CartItem 
                :pk="dump.pk"
                :title="dump.title"
                :ingredients="dump.ingredients"
                style="margin: 1rem;"
            />
        </div>
    </v-container>
</template>

<script>
import CartItem from '@/components/cart/CartItem'

export default {
    components: {
        CartItem,
    },
    data() {
        return {
            dumps : 
            [{
                pk: '6872350',
                title: '상추비빔밥',
                ingredients: ['고추장', '간장', '상추', '달걀', '참기름'],
            },
            {
                pk: '6872350',
                title: '호박볶음',
                ingredients: ['애호박', '베이컨', '마늘'],
            },
            {
                pk: '6872350',
                title: '열무비빔밥',
                ingredients: ['열무', '찹쌀가루', '쪽파', '양파'],
            }],
        }
    },
}
</script>

<style scoped>

</style>