<template>
  <div id="NavBar">
    <v-app-bar
        app
        color="primary"
        dark
      >
        <div class="d-flex align-center">
          <p>제철의 광장</p>
        </div>

        <v-spacer class="justify-center">
          <!-- 공간 -->
          <router-link to='/login' ><span class="clbue">임시 로그인</span></router-link>
        </v-spacer>

      </v-app-bar>
    </div>
</template>

<script>
export default {
  name: "NavBar",
}
</script>

<style>

</style>