import { Action, ActionConfig, ActionContext } from '@/actions/Action';
import Utils from '@/utils';

interface AdvisoryConfig extends ActionConfig {
    contractMessage: string;
    message: string;
    messageOptions: string[];
    jumpToUrl: string;
}

class AdvisoryAction extends Action {
    public config: AdvisoryConfig;

    constructor(config: AdvisoryConfig) {
        super(
            "Advisory",
            "This action will give an advisory."
        );
        this.config = config;
    }

    protected onAction(context?: ActionContext) {
        Utils.notify(`${this.config.message} ${this.config.contractMessage}`, this.onResult, this.config);
    }

    protected onStop() {
        // no-op
    }

    private onResult(result: boolean, config?: AdvisoryConfig) {
        if (result && config) {
            window.open(config.jumpToUrl, "_blank");
        }
    }
}

export default new AdvisoryAction({
    threshold: -10,
    contractMessage: "Need some help? Do you want tell us what's happened?",
    message: "You may still feel alone, but I am here. I can’t imagine what it’s like, but I want to listen.",
    messageOptions: [
        "You may still feel alone, but I am here. I can’t imagine what it’s like, but I want to listen.",
        "I want to be here for you, I won’t leave you behind",
        "I can't begin to imagine what you're going through, but know that I'm here for you.",
        "I know this is hard, but I will not give up on you.",
        "No matter how dark your days get, I'll be here for you. I'm just a phone call or a text away.",
        "Don't let the darkness steal the beautiful person you have inside.",
        "I can't even pretend to know what you are going through, but you aren't alone and you are cared for.",
        "You are important in my life.",
    ],
    jumpToUrl: "mailto:yiwwan@microsoft.com"
});
