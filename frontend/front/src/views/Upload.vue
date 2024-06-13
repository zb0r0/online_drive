<template>
  <div>
    <h1>Upload File</h1>
    <form @submit.prevent="uploadFile" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="file" class="form-label">Choose file</label>
        <input type="file" @change="onFileChange" class="form-control" required />
      </div>
      <div class="mb-3">
        <button type="submit" class="btn btn-primary">Upload</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from '../plugins/axios';

export default {
  name: 'UploadPage',
  data() {
    return {
      file: null
    };
  },
  methods: {
    onFileChange(e) {
      this.file = e.target.files[0];
    },
    async uploadFile() {
      if (!this.file) {
        alert('Please select a file to upload.');
        return;
      }

      try {
        const formData = new FormData();
        formData.append('file', this.file);

        await axios.post('/files', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        this.$router.push('/');
      } catch (error) {
        console.error('Error uploading file:', error);
      }
    }
  }
};
</script>

<style scoped>
/* Dodaj style, jeśli potrzebujesz */
</style>
