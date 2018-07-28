<template>
    <div :class="borderStyle">
        <router-link to="/" class="no-underline">
            <div class="w-12 h-12 flex justify-center">
                <div class="flex flex-col justify-center">
                    <i :class="iconStyle"></i>
                </div>
            </div>
        </router-link>
    </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { Prop } from "vue-property-decorator";

@Component
export default class HomeButton extends Vue {
  public borderStyle: string[] = [
    "home-button",
    "nav-button",
    `border-${this.color}`
  ];
  public iconStyle: string[] = [
    "fa",
    "fa-arrow-left",
    "text-3xl",
    `text-${this.color}`
  ];
  @Prop({ default: "white" })
  public color!: string;
}
</script>

<style scoped>
.home-button {
  position: fixed;
  bottom: 3rem;
  right: 3rem;
  z-index: 100;
}
</style>
