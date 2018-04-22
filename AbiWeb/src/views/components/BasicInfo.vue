<style scoped>
.table {
    padding: 20px;
}
</style>

<template>
<Table class="table" stripe :columns="tableColumns" :data="tableData" :loading="loading">
</Table>
</template>

<script>
import Axios from 'axios'
export default {
    props: ['id'],
    data () {
        return {
            loading: true,
            tableData: [],
            tableColumns: [
                {
                    title: '时期',
                    key: 'period'
                },
                {
                    title: '年化收益率',
                    key: 'rtn'
                },
                {
                    title: '年化波动率',
                    key: 'volatility'
                },
                {
                    title: '年化夏普率',
                    key: 'sharpe'
                },
                {
                    title: '最大回撤',
                    key: 'mdd'
                }
            ]
        }
    },
    methods: {
        getTableData () {
            this.loading = true;
            Axios.get('http://localhost:9999/api/details/basic?id='+this.id).then(response => {
                this.tableData = response.data;
                this.loading = false;
            });
        }
    },
    mounted () {
        this.getTableData();
    }
}
</script>

