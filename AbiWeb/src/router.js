const routers = [
    {
        path: '/',
        meta: {
            title: ''
        },
        component: (resolve) => require(['./views/index.vue'], resolve)
    },
    {
        path: '/filelist',
        name: 'fileList',
        meta: {
            title: '文件目录'
        },
        component: (resolve) => require(['./views/fileList.vue'], resolve)
    },
    {
        path: '/details',
        name: 'details',
        meta: {
            title: '策略详情'
        },
        component: (resolve) => require(['./views/details.vue'], resolve)
    }
];
export default routers;