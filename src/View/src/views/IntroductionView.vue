<template>
  <div class="h-screen">
    <intro-section fixed class="h-full" :src="require('../assets/images/bg-intro-1.jpg')">
      <div class="flex items-center justify-center h-full">
        <div class="flex items-center justify-center h-full w-2/5">
          <div class="max-w-lg text-white font-mono text-50pt opacity-50 font-extrabold">
            OUR INSPIRATION
          </div>
        </div>
        <div class="flex items-center justify-center h-full w-3/5">
          <div class="text-left max-w-lg text-white font-mono text-2xl">
            &nbsp;&nbsp;&nbsp;&nbsp;
            <font class="text-4xl">WHEN</font> we come down with a cold, most of us don't hesitate to pop a pill or visit the doctor. But if we can't seem to shake our endless worries or hopelessness, we keep it down as if nothing is wrong. Hence although roughly one in four adults in the U.S. suffers from a diagnosable mental disorder, less than half receive treatment. If left ignored, mental disorders can impede all aspects of health. For all these reasons, recognizing the warning signs of mental illness is one of the most important challenges facing our society today.
          </div>
        </div>
      </div>
    </intro-section>
    <intro-section fixed class="h-full" :src="require('../assets/images/bg-intro-2.jpg')">
      <div class="flex items-center justify-center h-full">
        <div class="flex items-center justify-center h-full w-3/5">
          <div class="text-left max-w-lg text-white font-mono opacity-80 text-2xl">
            &nbsp;&nbsp;&nbsp;&nbsp;
            <font class="text-4xl">WECARE</font> is an AI based mood tracker that can be integrated into every social media platforms from Twitter to WeChat. By tracking the text, images and voice messages in your content and comments, WeCare is able to analyze your daily feelings and take action when your mood swings and triggers a threshold. WeCare’s actions range from suggesting music to notifying your emergency contact depending on your status.
          </div>
        </div>
        <div class="flex items-center justify-center h-full w-2/5">
          <div class="max-w-lg text-white font-mono text-50pt opacity-50 font-extrabold">
            WHAT WE ARE
          </div>
        </div>
      </div>
    </intro-section>
    <home-button></home-button>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";

import HomeButton from "@/components/App/HomeButton.vue";
import IntroSection from "@/components/IntroductionView/IntroSection.vue";

@Component({
  components: {
    HomeButton,
    IntroSection
  }
})
export default class IntroductionView extends Vue {}
</script>

<style scoped>
.centralize {
  left: 50%;
  top: 50%;
  transform: translateX(-50%) translateY(50%);
}

.text-50pt {
  font-size: 50pt;
}

.scrolling-section-shadow {
  box-shadow: 0 0 50px rgba(0, 0, 0, 0.5);
}
</style>
