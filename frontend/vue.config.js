const path = require('path');

module.exports = {
  outputDir: path.resolve(__dirname, '../backend/static'),  // Katalog statyczny dla Flask
  indexPath: path.resolve(__dirname, '../backend/templates/index.html'),  // Ścieżka do index.html
  assetsDir: '',  // Katalog, w którym będą umieszczone zasoby (pliki CSS, JS, itp.)
  publicPath: process.env.NODE_ENV === 'production' ? './' : '/',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000',  // Adres backendu Flask
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
};
