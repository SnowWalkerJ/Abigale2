<style scoped>
.main {
    padding: 30px;
}
.toolbox Col Input{
    margin: 30px;
    align-self: center;
}
.table {
    margin: 20px;
    width: 80vw;
}
.breadcrumb {
    margin-left: 30px;
    margin-top: 10px;
}
.btn-toolbox {
    margin-left: 10px;
}
</style>
<template>
<Layout class="main">
    <Row class="toolbox">
        <Col span="12">
            <Button class="btn-toolbox" @click="debug"><Icon type="document" size="15"/>新建策略</Button>
            <Button class="btn-toolbox" @click="newFolder"><Icon type="folder" size="15"/>新建文件夹</Button>
            <Button class="btn-toolbox" @click="refresh()"><Icon type="refresh" size="15"/>刷新</Button>
        </Col>
        <Col span="12">
            <Tooltip content="支持正则表达式"><Input v-model="nameFilter" placeholder="文件名" icon="search" style="width: 300px"/></Tooltip>
        </Col>
    </Row>
    <Row>
        <Breadcrumb class="breadcrumb">
            <BreadcrumbItem v-for="(name, i) in this.pathCrumbs" :key="i" :to="fullPath(i)">{{name}}</BreadcrumbItem>
        </Breadcrumb>
    </Row>
    <Row>
        <Table border class="table" :columns="tableColumns" :data="dataToShow" @on-row-dblclick="this.enter"/>
    </Row>
</Layout>
</template>

<script>
import Util from '../libs/util.js'
export default {
    props: {
        path: {
            type: String
        }
    },
    data () {
        return {
            nameFilter: '',
            savedPath: 'Root/',
            files: [],
        };
    },
    methods: {
        fullPath: function(n) {
            var target = '';
            for (var i = 0; i <= n; i++ ) {
                target = target + this.pathCrumbs[i] + '/';
            }
            return window.location.pathname + '?path=' + target;
        },
        debug: function () {
            console.log(this.path);
        },
        enter: function (data, index) {
            if (data.type === 'folder') {
                this.$router.push(window.location.pathname + '?path=' + this.realPath + data.name + '/');
            }
        },
        newFolder: function () {
            var folderName = '';
            this.$Modal.confirm({
                title: '文件夹名称',
                render: (h) => {
                    return h('Input', {
                        props: {
                            value: folderName,
                            autofocus: true,
                            placeholder: '请输入新建文件夹的名称'
                        },
                        on: {
                            input: (val) => {
                                folderName = val;
                            }
                        }
                    })
                },
                onOk: () => {
                    Util.ajax.request({
                        method: 'post',
                        url: '/api/files/mkdir?path=' + this.realPath + '&name=' + folderName,
                        timeout: 100
                    }).then(response => {
                        if (response.data.status) {
                            this.$Message.info("创建成功");
                            this.refresh();
                        } else {
                            this.$Message.error("创建失败：" + response.data.msg);
                        }
                    });
                    this.$Message.info(folderName);
                }
            });
        },
        view: function (data) {
            this.$router.push('/details?id='+data.link);
        },
        remove: function (data) {
            data.type === 'folder' ? this.removeFolder(data) : this.removeFile(data);
        },
        removeFolder (data) {
            this.$Modal.confirm({
                title: '删除文件夹',
                content: '确认删除`' + data.name + '`?',
                onOk: () => {
                    Util.request({
                        method: 'post',
                        url: '/api/files/rm_dir?path=' + data.path + '&name=' + data.name,
                        timeout: 100
                    }).then(response => {
                        if (response.data.status) {
                            this.$Message.info("删除成功");
                            this.refresh();
                        } else {
                            this.$Message.error("删除失败：" + response.data.msg);
                        }
                    });
                }
            });
        },
        removeFile(data) {
            this.$Modal.confirm({
                title: '删除文件',
                content: '确认删除`' + data.name + '`?',
                onOk: () => {
                    Util.request({
                        method: 'post',
                        url: '/api/files/rm_file?path=' + data.path + '&name=' + data.name,
                        timeout: 100
                    }).then(response => {
                        if (response.data.status) {
                            this.$Message.info("删除成功");
                            this.refresh();
                        } else {
                            this.$Message.error("删除失败：" + response.data.msg);
                        }
                    });
                }
            });
        },
        refresh (path) {
            path = path === undefined ? this.realPath : path;
            console.log("refresh");
            Util.ajax.request({
                method: 'get',
                url: '/api/files/ls?path=' + path,
                timeout: 100
            }).then(response => {
                this.files = response.data.data;
            });
        }
    },
    computed: {
        realPath () {
            if (this.path != undefined) {
                if (this.path !== this.savedPath) this.refresh(this.path);
                this.savedPath = this.path;
            }
            return this.savedPath;
        },
        pathCrumbs () {
            var pathComponents = this.realPath.split("/");
            pathComponents.pop();
            return pathComponents;
        },
        userFilter () {
            var users = this.files.map(doc => doc.owner);
            var uniqueUsers = [...new Set(users)];
            var filter = uniqueUsers.map(user => ({value: user, label: user}));
            return filter;
        },
        dataToShow () {
            return this.files;
            //let regex = RegExp(this.nameFilter);
            //return this.files.filter(val => regex.exec(val.name));
        },
        tableColumns(){
            return [
                {
                    title: '文件名',
                    key: 'name',
                    sortable: true,
                    render: (h, params) => {
                        return h('div', [
                            h("Icon", {
                                props: {
                                    type: params.row.type==='folder' ? 'folder': 'document-text',
                                    size: 30,
                                    color: params.row.type==='folder' ? 'chocolate' : 'lightslategray'
                                },
                                style: {
                                    marginRight: '10px'
                                }
                            }),
                            h("span", {
                                style: {
                                    fontSize: '16px',
                                    color: params.row.type==='folder' ? 'chocolate' : 'lightslategray'
                                }
                            }, params.row.name)
                        ]);
                    }
                },
                {
                    title: '类型',
                    key: 'type',
                    sortable: true,
                    sortType: 'desc',
                    render: (h, params) => {
                        return h('span', params.row.type==='folder' ? '文件夹': '文件');
                    }
                },
                {
                    title: '所有者',
                    key: 'owner',
                    sortable: true,
                    filters: this.userFilter,
                    // filters: [{
                    //     label: 'snowwalkerj',
                    //     value: 'snowwalkerj'
                    // }],
                    filterMethod (value, row) {
                        return value === row.owner;
                    }
                },
                {
                    title: '操作',
                    key: 'operation',
                    width: 150,
                    align: 'center',
                    render: (h, params) => {
                        return h('div', [
                            h('Button', {
                                props: {
                                    type: 'primary',
                                    size: 'small'
                                },
                                style: {
                                    marginRight: '5px',
                                    display: this.$store.getters.isLogin && params.row.type === 'file' ? 'inline' : 'none'
                                },
                                on: {
                                    click: () => {
                                        this.view(params.row)
                                    }
                                }
                            }, 'View'),
                            h('Button', {
                                props: {
                                    type: 'error',
                                    size: 'small'
                                },
                                style: {
                                    display: this.$store.getters.isLogin && (params.row.owner === this.$store.getters.username || this.$store.getters.isAdmin)? 'inline' : 'none'
                                },
                                on: {
                                    click: () => {
                                        this.remove(params.row)
                                    }
                                }
                            }, 'Delete')
                        ]);
                    }
                }
            ];
        } 
    },
    mounted () {
        this.refresh();
    }
};
</script>

