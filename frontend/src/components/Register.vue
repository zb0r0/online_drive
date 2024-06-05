<template>
  <div>
    <h1>Create Your Online Drive Account</h1>
    <form @submit.prevent="register">
      <input type="text" v-model="registerForm.username" placeholder="Username" required>
      <input type="email" v-model="registerForm.email" placeholder="Email" required>
      <input type="password" v-model="registerForm.password" placeholder="Password" required>
      <button type="submit" class="btn btn-primary">Register</button>
      <span v-if="registerError" style="color: red;">{{ registerError }}</span>
    </form>
  </div>
</template>

<script>
export default {
  name: 'RegisterPage',
  data() {
    return {
      registerForm: {
        username: '',
        email: '',
        password: ''
      },
      registerError: ''
    };
  },
  methods: {
    register() {
      fetch('/api/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.registerForm)
      })
      .then(response => response.json())
      .then(data => {
        if (data.message === 'Registration successful') {
          this.$router.push('/login');
        } else {
          this.registerError = 'Registration failed. Please check your information.';
        }
      })
      .catch(error => {
        console.error('Error:', error);
        this.registerError = 'Error registering. Please try again.';
      });
    }
  }
};
</script>

<style scoped>
h1 {
  color: #333;
  font-size: 24px;
}

form {
  margin-top: 20px;
}

input[type="text"],
input[type="email"],
input[type="password"] {
  display: block;
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.btn {
  display: inline-block;
  padding: 6px 12px;
  margin-bottom: 0;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.42857143;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  cursor: pointer;
  border: 1px solid transparent;
  border-radius: 4px;
  user-select: none;
}

.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}

span {
  display: block;
  margin-top: 10px;
  font-size: 14px;
}
</style>
