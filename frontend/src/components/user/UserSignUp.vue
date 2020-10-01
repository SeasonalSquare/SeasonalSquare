<template >
    <v-row>
      <v-col cols="0" lg="3" md="3"></v-col>
      <v-col cols="12" lg="6" md="6">
        <div  class="section_signUp"> 
          <h3 class="tit_signUp">회원가입</h3>
           <p style="border-bottom:1px solid black;color:#666;font-size:12px;text-align: right;line-height: 17px;padding: 23px 0 10px"><span class="subrequired">*</span> 필수입력사항</p>
          <div style="padding-top: 0px;">
            <v-row>
              <v-col cols="4"  lg="4"> <v-subheader class="subtitle">아이디<span class="subrequired">*</span></v-subheader></v-col>
              <v-col cols="5"  lg="6">
                <v-text-field  
                 v-model="email"
                  label="이메일을 입력해주세요" solo  required
                  :rules="emailRules"
                ></v-text-field>
              </v-col>

              <v-col cols="3" lg="2">
                <v-btn color="#fff" style="border: 1px solid #5C5749;" class="btn">
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
              <v-col cols="0" lg="3"></v-col>
              <v-col cols="12" lg="6">
                <v-btn color="#5C5749" style="border: 1px solid #5C5749;margin-top:15px" class="btn"><span style="color:#fff">가입하기</span></v-btn>
              </v-col>
              <v-col cols="0" lg="3"></v-col>
            </v-row>
          </div>
          
        </div>
      </v-col>
      <v-col cols="0" lg="3" md="3"></v-col>
   </v-row>
</template>

<script>
// import http from '@/util/http-common.js'

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