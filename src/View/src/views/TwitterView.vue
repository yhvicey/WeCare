<template>
  <div class="bg-grey-light font-sans min-h-screen">
    <fake-header></fake-header>
    <div class="container mx-auto flex flex-row mt-3 text-sm leading-normal">
      <profile :state="state"></profile>
      <main-content :state="state"></main-content>
      <dashboard :state="state"></dashboard>
    </div>
    <home-button color="white"></home-button>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { Watch } from "vue-property-decorator";

import { Action, Advisory, SMSAlert, PlayMusic } from "@/actions";
import Api from "@/api";
import { PostState, TwitterViewState } from "@/models";

import FakeHeader from "@/components/TwitterView/FakeHeader.vue";
import Profile from "@/components/TwitterView/Profile.vue";
import MainContent from "@/components/TwitterView/MainContent.vue";
import Dashboard from "@/components/TwitterView/Dashboard.vue";
import HomeButton from "@/components/App/HomeButton.vue";

@Component({
  components: {
    Profile,
    FakeHeader,
    MainContent,
    Dashboard,
    HomeButton
  }
})
export default class TwitterView extends Vue {
  public state: TwitterViewState = {
    actions: [Advisory, SMSAlert, PlayMusic],
    messageScore: 0,
    session: [
      {
        comment: 59,
        content:
          "Welcome to WeCare Playground!\n" +
          "Feel free to enter statements with negative words in above textbox, then hit enter to send them.\n" +
          "There are also some sample statements below the textbox, click them to enter.\n" +
          "After sending, check the dashboard in right side to see what will happen.",
        id: "wecareplay",
        like: 666,
        liked: true,
        name: "WeCare Playground",
        retweet: 233,
        time: new Date()
      }
    ],
    sessionId: null,
    sessionScore: 0,
    sessionScoreIncre: 0
  };

  public async mounted() {
    const sessionId = await Api.requestSessionId();
    if (sessionId === null) {
      return;
    }
    this.state.sessionId = sessionId;
  }
}
</script>


<style scoped>
</style>
