<template>
  <v-row>
    <span style="background:#f7f7f7;width:100%;margin-top:0;padding-top:50px" class="tit">이 농산물 어때요?</span>
    <v-carousel cycle  interval="9000"   height="auto" >
      <!-- hide-delimiter-background -->
        <v-carousel-item v-for="(produce, i) in produces" :key="i">
          <v-sheet color="#f7f7f7" height="450" >
            <v-row class="fill-height" align="center" justify="center">
              <v-col cols="0" lg="2" md="2"> </v-col>
              <v-col cols="12" lg="4"  md="4" >
                  <v-hover v-slot:default="{ hover }">
                      <a   @click="goProduce(produce.name)">
                      <v-img :aspect-ratio="16/9" :src="imgURL(produce.name)" > 
                        <v-row align="end" class="fill-height">
                          <v-col
                            align-self="start" align="left"
                            style="padding-top:0px !important"
                            cols="12"
                          >
                            <v-avatar color="#EC8852" style="opacity: 0.8;z-index:1" size="70" tile>
                              <span style="font-size:20px;font-weight:bold">{{produce.value}}</span> %
                              <!-- <i style="color:#070279" class="fas fa-arrow-down"></i> -->
                              <v-icon size="22" v-if="produce.direction == 0" color="#070279">{{arrowDown}}</v-icon>
                              <v-icon size="22" v-else-if="produce.direction == 1" color="#AF0000">{{arrowUp}}</v-icon>
                            </v-avatar>
                          </v-col>

                          <v-col class="py-0" style="padding-right:0px;padding-left:0px;">
                            <v-list-item
                              color="rgba(0, 0, 0, .4)"
                              dark
                            >
                              <v-list-item-content style="background:#333;">
                                <v-list-item-title class="title">{{produce.fullname}}</v-list-item-title>
                                <v-list-item-subtitle>{{produce.price}}원</v-list-item-subtitle>
                              </v-list-item-content>
                            </v-list-item>
                          </v-col>
                        </v-row>
                        <div style="position:absolute; top:0px; color:white; width:100%; height:100%; background:black; opacity: 0.8;"
                          v-if="hover"
                          class="d-flex transition-fast-in-fast-out  darken-2 v-card--reveal display-3 white--text"
                        >
                              <div style="font-size:15px">
                                <span  class="name" >{{produce.fullname}}</span>
                                <span class="price">{{produce.price}}원 ({{produce.unit}})</span>
                                <span class="des">{{produce.kcal}}</span>
                                <span class="des">제철 {{produce.months}}</span>
                              </div>
                          </div>
                      </v-img>
                      </a>
                  </v-hover>
              </v-col>
              
              <v-col cols="12" lg="4"  md="4">
                <div style="font-size:28px;font-weight:700"></div>
                <div >
                  <h2 style="margin-bottom:20px;color:#333">‘<span style="font-weight:700;color:#EC8852">{{produce.fullname}}</span>’ <span style="color:#5C5749;font-size:39px">더</span> 맛있어지는 방법 <i style="color:#5C5749"  class="fas fa-exclamation"></i></h2>
                  <recipe-main  :food="produce.name" ></recipe-main> 
                </div>
              </v-col>
              <v-col cols="12" lg="2"  md="2"></v-col>
            </v-row>
          </v-sheet>
        </v-carousel-item>

    </v-carousel>
  </v-row>
</template>

<script>
import RecipeMain from '@/components/layout/RecipeMain.vue'
import { mdiArrowDownBold,mdiArrowUpBold    } from '@mdi/js';
import '@fortawesome/fontawesome-free/css/all.css'
const baseURL = "http://j3a503.p.ssafy.io:8000"

export default {
  name: 'FoodCarousel',
  components: {
    RecipeMain,
  },
  props: ['produces'],
  data() {
    return {
       arrowDown : mdiArrowDownBold,
       arrowUp: mdiArrowUpBold ,
    }
  },
  methods: {
    goProduce(foodName){
      // 작믈 이름을 넘겨주세요
      //alert(foodName);
      this.$router.push({name: 'RecipeList', params: {grocery: foodName}});
    },
     imgURL(name) { return baseURL + "/produceImg?name=" + name },
  },
  
}
</script>

<style scoped>
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: .5;
  position: absolute;
  width: 100%;
}
 .tit{
    font-weight: 700;
    font-size: 28px;
    line-height: 32px;
    letter-spacing: -0.3px;
    text-align: center;
 }
 
.name{
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    max-height: 60px;
    margin-top: 11px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    font-weight:700;
    font-size:40px;
}
.price{
    font-weight: 700;
    color: #EC8852 ;
    font-size:40px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    
}
.des{
    display: block;
    font-size: 25px;
    color: #fff;
    line-height: 34px;  
}
</style>
