<template >
  <v-container style="text-align: center; margin-top: 2rem;">
        <v-row v-if="!loggedIn" >
          <v-icon x-large color="#EC8852">mdi-carrot</v-icon>
          <v-icon x-large color="#7CB342">mdi-food-apple</v-icon>
          <v-icon x-large color="#795548">mdi-food-croissant</v-icon>
          <v-icon x-large color="#4B9AD6">mdi-food-fork-drink</v-icon>
          <v-icon x-large color="#B59247">mdi-food-drumstick</v-icon>
          <v-icon x-large color="#E64E30">mdi-noodles</v-icon>
          <v-icon x-large color="#FFE1A2">mdi-bread-slice</v-icon>
          <div style="font-weight: 700; font-size: 1.7rem;">페이지를 찾을 수 없습니다.</div>
          <v-container>
              <div>
                 로그인회원만 사용가능합니다
              </div>
          </v-container>
        </v-row>

        <v-row v-else >
          <v-col cols="12" lg="12">
            <div  class="section_login"> 
              <h2 style="text-align: center;"> 회원 정보</h2>
              <div style="font-size:12px;color:#EC8852">선택하신 비건·알레르기 정보를 기반으로 맞춤형 농작물과 레시피를 추천해줍니다.</div>
              <div style="text-align: right;">{{$store.state.myProfile.email}}</div>
            </div>
          </v-col>

          <v-divider style="border:1px solid #EC8852 "></v-divider>
        
        <v-col cols="12"></v-col>
        <v-row  style="text-align:left;  padding-left:45px; font-size:20px; font-weight:700" >
           <i class="fas fa-leaf" style="padding-right:10px;color:#6AAB38"></i> 비건 선택
        </v-row>
        <v-row class="border" >
          <v-row>
          <v-col cols="12" sm="12" md="12">
            <v-radio-group v-model="vege" row >             
                <v-radio   v-for="(v,index) in veganInfo" :key="'v'+index" 
                :label=v color="#EC8852" :value=v class="vege"
              >
            </v-radio>
              <v-radio label="해당없음" color="#EC8852" value="해당없음" class="vege" checked>
            </v-radio>
            </v-radio-group>
          </v-col>
          </v-row>
        </v-row>

        <v-col cols="12"></v-col>
         <v-row  style="text-align:left;  padding-left:45px; font-size:20px; font-weight:700" >
           <i class="fas fa-allergies" style="padding-right:10px;color:#F3AE79"></i> 알레르기 선택
        </v-row>
        <v-row class="border" >
          <!-- <v-row style="">
            <v-col cols="12"  class="gubun">
              <h4><i class="fas fa-seedling"></i> 기타</h4>
            </v-col>
            <v-col cols="4" sm="2" md="2" v-for="(a,index) in allergy_info1" :key="'a1'+index" style="padding-top:0px" >
              <v-checkbox
                v-model="allergy_chk"
                :label=a
                color="#EC8852"
                :value=a
                hide-details
                class="allergy_chk" style="text-align:center"
              ></v-checkbox>
            </v-col>
          </v-row> -->
          <v-col cols="12"></v-col>
          <v-row >
            <v-col cols="12"  class="gubun">
              <h4><i class="fas fa-drumstick-bite" style="color:#E55B53" ></i> 육류</h4>
            </v-col>
            <v-col cols="4" sm="2" md="2"  v-for="(a,index) in allergy_info2" :key="'a2'+index" style="padding-top:0px" >
              <v-checkbox
                v-model="allergy_chk"
                :label=a
                color="#EC8852"
                :value=a
                hide-details
                class="allergy_chk"
              ></v-checkbox>
            </v-col>
          </v-row>
          
          <v-col cols="12"></v-col>
          <v-row >
            <v-col cols="12"  class="gubun">
              <h4><i class="fas fa-fish" style="color:#64A9C1"></i> 생선/해산물</h4>
            </v-col>
            <v-col cols="4" sm="2" md="2" v-for="(a,index) in allergy_info3" :key="'a3'+index" style="padding-top:0px" >
              <v-checkbox
                v-model="allergy_chk"
                :label=a
                color="#EC8852"
                :value=a
                hide-details
                class="allergy_chk"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-col cols="12"></v-col>

          <v-row >
            <v-col cols="12"  class="gubun">
              <h4><i class="fas fa-seedling"  style="color:#C28B36"></i> 곡물</h4>
            </v-col>
            <v-col cols="4" sm="2" md="2" v-for="(a,index) in allergy_info4" :key="'a4'+index"  style="padding-top:0px">
              <v-checkbox
                v-model="allergy_chk"
                :label=a
                color="#EC8852"
                :value=a
                hide-details
                class="allergy_chk"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-col cols="12"></v-col>

          <v-row  >
            <v-col cols="12"  class="gubun">
              <h4><i class="fas fa-apple-alt" style="color:#D42F2B"></i> 과일</h4>
            </v-col>
            <v-col cols="4" sm="2" md="2" v-for="(a,index) in allergy_info5" :key="'a5'+index"  style="padding-top:0px">
              <v-checkbox
                v-model="allergy_chk"
                :label=a
                color="#EC8852"
                :value=a
                hide-details
                class="allergy_chk"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-col cols="12"></v-col>

          <v-row >
            <v-col cols="12"  class="gubun">
              <h4><i class="fas fa-carrot" style="color:#EC8314"></i> 채소</h4>
            </v-col>
            <v-col cols="4" sm="2" md="2"  v-for="(a,index) in allergy_info6" :key="'a6'+index" style="padding-top:0px">
              <v-checkbox
                v-model="allergy_chk"
                :label=a
                color="#EC8852"
                :value=a
                hide-details
                class="allergy_chk"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-col cols="12"></v-col>
          <v-row style="">
            <v-col cols="12"  class="gubun">
              <h4><i class="fas fa-shopping-basket" style="color:#7F6333"></i> 기타</h4>
            </v-col>
            <v-col cols="4" sm="2" md="2" v-for="(a,index) in allergy_info1" :key="'a1'+index" style="padding-top:0px" >
              <v-checkbox
                v-model="allergy_chk"
                :label=a
                color="#EC8852"
                :value=a
                hide-details
                class="allergy_chk" style="text-align:center"
              ></v-checkbox>
            </v-col>
          </v-row>
          </v-row>

          <v-col cols="12"></v-col>
          <v-divider></v-divider>

          <v-row>
            <v-col cols="0" lg="2"></v-col>
            <v-col cols="12" lg="8">
              <v-btn color="#5C5749" style="border: 1px solid #5C5749;margin-top:15px" @click="goInfoUpdate()" class="btn"><span style="color:#fff">수정하기</span></v-btn>
            </v-col>
            <v-col cols="0" lg="2"></v-col>
          </v-row>

        </v-row>
    <scroll-top/>
    </v-container>
</template>

<script>
import http from '@/util/http-common.js'
import { mapState ,mapGetters } from 'vuex'
import ScrollTop from '@/components/layout/ScrollTop.vue'

export default {
  name: "UserProfile",
  components: {
    ScrollTop,
  },
  data() {
    return {
      veganInfo: ["vegan", "lacto-vegetarian", "ovo-vegetarian", "lacto-ovo-vegetarian", "pesco-vegetarian", "pollo-vegetarian"],
      vege:  "",
      allergy_chk : [],
      allergy_info1: ["견과류","갑각류","난류","어패류","연체류","깨","알코올","카페인","버섯류","유제품", ],      
      allergy_info2: ["소고기","돼지고기","닭고기","양고기" ],
      allergy_info3: ["장어","가자미","멸치","대구","갈치","고등어" ],
      allergy_info4: ["대두","쌀","메밀","밀","팥","옥수수" ],
      allergy_info5: ["딸기","망고","멜론","포도","키위","복숭아" ],
      allergy_info6: ["계피","겨자","생강","당근","샐러리","오이","마","토마토","토란","마늘","고구마","시금치","양파","감자","밤","가지","연근","무"],
    };
  },
  methods:{
    goInfoUpdate(){

      let data = {
        "allergy_list":this.allergy_chk,
        "vegetarian":this.vege == "해당없음"? null :this.vege
      }

      http.post('/accounts/allergy-vegan/',JSON.stringify(data) , this.$store.getters.config)
      .then(res => {
          res
          this.$dialog.notify.success('회원정보 수정이 완료되었습니다', {
            position: 'top-right',
            timeout: 3000
          })
          this.$store.dispatch("setUserInfo", data.token);
      })
      .catch(error => {
        let data = error.response.data;
        console.log('failed', data)
      })
    }
  },
  computed : {
    ...mapGetters(['loggedIn','config']),
    ...mapState(['myProfile','info']),
  },
  mounted() {
    let vegi = this.$store.state.info.vegetarian
    vegi = vegi == null?  "해당없음" : vegi

    document.querySelectorAll('.vege label').forEach((elem) => {
      if(vegi == elem.innerHTML) this.vege = vegi;
    });

    document.querySelectorAll('.allergy_chk label').forEach((elem) => {
      if(this.$store.state.info.allergy.indexOf(elem.innerHTML) != -1)
        this.allergy_chk.push(elem.innerHTML)
    });

  },
}
</script>

<style scoped>

.section_login{
   /* background: gray; */
   /* width: 100%; */
   margin: 0 auto;
}
.btn{
  width: 100%;
  height: 54px !important;
  display: block;
  overflow: hidden;
  border-radius: 3px;
  font-size:16px
}
.border{
  border:3px solid rgb(247, 247, 247);
  padding-left:45px;
  padding-right:45px;
  background:  rgb(247, 247, 247);;
}
.gubun{
  text-align:left;padding-bottom:0px;
}
</style>