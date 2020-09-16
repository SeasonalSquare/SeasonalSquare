<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <h1>다음은 API위한 테스트 인풋 박스입니다.</h1>
          <v-text-field
            label="농수산물"
            solo
            v-model="TestInput"
            @keypress.enter="TextInput"
          >
          </v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        TestInput: ''

      }
   },
   methods:{
     TextInput() {
       console.log(this.TestInput)
     }
   }
  }
</script>
