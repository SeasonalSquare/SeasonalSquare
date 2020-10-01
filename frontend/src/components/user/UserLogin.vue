<template >
    <v-row>
      <v-col cols="12" md="12" >
        <div  class="section_login"> 
          <h3 class="tit_login">로그인</h3> 
          <div style="padding-top: 36px;">
            <v-text-field style="margin-bottom:0px !important" 
              v-model="email"
              label="이메일을 입력해주세요" solo  required
              ref="email"
            ></v-text-field>

            <v-text-field  solo
              v-model="password"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show1 ? 'text' : 'password'"
              label="비밀번호를 입력해주세요"
              @click:append="show1 = !show1"
              required
            ></v-text-field>
            <v-btn color="#5C5749" style="border: 1px solid #5C5749;margin-top:15px" @click="goLogin()" class="btn"><span style="color:#fff">로그인</span></v-btn>
            <v-btn color="#fff" style="border: 1px solid #5C5749;margin-top:10px" @click="goSignUp()" class="btn"><span style="color:#5C5749">회원가입</span></v-btn>
          </div>
          
        </div>

      </v-col>
   </v-row>
</template>

<script>
import http from '@/util/http-common.js'

export default {
  name: "UserLogin",
  data() {
    return {
         show1: false,
         email: null,
         password: null,
         username: "a2",
    };
  },
  methods:{
    goSignUp(){
      this.$router.push({name: 'UserSignUp'})
    },
    goLogin(){
      let form = new FormData();
      form.append("email", this.email);
      form.append("password", this.password);
      form.append("username", this.username);
      console.log(this.email);

      http.post('/rest-auth/login/',form , {
                 headers: {
                    'Content-Type': 'multipart/form-data'
              }
           })
          .then(res => {
            let frm = new FormData();
            frm.append("password", this.password);
            frm.append("username", this.username);
            
            console.log(">>"+res);

             http.post("/accounts/token/",frm , {
                 headers: {
                    'Content-Type': 'multipart/form-data'
                }
              }).then(res => {
                const data = res.data;
                console.log(">>>>>>>"+data.token);
                // console.log(">>>>>>>"+JSON.stringify(res));

                this.$store.dispatch("setAuth", "JWT " + data.token)
                this.$store.dispatch("setUserProfile", data.token);
                this.$router.push("/")

            })
          })
          .catch(error => {
            // console.log('failed', error.response.data)
            if(error.response.data.email != null){
             this.$dialog.notify.error('유효한 이메일 주소를 입력하십시오', {
                position: 'top-right',
                timeout: 2000
              })
              this.$refs.email.focus();
            }else{
              this.$dialog.notify.error('아이디 또는 비밀번호 오류입니다', {
                position: 'top-right',
                timeout: 2000
              })
            }
          })

      
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