<style scoped>

</style>

<template>
<Tabs @on-click="click">
    <TabPane v-for="key in this.keys" :key="key" :label="key" :name="key">
        <VueHighcharts class="chart" :highcharts="Highstock" :options="chartOptions(key, data)" :ref="'chart' + key"/>
    </TabPane>
</Tabs>
</template>

<script>
import VueHighcharts from 'vue2-highcharts'
import Highstock from 'highcharts/highstock'
import Axios from 'axios'

export default {
    components: {VueHighcharts},
    props: ['field', 'id'],
    data () {
        return {
            keys: [],
            data: {},
            Highstock: Highstock
        }
    },
    methods: {
        click: function (name) {
            if (this.data[name]) return;
            let chart = this.$refs['chart' + name][0];
            console.log(chart);
            chart.delegateMethod('showLoading', 'Loading...');
            Axios.get('http://localhost:9999/api/details/' + this.field + '/query/' + name + '?id=' + this.id).then(response => {
                this.data[name] = response.data;
                chart.addSeries({
                    type: 'column',
                    name: name,
                    data: response.data
                });
                this.data[name] = true;
                chart.delegateMethod("hideLoading");
            });
        },
        chartOptions: function(key, data){
            return {
                chart: {
                    alignTicks: false
                },

                rangeSelector: {
                    selected: 5
                },

                title: {
                    text: key
                },

                series: []
            };
        }
    },
    mounted () {
        Axios.get('http://localhost:9999/api/details/' + this.field + '/keys').then(response => {
            this.keys = response.data;
            this.data = {};
            for (var i in this.keys) {
                this.data[this.keys[i]] = false;
            }
            setTimeout(() => {
                this.click(this.keys[0]);
            }, 100);
        });
    }
}
</script>

