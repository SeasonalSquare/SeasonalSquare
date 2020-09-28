<template>
  <v-row>
     <template v-for="(produce,i) in produces">
        <v-col :key="i" cols="12" lg="3" md="3" xl="3" align="center" style="margin-top:50px" >
          <div class="box" style="height:320px;width:249px">
            <a   @click="goProduce(produce)" ><v-img :src="imgURL(produce.name)"  class="scale" style="height:100%" ></v-img></a>
          </div>
          <div>
            <span  class="name"><a  @click="goProduce(produce)"  style="color:#333;">{{produce.fullname}}</a></span>
            <span  class="price">{{produce.price}}원 <span style="color:#333;font-size:14px">({{produce.unit}})</span></span>
            <span  class="des">칼로리 {{produce.kcal}}</span>
            <span  class="des">제철 {{produce.months}}</span>
          </div>
        </v-col>
     </template>
  </v-row>
</template>

<script>
 import httpPro from '@/util/http-produce.js'
const baseURL = "http://j3a503.p.ssafy.io:8000"

export default {
  name: 'FoodItem',
  components: {
  },
  data() {
    return {
      produces:null,
    }
  },
  created() {
      httpPro.get(`/todayProduce`).then(res => {
        console.log(this.cate)
        this.produces=res.data
        this.produces.splice(8)
      }).catch(err => {
        console.log(err + "죽인다")
      })
  },
  methods: {
    goProduce(produce){
      this.$router.push({name: 'RecipeList', params: {produce: produce}});
    },
    imgURL(name) { return baseURL + "/produceImg?name=" + name },
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
    font-size: 13px;
    color: #666;
    line-height: 19px;  
}
.scale {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.5s ease-in-out; 
}
.scale:hover {
  transform: scale(1.1);
  -webkit-transform: scale(1.1);
  -moz-transform: scale(1.1);
  -ms-transform: scale(1.1);
  -o-transform: scale(1.1);
}
.box{
   overflow:hidden 
}
</style>
