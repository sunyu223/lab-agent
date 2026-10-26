<template>
  <div class="login-container">
    <div class="login-box">
      <h1 style="font-size: 28px">实验室预约系统</h1>
      <div style="margin-top: 5px; margin-bottom: 20px">基于AI Agent的智能实验室预约系统</div>

      <el-form ref="formRef" :rules="rules" :model="form" label-width="0px" style="width: 100%">
        <el-form-item prop="username">
          <el-input v-model="form.username" placeholder="请输入账号" prefix-icon="User" />
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            v-model="form.password"
            placeholder="请输入密码"
            :prefix-icon="Lock"
            type="password"
            show-password
          />
        </el-form-item>
        <div>
          <el-button
            size="large"
            type="primary"
            style="width: 100%"
            @click="login"
            :loading="LoadingValue"
            >登录</el-button
          >
          <div style="text-align: right; margin-top: 20px">
            <el-link href="/register" type="primary">没有账号？立即注册</el-link>
          </div>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { ElMessage } from 'element-plus'
import { Lock } from '@element-plus/icons-vue'
import { useRouter } from 'vue-router'
import { loginApi } from '@/api/auth'
import { useUser } from '@/utils/user'

const { saveLoginData } = useUser()

const form = reactive({
  username: '',
  password: ''
})

const router = useRouter()
const loadingValue = ref(false)
const formRef = ref()
const rules = {
  username: [{ required: true, message: '请输入账号', trigger: 'blur' }],
  password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
}
const login = async () => {
  const valid = await formRef.value.validate().catch(() => false)
  if (!valid) return
  loadingValue.value = true
  try {
    const res = await loginApi(form)
    if (res.code === 200) {
      saveLoginData(res.data)
      ElMessage.success('登录成功')
      await router.push('/manager/home')
    }
  } finally {
    loadingValue.value = false
  }
}
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.login-box {
  width: 380px;
  border-radius: 8px;
  box-shadow: 0 8 10px rgba(0, 0, 0, 0.1);
  padding: 30px;
  text-align: center;
}
</style>
