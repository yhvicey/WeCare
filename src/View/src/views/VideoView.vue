<template>
  <div class="w-full h-screen">
    <div class="video-bg w-full h-full"></div>
    <div class="main-content w-4/5 h-4/5 flex justify-center items-center flex-col rounded-lg shadow-lg">
      <div class="w-full h-full p-5 rounded-lg">
        <video class="video-js vjs-big-play-centered w-full h-full rounded-lg" id="player" controls preload>
          <source src="https://files.vicey.cn/public/final.mp4" type="video/mp4">
        </video>
      </div>
      <!-- <div class="w-full h-1/4 px-10 mt-5 rounded-lg flex justify-center items-center">
        <div class="w-full h-full p-4 bg-yellow-lighter rounded-lg shadow-lg">
          Have you ever
        </div>
      </div> -->
    </div>
    <home-button></home-button>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { Prop } from "vue-property-decorator";

import "video.js/dist/video-js.min.css";

import VideoJs from "video.js";

import HomeButton from "@/components/App/HomeButton.vue";
import Utils from "@/utils";

@Component({
  components: {
    HomeButton
  }
})
export default class VideoView extends Vue {
  public mounted() {
    const player = VideoJs("player");
    player.ready(function(this: VideoJs.Player) {
      this.on("ended", function(event: Event) {
        Utils.notify(
          "Do you like this video? Please go to our project site and UPVOTE for us!",
          result => {
            if (result) {
              window.open(
                "https://garagehackbox.azurewebsites.net/hackathons/1214/projects/70915",
                "_blank"
              );
            }
          }
        );
      });
    });
  }
}
</script>

<style scoped>
.video-bg {
  position: fixed;
  top: 0%;
  left: 0%;
  background-image: url("../assets/images/bg-video.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  z-index: 1;
  filter: blur(5px);
}

.main-content {
  background-color: rgba(255, 255, 255, 0.35);
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
}

.pt-36 {
  padding-top: 9rem;
}

.h-4\/5 {
  height: 80%;
}

.h-1\/4 {
  height: 25%;
}

.h-3\/4 {
  height: 75%;
}

.h-4\/5 {
  height: 80%;
}
</style>
