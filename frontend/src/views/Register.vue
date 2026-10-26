<!-- <script setup lang="ts">
import { ElFormItem } from 'element-plus'
import { h } from 'vue'
</script> -->

<template>
  <div class="register-container">
    <div class="register-box">
      <h1 style="font-size: 24px; margin-bottom: 20px">欢迎注册实验室预约系统！</h1>

      <el-form ref="formRef" :rules="rules" :model="form" label-width="0px" style="width: 100%">
        <el-form-item prop="username">
          <el-input v-model="form.username" placeholder="请输入账号" :prefix-icon="User" />
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
        <el-form-item prop="confirmPassword">
          <el-input
            v-model="form.confirmPassword"
            placeholder="请确认密码"
            :prefix-icon="Lock"
            type="password"
            show-password
          />
        </el-form-item>
        <div>
          <el-button
            size="large"
            type="primary"
            :loading="loadingValue"
            style="width: 100%"
            @click="register"
            >注册</el-button
          >
          <div style="text-align: right; margin-top: 20px">
            <el-link href="/login" type="primary">已有账号？请登录</el-link>
          </div>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { User, Lock } from '@element-plus/icons-vue'
import { registerApi } from '@/api/auth'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'

const router = useRouter()
const form = reactive({
  username: '',
  password: '',
  confirmPassword: ''
})
const formRef = ref()
const validatePass = (rule, value, callback) => {
  if (value === '') {
    callback(new Error('请确认密码'))
  }
  if (value !== form.password) {
    callback(new Error('两次输入的密码不一致'))
  } else {
    callback()
  }
}
const rules = {
  username: [{ required: true, message: '请输入账号', trigger: 'blur' }],
  password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
  confirmPassword: [
    { required: true, message: '请确认密码', trigger: 'blur' },
    { validator: validatePass, trigger: 'blur' }
  ]
}

const loadingValue = ref(false)
const register = async () => {
  const valid = await formRef.value.validate().catch(() => false)
  if (!valid) return
  loadingValue.value = true
  try {
    const res = await registerApi(form)
    if (res.code === 200) {
      ElMessage.success('注册成功')
      await router.push('/login')
    }
  } finally {
    loadingValue.value = false
  }
}
</script>

<style scoped>
.register-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.register-box {
  width: 380px;
  border-radius: 8px;
  box-shadow: 0 8 10px rgba(0, 0, 0, 0.1);
  padding: 30px;
  text-align: center;
}
</style>
