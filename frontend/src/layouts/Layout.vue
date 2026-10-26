<template>
  <div class="common-layout">
    <el-container style="min-height: 100vh">
      <el-header
        style="
          display: flex;
          align-items: center;
          border-bottom: 1px solid #ddd;
          background-color: #fff;
        "
      >
        <div
          style="flex: 1; display: flex; align-items: center; font-size: 24px; font-weight: bold"
        >
          <img style="width: 40px" src="@/assets/imgs/logo.png" alt="" />
          <div style="margin-left: 5px">智能实验室预约系统</div>
        </div>

        <!-- 关键：用el-dropdown实现下拉菜单 -->
        <el-dropdown @command="onCommand">
          <div style="display: flex; align-items: center; cursor: pointer">
            <img src="@/assets/imgs/logo.png" alt="" style="width: 30px; border-radius: 50%" />
            <div style="margin-left: 3px">管理员</div>
          </div>

          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item command="handlelogout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </el-header>
      <el-container>
        <el-aside width="220px">
          <el-menu router style="height: 100%" default-active="/manager/home">
            <el-menu-item index="/manager/home">
              <el-icon><icon-menu /></el-icon>
              <span>系统首页</span>
            </el-menu-item>
            <el-menu-item index="/manager/lab">
              <el-icon><House /></el-icon>
              <span>实验室管理</span>
            </el-menu-item>
            <el-menu-item index="/manager/equ">
              <el-icon><Setting /></el-icon>
              <span>设备列表管理</span>
            </el-menu-item>
            <el-menu-item index="/manager/user">
              <el-icon><User /></el-icon>
              <span>用户管理</span>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { Menu as IconMenu, Setting, User, House } from '@element-plus/icons-vue'
import { logout } from '@/utils/auth'
const router = useRouter()
const onCommand = (command) => {
  if (command === 'handlelogout') {
    logout()
    localStorage.removeItem('token') //清登录状态
    router.push('/login')
  }
}
</script>
