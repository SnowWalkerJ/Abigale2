import axios from 'axios';
import env from '../config/env';

let util = {

};
util.title = function(title) {
    title = title ? 'Abigale2 - ' + title : 'Abigale2';
    window.document.title = title;
};

util.ajaxUrl = env === 'development' ?
    'http://localhost:8080' :
    env === 'production' ?
    'http://localhost:8080' :
    'http://debug.url.com';

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