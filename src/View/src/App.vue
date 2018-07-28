<template>
  <div id="app h-full">
    <keep-alive>
      <notifier></notifier>
    </keep-alive>
    <router-view/>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import "font-awesome/css/font-awesome.min.css";

import "@/assets/styles/tailwind.css";

import Notifier from "@/components/App/Notifier.vue";

@Component({
  components: {
    Notifier
  }
})
export default class App extends Vue {}
</script>

<style lang="scss">
html,
body {
  background-color: #000000;
  height: 100%;
}

input {
  cursor: pointer;
}

input:focus {
  outline: none;
}

select:focus {
  outline: none;
}

textarea {
  resize: none;
}

textarea:focus {
  outline: none;
}

a {
  text-decoration-line: none;
  cursor: pointer;
}

.nav-button {
  border-width: 2px;
  border-style: solid;
  background-color: transparent;
  cursor: pointer;
  padding: 1px;
  border-radius: 2rem;
  transition: transform 0.125s;

  &:active {
    transform: scale(0.9, 0.9);
  }
}

.bg-tweet {
  background-color: #eaf5fe;
}
</style>
