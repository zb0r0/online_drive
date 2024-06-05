<template>
  <div>
    <h1>Upload Files</h1>
    <form @submit.prevent="uploadFile">
      <input type="file" @change="onFileChange" required>
      <button type="submit" class="btn btn-primary">Upload File</button>
      <span v-if="uploadError" style="color: red;">{{ uploadError }}</span>
    </form>
  </div>
</template>

<script>
export default {
  name: 'UploadPage',
  data() {
    return {
      fileToUpload: null,
      uploadError: ''
    };
  },
  methods: {
    onFileChange(event) {
      this.fileToUpload = event.target.files[0];
    },
    uploadFile() {
      if (!this.fileToUpload) {
        this.uploadError = 'Please select a file.';
        return;
      }

      let formData = new FormData();
      formData.append('file', this.fileToUpload);

      fetch('/api/upload', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        console.log(data.message);
        this.$router.push('/');
      })
      .catch(error => {
        console.error('Error:', error);
        this.uploadError = 'Error uploading file. Please try again.';
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

input[type="file"] {
  display: block;
  margin-bottom: 10px;
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
