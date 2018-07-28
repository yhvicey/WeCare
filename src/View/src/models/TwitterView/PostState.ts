import MessageState from '@/models/MessageState';

export default interface PostState extends MessageState {
    comment: number;
    id: string;
    like: number;
    liked: boolean;
    name: string;
    retweet: number;
    time: Date;
}
