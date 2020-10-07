<template>
  <v-container >
   <v-row  style="margin-top:50px">
      <v-col cols="12" class="tit"><a  @click="goProduceMore()" style="color:#333">오늘의 맞춤 추천 농작물 <i class="fas fa-chevron-right " style="padding-left:10px"></i></a>
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
    goProduceMore(){
       this.$router.push({name: 'ProduceMore'})
    }
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
