import request from '@/utils/request'

/**
 * 获取当前登录用户信息
 * @returns
 */
export function getUserInfo() {
  return request({
    url: '/api/user/info',
    method: 'get'
  })
}

/**
 * 更新用户信息请求
 * @param {Object} data
 * @returns
 */
export function updateUserInfo(data) {
  return request({
    url: '/api/user/update',
    method: 'put',
    data
  })
}
