<template>
  <v-container class="justify-center text-center">
    <h1>Hi There!</h1>
        <v-text-field
          label="ID"
          solo
          v-model="id"
        >
        </v-text-field>
        <v-text-field
          label="Password"
          solo
          v-model="password"
          @keypress.enter="tempLogin"
        >
        </v-text-field>
  </v-container>
</template>

<script>
import http from '@/util/http-common.js'

export default {
  name:'TempLogin',
  data() {
    return {
      id: "",
      password: "",
    }
  },
  methods:{
    tempLogin() {
      http
        .post('/accounts/token/', {
          username: this.id,
          password: this.password
        })
      .then( res => {
        console.log(res)
      })
      .catch( err => {
        console.log(err + "죽인다")
      })
    },
    loginHandler() {
      http
        .post(`/user/login`, {
          email: this.email,
          password: this.pw,
        })
        .then(({ data }) => {
          // JSON 형태
          let msg = "아이디 혹은 비밀번호를 다시 확인해주세요.";

          if (data.success === "success") {
            this.$session.set("email", this.email);
            this.$session.set("userNo", data.userinfo.userNo);
            this.$session.set("name", data.userinfo.name);
            this.$session.set("gender", data.userinfo.gender);
            this.$session.set("birth", data.userinfo.birth);
            this.$session.set("phone", data.userinfo.phone);
            this.$session.set("token", data.token);
            this.$router.push("/");
            this.$router.go();
          } else {
            alert(msg);
          }
        })
        .catch((err) => {
          alert(err + "에러가 발생했습니다");
        });
    },

  }
}
</script>

<style>

</style>