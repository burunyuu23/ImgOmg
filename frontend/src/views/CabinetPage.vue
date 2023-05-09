<script>
  export default {
      methods: {
          async doing() {
              let obj = await this.$axios
                  .get('http://localhost:8000/')
              console.log(obj);
          },
          async doing2() {
              let obj = await this.$axios
                  .post('http://localhost:8000/add-test/',
                      {
                          'id':'5',
                          'name':'testname'
                      })
              console.log(obj);
          }
      }
  }
</script>

<template>
hi there!
  <v-btn @click="doing2">click me</v-btn>
</template>

<style scoped>

</style>