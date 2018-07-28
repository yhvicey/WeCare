import Vue from 'vue';
import Router from 'vue-router';

import HomeView from '@/views/HomeView.vue';
import IntroductionView from '@/views/IntroductionView.vue';
import VideoView from '@/views/VideoView.vue';
import TwitterView from '@/views/TwitterView.vue';

Vue.use(Router);

const routes = [
  {
    path: '/',
    component: HomeView
  },
  {
    path: '/introduction',
    component: IntroductionView
  },
  {
    path: '/video',
    component: VideoView
  },
  {
    path: '/twitter',
    component: TwitterView
  },
  {
    path: '/live',
    component: TwitterView
  },
];

export default new Router({
  routes,
});
