import { Action } from '@/actions';
import MessageState from '@/models/MessageState';

export default interface RootState<T extends MessageState> {
    actions: Action[];
    messageScore: number;
    session: T[];
    sessionId: string | null;
    sessionScore: number;
    sessionScoreIncre: number;
}
