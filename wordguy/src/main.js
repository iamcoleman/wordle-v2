import Vue from 'vue';
import VueCountdown from '@chenfengyuan/vue-countdown';
import Toast from 'vue-toastification';
import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
import 'vue-toastification/dist/index.css'; // vue-toastification styles

Vue.config.productionTip = false;

// Add VueCountdown
Vue.component(VueCountdown.name, VueCountdown);

// Add vue-toastification
const toastOptions = {
  transition: 'Vue-Toastification__fade',
  position: 'top-center',
  maxToasts: 5,
  newestOnTop: true,
  icon: false,
  timeout: 4000,
};
Vue.use(Toast, toastOptions);

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
