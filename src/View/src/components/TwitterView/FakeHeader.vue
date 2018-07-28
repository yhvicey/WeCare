<template>
    <div class="bg-white h-11.5">
        <div class="container mx-auto flex flex-row items-center py-2">
            <nav class="w-2/5 mb-2">
                <a class="text-grey-dark text-sm font-bold font-3.25 pb-3.5 pl-1 pr-3.5 border-b-2 border-solid border-transparent text-blue border-blue">
                    <i class="fa fa-home fa-lg ml-2"></i> Home
                </a>
                <a class="text-grey-dark text-sm font-bold font-3.25 pb-3.5 pl-1 pr-3.5 border-b-2 border-solid border-transparent hover:text-blue hover:border-blue">
                    <i class="fa fa-bolt fa-lg ml-2"></i> Moments
                </a>
                <a class="text-grey-dark text-sm font-bold font-3.25 pb-3.5 pl-1 pr-3.5 border-b-2 border-solid border-transparent hover:text-blue hover:border-blue">
                    <i class="fa fa-bell fa-lg ml-2"></i> Notifications
                </a>
                <a class="text-grey-dark text-sm font-bold font-3.25 pb-3.5 pl-1 pr-3.5 border-b-2 border-solid border-transparent hover:text-blue hover:border-blue">
                    <i class="fa fa-envelope fa-lg ml-2"></i> Messages
                </a>
            </nav>

            <div class="w-1/5 text-center my-0">
                <a>
                    <i class="fa fa-twitter fa-lg text-blue"></i>
                </a>
            </div>

            <div class="w-2/5 flex justify-end">
                <div class="mr-4 relative">
                    <input type="text" class="bg-grey-lighter h-8 px-4 py-2 text-xs w-48 rounded-full" placeholder="Search Twitter">
                    <span class="flex items-center absolute pin-r pin-y mr-3">
                        <i class="fa fa-search text-grey"></i>
                    </span>
                </div>
                <div class="mr-4">
                    <a><img src="../../assets/images/icon.png" alt="avatar" class="h-8 w-8 rounded-full"></a>
                </div>
                <div>
                    <button class="bg-blue hover:bg-blue-dark text-white font-medium py-2 px-4 rounded-full">Tweet</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";

@Component
export default class FakeHeader extends Vue {}
</script>

<style scoped>
nav a {
  transition: all 0.15s ease-in-out;
}

.h-11\.5 {
  height: 2.875rem;
}

.pb-3\.5 {
  padding-bottom: 0.875rem;
}

.pr-3\.5 {
  padding-right: 0.875rem;
}

.font-3\.25 {
  font-size: 0.8125rem;
}
</style>
