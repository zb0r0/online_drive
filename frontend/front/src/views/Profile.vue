<template>
  <div>
    <h2>Hello, {{ profile.username }}</h2>
    <p>Username: {{ profile.username }}</p>
    <p>Email: {{ profile.email }}</p>
    <p>Premium: {{ profile.premium ? 'Yes' : 'No' }}</p>
    <div v-if="!profile.premium">
      <button @click="buyPremium" class="btn btn-primary">Buy Premium</button>
    </div>
  </div>
</template>

<script>
import axios from '../plugins/axios';

export default {
  name: 'ProfilePage',
  data() {
    return {
      profile: {}
    };
  },
  methods: {
    async fetchProfile() {
      try {
        const response = await axios.get(`/users/${localStorage.getItem('userId')}`);
        this.profile = response.data;
      } catch (error) {
        console.error('Error fetching profile:', error);
      }
    },
    async buyPremium() {
      try {
        await axios.post('/buy_premium');
        this.fetchProfile();
      } catch (error) {
        console.error('Error buying premium:', error);
      }
    }
  },
  created() {
    this.fetchProfile();
  }
};
</script>
