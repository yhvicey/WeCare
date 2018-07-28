<template>
    <div class="profile w-64 pl-4 pl-0 min-width-72">
        <div class="bg-white mb-3">
            <div class="profile-header bg-blue">
                <div class="image-background rounded-full bg-white flex justify-center">
                    <img class="image rounded-full bg-white mx-auto my-auto" src="../../assets/images/icon.png" alt="avatar" />
                </div>
            </div>
            <div class="profile-content">
                <div class="profile-name">WeCare Playground</div>
                <div class="profile-id">@wecareplay</div>
                <div class="profile-status container flex flex-row">
                    <div class="container flex flex-col">
                        <div class="profile-label">Tweets</div>
                        <div class="profile-value">{{ state.session.length }}</div>
                    </div>
                    <div class="container flex flex-col">
                        <div class="profile-label">Following</div>
                        <div class="profile-value">10</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="trends bg-white p-3 mb-3">
            <div class="mb-3">
                <span class="text-lg font-bold">Trends for you</span>
                <span> &middot; </span>
                <span>
                    <a class="cursor-pointer text-blue text-xs">Change</a>
                </span>
            </div>

            <div class="mb-3 leading-tight">
                <div>
                    <a href="https://garagehackbox.azurewebsites.net/hackathons/oneweek/main" target="_blank" class="cursor-pointer text-blue font-bold">#Hack</a>
                </div>
                <div>
                    <a class="cursor-pointer text-grey-dark text-xs">645K Tweets</a>
                </div>
            </div>

            <div class="mb-3 leading-tight">
                <div>
                    <a href="https://garagehackbox.azurewebsites.net/hackathons/1214/projects/70915" target="_blank" class="cursor-pointer text-blue font-bold">WeCare</a>
                </div>
                <div>
                    <a class="cursor-pointer text-grey-dark text-xs">MS Hack 2018</a>
                </div>
            </div>

            <div class="mb-3 leading-tight">
                <div>
                    <a href="https://bing.com/search?q=mentalhealth" target="_blank" class="cursor-pointer text-blue font-bold">#MentalHealth</a>
                </div>
                <div>
                    <a class="cursor-pointer text-grey-dark text-xs">21.7K Tweets</a>
                </div>
            </div>

            <div class="mb-3 leading-tight">
                <div>
                    <a href="https://garagehackbox.azurewebsites.net/hackathons/oneweek/challengesmain/HackForGood#section1" target="_blank" class="cursor-pointer text-blue font-bold">#Hack4Good</a>
                </div>
                <div>
                    <a class="cursor-pointer text-grey-dark text-xs">45K Tweets</a>
                </div>
            </div>

            <div class="mb-3 leading-tight">
                <div>
                    <a href="https://microsoft.sharepoint.com/teams/HackforGoodHealth_Dynamics365Hackathon" target="_blank" class="cursor-pointer text-blue font-bold">#HealthyApp</a>
                </div>
                <div>
                    <a class="cursor-pointer text-grey-dark text-xs">36K Tweets</a>
                </div>
            </div>

        </div>
    </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { Prop } from "vue-property-decorator";
import { TwitterViewState } from "@/models";

@Component
export default class Profile extends Vue {
  @Prop() public state!: TwitterViewState;
}
</script>

<style scoped>
.profile {
  width: 18rem;
}

.profile-header {
  height: 95px;
  cursor: pointer;
}

.profile-content {
  background-color: #fff;
  height: 113px;
}

.profile-name {
  font-weight: bold;
  font-size: 18px;
  margin-left: 5rem;
  padding-top: 0.5rem;
  cursor: pointer;
}

.profile-id {
  font-size: 14px;
  font-family: "Segoe UI", Arial, sans-serif;
  margin-left: 5rem;
  color: #657786;
  margin-top: -0.3rem;
  cursor: pointer;
}

.profile-status {
  padding: 0.6rem 16px;
}

.profile-label {
  font-weight: bold;
  font-size: 12px;
  font-family: "Segoe UI", Arial, sans-serif;
  color: #657786;
  cursor: pointer;
}

.profile-value {
  font-weight: bold;
  font-size: 18px;
  color: #1da1f2;
  cursor: pointer;
}

.trends * {
  text-decoration-line: none;
}

.image-background {
  height: 72px;
  width: 72px;
  position: relative;
  margin-left: 8px;
  top: 59px;
}

.image {
  height: 68px;
  width: 68px;
}

.min-width-72 {
  width: 18rem;
}
</style>
