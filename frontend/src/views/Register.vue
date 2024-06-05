<template>
  <div>
    <Navbar />
    <h1>Register</h1>
    <form @submit.prevent="register">
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" class="form-control" id="username" v-model="form.username">
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" class="form-control" id="email" v-model="form.email">
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" class="form-control" id="password" v-model="form.password">
      </div>
      <div class="mb-3">
        <label for="confirmPassword" class="form-label">Confirm Password</label>
        <input type="password" class="form-control" id="confirmPassword" v-model="form.confirmPassword">
      </div>
      <button type="submit" class="btn btn-primary">Register</button>
    </form>
    <p>Already have an account? <router-link to="/login">Log in</router-link></p>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';

export default {
  name: 'RegisterPage',
  components: {
    Navbar
  },
  data() {
    return {
      form: {
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
      }
    };
  },
  methods: {
    register() {
      // Implement register logic here
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
