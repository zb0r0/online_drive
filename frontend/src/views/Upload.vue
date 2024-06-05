<template>
  <div>
    <Navbar />
    <h1>Upload File</h1>
    <form @submit.prevent="uploadFile" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="file" class="form-label">File</label>
        <input type="file" class="form-control" id="file" @change="handleFileUpload">
      </div>
      <button type="submit" class="btn btn-primary">Upload</button>
    </form>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';

export default {
  name: 'UploadPage',
  components: {
    Navbar
  },
  data() {
    return {
      selectedFile: null
    };
  },
  methods: {
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0];
    },
    uploadFile() {
      const formData = new FormData();
      formData.append('file', this.selectedFile);

      // Implement file upload logic here
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
