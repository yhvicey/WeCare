<template>
  <div class="notification w-full h-screen bg-black" @click="onClick" v-if="visible">
    <div class="w-full h-full flex flex-col items-center justify-center">
      <div class="w-1/5 h-8 py-2 bg-white text-black text-center border-b rounded-t-lg">
        Notification
      </div>
      <div class="w-1/5 min-h-16 p-4 bg-white text-sm text-black text-center">
        {{ message }}
      </div>
      <div class="w-1/5 h-12 bg-white flex justify-end items-center rounded-b-lg">
        <input class="w-1/2 h-full bg-white hover:bg-grey border-t border-r rounded-bl-lg" type="button" value="Yes" @click="onConfirm" />
        <input class="w-1/2 h-full bg-white hover:bg-grey border-t rounded-br-lg" type="button" value="No" @click="onCancel" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { Prop } from "vue-property-decorator";

import Utils from "@/utils";

import EventBus from "@/components/App/EventBus";

@Component
export default class Notifier extends Vue {
  public visible: boolean = false;
  public message: string = "";

  public callback: ((result: boolean, callbackArg?: any) => void) | undefined;
  public callbackArgument: any | undefined;

  public created() {
    EventBus.$on("show-notification", this.onShowNotification);
  }

  public async onCancel() {
    if (this.callback) {
      await this.callback(false, this.callbackArgument);
    }
  }

  public onClick() {
    this.visible = false;
  }

  public async onConfirm() {
    if (this.callback) {
      await this.callback(true, this.callbackArgument);
    }
  }

  public onShowNotification(
    message: string,
    callback: (result: boolean, callbackArg?: any) => void,
    arg: any
  ) {
    this.message = message;
    if (callback) {
      this.callback = callback;
    }
    if (arg) {
      this.callbackArgument = arg;
    }
    this.visible = true;
  }
}
</script>

<style scoped>
.notification {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 100;
  background-color: rgba(0, 0, 0, 0.3);
}

.min-h-16 {
  min-height: 4rem;
}
</style>
