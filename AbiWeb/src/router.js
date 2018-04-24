const routers = [
    {
        path: '/',
        meta: {
            title: '',
            needsLogin: false,
            keepAlive: true
        },
        component: (resolve) => require(['./views/index.vue'], resolve)
    },
    {
        path: '/filelist',
        name: 'fileList',
        meta: {
            title: '文件目录',
            needsLogin: true,
            keepAlive: true
        },
        props: (route) => ({path: route.query.path}),
        component: (resolve) => require(['./views/fileList.vue'], resolve)
    },
    {
        path: '/details',
        name: 'details',
        meta: {
            title: '策略详情',
            needsLogin: true,
            keepAlive: false
        },
        props: (route) => ({id: route.query.id}),
        component: (resolve) => require(['./views/details.vue'], resolve)
    },
    {
        path: '/login',
        name: 'login',
        meta: {
            title: '登录',
            needsLogin: false,
            keepAlive: true
        },
        component: (resolve) => require(['./views/login.vue'], resolve)
    },
    {
        path: '/logout',
        name: 'logout',
        meta: {
            title: '退出登录',
            needsLogin: true,
            keepAlive: false
        },
        component: (resolve) => require(['./views/logout.vue'], resolve)
    }
];
export default routers;