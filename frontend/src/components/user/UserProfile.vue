<template >
    <v-row>
      <v-col v-if="!loggedIn" cols="12" md="12">
        로그인회원만 사용가능합니다
      </v-col>
      <v-col v-else cols="12" md="12" >
        회원정보
        {{$store.state.myProfile.email}}
      </v-col>
   </v-row>
</template>

<script>
// import http from '@/util/http-common.js'
import { mapState ,mapGetters } from 'vuex'

export default {
  name: "UserProfile",
  data() {
    return {
    };
  },
  methods:{
  },
  computed : {
    ...mapGetters(['loggedIn']),
    ...mapState(['myProfile']),
  },
}
</script>

<style scoped>
</style>