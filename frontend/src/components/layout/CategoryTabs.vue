<template >
  <v-app>
     <v-tabs fixed-tabs  grow color="#EC8852" >
        <v-tab v-for="(cate,index) in categoryBig" :key="index" style="width:60px;">
          <div style="font-weight:bold;font-size:14px" >
              {{cate}}
          </div>
        </v-tab>
     </v-tabs>
  </v-app>
</template>

<script>
export default {
  name: "CategoryTabs",
  data() {
    return {
       categoryBig:['식량작물', '채소류', '특용작물', '과일류', '축산물', '수산물']
    };
  },
 
}
</script>

<style scoped>
</style>