<template>
  <div class="app-shell">
    <aside class="sidebar">
      <div class="brand">
        <div class="brand-mark">果</div>
        <div>
          <strong>鲜果会员</strong>
          <span>管理系统</span>
        </div>
      </div>

      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.to" :to="item.to" class="nav-item">
          <component :is="item.icon" size="18" />
          <span>{{ item.label }}</span>
        </RouterLink>
      </nav>
    </aside>

    <main class="main-panel">
      <header class="topbar">
        <div>
          <p>Fruit Store CRM</p>
          <h1>{{ currentTitle }}</h1>
        </div>
        <div class="status-pill">
          <Activity size="16" />
          <span>运行中</span>
        </div>
      </header>

      <RouterView :key="route.fullPath" />
    </main>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { RouterLink, RouterView, useRoute } from 'vue-router'
import {
  Activity,
  BadgePercent,
  CalendarClock,
  Gauge,
  Gift,
  Sprout,
  Users,
} from 'lucide-vue-next'

const route = useRoute()

const navItems = [
  { to: '/', label: '经营概览', icon: Gauge },
  { to: '/members', label: '会员管理', icon: Users },
  { to: '/levels', label: '会员等级', icon: BadgePercent },
  { to: '/points', label: '积分兑换', icon: Gift },
  { to: '/presales', label: '预售活动', icon: CalendarClock },
  { to: '/recommendations', label: '鲜果推荐', icon: Sprout },
]

const currentTitle = computed(() => navItems.find((item) => item.to === route.path)?.label || '经营概览')
</script>
