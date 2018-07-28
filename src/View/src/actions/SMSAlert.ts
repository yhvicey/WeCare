import { Action, ActionConfig, ActionContext } from '@/actions/Action';
import Utils from '@/utils';
import Api from '@/api';

interface SMSAlertConfig extends ActionConfig {
    messageTemplate: string;
    to: string;
}

class SMSAlertAction extends Action {
    public config: SMSAlertConfig;

    constructor(config: SMSAlertConfig) {
        super(
            "Send SMS Alert",
            "After this action is triggered, we will send a short message to preset phone number.\n" +
            "Please note that currently only numbers in white list can receive sms alert."
        );
        this.config = config;
    }

    protected async onAction(context?: ActionContext) {
        await Api.sendSMS(Utils.format(this.config.messageTemplate, context && context.sessionScore), this.config.to);
    }

    protected async onStop() {
        // no-op
    }
}

export default new SMSAlertAction({
    threshold: -15,
    messageTemplate: "Your patient is exhibiting extreme emotional disturbance.",
    to: ""
});
