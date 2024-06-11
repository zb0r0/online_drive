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
    <router-link to="/register">Don't have an account? Sign up</router-link>
    <div v-if="message" class="alert" :class="{'alert-success': success, 'alert-danger': !success}">
      {{ message }}
    </div>
  </div>
</template>

<script>
import axios from '../plugins/axios';

export default {
  name: 'LoginPage',
  data() {
    return {
      email: '',
      password: '',
      message: '',
      success: false
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
        this.success = true;
        this.message = 'Logged in successfully';
        this.$router.push('/');
      } catch (error) {
        this.success = false;
        if (error.response && error.response.data) {
          console.error('Error response data:', error.response.data);
          this.message = 'Login failed: ' + error.response.data.message;
        } else {
          console.error('Error:', error);
          this.message = 'Login failed: Unknown error';
        }
      }
    }
  }
};
</script>
