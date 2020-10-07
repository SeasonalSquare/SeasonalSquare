<template>
  <div id="NavBar">
    <v-app-bar
        app height="35%"
        color="#FFFFFF"
        dark flat id="nav"
      >
        <!-- <div class="d-flex align-center">
          <p>제철의 광장</p>
        </div> -->

        <v-spacer class="justify-center">
          <!-- 공간 -->
        </v-spacer>

        <div  class="text-right" id="userMenu">
           <ul class="list_menu" v-if="!loggedIn">
            <li  class="menu" >
            <li  class="menu" > <a class="nav1" @click="goSignUp()">회원가입</a> </li>
            <li class="menu"  style="padding-right:10px"> | </li>
            <li  class="menu" > <a class="nav2" @click="goLogin()">로그인</a> </li>
          </ul>
          <ul class="list_menu"  v-else>
            <li  class="menu" >
            <li  class="menu" > <a class="nav1" @click="goCart()">장바구니</a> </li>
            <li class="menu"  style="padding-right:10px"> | </li>
            <li  class="menu" > <a class="nav2" style="padding-right:10px;" @click="goMyProfile()">내정보</a> </li>
            <li class="menu"  style="padding-right:10px"> | </li>
            <li  class="menu" > <a class="nav2" @click="goLogout()">로그아웃</a> </li>
          </ul>
        </div>
      </v-app-bar>

      <v-row  align="center" style="margin-top:30px">
        <v-col align="center">
            <div style="">
              <a  @click.prevent="moveToMain"><v-img width="115px" src="@/assets/logo2.png"></v-img></a>
            </div>
        </v-col>
      </v-row>

      <v-row>
        <v-col align="center" style="margin:auto;padding:0px;">
            <div style="border-bottom:solid 1px rgba(0,0,0,0.1);height:48px;" class="shadow">
            </div>
        </v-col>
      </v-row>
    </div>
</template>

<script>
import {mapState,mapGetters} from 'vuex'

export default {
  name: "NavBar",
  data(){
    return{
        windowTop: 0,
        
    }
  },
  components: {
  },
  computed: {
      ...mapState(['token', 'myProfile']),
      ...mapGetters(['loggedIn'])
  },
  watch: {
    windowTop: function() {
        if (this.windowTop >= 100) {
           let navi =  document.getElementById('nav');        
           navi.style.borderBottom = 'solid 1px rgba(0,0,0,0.1)';
        }
        else {
          let navi =  document.getElementById('nav');  
          navi.style.borderBottom= '';
        }
    }
  },
  methods:{

      onScroll(e) {
        this.windowTop = e.target.documentElement.scrollTop;
      },
      goLogin(){
        this.$router.push({name: 'UserLogin'}).catch(() => {})
      },
      goSignUp(){
        this.$router.push({name: 'UserSignUp'}).catch(() => {})
      },
      goCart(){
        this.$router.push({name: 'AllCart'}).catch(() => {})
      },
      moveToMain() {
        this.$router.push("/").catch(() => {})
      },
      goLogout() {
         this.$store.dispatch("logout")
         this.moveToMain();
      },
      goMyProfile(){
        if (this.loggedIn) {
          this.$router.push({ name: 'UserProfile' }).catch(() => {})
        } else {
            this.$dialog.notify.error('로그인 해주세요', {
                position: 'top-right',
                timeout: 2000
            })
        }
      }
    },
    mounted() {
        window.addEventListener("scroll", this.onScroll)
    },
    beforeDestroy() {
        window.removeEventListener("scroll", this.onScroll);
    },

}
</script>

<style scoped>
ul{
  list-style-type: none;
}
#userMenu .menu {
    position: relative;
    z-index: 400;
    float: left;
    font-size: 14px;
    font-weight: bold;
    color:#a4aaa6;
}
#userMenu .list_menu{
  float: right;
}
#userMenu *{
  letter-spacing:-.3px;
}
.shadow {
  -webkit-box-shadow: 0 6px 4px -4px rgba(0, 0, 0, 0.1) !important;
  -moz-box-shadow: 0 6px 4px -4px rgba(0, 0, 0, 0.1) !important;
  box-shadow: 0 6px 4px -4px  rgba(0, 0, 0, 0.1) !important;
}
.nav1{
  color:#EC8852;
  font-weight:700;
  padding-right:10px;
}
.nav2{
  color:#333;
  font-weight:700;
}
</style>