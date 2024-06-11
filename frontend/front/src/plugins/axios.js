import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://127.0.0.1:5000/api', // Zmień na właściwy URL twojego backendu
  headers: {
    'Content-Type': 'application/json',
  },
});

// Dodaj interceptor do dodawania tokena JWT do nagłówków
instance.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});

export default instance;
