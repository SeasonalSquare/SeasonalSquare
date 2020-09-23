<template>
  <v-app>
    <NavBar/>
    <router-view></router-view>
    <Footer/>
  </v-app>
</template>

<script>
// import Main from '@/components/Main.vue';
// Layouts
import NavBar from '@/components/layout/NavBar.vue'
import Footer from '@/components/layout/Footer.vue'

export default {
  name: 'App',

  components: {
    // Main,
    NavBar,
    Footer,
  },
  data() {
    return {

    }
  },
};
</script>
