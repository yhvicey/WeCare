<template>
  <div class="dashboard">
    <div class="bg-white p-2 mb-3">
      <div>
        <span class="text-lg font-bold m-2">Dashboard</span>
      </div>

      <div class="flex">

      </div>

      <div class="flex flex-col border-b border-solid border-grey-light font-mono pl-2">
        <div>Current Statement Score:</div>
        <div class="mx-auto font-bold">{{ state.messageScore.toFixed(3) }}</div>
      </div>
      <div class="flex flex-col border-b border-solid border-grey-light font-mono pl-2">
        <div>Current Session Score:</div>
        <div class="mx-auto font-bold">{{ state.sessionScore.toFixed(3) }}
          <i :class="sessionScoreArrowStyle"></i>
        </div>
      </div>
      <action-board :state="state"></action-board>
    </div>
    <div class="mb-3 text-xs">
      <span class="mr-2">
        <a class="cursor-pointer text-grey-darker">&copy; 2018 Twitter</a>
      </span>
      <span class="mr-2">
        <a class="cursor-pointer text-grey-darker">About</a>
      </span>
      <span class="mr-2">
        <a class="cursor-pointer text-grey-darker">Help Center</a>
      </span>
      <span class="mr-2">
        <a class="cursor-pointer text-grey-darker">Terms</a>
      </span>
      <span class="mr-2">
        <a class="cursor-pointer text-grey-darker">Privacy policy</a>
      </span>
      <span class="mr-2">
        <a class="cursor-pointer text-grey-darker">Cookies</a>
      </span>
      <span class="mr-2">
        <a class="cursor-pointer text-grey-darker">Ads info</a>
      </span>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { Prop, Watch } from "vue-property-decorator";

import { TwitterViewState } from "@/models";
import { Action } from "@/actions";

import ActionBoard from "@/components/TwitterView/ActionBoard.vue";

@Component({
  components: {
    ActionBoard
  }
})
export default class Dashboard extends Vue {
  @Prop() public state!: TwitterViewState;

  public get sessionScoreArrowStyle(): string[] {
    if (this.state.sessionScoreIncre > 0) {
      return ["fa", "fa-arrow-up", "text-green"];
    } else if (this.state.sessionScoreIncre < 0) {
      return ["fa", "fa-arrow-down", "text-red"];
    } else {
      return ["fa", "fa-arrow-right"];
    }
  }
}
</script>

<style scoped>
.dashboard {
  width: 20rem;
}

div[contenteditable]:focus {
  outline: none;
  border-color: #bcdefa;
}
</style>
