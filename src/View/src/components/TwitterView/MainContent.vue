<template>
  <div class="w-1/2 bg-white mb-4 mx-3 min-width-152">
    <div class="bg-tweet container w-full border-b min-h-38 px-3 py-2.5">
      <div class="container flex flex-row justify-between mt-1">
        <img class="h-8 w-8 rounded-full ml-4" src="../../assets/images/icon.png" alt="avatar">
        <textarea class="border-2 border-blue-lighter rounded-lg min-width-127 min-height-20.5 p-2" v-model="content" placeholder="What's happening?" @keydown.enter="onSend" ref="textBox" @input="onInput"></textarea>
      </div>
      <div class="ml-12 mb-1 mt-2">
        <input class="bg-white cursor-pointer border rounded-full shadow m-1 p-10px" v-for="(example, index) of examples" :key="index" type="button" :value="example" @click="onClick" />
      </div>
    </div>
    <transition-group name="fade">
      <post v-for="(post, index) of state.session" :key="state.session.length - index - 1" :post="post"></post>
    </transition-group>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { Prop } from "vue-property-decorator";

import Api from "@/api";
import { PostState, TwitterViewState } from "@/models";

import Post from "@/components/TwitterView/Post.vue";

@Component({
  components: {
    Post
  }
})
export default class MainContent extends Vue {
  public examples: string[] = [
    "Life is never so easy",
    "I don't wanna go to work today",
    "What a f**king day",
    "**** off",
    "Leave me alone",
    "Oh plz kill me",
    "I hate all of you",
    "Die die die"
  ];

  public content: string = "";
  @Prop() public sessionId!: string;
  @Prop() public state!: TwitterViewState;

  public async onClick(e: MouseEvent) {
    const element = e.target as HTMLInputElement;
    if (element !== null) {
      this.content = element.value;
      (this.$refs.textBox as HTMLElement).focus();
    }
  }

  public onInput(event: Event) {
    const el = event.target as HTMLInputElement;
    if (el.scrollHeight > el.clientHeight) {
      el.style.height = "auto";
      el.style.height = `${el.scrollHeight + 16}px`;
    }
  }

  public async onSend(e: KeyboardEvent) {
    e.returnValue = false;
    if (this.content.length) {
      const el = e.target as HTMLInputElement;
      const postContent = this.content;
      this.content = "";
      if (el.hasAttribute("style")) {
        el.attributes.removeNamedItem("style");
      }
      const post: PostState = {
        comment: 0,
        content: postContent,
        id: "wecareplay",
        like: 0,
        liked: false,
        name: "WeCare Playground",
        retweet: 0,
        time: new Date()
      };
      if (this.state.sessionId === null) {
        console.warn("No session id, won't send post.");
        return;
      }
      const statementScore = await Api.sendPost(this.state.sessionId, post);
      if (statementScore === null) {
        return;
      }
      this.state.messageScore = statementScore;
      this.state.session.splice(0, 0, post);
      const sessionScore = await Api.fetchSessionScore(this.state.sessionId);
      if (sessionScore === null) {
        return;
      }
      this.state.sessionScore = sessionScore;
    }
  }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.min-h-38 {
  min-height: 9.5rem;
}

.py-2\.5 {
  padding-top: 0.625rem;
  padding-bottom: 0.625rem;
}

.ml-0\.5 {
  margin-left: 0.125rem;
}

.ml-14 {
  margin-left: 3.5rem;
}

.min-width-152 {
  width: 38rem;
}

.min-width-127 {
  width: 31.75rem;
}

.min-height-20\.5 {
  height: 5.125rem;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.75s ease-in-out;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
