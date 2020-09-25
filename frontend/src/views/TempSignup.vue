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
        label="Password1"
        solo
        v-model="password1"
      >
      </v-text-field>
      <v-text-field
        label="Password2"
        solo
        v-model="password2"
        @keypress.enter="TempSignup"
      >
      </v-text-field>
  </v-container>
</template>

<script>
import http from '@/util/http-common.js'

export default {
  name:'TempSignup',
  data() {
    return {
      id: "",
      password1: "",
      password2: "",
    }
  },
  methods:{
    TempSignup() {
      http
        .post('/rest-auth/signup/', {
          username: this.id,
          password1: this.password1,
          password2: this.password2
        })
      .then( res => {
        console.log(res)
      })
      .catch( err => {
        console.log(err + " 뒤진다")
      })
    },
    

  }
}
</script>

<style>

</style>