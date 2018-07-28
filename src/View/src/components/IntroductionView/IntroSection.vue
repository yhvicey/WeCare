<template>
  <div :class="customClass" :style="customStyle">
    <slot></slot>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { Prop } from "vue-property-decorator";

@Component
export default class IntroSection extends Vue {
  @Prop({ default: "white" })
  public color!: string;
  @Prop({ default: "" })
  public src!: string;
  @Prop({ default: false })
  public fixed!: boolean;

  public get useImage() {
    return this.src !== undefined && this.src !== "";
  }

  public get customClass(): string[] {
    return [
      "section",
      this.fixed ? "bg-fixed" : "",
      this.useImage ? "" : `bg-${this.color}`
    ];
  }

  public get customStyle(): string {
    return this.useImage ? `background-image:url(${this.src})` : "";
  }
}
</script>

<style scoped>
.section {
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
}
</style>
