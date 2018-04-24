import Vue from 'vue';
import iView from 'iview';
import VueRouter from 'vue-router';
import Routers from './router';
import Vuex from 'vuex';
import Util from './libs/util';
import App from './app.vue';
import 'iview/dist/styles/iview.css';


Vue.use(VueRouter);
Vue.use(Vuex);

Vue.use(iView);


// 路由配置
const RouterConfig = {
    mode: 'history',
    routes: Routers
};
const router = new VueRouter(RouterConfig);

router.beforeEach((to, from, next) => {
    
    Util.title(to.meta.title);
    if (to.meta.needsLogin && !store.getters.isLogin) {
        iView.Message.warning("请登录");
        router.push('/login');
    } else {
        iView.LoadingBar.start();
        next();
    }
});

router.afterEach(() => {
    iView.LoadingBar.finish();
    window.scrollTo(0, 0);
});


const store = new Vuex.Store({
    state: {
        currentUser: null
    },
    getters: {
        isLogin(state) {
            return state.currentUser !== null;
        },
        isAdmin(state) {
            return state.currentUser !== null && state.currentUser.isAdmin;
        },
        username(state) {
            return state.currentUser.username;
        }
    },
    mutations: {
        login(state, username, isAdmin) {
            state.currentUser = {
                username: username,
                isAdmin: isAdmin
            };
        },
        logout(state) {
            state.currentUser = null;
        }
    },
    actions: {

    }
});


new Vue({
    el: '#app',
    router: router,
    store: store,
    render: h => h(App)
});