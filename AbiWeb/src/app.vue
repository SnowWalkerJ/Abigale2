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
                    <MenuItem name="fileList" key="/filelist">
                        <Icon type="folder"></Icon>
                        <span>文件目录</span>
                    </MenuItem>
                    <MenuItem name="details" key="/details">
                        <Icon type="stats-bars"></Icon>
                        <span>策略详情</span>
                    </MenuItem>
                    <MenuItem name="admin" key="/admin">
                        <Icon type="person"></Icon>
                        <span>管理员选项</span>
                    </MenuItem>
                </Menu>
                </Affix>
            </Sider>
            <Layout>
                <div :style="{minHeight: '100vh'}">
                    <router-view></router-view>
                </div>
            </Layout>
        </Layout>
    </div>
</template>
<script>
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
