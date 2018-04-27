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
import Util from '../../libs/util.js'
export default {
    props: {
        id: String
    },
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
                },
                {
                    title: '换手率',
                    key: 'turnover'
                }
            ]
        }
    },
    methods: {
        getTableData () {
            this.loading = true;
            Util.ajax.request({
                method: "get",
                url: '/api/details/basic',
                params: {
                    id: this.id,
                },
                timeout: 500
            }).then(response => {
                this.tableData = response.data.data;
                this.loading = false;
            });
        }
    },
    mounted () {
        this.getTableData();
    }
}
</script>

