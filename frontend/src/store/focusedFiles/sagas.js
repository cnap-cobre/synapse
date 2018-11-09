import * as types from './types';
import {fileHistoryActions} from '../FileHistory';
import { all, put, takeEvery } from 'redux-saga/effects';

function *getFileHistory(action) {
  console.log("CKAE", action);
  yield put(fileHistoryActions.pending(action.filePath));
}

export default function* () {
  yield all([
    takeEvery(types.SET_FOCUSED_FILE, getFileHistory)
  ])
}