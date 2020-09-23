<template>
  <v-container  align="center" class="text-center">
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

  
    <v-btn id="scrollButton"
        fab
        small
        color="#5C5749"
        retain-focus-on-click
        @click="scrollToTop"
    > 
        <v-icon color="#fff">mdi-chevron-up</v-icon>
    </v-btn>
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
      // categoryBig:['식량작물', '채소류', '특용작물', '과일류', '축산물', '수산물'],
      windowTop: 0,
    }
  },
  watch: {
    windowTop: function() {
        if (this.windowTop > 300) {
            let btn = document.getElementById('scrollButton')
            btn.style.display = 'block'
        }
        else {
            let btn = document.getElementById('scrollButton')
            btn.style.display = 'none'
        }
    }
  },
  mounted() {
      window.addEventListener("scroll", this.onScroll)
  },
  beforeDestroy() {
      window.removeEventListener("scroll", this.onScroll);
  },
  methods: {
      scrollToTop() {
          window.scroll({top: 0, left: 0, behavior: 'smooth'})
      },
      onScroll(e) {
          this.windowTop = e.target.documentElement.scrollTop;
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
 #scrollButton {
   z-index: 10;
    position: fixed;
    display: none;
    bottom: 50px;
    right: 30px;
}
</style>
