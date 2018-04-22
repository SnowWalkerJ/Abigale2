<style scoped>
.main {
    padding-bottom: 30px;
}
.toolbox Col Input{
    padding: 10px;
    margin: 20px;
    align-self: center;
}
</style>
<template>
<Layout class="main">
    <Row class="toolbox">
        <Col span="8">
            <Button>新建策略</Button>
        </Col>
        <Col span="8">
            <Select v-model="userFilter" placeholder="所有者" clearable style="width:200px">
                <Option v-for="item in userList" :value="item.value" :key="item.value">{{ item.label }}</Option>
            </Select>
        </Col>
        <Col span="8"><Input v-model="nameFilter" placeholder="文件名" icon="search" style="width: 300px"></Input></Col>
    </Row>
    <Row>
        <Table>
        </Table>
    </Row>
</Layout>
</template>
<script>
export default {
    data () {
        return {
            nameFilter: '',
            userFilter: '',
            userList: [
                {
                    value: 'snowwalkerj',
                    label: 'snowwalkerj'
                },
                {
                    value: 'Allen',
                    label: 'Allen'
                }
            ],
            tableColumns: [
                {
                    title: '文件名',
                    key: 'filename',
                    sortable: true
                },
                {
                    title: '所有者',
                    key: 'owner',
                    sortable: true
                },
                {
                    title: '操作',
                    key: 'operation'
                }
            ]
        };
    }
};
</script>


