<template>
  <div>
    <Navbar />
    <h1>Welcome to the Home Page</h1>
    <div v-if="isAuthenticated">
      <h2>Your Files:</h2>
      <ul>
        <li v-for="file in files" :key="file.id">
          <a :href="getFileUrl(file.filename)">{{ file.filename }}</a>
          <form @submit.prevent="deleteFile(file.id)" style="display: inline;">
            <button type="submit" class="btn btn-danger btn-sm">Delete</button>
          </form>
        </li>
      </ul>
      <router-link to="/upload">Upload New File</router-link>
    </div>
    <div v-else>
      <p>Please <router-link to="/login">log in</router-link> to see your files.</p>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';

export default {
  name: 'HomePageComponent',
  components: {
    Navbar
  },
  data() {
    return {
      isAuthenticated: false, // To be updated with real authentication check
      files: [] // Fetch the files from backend
    };
  },
  methods: {
    getFileUrl(filename) {
      return `/uploads/${filename}`;
    },
    // deleteFile(fileId) {
    //   // Implement file deletion logic here
    // }
  },
  mounted() {
    // Implement authentication status check logic and fetch files here
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
