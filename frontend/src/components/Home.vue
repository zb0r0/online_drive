<template>
  <div>
    <h1>Welcome to Your Online Drive</h1>
    <div v-if="authenticated">
      <h2>Your Files:</h2>
      <ul>
        <li v-for="file in files" :key="file.id">
          <a :href="getFileUrl(file.filename)" target="_blank">{{ file.filename }}</a>
          <button @click="deleteFile(file.id)" class="btn btn-danger btn-sm">Delete</button>
        </li>
      </ul>
      <input type="file" @change="onFileChange">
      <button @click="uploadFile" class="btn btn-primary">Upload File</button>
    </div>
    <div v-else>
      <p>Please <router-link to="/login">log in</router-link> to see your files.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      files: [],
      authenticated: false,
      fileToUpload: null
    };
  },
  mounted() {
    this.getFiles();
  },
  methods: {
    getFiles() {
      fetch('/api/files')
        .then(response => response.json())
        .then(data => {
          this.files = data.files;
          this.authenticated = true;
        })
        .catch(error => {
          console.error('Error:', error);
          this.authenticated = false;
        });
    },
    deleteFile(fileId) {
      fetch(`/api/delete/${fileId}`, {
        method: 'POST'
      })
      .then(response => response.json())
      .then(data => {
        console.log(data.message);
        this.getFiles();
      })
      .catch(error => console.error('Error:', error));
    },
    onFileChange(event) {
      this.fileToUpload = event.target.files[0];
    },
    uploadFile() {
      if (!this.fileToUpload) return;

      let formData = new FormData();
      formData.append('file', this.fileToUpload);

      fetch('/api/upload', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        console.log(data.message);
        this.getFiles();
      })
      .catch(error => console.error('Error:', error));
    },
    getFileUrl(filename) {
      return `/static/${filename}`;
    }
  }
};
</script>

<style scoped>
h1 {
  color: #333;
  font-size: 24px;
}

h2 {
  color: #555;
  font-size: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}

p {
  color: #777;
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

.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}

input[type="file"] {
  display: inline-block;
  margin-bottom: 10px;
}

</style>
