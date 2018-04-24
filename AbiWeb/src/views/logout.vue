<template>

</template>

<script>
import Util from '../libs/util'
export default {
    mounted () {
        Util.ajax.request({
            url: '/api/logout'
        }).then(response => {
            this.$store.commit('logout');
            this.$Message.info("登出成功");
            this.$router.push('/');
        }).catch(error => {
            this.$Message.info("没有成功登出："+error.reason);
            this.$router.go(-1);
        });
    }
}
</script>


