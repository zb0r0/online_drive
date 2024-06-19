<template>
  <div>
    <h1>Welcome to the Home Page</h1>
    <div v-if="isAuthenticated">
      <h2>Your Files:</h2>
      <ul>
        <li v-for="file in files" :key="file.id">
          <a :href="getBackendFileUrl(file.filename)" target="_blank">{{ file.filename }}</a>
          <button @click="deleteFile(file.id)" class="btn btn-danger btn-sm">Delete</button>
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
import axios from '../plugins/axios';

export default {
  name: 'HomePage',
  data() {
    return {
      files: [],
      isAuthenticated: false
    };
  },
  methods: {
    async fetchFiles() {
      try {
        const response = await axios.get('/files');
        console.log('Fetched files:', response.data);
        this.files = response.data;
      } catch (error) {
        console.error('Error fetching files:', error);
      }
    },
    async deleteFile(fileId) {
      try {
        await axios.delete(`/files/${fileId}`);
        console.log(`Deleted file with id: ${fileId}`);
        this.fetchFiles();
      } catch (error) {
        console.error('Error deleting file:', error);
      }
    },
    getBackendFileUrl(filename) {
      const backendBaseUrl = 'http://127.0.0.1:5000/uploads';
      return `${backendBaseUrl}/${filename}`;
    }
  },
  created() {
    this.isAuthenticated = !!localStorage.getItem('token');
    if (this.isAuthenticated) {
      this.fetchFiles();
    }
  }
};
</script>
