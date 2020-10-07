<template>
    <v-card
        class="mx-auto"
    >
        <v-list shaped>
            <v-list-group
                :value="true"
                prepend-icon="mdi-bowl-mix"
                active-class="deep-purple--text text--accent-4"
                no-action
            >
                <template v-slot:activator>
                    <v-list-item-content>
                        {{ title }}
                    </v-list-item-content>
                </template>

                <v-list-item-group
                    multiple
                    style="padding-start: 0.5rem;"
                >
                    <template v-for="(item, i) in ingredients">
                        <v-divider
                            v-if="!item"
                            :key="`divider-${i}`"
                        ></v-divider>

                        <v-list-item
                            v-else
                            :key="`item-${i}`"
                            :value="item"
                            active-class="cart-active-checkbox"
                        >
                            <template v-slot:default="{ active }">
                            <v-list-item-content>
                                <v-list-item-title v-text="item"></v-list-item-title>
                            </v-list-item-content>

                            <v-list-item-action>
                                <v-checkbox
                                :input-value="active"
                                color="#EC8852"
                                ></v-checkbox>
                            </v-list-item-action>
                            </template>
                        </v-list-item>
                    </template>
                    <v-btn
                        block
                        large
                        color="#EC8852"
                        @click.prevent="goRecipeDetail"
                        style="margin-top: 1rem"
                    >
                        요리하러 가기
                    </v-btn>
                </v-list-item-group>
            </v-list-group>
        </v-list>
    </v-card>
</template>

<script>
export default {
    props : {
        pk: {
            type: Number,
            required: true,
        },
        image: {
            type: String,
            required: true,
        },
        title: {
            type: String,
            required: true,
        },
        ingredients: {
            type: Array,
            required: true,
        }
    },
    methods: {
        goRecipeDetail(){
            let summary = {
                pk: this.pk,
                image: this.image,
                title: this.title,
            }
            this.$router.push({name: 'RecipeDetail', params: {pk: this.pk, summary: summary}});
        }
    },
}
</script>

<style scoped>
.cart-active-checkbox {
    color: #5C5749 !important;
    caret-color: #5C5749 !important;
}
.v-list-item--active .v-list-item__title{
    text-decoration-color: #EC8852;
    text-decoration-line: line-through;
}
</style>
