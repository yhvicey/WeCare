<template>
    <div class="flex bg-white border-b border-solid border-grey-light">
        <div class="w-1/8 text-right pl-3 pt-3">
            <div>
                <a href="#">
                    <img src="../../assets/images/icon.png" alt="avatar" class="rounded-full h-12 w-12 mr-2">
                </a>
            </div>
        </div>
        <div class="w-7/8 p-3 pl-0">
            <div class="flex ml-1 justify-between">
                <div>
                    <span class="cursor-pointer font-bold">{{ post.name }}</span>
                    <span class="cursor-pointer text-grey-dark"> @{{ post.id }} </span>
                    <span class="text-grey-dark"> &middot; </span>
                    <span class="cursor-pointer text-grey-dark">{{ post.time.getDay() }} {{ monthMap[post.time.getMonth()] }} {{ post.time.getFullYear() }}</span>
                </div>
                <div>
                    <i class="cursor-pointer fa fa-chevron-down"></i>
                </div>
            </div>

            <div class="mb-2 ml-2 mr-3 mt-px">
                <p class="mb-px" v-for="(statement, index) of post.content.split('\n')" :key="index">{{ statement }}</p>
            </div>

            <div class="pb-2">
                <span class="mr-8">
                    <a class="cursor-pointer text-grey-dark no-underline hover:text-blue-light">
                        <i class="fa fa-comment fa-lg mr-2"></i> {{ post.comment }}</a>
                </span>
                <span class="mr-8">
                    <a class="cursor-pointer text-grey-dark no-underline hover:text-blue">
                        <i class="fa fa-retweet fa-lg mr-2"></i> {{ post.retweet }}</a>
                </span>
                <span class="mr-8">
                    <a :class="{
                        'cursor-pointer': true,
                        'text-grey-dark': true,
                        'no-underline': true,
                        'hover:text-red': true,
                        'text-red': post.liked
                        }" @click="onLike($event, post)">
                        <i class="fa fa-heart fa-lg mr-2"></i> {{ post.like }}</a>
                </span>
                <span class="mr-8">
                    <a class="cursor-pointer text-grey-dark no-underline hover:text-blue">
                        <i class="fa fa-envelope fa-lg mr-2"></i>
                    </a>
                </span>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { Prop } from "vue-property-decorator";

import { PostState } from "@/models";

@Component
export default class Post extends Vue {
  public monthMap = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"
  ];
  @Prop() public post!: PostState;

  public onLike(e: MouseEvent, post: PostState) {
    if (!post.liked) {
      post.like++;
      post.liked = true;
    } else {
      post.like--;
      post.liked = false;
    }
  }
}
</script>

<style>
.w-1\/8 {
  width: 12.5%;
}

.w-7\/8 {
  width: 87.5%;
}

p {
  word-wrap: break-word;
  word-break: normal;
}
</style>
