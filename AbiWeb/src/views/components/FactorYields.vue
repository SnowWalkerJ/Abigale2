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
    props: {
        id: String,
        name: String
    },
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
                yAxis: {
                    // labels: {
                    //     formatter: function () {
                    //         return (this.value > 0 ? ' +' : '') + this.value * 100 + '%';
                    //     }
                    // },
                    plotLines: [{
                        value: 0,
                        width: 2,
                        color: 'silver'
                    }]
                },
                // plotOptions: {
                //     series: {
                //         compare: 'percent',
                //         showInNavigator: true
                //     }
                // },
                tooltip: {
                    pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y*100}%</b><br/>',
                    valueDecimals: 2,
                    split: true
                },
                title: {
                    text: '因子归因'
                },
                series: []
            };
        },
    },
    mounted () {
        Util.ajax.request({
            method: "get",
            url: '/api/details/factorYields',
            params: {
                id: this.id,
            },
            timeout: 500
        }).then(response => {
            for (var name in response.data.data) {
                this.$refs.chart.addSeries({
                    name: name,
                    data: response.data.data[name],
                    tooltip: {
                        valueDecimals: 2
                    }
                });
            }
        });
    }
}
</script>
