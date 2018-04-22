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
import Axios from 'axios'

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
        Axios.get('http://localhost:9999/api/details/netValues?id='+this.id).then(response => {
            this.$refs.chart.addSeries({
                name: this.name,
                data: response.data,
                tooltip: {
                    valueDecimals: 2
                }
            });
        });
    }
}
</script>
