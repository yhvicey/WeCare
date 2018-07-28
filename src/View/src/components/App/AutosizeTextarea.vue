<template>
  <textarea @input="changeHeight" v-model="val" />
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { Prop, Watch } from "vue-property-decorator";

@Component
export default class AutosizeTextarea extends Vue {
  @Prop({ default: 0, type: Number })
  public padding!: number;
  @Prop({ default: "", type: [String, Number, Object, Boolean] })
  public value!: string | number | object | boolean;

  public get val() {
    return this.value;
  }

  public set val(value: string | number | object | boolean) {
    this.$emit("input", value);
  }

  public mounted() {
    this.$el.style.height = `${this.$el.scrollHeight + this.padding}px`;
    this.$el.style.overflowY = "hidden";
  }

  private changeHeight() {
    this.$el.style.height = "auto";
    this.$el.style.height = `${this.$el.scrollHeight + this.padding}px`;
  }

  @Watch("value")
  public async onValueChange() {
    await this.$nextTick();
    this.changeHeight();
  }
}
</script>

<style scoped>
</style>
