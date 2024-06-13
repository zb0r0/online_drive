<template>
  <div>
    <h1 class="mb-4">Login</h1>
    <form @submit.prevent="login">
      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" v-model="email" class="form-control" required />
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" v-model="password" class="form-control" required />
      </div>
      <div class="mb-3">
        <button type="submit" class="btn btn-primary">Login</button>
      </div>
    </form>
    <router-link to="/register">Don't have an account? Register</router-link>
  </div>
</template>

<script>
import axios from '../plugins/axios';

export default {
  name: 'LoginPage',
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('/login', {
          email: this.email,
          password: this.password
        });

        localStorage.setItem('token', response.data.token);
        localStorage.setItem('userId', response.data.userId);
        this.$router.push('/profile');
      } catch (error) {
        console.error('Error logging in:', error);
      }
    }
  }
};
</script>
