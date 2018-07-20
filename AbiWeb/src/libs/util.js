import axios from 'axios';
import {env, ajaxUrl} from '../config/config';

let util = {

};
util.title = function(title) {
    title = title ? 'Abigale2 - ' + title : 'Abigale2';
    window.document.title = title;
};

util.ajaxUrl = ajaxUrl;

axios.defaults.withCredentials = true;
util.ajax = axios.create({
    baseURL: util.ajaxUrl,
    timeout: 3000,
    withCredentials: true
});

util.handleAPI = function (this_, errMsg, onSuccess) {
    let handler = function (response) {
        if (response.data.status) {
            onSuccess(response.data);
        } else {
            this_.$Message.error(errMsg + ":" + response.data.msg);
        }
    }
    return handler;
}

export default util;