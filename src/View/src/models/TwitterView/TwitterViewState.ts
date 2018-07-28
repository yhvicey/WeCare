import { Action } from '@/actions';
import RootState from "@/models/RootState";
import PostState from '@/models/TwitterView/PostState';

export default interface TwitterViewState extends RootState<PostState> {
}
