<template>
  <div>
    <h1>Login to Your Online Drive</h1>
    <form @submit.prevent="login">
      <input type="email" v-model="loginForm.email" placeholder="Email" required>
      <input type="password" v-model="loginForm.password" placeholder="Password" required>
      <button type="submit" class="btn btn-primary">Login</button>
      <span v-if="loginError" style="color: red;">{{ loginError }}</span>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      loginForm: {
        email: '',
        password: ''
      },
      loginError: ''
    };
  },
  methods: {
    login() {
      fetch('/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.loginForm)
      })
      .then(response => response.json())
      .then(data => {
        if (data.message === 'Login successful') {
          this.$router.push('/');
        } else {
          this.loginError = 'Login unsuccessful. Please check your credentials.';
        }
      })
      .catch(error => {
        console.error('Error:', error);
        this.loginError = 'Error logging in. Please try again.';
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
