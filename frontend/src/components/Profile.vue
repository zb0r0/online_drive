<template>
  <div>
    <h1>User Profile</h1>
    <p>Welcome, {{ currentUser.username }}</p>
    <p>Email: {{ currentUser.email }}</p>
    <button @click="buyPremium" class="btn btn-primary">Buy Premium</button>
    <p v-if="currentUser.premium">You are a premium user!</p>
  </div>
</template>

<script>
export default {
  name: 'ProfilePage',
  data() {
    return {
      currentUser: {}
    };
  },
  mounted() {
    this.getCurrentUser();
  },
  methods: {
    getCurrentUser() {
      fetch('/api/current_user')
        .then(response => response.json())
        .then(data => {
          this.currentUser = data.user;
        })
        .catch(error => {
          console.error('Error:', error);
        });
    },
    buyPremium() {
      fetch('/api/buy_premium', {
        method: 'POST'
      })
      .then(response => response.json())
      .then(data => {
        console.log(data.message);
        this.getCurrentUser();
      })
      .catch(error => console.error('Error:', error));
    }
  }
};
</script>

<style scoped>
h1 {
  color: #333;
  font-size: 24px;
}

p {
  margin-bottom: 10px;
  font-size: 16px;
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
</style>
