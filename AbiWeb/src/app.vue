<style scoped>
    .layout-con{
        height: 100%;
        width: 100%;
    }
    .menu-item span{
        display: inline-block;
        overflow: hidden;
        width: 73px;
        text-overflow: ellipsis;
        white-space: nowrap;
        vertical-align: bottom;
        transition: width .2s ease .2s;
    }
    .menu-item i{
        transform: translateX(0px);
        transition: font-size .2s ease, transform .2s ease;
        vertical-align: middle;
        font-size: 16px;
    }
    .collapsed-menu span{
        width: 0px;
        transition: width .2s ease;
    }
    .collapsed-menu i{
        transform: translateX(5px);
        transition: font-size .2s ease .2s, transform .2s ease .2s;
        vertical-align: middle;
        font-size: 22px;
    }
</style>
<template>
    <div class="layout">
        <Layout :style="{minHeight: '100vh'}">
            <Sider collapsible :collapsed-width="78" v-model="isCollapsed">
                <Affix>
                <Menu :active-name="this.$route.name" theme="dark" width="auto" :class="menuitemClasses" @on-select="route">
                    <MenuItem v-if="!$store.getters.isLogin" name="login" key="/login">
                        <Icon type="log-in"></Icon>
                        <span>登录</span>
                    </MenuItem>
                    <MenuItem v-if="$store.getters.isLogin" name="fileList" key="/filelist">
                        <Icon type="folder"></Icon>
                        <span>文件目录</span>
                    </MenuItem>
                    <MenuItem v-if="$store.getters.isLogin" name="details" key="/details">
                        <Icon type="stats-bars"></Icon>
                        <span>策略详情</span>
                    </MenuItem>
                    <MenuItem v-if="$store.getters.isAdmin" name="admin" key="/admin">
                        <Icon type="person"></Icon>
                        <span>管理员选项</span>
                    </MenuItem>
                    <MenuItem v-if="$store.getters.isLogin" name="logout" key="/logout">
                        <Icon type="log-out"></Icon>
                        <span>登出</span>
                    </MenuItem>
                </Menu>
                </Affix>
            </Sider>
            <Layout>
                <div :style="{minHeight: '100vh'}">
                    <keep-alive>
                        <router-view v-if="$route.meta.keepAlive">
                            <!-- 这里是会被缓存的视图组件，比如 Home！ -->
                        </router-view>
                    </keep-alive>

                    <router-view v-if="!$route.meta.keepAlive">
                        <!-- 这里是不被缓存的视图组件，比如 Edit！ -->
                    </router-view>
                </div>
            </Layout>
        </Layout>
    </div>
</template>
<script>
    import Util from './libs/util'
    export default {
        data () {
            return {
                isCollapsed: false
            };
        },
        computed: {
            menuitemClasses: function () {
                return [
                    'menu-item',
                    this.isCollapsed ? 'collapsed-menu' : ''
                ];
            }
        },
        mounted() {
            Util.ajax.request({
                method: 'get',
                url: '/api/users/whoami',
                timeout: 1000
            }).then(response => {
                this.$store.commit('login', response.data.data);
            }).catch(error => {});
        },
        beforeDestroy() {

        },
        methods: {
            route (target) {
                this.$router.push(target);
            },
        }
    };
</script>
