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
<template v-if="this.id != null">
<Row>
    <h1 class="title">{{ strategyName }}</h1>
</Row>
<Row>
    <Col span="24">
        <Card title="基本信息">
            <BasicInfo :id="this.id" :name="strategyName"/>
        </Card>
    </Col>
</Row>

<Row>
    <Col span="24">
        <Card title="净值曲线">
            <NetValue :id="this.id"/>
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
            <Risks field="styleRisks" :id="this.id"/>
        </Card>
    </Col>
</Row>

<Row>
    <Col span="24">
        <Card title="行业暴露">
            <Risks field="industryRisks" :id="this.id"/>
        </Card>
    </Col>
</Row>
</template>
</div>
</template>

<script>
import Util from '../libs/util'
import BasicInfo from './components/BasicInfo.vue'
import NetValue from './components/NetValue.vue'
import Risks from './components/Risks.vue'

export default {
    props: ['id'],
    data () {
        return {
            strategyName: ''
        };
    },
    components: {
        BasicInfo, NetValue, Risks
    },
    mounted () {
        if (this.id == undefined || this.id == null) {
            console.log(this.id);
            this.$Message.error("没有选中要查看的策略");
            this.$router.go(-1);
        } else {
            Util.ajax.request({
                method: 'get',
                url: "/api/details/name?id=" + this.id
            }).then(response => {
                this.strategyName = response.data.data.strategyName;
            });
        }  
    },
    computed: {
        fileId () {

        }
    },
};
</script>


