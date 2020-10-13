<template>
  <v-app>
    <NavBar/>
    <router-view></router-view>
    <Footer/>
  </v-app>
</template>

<script>
// Layouts
import NavBar from '@/components/layout/NavBar.vue'
import Footer from '@/components/layout/Footer.vue'

export default {
  name: 'App',

  components: {
    NavBar,
    Footer,
  },
  data() {
    return {

    }
  },
};
</script>
