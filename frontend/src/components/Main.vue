<template>
<v-app>
  <v-container  fluid style="padding-top:0px"> 
    <v-row align="center" class="text-center">
      <v-col cols="12" align="center" style="padding-top:0px">
        <food-carousel :produces="produces" ></food-carousel>
      </v-col>
    </v-row>
    <category-main-food/>
     {{getN}}
  </v-container>
</v-app>
</template>

<script>
// import http from '@/util/http-common.js'
  import httpPro from '@/util/http-produce.js'
  import FoodCarousel from '@/components/layout/FoodCarousel.vue'
  import CategoryMainFood from '@/components/layout/CategoryMainFood.vue'
 import { mapState,mapGetters  } from 'vuex'

  export default {
    name: 'Main',
    components : {
      FoodCarousel,
      CategoryMainFood,
    },
    computed : {
      ...mapGetters(['loggedIn','config']),
      ...mapState(['info']),
        getN () { 
          let url = "";
          // console.log("******info 변화: "+ JSON.stringify(this.$store.getters.getN))
          
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
        testInput: '',
        recipes: [],
        produces : null,
      }
   },
   methods:{
      async call(url) {
        // console.log(">>>>>>>>>url"+url)
        httpPro.get(url).then(res => {
            this.produces=res.data
              this.produces.splice(8)
            // console.log(">>>>>>>>>produces:"+JSON.stringify(this.produces));
            }).catch(err => {
              console.log(err)
          })
      },
   },
  async created() {
    
    // console.log("?????? "+JSON.stringify(this.$store.getters.config));

    let url = "";
    // console.log("created>>>"+JSON.stringify(this.info));
    
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


      // httpPro.get(`/todayProduce`).then(res => {
      //   this.produces=res.data
      //   this.produces.splice(7)
      // }).catch(err => {
      //   console.log(err)
      // })
    }
  }
</script>
