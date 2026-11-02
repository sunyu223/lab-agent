import request from '@/utils/request'

/**
 * 登录请求
 * @param {Object} data
 * @returns
 */
export function loginApi(data) {
  return request({
    url: '/api/auth/login',
    method: 'post',
    data
  })
}

/**
 * 注册请求
 * @param {Object} data
 * @returns
 */
export function registerApi(data) {
  return request({
    url: '/api/auth/register',
    method: 'post',
    data
  })
}
