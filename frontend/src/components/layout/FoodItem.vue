<template>
  <v-row>
     <template v-for="(produce,i) in produces">
        <v-col :key="i" cols="12" lg="3" md="3" xl="3" align="center" style="margin-top:50px" >
          <div class="box" style="height:320px;width:249px;border:1px solid rgb(247, 247, 247)">
            <a   @click="goProduce(produce)" ><v-img :src="imgURL(produce.fullname)"  class="scale" style="height:100%" ></v-img></a>
          </div>
          <div>
            <span  class="name"><a  @click="goProduce(produce)"  style="color:#333;">{{produce.fullname}}</a></span>
            <span  class="price">{{produce.price}}원 <span style="color:#333;font-size:14px">({{produce.unit}})</span></span>
            <span  class="des">칼로리 {{produce.kcal}}</span>
            <span  class="des">제철 {{formatMonths(produce.months)}}</span>
          </div>
        </v-col>
     </template>
     {{getN}}
  </v-row>
</template>

<script>
 import httpPro from '@/util/http-produce.js'
 import { mapState,mapGetters } from 'vuex'
const baseURL = "http://j3a503.p.ssafy.io:8000"

export default {
  name: 'FoodItem',
  components: {
  },
  computed : {
    ...mapGetters(['loggedIn','config']),
    ...mapState(['info']),
      getN () { 
          let url = "";
         //console.log("******info 변화: "+ JSON.stringify(this.$store.getters.getN))
          
          if(this.$store.getters.getN == null || this.$store.getters.getN == ""){
            url = "/todayProduce"
          }else{
            let vege = this.$store.state.info.vegetarian;
            if(vege == null) vege = 0;

            url=`/todayProduceWithout?allergies=${this.$store.state.info.allergy},&vegi=${vege}` 
          }
    
          this.call(url);

        return ''
      }
  },
  data() {
    return {
      produces:null,
    }
  },
  created() {
    let url = "";

    if(this.info == null || this.info == ""){
       url = "/todayProduce"
    }else{
      let vege = this.$store.state.info.vegetarian;
      if(vege == null) vege = 0;

      url=`/todayProduceWithout?allergies=${this.$store.state.info.allergy},&vegi=${vege}` 
    }
    url
    // httpPro.get(url).then(res => {
    //   this.produces=res.data
    //   this.produces.splice(8)
    // }).catch(err => {
    //   console.log(err)
    // })
  },
  
  methods: {
    goProduce(produce){
      this.$store.commit('setProduce', produce);
      this.$router.push({name: 'RecipeList'});
    },
    imgURL(name) { return baseURL + "/produceImg?name=" + name },
    formatMonths(months){
      if(months === '-') return '없음'
      else return months.replaceAll(" ", ", ") + '월'
    },
    async call(url) {
        //console.log(">>>>>>>>>url"+url)
        httpPro.get(url).then(res => {
            this.produces=res.data
              this.produces.splice(8)
            //console.log(">>>>>>>>>produces:"+JSON.stringify(this.produces));
            }).catch(err => {
              console.log(err)
          })
      },
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
