<template>
  <div class="page-stack">
    <section class="stats-grid">
      <StatCard label="推荐数量" :value="recommendations.length" hint="今日可售鲜果" :icon="Sprout" />
      <StatCard label="最高新鲜度" :value="topFreshness" hint="优先陈列" :icon="Gauge" />
      <StatCard label="匹配会员" :value="selectedMemberName" hint="按偏好排序" :icon="UserRound" />
      <StatCard label="分类数量" :value="categoryCount" hint="覆盖货架" :icon="Boxes" />
    </section>

    <section class="panel">
      <div class="panel-header">
        <h2>新鲜水果推荐</h2>
        <select v-model.number="selectedMemberId" @change="loadRecommendations">
          <option :value="0">通用推荐</option>
          <option v-for="member in members" :key="member.id" :value="member.id">
            {{ member.name }}
          </option>
        </select>
      </div>
      <div class="recommendation-grid">
        <article v-for="fruit in recommendations" :key="fruit.id" class="fruit-card">
          <div class="fruit-visual">{{ fruit.name.slice(0, 1) }}</div>
          <div class="fruit-body">
            <div>
              <strong>{{ fruit.name }}</strong>
              <span>{{ fruit.origin }} · {{ fruit.category }}</span>
            </div>
            <b>新鲜度 {{ fruit.freshness_score }}</b>
            <strong class="price-label">￥{{ fruit.price }}</strong>
            <p>{{ fruit.reason }}</p>
            <div class="tag-list">
              <span v-for="tag in fruit.tags" :key="tag">{{ tag }}</span>
            </div>
          </div>
        </article>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { Boxes, Gauge, Sprout, UserRound } from 'lucide-vue-next'

import { fallbackMembers, fallbackRecommendations } from '../api/fallback'
import { memberApi } from '../api/members'
import { recommendationApi } from '../api/recommendations'
import StatCard from '../components/StatCard.vue'
import { keepList } from '../utils/dataState'

const members = ref([...fallbackMembers])
const recommendations = ref([...fallbackRecommendations])
const selectedMemberId = ref(0)

const topFreshness = computed(() => Math.max(...recommendations.value.map((fruit) => fruit.freshness_score), 0))
const selectedMemberName = computed(() => {
  if (!selectedMemberId.value) return '通用'
  return members.value.find((member) => member.id === selectedMemberId.value)?.name || '通用'
})
const categoryCount = computed(() => new Set(recommendations.value.map((fruit) => fruit.category)).size)

async function loadRecommendations() {
  const recommendationList = await recommendationApi
    .list(selectedMemberId.value || undefined)
    .catch(() => fallbackRecommendations)
  recommendations.value = keepList(recommendationList, recommendations.value)
}

onMounted(async () => {
  const memberList = await memberApi.list().catch(() => fallbackMembers)
  members.value = keepList(memberList, members.value)
  await loadRecommendations()
})
</script>
