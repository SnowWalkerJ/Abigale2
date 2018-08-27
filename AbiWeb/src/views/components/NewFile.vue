<template>
<Modal v-model="modal" @on-ok="clickOk">
    <Form ref="uploadForm" :model="uploadForm">
        <FormItem prop="filename" label="文件名">
            <Input type="text" v-model="uploadForm.filename" placeholder="文件名"/>
        </FormItem>
        <FormItem label="上传文件">
            <Upload
                type="drag"
                action="/api/files/new/web"
                :format="['json']"
                :on-success="uploadSuccess">
                <div style="padding: 20px 0">
                    <Icon type="ios-cloud-upload" size="52" style="color: #3399ff"></Icon>
                    <p>点击或拖置文件上传</p>
                </div>
            </Upload>
        </FormItem>
    </Form>
</Modal>
</template>

<script>
import Util from '../../libs/util'
export default {
    props: {
        path: String,
        value: Boolean
    },
    data () {
        return {
            host: Util.ajaxUrl,
            fileId: null,
            uploadForm: {
                filename: '',
            }
        }
    },
    methods: {
        uploadSuccess (response, file) {
            this.fileId = response.fileId;
            this.uploadForm.filename = file.name;
        },
        clickOk () {
            if (this.uploadForm.filename === '') {
                this.$Modal.error({content: "请输入文件名"});
                return;
            } else if (this.fileId === null) {
                this.$Modal.error({content: "未选择文件"});
                return;
            }
            Util.ajax.request({
                url: '/api/files/new/confirm',
                method: 'post',
                params: {
                    id: this.fileId,
                    name: this.uploadForm.filename,
                    path: this.path
                }
            }).then(Util.handleAPI(this, "上传失败", data => {
                this.$Message.success("上传成功");
                this.$emit("success");
            }));
        }
    },
    computed: {
        modal: {
            get () {
                return this.value;
            },
            set (val) {
                this.$emit("input", val);
            }
        },
    }
}
</script>

