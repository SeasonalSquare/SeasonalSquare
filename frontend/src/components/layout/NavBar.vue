<template>
  <div id="NavBar">
    <v-app-bar
        app height="35%"
        color="#FFFFFF"
        dark flat id="nav"
      >
        <div class="d-flex align-center">
          <p>제철의 광장</p>
        </div>

        <v-spacer class="justify-center">
          <!-- 공간 -->
          <router-link to='/login' ><span class="clbue">임시 로그인</span></router-link>
        </v-spacer>

        <div  class="text-right" id="userMenu">
          <ul class="list_menu">
            <li  class="menu" style="color:#EC8852;padding-right:10px"> 회원가입 </li>
            <li class="menu"  style="padding-right:10px"> | </li>
            <li  class="menu" style="color:#333"> 로그인 </li>
          </ul>
        </div>
      </v-app-bar>

      <v-row  align="center" style="margin-top:30px">
        <v-col align="center">
            <div style="">
              <v-img width="115px" src="@/assets/logo2.png" @click.prevent="moveToMain"></v-img>
            </div>
        </v-col>
      </v-row>

      <v-row>
        <v-col align="center" style="margin:auto;padding:0px;">
            <div style="border-bottom:solid 1px rgba(0,0,0,0.1);" class="shadow">
                <category-tabs style="width:80%;height:48px;" />
            </div>
        </v-col>
      </v-row>
    </div>
</template>

<script>
import CategoryTabs from "@/components/layout/CategoryTabs.vue"

export default {
  name: "NavBar",
  data(){
    return{
        windowTop: 0,
        
    }
  },
  components: {
      CategoryTabs,
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
        moveToMain() {
          this.$router.push("/").catch(() => {})
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
  -webkit-box-shadow: 0 6px 4px -4px rgba(0, 0, 0, 0.1);
  -moz-box-shadow: 0 6px 4px -4px rgba(0, 0, 0, 0.1);
  box-shadow: 0 6px 4px -4px rgba(0, 0, 0, 0.1);
}

</style>