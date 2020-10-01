import Vue from "vue";
import Vuex from "vuex";
import http from '@/util/http-common.js'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: sessionStorage.getItem("token"),
    myProfile: sessionStorage.getItem("myProfile")?JSON.parse(sessionStorage.getItem("myProfile")):[],
  },
  getters: {
    config: (state) => ({headers: { Authorization: state.token }}),
    loggedIn(state){
      if(state.myProfile!=null && state.myProfile && state.myProfile!="" && state.myProfile!="null"){
        return true
      }
      return false
    }, 
  },
  mutations: {
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
  actions: {
    setUserProfile( { commit, getters } ) {

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
