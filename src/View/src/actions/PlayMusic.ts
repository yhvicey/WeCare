import { Action, ActionConfig } from '@/actions/Action';
import Utils from '@/utils';

interface PlayMusicConfig extends ActionConfig {
    message: string;
    audioUrl: string;
}

class PlayMusicAction extends Action {
    public config: PlayMusicConfig;
    private audio: HTMLAudioElement | null = null;

    constructor(config: PlayMusicConfig) {
        super(
            "Play Music",
            "After this action is triggered, we will play a song for you.\nYou can config its play url at config panel."
        );
        this.config = config;
    }

    protected async onAction() {
        Utils.notify(this.config.message,
            async result => {
                if (result) {
                    this.audio = new Audio(this.config.audioUrl);
                    await this.audio.play();
                }
            });
    }

    protected async onStop() {
        if (this.audio === null) {
            return;
        }
        this.audio.pause();
    }
}

export default new PlayMusicAction({
    threshold: -5,
    message: "You are beautiful. You are loved. You are not alone. Want some music?",
    audioUrl: "/audio/wind.mp3"
});
