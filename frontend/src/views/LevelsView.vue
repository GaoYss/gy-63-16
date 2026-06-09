<template>
  <div class="page-stack">
    <section class="stats-grid">
      <StatCard label="等级数量" :value="levels.length" hint="会员分层配置" :icon="BadgePercent" />
      <StatCard label="最高门槛" :value="maxMinPoints" hint="积分升级目标" :icon="TrendingUp" />
      <StatCard label="最低折扣" :value="bestDiscount" hint="核心权益力度" :icon="Percent" />
      <StatCard label="权益总数" :value="benefitTotal" hint="展示给会员" :icon="Sparkles" />
    </section>

  <div class="content-grid two-columns">
    <section class="panel">
      <div class="panel-header">
        <h2>等级权益</h2>
      </div>
      <div class="card-grid">
        <article v-for="level in levels" :key="level.id" class="level-card">
          <div>
            <strong>{{ level.name }}</strong>
            <span>{{ level.min_points }} 分起</span>
          </div>
          <b>{{ Math.round(level.discount * 100) }} 折</b>
          <div class="level-progress">
            <div :style="{ width: `${levelProgress(level)}%` }"></div>
          </div>
          <ul>
            <li v-for="benefit in level.benefits" :key="benefit">{{ benefit }}</li>
          </ul>
        </article>
      </div>
    </section>

    <section class="panel">
      <div class="panel-header">
        <h2>新增等级</h2>
      </div>
      <MessageBanner :message="message" :type="messageType" />
      <form class="form-stack" @submit.prevent="submit">
        <label>
          等级名称
          <input v-model="form.name" required placeholder="如 铂金会员" />
        </label>
        <label>
          最低积分
          <input v-model.number="form.min_points" min="0" type="number" />
        </label>
        <label>
          折扣
          <input v-model.number="form.discount" max="1" min="0.1" step="0.01" type="number" />
        </label>
        <label>
          权益
          <input v-model="benefitText" placeholder="用逗号分隔" />
        </label>
        <button class="primary-button" type="submit">保存等级</button>
      </form>
    </section>
  </div>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from 'vue'
import { BadgePercent, Percent, Sparkles, TrendingUp } from 'lucide-vue-next'

import { levelApi } from '../api/levels'
import { fallbackLevels } from '../api/fallback'
import MessageBanner from '../components/MessageBanner.vue'
import StatCard from '../components/StatCard.vue'
import { keepList } from '../utils/dataState'

const levels = ref([...fallbackLevels])
const benefitText = ref('')
const message = ref('')
const messageType = ref('success')
const form = reactive({
  name: '',
  min_points: 0,
  discount: 0.95,
})

const maxMinPoints = computed(() => Math.max(...levels.value.map((level) => level.min_points), 0))
const bestDiscount = computed(() => {
  if (!levels.value.length) return '-'
  return `${Math.round(Math.min(...levels.value.map((level) => level.discount)) * 100)} 折`
})
const benefitTotal = computed(() => levels.value.reduce((sum, level) => sum + level.benefits.length, 0))

function levelProgress(level) {
  if (!maxMinPoints.value) return 12
  return Math.max(12, Math.round((level.min_points / maxMinPoints.value) * 100))
}

async function loadLevels() {
  const levelList = await levelApi.list().catch(() => fallbackLevels)
  levels.value = keepList(levelList, levels.value)
}

async function submit() {
  try {
    await levelApi.create({
      ...form,
      benefits: benefitText.value
        .split(/[,，]/)
        .map((item) => item.trim())
        .filter(Boolean),
    })
    Object.assign(form, { name: '', min_points: 0, discount: 0.95 })
    benefitText.value = ''
    message.value = '等级已保存'
    messageType.value = 'success'
    await loadLevels()
  } catch (error) {
    message.value = error.message
    messageType.value = 'error'
  }
}

onMounted(loadLevels)
</script>
