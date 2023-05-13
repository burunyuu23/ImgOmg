<template>
  <div>
    <p>{{ user.name }}</p>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'TestPage',
  data() {
    return {
      user: {}
    }
  },
  mounted() {
    axios.get('/api/user/current')
        .then(response => {
          this.user = response.data
        })
  }
}
</script>