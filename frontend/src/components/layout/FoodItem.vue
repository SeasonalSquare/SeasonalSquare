<template>
  <v-row>
     <template v-for="(food,i) in foods">
        <v-col :key="i" cols="12" lg="3" md="3" xl="3" align="center" >
          <v-img :src="food.image" style="height:320px;width:249px"></v-img>
          <div>
            <span  class="name">{{food.title}}</span>
            <span  class="price">7,000원</span>
            <span  class="des">설명</span>
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
  data() {
    return {
      foods:null,
    }
  },
  created() {
      http.get(`/recipe/grocery/감자`).then(res => {
        console.log(this.cate)
        this.foods=res.data
        this.foods.splice(8)
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
    text-overflow: ellipsis;
    white-space: nowrap;
    max-height: 50px;
    margin-top: 11px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    font-weight:700;
    font-size:20px;
}
.price{
    font-weight: 700;
    color: #EC8852 ;
    font-size:17px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    
}
.des{
    display: block;
    padding-top: 8px;
    font-size: 13px;
    color: #666;
    line-height: 19px;  
}
</style>
