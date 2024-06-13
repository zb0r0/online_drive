<template>
  <div>
    <h1 class="mb-4">Register</h1>
    <form @submit.prevent="register">
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" v-model="username" class="form-control" required />
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" v-model="email" class="form-control" required />
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" v-model="password" class="form-control" required />
      </div>
      <div class="mb-3">
        <label for="confirmPassword" class="form-label">Confirm Password</label>
        <input type="password" v-model="confirmPassword" class="form-control" required />
      </div>
      <div class="mb-3">
        <button type="submit" class="btn btn-primary">Register</button>
      </div>
    </form>
    <router-link to="/login">Already have an account? Log in</router-link>
  </div>
</template>

<script>
import axios from '../plugins/axios';

export default {
  name: 'RegisterPage',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirmPassword: ''
    };
  },
  methods: {
    async register() {
      if (this.password !== this.confirmPassword) {
        alert("Passwords do not match");
        return;
      }
      try {
        await axios.post('/users', {
          username: this.username,
          email: this.email,
          password: this.password
        });
        this.$router.push('/login');
      } catch (error) {
        if (error.response && error.response.data.message) {
          alert(error.response.data.message);
        } else {
          console.error('Registration failed:', error);
        }
      }
    }
  }
};
</script>
