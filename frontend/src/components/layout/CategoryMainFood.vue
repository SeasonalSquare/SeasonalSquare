<template>
  <v-row>

    <v-row v-for="(cate,index) in categoryBig" :key="index">
      <v-col cols="12" style="color:#333;font-weight:700"><h3>{{cate}}</h3></v-col>
      <v-col cols="12">ccccccccccc</v-col>
    </v-row>
    
  </v-row>
</template>

<script>
import '@fortawesome/fontawesome-free/css/all.css'

export default {
  name: 'CategoryMainFood',
  components: {
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
</style>
