<template>
  <div class="flex flex-col border-b border-solid border-grey-light font-mono pl-2 pb-2">
    <div>Select action for more details:</div>
    <div v-for="(action, index) of sortedActions" :key="index">
      <input :class="{
                        'w-full': true,
                        'my-2': true,
                        'bg-green': !action.triggered && selectedAction !== action,
                        'bg-green-dark': !action.triggered && selectedAction === action,
                        'hover:bg-green-dark': !action.triggered,
                        'bg-red': action.triggered && selectedAction !== action,
                        'bg-red-dark': action.triggered && selectedAction === action,
                        'hover:bg-red-dark': action.triggered,
                        'text-white': true,
                        'font-medium': true,
                        'py-2': true,
                        'px-4': true,
                        'rounded-full': true
                      }" type="button" :value="`${action.friendlyName} (Threshold: ${ action.config.threshold })`" @click="onActionSelected(action)" />
    </div>
    <div class="flex flex-col" v-if="selectedAction !== null" ref="selectedActionBoard">
      <div>Selected Action:
        <span class="font-bold">{{ selectedAction.friendlyName }}</span>
      </div>
      <div>Description:
        <p class="text-xs pr-px" v-for="(statement, index) of selectedAction.description.split('\n')" :key="index">{{ statement }}</p>
      </div>
      <div>
        <label>triggered: </label>
        <input type="checkbox" :checked="selectedAction.triggered" @click="onTriggerClick(selectedAction)" />
      </div>
      <div v-for="(item, index) of selectedActionConfigItems" :key="index">
        <div v-if="typeof item.value === 'boolean'">
          <label>{{ item.name }}: </label>
          <input type="checkbox" v-model="selectedAction.config[item.name]" />
        </div>
        <div v-else-if="typeof item.value === 'string' || typeof item.value === 'number'">
          <label>{{ item.name }}: </label>
          <autosize-textarea class="w-full border-2 px-1 rounded-lg" v-model="selectedAction.config[item.name]" :padding="4"></autosize-textarea>
          <div v-if="selectedAction.config.hasOwnProperty(`${item.name}Options`) && (selectedAction.config[`${item.name}Options`] instanceof Array)">
            <label>{{ item.name }} Options: </label>
            <select class="w-full border-2 px-1 rounded-lg" @change="onOptionChange($event, selectedAction, item.name)">
              <option v-for="(option, index) of selectedAction.config[`${item.name}Options`]" :key="index">
                {{ option }}
              </option>
            </select>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { Prop, Watch } from "vue-property-decorator";
import { Action } from "@/actions";
import { setTimeout } from "timers";
import { TwitterViewState } from "@/models";

import AutosizeTextarea from "@/components/App/AutosizeTextarea.vue";

@Component({
  components: {
    AutosizeTextarea
  }
})
export default class ActionBoard extends Vue {
  public selectedAction: Action | null = null;
  @Prop() public state!: TwitterViewState;

  public get sortedActions(): Action[] {
    return this.state.actions.sort(
      (actionA, actionB) => actionB.config.threshold - actionA.config.threshold
    );
  }

  public get selectedActionConfigItems(): Array<{
    name: string;
    value: string | string[] | number | boolean;
  }> {
    if (this.selectedAction === null) {
      return [];
    }
    const action = this.selectedAction;
    return Object.keys(action.config).map(itemName => {
      return {
        name: itemName,
        value: action.config[itemName]
      };
    });
  }

  public async onActionSelected(action: Action) {
    const selectedAction = this.selectedAction;
    this.selectedAction = null;
    await this.$nextTick();
    if (selectedAction !== action) {
      this.selectedAction = action;
    }
  }

  public onOptionChange(event: Event, action: Action, itemName: string) {
    const selectElement = event.target as HTMLSelectElement;
    action.config[itemName] =
      selectElement.selectedOptions[0] &&
      selectElement.selectedOptions[0].value;
  }

  public onTriggerClick(action: Action) {
    if (action.triggered === true) {
      action.stop();
    } else {
      action.action();
    }
  }

  @Watch("state.sessionScore")
  public onSessionScoreChanged(val: number, oldVal: number) {
    this.state.sessionScoreIncre = val - oldVal;
    const growing = this.state.sessionScoreIncre > 0;
    this.sortedActions.reverse().some(action => {
      if (growing && val > action.config.threshold && action.triggered) {
        action.stop();
        return false;
      } else if (!growing && val <= action.config.threshold) {
        if (!action.triggered) {
          action.action({
            sessionScore: val,
            messageScore: this.state.messageScore
          });
        }
        return true;
      }
      return false;
    });
  }
}
</script>

<style scoped>
select:focus {
  border-color: #bcdefa;
}

textarea:focus {
  border-color: #bcdefa;
}
</style>
