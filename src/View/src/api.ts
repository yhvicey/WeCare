import { PostState, SMSState } from '@/models';

const apiUrl: string = "http://localhost:5000";

export default class Api {
    public static async fetchPosts(sessionId: string): Promise<PostState[] | null> {
        try {
            const req = new Request(`${apiUrl}/session/${sessionId}`, {
                method: "GET"
            });
            const res = await fetch(req);
            return (await res.json()) as PostState[];
        } catch (err) {
            console.error(`Error occured while fetching posts. SessionId: ${sessionId}.`);
            console.error(err);
            return null;
        }
    }

    public static async fetchSessionScore(sessionId: string): Promise<number | null> {
        try {
            const req = new Request(`${apiUrl}/session/${sessionId}/score`, {
                method: "GET"
            });
            const res = await fetch(req);
            return (await res.json()) as number;
        } catch (err) {
            console.error(`Error occured while fetching session score. SessionId: ${sessionId}`);
            console.error(err);
            return null;
        }
    }

    public static async requestSessionId(): Promise<string | null> {
        try {
            const req = new Request(`${apiUrl}/session`, {
                method: "GET"
            });
            const res = await fetch(req);
            return await res.text();
        } catch (err) {
            console.error("Error occured while getting token.");
            console.error(err);
            return null;
        }
    }

    public static async sendPost(sessionId: string, post: PostState): Promise<number | null> {
        try {
            console.debug(`Sending post: ${JSON.stringify(post)}`);
            const req = new Request(`${apiUrl}/session/${sessionId}`, {
                method: "POST",
                body: JSON.stringify(post),
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const res = await fetch(req);
            return (await res.json()) as number;
        } catch (err) {
            console.error(`Error occured while sending message. SessionId: ${sessionId}.`);
            console.error(err);
            return null;
        }
    }

    public static async sendSMS(message: string, phone: string): Promise<number | null> {
        try {
            const sms = { body: message, to: phone } as SMSState;
            console.debug(`Sending post: ${JSON.stringify(sms)}`);
            const req = new Request(`${apiUrl}/action/sms`, {
                method: "POST",
                body: JSON.stringify(sms),
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const res = await fetch(req);
            return (await res.json()) as number;
        } catch (err) {
            console.error(`Error occured while sending message: ${message}, to: ${phone}`);
            console.error(err);
            return null;
        }
    }
}
