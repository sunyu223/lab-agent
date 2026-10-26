import axios from 'axios'
import { getToken } from './auth'
import { ElMessage } from 'element-plus'

const service = axios.create({
  baseURL: import.meta.env.VITE_BASE_API,
  timeout: 30000 //30s
})

// 请求拦截器的配置
service.interceptors.request.use(
  (config) => {
    const token = getToken()
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (err) => Promise.reject(err)
)

// 响应拦截器的配置
service.interceptors.response.use(
  (res) => {
    const data = res.data
    if (data.code !== 200) {
      ElMessage.error(data.message || '请求失败')
      if (data.code === 401) {
        logout()
        router.push('/login')
        return Promise.reject(data)
      }
    }
    return data
  },
  (err) => {
    if (err.response) {
      const httpCode = err.response.status
      if (httpCode === 401) {
        ElMessage.error('登录信息已过期，请重新登录')
        logout()
        router.push('/login')
      } else {
        ElMessage.error(err.response.data ? err.response.data.message : '请求失败')
      }
    } else {
      // 后端没启动，网络异常了
      ElMessage.error('网络异常了，请检查后端服务')
    }
    return Promise.reject(err)
  }
)

export default service
