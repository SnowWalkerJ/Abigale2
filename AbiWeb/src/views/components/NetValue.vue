<style scoped>
chart {
    min-height: 40vh;
    width: 80vw;
}
</style>


<template>
<VueHighcharts class="chart" :highcharts="Highstock" :options="chartOptions" ref="chart"/>
</template>

<script>
import VueHighcharts from 'vue2-highcharts'
import Highstock from 'highcharts/highstock'
import Util from '../../libs/util.js'

export default {
    components: {
        VueHighcharts
    },
    props: ['id', 'name'],
    data () {
        return {
            data: {},
            Highstock: Highstock
        }
    },
    computed: {
        chartOptions () {
            return {
                rangeSelector: {
                    selected: 5
                },
                title: {
                    text: '净值曲线（超额收益）'
                },
                series: []
            };
        },
    },
    mounted () {
        Util.ajax.request({
            method: "get",
            url: '/api/details/netValues?id='+this.id,
            timeout: 500
        }).then(response => {
            this.$refs.chart.addSeries({
                name: this.name,
                data: response.data.data,
                tooltip: {
                    valueDecimals: 2
                }
            });
        });
    }
}
</script>
