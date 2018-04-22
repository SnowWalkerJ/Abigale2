<style scoped>

.title {
    padding: 10px 0 10px 30px;
    font-size: 250%;
}
.chart {
    height:'40vh';
    width:'80vw';
}
</style>

<template>
<div>
<BackTop></BackTop>
<Row>
    <h1 class="title">{{ strategyName }}</h1>
</Row>
<Row>
    <Col span="24">
        <Card title="基本信息">
            <BasicInfo :id="this.fileId" :name="strategyName"/>
        </Card>
    </Col>
</Row>

<Row>
    <Col span="24">
        <Card title="净值曲线">
            <NetValue :id="this.fileId"/>
        </Card>
    </Col>
</Row>

<!-- <Row>
    <Col span="24">
        <Card title="风险分解">
            <div v-html="graph"></div>
        </Card>
    </Col>
</Row> -->

<Row>
    <Col span="24">
        <Card title="风格暴露">
            <Risks field="styleRisks" :id="this.fileId"/>
        </Card>
    </Col>
</Row>

<Row>
    <Col span="24">
        <Card title="行业暴露">
            <Risks field="industryRisks" :id="this.fileId"/>
        </Card>
    </Col>
</Row>
</div>
</template>

<script>
import Viz from 'viz.js'
import Axios from 'axios'
import BasicInfo from './components/BasicInfo.vue'
import NetValue from './components/NetValue.vue'
import Risks from './components/Risks.vue'
export default {
    // props: ['fileId'],
    data () {
        return {
            fileId: '123',
            strategyName: ''
        };
    },
    components: {
        BasicInfo, NetValue, Risks
    },
    mounted () {
        Axios.get("http://localhost:9999/api/details/name?id="+this.fileId).then(response => {
            this.strategyName = response.data.strategyName;
        });
    },
    computed: {
    },
};
</script>


