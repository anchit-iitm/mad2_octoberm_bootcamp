import { createApp } from 'vue'
// from flask import Flask
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app123')
