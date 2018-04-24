import axios from 'axios';
import env from '../config/env';

let util = {

};
util.title = function(title) {
    title = title ? 'Abigale2 - ' + title : 'Abigale2';
    window.document.title = title;
};

const ajaxUrl = env === 'development' ?
    'http://localhost:8080' :
    env === 'production' ?
    'http://localhost:8080' :
    'http://debug.url.com';

axios.defaults.withCredentials = true;
util.ajax = axios.create({
    baseURL: ajaxUrl,
    timeout: 3000,
    withCredentials: true
});

export default util;