<style scoped>
.form {
    width: 30vw;
}
.center {
    margin: 40px auto;
}
.button {
    margin-left: 13vw;
}
</style>


<template>
<Card class="form center">
    <p slot="title">登录</p>
    <Form ref="loginForm" :model="loginForm" :rules="loginRule" label-position="left" show-message>
        <FormItem prop="username" label="用户名" show-message>
            <Input type="text" v-model="loginForm.username" placeholder="Username">
                <Icon type="ios-person-outline" slot="prepend"></Icon>
            </Input>
        </FormItem>
        <FormItem prop="password" label="密码" show-message>
            <Input type="password" v-model="loginForm.password" placeholder="Password">
                <Icon type="ios-locked-outline" slot="prepend"></Icon>
            </Input>
        </FormItem>
        <FormItem>
            <Button class="button" type="primary" @click="handleSubmit('loginForm')">登录</Button>
        </FormItem>
    </Form>
</Card>
</template>
<script>
    import Util from '../libs/util.js'
    export default {
        data () {
            return {
                loginForm: {
                    username: '',
                    password: ''
                },
                loginRule: {
                    username: [
                        { required: true, message: '请输入用户名', trigger: 'blur' }
                    ],
                    password: [
                        { required: true, message: '请输入密码', trigger: 'blur' },
                        { type: 'string', min: 6, message: '密码长度不得少于6位', trigger: 'blur' }
                    ]
                }
            }
        },
        computed: {
            encryptedForm () {
                const sha256 = require('js-sha256');
                let encryptedPassword = sha256(this.loginForm.password);
                return {
                    username: this.loginForm.username,
                    password: encryptedPassword
                }
            }
        },
        methods: {
            handleSubmit(name) {
                this.$refs[name].validate((valid) => {
                    if (valid) {
                        Util.ajax.request({
                            method: 'post',
                            url: '/api/login',
                            data: this.encryptedForm,
                            timeout: 1000
                        }).then(response => {
                            if (response.data.status) {
                                this.$store.commit('login', response.data.data);
                                setTimeout(() => {
                                    router.push('/');
                                }, 100);
                            } else {
                                this.$Message.error("登录失败：" + response.data.msg);
                            }
                        });
                    } else {
                        this.$Message.error('登录信息不符合要求，请重新填写！');
                    }
                })
            },
        }
    }
</script>
