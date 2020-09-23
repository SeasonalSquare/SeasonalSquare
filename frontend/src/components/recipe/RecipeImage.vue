<template>
    <v-img
        :src="src"
        lazy-src="https://picsum.photos/id/11/100/60"
        aspect-ratio="1"
        class="grey lighten-2"
        :max-width="maxWidth"
        :max-height="maxHeight"
        style="border-radius: 15px"
    >
    <template v-slot:placeholder>
        <v-row
            class="fill-height ma-0"
            align="center"
            justify="center"
        >
        <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
        </v-row>
    </template>
    </v-img>
</template>

<script>
export default {
    props : {
        src: {
            type: String,
            required: true,
        },
        maxWidth: {
            type: Number,
            required: true,
        },
        maxHeight: {
            type: Number,
            required: true,
        }
    },
}
</script>

<style scoped>
</style>