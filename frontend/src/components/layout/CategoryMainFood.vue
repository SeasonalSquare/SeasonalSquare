<template>
  <v-container >
     <!-- align="center" class="text-center" -->
    <!-- <v-row v-for="(cate,index) in categoryBig" :key="index" style="margin-top:50px">
      <v-col cols="12" class="tit">{{cate}} <i style="font-size:25px" class="fas fa-chevron-right"></i>
        <v-col cols="12">
          <food-item :cate="cate" />
        </v-col>
      </v-col>
    </v-row> -->

   <v-row  style="margin-top:50px">
      <v-col cols="12" class="tit">오늘의 추천 농작물
        <v-col cols="12">
          <food-item />
        </v-col>
      </v-col>
    </v-row>

    <scroll-top/>
  </v-container >
</template>

<script>
import '@fortawesome/fontawesome-free/css/all.css'
import FoodItem from '@/components/layout/FoodItem.vue'
import ScrollTop from '@/components/layout/ScrollTop.vue'

export default {
  name: 'CategoryMainFood',
  components: {
    FoodItem,
    ScrollTop,
  },
  data() {
    return {
    }
  },
  watch: {
  },
  methods: {
  }
  
}
</script>

<style scoped>
 .tit{
    font-weight: 700;
    font-size: 28px;
    line-height: 32px;
    letter-spacing: -0.3px;
    text-align: center;
 }
</style>
