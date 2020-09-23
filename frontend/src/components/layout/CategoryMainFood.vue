<template>
  <v-container  align="center" class="text-center">
    <v-row v-for="(cate,index) in categoryBig" :key="index" style="margin-top:50px">
      <v-col cols="12" class="tit">{{cate}} <i style="font-size:25px" class="fas fa-chevron-right"></i>
        <v-col cols="12">
          <food-item :cate="cate" />
        </v-col>
      </v-col>
    </v-row>
  </v-container >
</template>

<script>
import '@fortawesome/fontawesome-free/css/all.css'
import FoodItem from '@/components/layout/FoodItem.vue'

export default {
  name: 'CategoryMainFood',
  components: {
    FoodItem,
  },
  data() {
    return {
      categoryBig:['식량작물', '채소류', '특용작물', '과일류', '축산물', '수산물']
    }
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
