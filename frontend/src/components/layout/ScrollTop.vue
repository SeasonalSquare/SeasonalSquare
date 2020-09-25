<template>
     <v-tooltip top >
       <template v-slot:activator="{ on, attrs }">
        <v-btn id="scrollButton"  v-bind="attrs" v-on="on"
            fab
            
            color="#5C5749"
            retain-focus-on-click
            @click="scrollToTop"
        > 
        <i style="color:#fff;font-size:25px" class="fas fa-arrow-up"></i>
        </v-btn>
       </template>
      <span>Return to Top</span>
    </v-tooltip>
</template>

<script>
export default {
  name: 'ScrollTop',
  components: {
  },
  data() {
    return {
      windowTop: 0,
    }
  },
  watch: {
    windowTop: function() {
        if (this.windowTop > 300) {
            let btn = document.getElementById('scrollButton')
            btn.style.display = 'block'
        }
        else {
            let btn = document.getElementById('scrollButton')
            btn.style.display = 'none'
        }
    }
  },
  mounted() {
      window.addEventListener("scroll", this.onScroll)
  },
  beforeDestroy() {
      window.removeEventListener("scroll", this.onScroll);
  },
  methods: {
      scrollToTop() {
          window.scroll({top: 0, left: 0, behavior: 'smooth'})
      },
      onScroll(e) {
          this.windowTop = e.target.documentElement.scrollTop;
      }
  }
  
}
</script>

<style scoped>
 #scrollButton {
   z-index: 10;
    position: fixed;
    display: none;
    bottom: 50px;
    right: 30px;
}
</style>
