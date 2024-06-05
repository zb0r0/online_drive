<template>
  <div>
    <Navbar />
    <h2>Hello, {{ currentUser.username }}</h2>
    <p>Username: {{ currentUser.username }}</p>
    <p>Email: {{ currentUser.email }}</p>
    <p>Premium: {{ currentUser.premium ? 'Yes' : 'No' }}</p>
    <div v-if="currentUser.premium">
      <p>You are a premium member!</p>
    </div>
    <div v-else>
      <form @submit.prevent="buyPremium">
        <button type="submit" class="btn btn-primary">Buy Premium</button>
      </form>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';

export default {
  name: 'ProfilePageComponent',
  components: {
    Navbar
  },
  data() {
    return {
      currentUser: {
        username: '',
        email: '',
        premium: false
      }
    };
  },
  methods: {
    buyPremium() {
      // Implement buy premium logic here
    }
  },
  mounted() {
    // Fetch the current user data from backend here
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
