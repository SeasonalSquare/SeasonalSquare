<template >
    <v-row>
      <v-col cols="12" md="12" >
        <div  class="section_login"> 
          <h3 class="tit_login">로그인</h3> 
          <div style="padding-top: 36px;">
            <v-text-field style="margin-bottom:0px !important" 
              v-model="id"
              label="아이디를 입력해주세요" solo  required
            ></v-text-field>

            <v-text-field  solo
              v-model="password"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show1 ? 'text' : 'password'"
              label="비밀번호를 입력해주세요"
              @click:append="show1 = !show1"
              required
            ></v-text-field>
            <v-btn color="#5C5749" style="border: 1px solid #5C5749;margin-top:15px" class="btn"><span style="color:#fff">로그인</span></v-btn>
            <v-btn color="#fff" style="border: 1px solid #5C5749;margin-top:10px" @click="goSignUp()" class="btn"><span style="color:#5C5749">회원가입</span></v-btn>
          </div>
          
        </div>


      </v-col>
   </v-row>
</template>

<script>
// import http from '@/util/http-common.js'

export default {
  name: "UserLogin",
  data() {
    return {
         show1: false,
         id: null,
         password: null,
    };
  },
  methods:{
    goSignUp(){
      this.$router.push({name: 'UserSignUp'})
    }
  },
 
}
</script>

<style scoped>
.tit_login{
    font-weight: 800;
    font-size: 20px;
    line-height: 20px;
    text-align: center;
}
.section_login{
   /* background: gray; */
   width: 340px;
   margin: 0 auto;
   padding-top: 90px;
   letter-spacing: -.6px;

}
.btn{
  width: 100%;
  height: 54px !important;
  display: block;
  overflow: hidden;
  border-radius: 3px;
  font-size:16px
}
</style>