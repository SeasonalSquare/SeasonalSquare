<template >
    <v-row>
      <v-col cols="0" lg="3" md="3"></v-col>
      <v-col cols="12" lg="6" md="6">
        <div  class="section_signUp"> 
          <h3 class="tit_signUp">회원가입</h3>
           <p style="border-bottom:1px solid black;color:#666;font-size:12px;text-align: right;line-height: 17px;padding: 23px 0 10px"><span class="subrequired">*</span> 필수입력사항</p>
          <div style="padding-top: 0px;">
            <v-row>
              <v-col cols="4"  lg="4"> <v-subheader class="subtitle">이메일<span class="subrequired">*</span></v-subheader></v-col>
              <v-col cols="5"  lg="6">
                <v-text-field  
                 v-model="email"
                  label="이메일을 입력해주세요" solo  required
                  :rules="emailRules"
                  ref="email"
                ></v-text-field>
              </v-col>

              <v-col cols="3" lg="2">
                <v-btn color="#fff" @click="goEmailChk()" style="border: 1px solid #5C5749;" class="btn">
                  <span style="color:#5C5749;font-size:14px;font-weight:bold">중복확인</span>
                </v-btn>
              </v-col>
              
            </v-row>

            <v-row>
              <v-col cols="4"  lg="4"> <v-subheader class="subtitle">비밀번호<span class="subrequired">*</span></v-subheader></v-col>
              <v-col cols="8"  lg="6">
                <v-text-field  label="비밀번호를 입력해주세요" solo  required
                  v-model="password1"
                  :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="show1 ? 'text' : 'password'"
                  @click:append="show1 = !show1"
                  :rules="passwordRules"
                  ref="password1"
                ></v-text-field>
              </v-col>
              <v-col cols="2"></v-col>
            </v-row>

            <v-row>
              <v-col cols="4"  lg="4"> <v-subheader class="subtitle">비밀번호 확인<span class="subrequired">*</span></v-subheader></v-col>
              <v-col cols="8"  lg="6">
                <v-text-field  label="비밀번호를 확인해주세요" solo  required
                 v-model="password2"
                   :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="show2 ? 'text' : 'password'"
                  @click:append="show2 = !show2"
                  :rules="passwordRules2"
                  ref="password2"
                ></v-text-field>
              </v-col>
              <v-col cols="2"></v-col>
            </v-row>

            <!-- <v-row>
              <v-col cols="4"  lg="4"> <v-subheader class="subtitle">휴대폰<span class="subrequired">*</span></v-subheader></v-col>
              <v-col cols="8"  lg="6">
                <v-text-field  label="숫자만 입력해주세요" solo  required></v-text-field>
              </v-col>
              <v-col cols="2"></v-col>
            </v-row> -->

            <v-row>
              <v-col cols="4"  lg="4"> <v-subheader class="subtitle">이름<span class="subrequired">*</span></v-subheader></v-col>
              <v-col cols="8"  lg="6">
                <v-text-field  
                  v-model="username"
                  label="이름을 입력해주세요" solo  required
                     :rules="usernameRules"
                     ref="username"
                ></v-text-field>
              </v-col>
              <v-col cols="2"></v-col>
            </v-row>

            <!-- <v-row>
              <v-col cols="4"  lg="4"> <v-subheader class="subtitle">성별<span class="subrequired">*</span></v-subheader></v-col>
              <v-col cols="8"  lg="6">
                <v-radio-group v-model="gender" row>
                  <v-radio label="남자" color="#EC8852" value="남자"></v-radio>
                  <v-radio label="여자" color="#EC8852" value="여자"></v-radio>
                </v-radio-group>
              </v-col>
              <v-col cols="2"></v-col>
            </v-row>

            <v-row>
              <v-col cols="4"  lg="4"> <v-subheader class="subtitle">생일<span class="subrequired">*</span></v-subheader></v-col>
              <v-col cols="8"  lg="6">
                <v-row>
                  <v-col cols="4"  style="padding-left:0px;padding-right:0px;">
                    <v-text-field  
                      v-model="id"
                      label="YYYY" solo  required
                    ></v-text-field>
                  </v-col>

                  <v-col cols="4"  style="padding-right:0px;">
                    <v-text-field  
                      v-model="id" 
                      label="MM" solo  required
                    ></v-text-field>
                  </v-col>

                  <v-col cols="4" style="padding-right:0px;">
                    <v-text-field  
                      v-model="id"
                      label="DD" solo  required
                    ></v-text-field>
                  </v-col>

                </v-row>
              </v-col>
              <v-col lg="2"></v-col>
            </v-row> -->

              <v-divider></v-divider>
            <v-row>
              <v-col cols="0" lg="2"></v-col>
              <v-col cols="12" lg="8">
                <v-btn color="#5C5749" style="border: 1px solid #5C5749;margin-top:15px" @click="goSignUp()" class="btn"><span style="color:#fff">가입하기</span></v-btn>
              </v-col>
              <v-col cols="0" lg="2"></v-col>
            </v-row>
          </div>
          
        </div>
      </v-col>
      <v-col cols="0" lg="3" md="3"></v-col>
   </v-row>
</template>

<script>
import http from '@/util/http-common.js'

export default {
  name: "UserSignUp",
  data() {
    return {
        show1: false,
        show2: false,
        email: null,
        password1: null,
        password2: null,
        username: null,
        emailRules: [
          // v => !!v || 'E-mail is required',
          v => /.+@.+\..+/.test(v) || '유효한 이메일 주소를 입력하십시오',
        ],
        passwordRules: [
          v => (v && v.length >= 8) || '비밀번호는 최소 8 문자를 포함해야 합니다',
        ],
        passwordRules2: [
          v => (v && v == this.password1) || '비밀번호가 일치하지 않습니다',
        ],
        usernameRules:[
          v => (v && v.length >= 1) || '이름은 필수 값 입니다',
        ],

    };
  },
  methods:{
    goEmailChk(){
      let form = new FormData();
      form.append("email", this.email);

      http.post('/rest-auth/signup/',form , {
              headers: {
                'Content-Type': 'multipart/form-data'
          }
        })
      .then(res => {
          console.log(res)
          
      })
      .catch(error => {
        // console.log('failed', error.response.data)
        if(error.response.data.email != null){
          let msg =error.response.data.email
          this.$dialog.notify.error(msg[0], {
            position: 'top-right',
            timeout: 3000
          })
          this.$refs.email.focus();
        }else{
          this.$dialog.notify.info('사용가능한 이메일입니다', {
            position: 'top-right',
            timeout: 3000
          })
        }
      })
    },
    goSignUp(){
      if(this.email == null){
        this.$dialog.notify.warning("이메일을 입력해주세요", {
            position: 'top-right',
            timeout: 3000
          })
          this.$refs.email.focus();
          return;
      }else if(this.password1 == null){
          this.$dialog.notify.warning("비밀번호를 입력해주세요", {
            position: 'top-right',
            timeout: 3000
          })
          this.$refs.password1.focus();
          return;
       }else if(this.password2 == null || this.password2 != this.password1){
          this.$dialog.notify.warning("비밀번호를 확인해주세요", {
            position: 'top-right',
            timeout: 3000
          })
          this.$refs.password2.focus();
          return;
      }else if(this.username == null){
          this.$dialog.notify.warning("이름을 입력해주세요", {
            position: 'top-right',
            timeout: 3000
          })
          this.$refs.username.focus();
          return;
      }

      let form = new FormData();
      form.append("email", this.email);
      form.append("password1", this.password1);
      form.append("password2", this.password2);
      form.append("username", this.username);

      http.post('/rest-auth/signup/',form , {
              headers: {
                'Content-Type': 'multipart/form-data'
          }
        })
      .then(res => {
          console.log(">>>>>>"+res)
          this.$dialog.notify.success('회원가입이 완료되었습니다', {
            position: 'top-right',
            timeout: 3000
          })
          this.$router.push({name: 'UserLogin'})
      })
      .catch(error => {
        let data = error.response.data;
        let msg;

        if(data.email != null){
          msg =data.email
          this.$refs.email.focus();
        }else if(data.password1 != null){
          msg =data.password1
          this.$refs.password1.focus();
        }else if(data.password2 != null){
          msg =data.password2
          this.$refs.password2.focus();
        }else if(data.username != null){
          msg =data.username
          this.$refs.username.focus();
        }else if(data.non_field_errors != null){
          msg =data.non_field_errors
          this.$refs.password2.focus();
        }else{
           console.log('failed', error.response.data)
           return;
        }

        this.$dialog.notify.error(msg[0], {
          position: 'top-right',
          timeout: 3000
        })


      })
    }
  },
 
}
</script>

<style scoped>
.tit_signUp{
    font-weight: 800;
    font-size: 30px;
    line-height: 20px;
    text-align: center;
}
.section_signUp{
   /* background: gray; */
   /* width: 500px; */
   margin: 0 auto;
   padding-top: 90px;
   letter-spacing: -.6px;

}
.btn{
  width: 100%;
  height: 50px !important;
  display: block;
  overflow: hidden;
  border-radius: 3px;
  font-size:16px
}
.subtitle{
   color:#333 !important;
   font-weight:700;
   letter-spacing:0;
}
.subrequired{
  color:#ee6a7b;
  font-size:13px;
  padding-bottom:2px;
}
</style>