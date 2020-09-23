<template>
  <v-row>
     <template v-for="(food,i) in foods">
        <v-col :key="i" cols="6" sm="2" md="2" lg="3" xl="3" align="center" >
          <v-img :src="food.image" style="height:320px;width:249px"></v-img>
          <div>
            <span  class="name">{{cate}}</span>
            <span style="font-size:16px">설명</span>
          </div>
        </v-col>
     </template>
  </v-row>
</template>

<script>
 import http from '@/util/http-common.js'

export default {
  name: 'FoodItem',
  components: {
  },
  props: ['cate'],
  data() {
    return {
      foods:null,
    }
  },
  created() {
      http.get(`/recipe/grocery/감자`).then(res => {
        // console.log(res.data)
        this.foods=res.data
        this.foods.splice(4)
      }).catch(err => {
        console.log(err + "죽인다")
      })
  },
  methods: {
  },

  
}
</script>

<style scoped>
.name{
     overflow: hidden;
    max-height: 50px;
    margin-top: 11px;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    font-weight:700;
    font-size:16px;
}
</style>
