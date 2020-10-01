import Vue from "vue";
import Vuex from "vuex";
import http from '@/util/http-common.js'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {  //앱에서 공유할 데이터 관리, this.$stroe.state.이름 으로 접근
    token: sessionStorage.getItem("token"),
    myProfile: sessionStorage.getItem("myProfile")?JSON.parse(sessionStorage.getItem("myProfile")):[],
  },
  getters: {  //얻기
    config: (state) => ({headers: { Authorization: state.token }}),
    loggedIn(state){
      if(state.myProfile!=null && state.myProfile && state.myProfile!="" && state.myProfile!="null"){
        return true
      }
      return false
    }, 
  },
  mutations: { //동기적 처리  -> state 값 변경
    SET_USERPROFILE(state, value) {
      sessionStorage.setItem("myProfile",JSON.stringify(value))
      state.myProfile = value
    },
    SET_AUTH(state,value){
      sessionStorage.setItem("token",value)
      state.token = value
    },
    LOGOUT(state){
      state.myProfile=""
      state.token=""
      sessionStorage.removeItem("myProfile")
      sessionStorage.removeItem("token")
    },
  },
  actions: { //비동기 처리(dispatch로 호출)  , action 끝나고 mutations 호출 (stroe.commit()으로 호출)
    
    //1. 로그인 성공시, 사용자 정보가져옴 -> 
    setUserProfile( { commit, getters } ) {
      //console.log(">>>>>>>>>getters "+ JSON.stringify(getters));

      return http.get('/rest-auth/user/', getters.config)
      .then((res) => {
        console.log("내 정보", res)
        commit('SET_USERPROFILE', res.data)
      })
      .catch(err => console.log(err))
    },
    setAuth({commit},value){
      commit('SET_AUTH',value)
    },
    logout({commit}){
      commit("LOGOUT")
    },
  },
  modules: {},
});
