<template>
  <div class="w-full h-screen">
    <div class="home-view absolute w-full h-full flex flex-col mx-auto">
      <div class="h-32"></div>
      <div class="main-title text-yellow-lighter mx-auto">WeCare</div>
      <div class="sub-title text-yellow-lighter self-center">- We care your mental health.</div>
      <div class="h-64"></div>
      <div class="container w-full flex flex-col mx-auto">
        <div class="container flex flex-row mx-auto justify-center">
          <router-link to="/introduction">
            <input class="nav-button w-64 h-10 mx-8 my-4 text-yellow-lighter border-yellow-lighter" type="button" value="Introduction" />
          </router-link>
          <router-link to="/video">
            <input class="nav-button w-64 h-10 mx-8 my-4 text-yellow-lighter border-yellow-lighter" type="button" value="Video" />
          </router-link>
        </div>
        <div class="container flex flex-row mx-auto justify-center">
          <router-link to="/twitter">
            <input class="nav-button w-64 h-10 mx-8 my-4 text-yellow-lighter border-yellow-lighter" type="button" value="Twitter Demo" />
          </router-link>
          <router-link to="/">
            <input class="nav-button w-64 h-10 mx-8 my-4 text-yellow-lighter border-yellow-lighter" type="button" value="Live Demo (WIP)" @click.prevent="wipAlert" />
          </router-link>
        </div>
        <div class="container flex flex-row mx-auto justify-center">
          <a href="https://garagehackbox.azurewebsites.net/hackathons/1214/projects/70915" target="_blank">
            <input class="nav-button w-64 h-10 mx-8 my-4 text-yellow-lighter border-yellow-lighter" type="button" value="Upvote for us!" />
          </a>
          <a href="mailto:yiwwan@microsoft.com">
            <input class="nav-button w-64 h-10 mx-8 my-4 text-yellow-lighter border-yellow-lighter" type="button" value="Feedback" />
          </a>
        </div>
      </div>
    </div>
    <video class="" autoplay loop id="video-background" muted>
      <source src="../../public/videos/videoplayback.mp4" type="video/mp4">
    </video>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";

@Component
export default class HomeView extends Vue {
  public wipAlert() {
    alert("Working in progress!");
  }
}
</script>

<style lang="scss" scoped>
@font-face {
  font-family: "Potra";
  src: url("../assets/fonts/Potra.ttf") format("truetype");
}

@font-face {
  font-family: "Calibril";
  src: url("../assets/fonts/calibril.ttf") format("truetype");
}

#video-background {
  position: fixed;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  z-index: 1;
  opacity: 0.6;
}

.home-view {
  z-index: 2;
  top: 0;
  left: 0;
}

.main-title {
  font-family: "Potra";
  font-size: 12rem;
}

.sub-title {
  font-family: "Calibril";
  font-size: 2.5rem;
  transform: translateX(50%);
}
</style>
