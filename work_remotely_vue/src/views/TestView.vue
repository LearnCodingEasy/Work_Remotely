<script setup>
// import { RouterLink, RouterView } from 'vue-router'
// import { ref } from 'vue'
// import axios from 'axios'

// import { onMounted } from 'vue'
// import { useUserStore } from '@/stores/user'
// import { useRouter } from 'vue-router'

// const userStore = useUserStore()
// userStore.initStore()
// const router = useRouter()

// onMounted(() => {})
</script>
<template>
  <div class="wrapper_page">
    <div class="inner_page">
      <h1>Home Page</h1>
      <p>Welcome to the home page!</p>
      <button @click="changePage">Change Page</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TestView',
  data() {
    return {}
  },
  mounted() {
    document.title = 'Home'
  },
  methods: {},
}
</script>

<style lang="scss" scoped></style>
