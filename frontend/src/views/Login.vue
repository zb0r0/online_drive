<template>
  <div>
    <Navbar />
    <h1>Login</h1>
    <form @submit.prevent="login">
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" class="form-control" id="username" v-model="form.username">
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" class="form-control" id="password" v-model="form.password">
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
    <p>Don't have an account? <router-link to="/register">Register</router-link></p>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';

export default {
  name: 'LoginPage',
  components: {
    Navbar
  },
  data() {
    return {
      form: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    login() {
      // Implement login logic here
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
