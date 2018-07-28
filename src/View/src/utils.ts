import EventBus from "@/components/App/EventBus";

export default class Utils {
    public static format(str: string, ...args: any[]): string {
        return str.replace(/{(\d+)}/g, (match, index: number) => {
            return typeof args[index] !== 'undefined'
                ? args[index]
                : match;
        });
    }

    public static notify(message: string, callback?: (result: boolean, callbackArg: any) => void, callbackArg?: any) {
        EventBus.$emit("show-notification", message, callback, callbackArg);
    }
}
