export interface ActionConfig {
    threshold: number;
    [configItemName: string]: string | string[] | number | boolean;
}

export interface ActionContext {
    sessionScore: number;
    messageScore: number;
}

export abstract class Action {
    public abstract config: ActionConfig;
    public description: string;
    public friendlyName: string;
    private triggeredFlag: boolean = false;

    public get triggered() {
        return this.triggeredFlag;
    }

    constructor(friendlyName: string, description: string) {
        this.friendlyName = friendlyName;
        this.description = description;
    }

    public action(context?: ActionContext): void {
        if (this.triggeredFlag === true) {
            return;
        }
        this.triggeredFlag = true;
        this.onAction(context);
    }

    public stop(context?: ActionContext) {
        if (this.triggeredFlag !== true) {
            return;
        }
        this.triggeredFlag = false;
        this.onStop(context);
    }

    protected abstract onAction(context?: ActionContext): void;

    protected abstract onStop(context?: ActionContext): void;
}
