// app.js
const app = Vue.createApp({
    data() {
        return {
            message: 'Hello Vue!'
        };
    },
    created() {
        console.log('Vue app created.');
    }
});

app.mount('#app');
