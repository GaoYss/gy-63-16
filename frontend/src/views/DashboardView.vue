<template>
  <div class="page-stack">
    <section class="stats-grid">
      <StatCard label="会员数量" :value="members.length" hint="覆盖等级权益" :icon="Users" />
      <StatCard label="预售活动" :value="presales.length" hint="可预约批次" :icon="CalendarClock" />
      <StatCard label="兑换商品" :value="rewards.length" hint="积分权益池" :icon="Gift" />
      <StatCard label="推荐鲜果" :value="recommendations.length" hint="按新鲜度排序" :icon="Sprout" />
    </section>

    <section class="content-grid two-columns">
      <div class="panel">
        <div class="panel-header">
          <h2>会员积分排行</h2>
        </div>
        <div class="rank-list">
          <article v-for="member in topMembers" :key="member.id" class="rank-item">
            <div>
              <strong>{{ member.name }}</strong>
              <span>{{ member.level?.name }}</span>
            </div>
            <b>{{ member.points }} 分</b>
          </article>
        </div>
      </div>

      <div class="panel">
        <div class="panel-header">
          <h2>热门预售</h2>
        </div>
        <article v-for="item in presales" :key="item.id" class="compact-card">
          <div>
            <strong>{{ item.title }}</strong>
            <span>{{ item.pickup_date }} 提货</span>
          </div>
          <b>{{ item.remaining }} 份</b>
        </article>
      </div>
    </section>

    <section class="panel">
      <div class="panel-header">
        <h2>今日鲜果推荐</h2>
      </div>
      <div class="recommendation-grid">
        <article v-for="fruit in recommendations.slice(0, 4)" :key="fruit.id" class="fruit-card">
          <div class="fruit-visual">{{ fruit.name.slice(0, 1) }}</div>
          <div class="fruit-body">
            <div>
              <strong>{{ fruit.name }}</strong>
              <span>{{ fruit.origin }} · {{ fruit.category }}</span>
            </div>
            <b>￥{{ fruit.price }} · 新鲜度 {{ fruit.freshness_score }}</b>
            <p>{{ fruit.reason }}</p>
          </div>
        </article>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { CalendarClock, Gift, Sprout, Users } from 'lucide-vue-next'

import { memberApi } from '../api/members'
import { pointApi } from '../api/points'
import { presaleApi } from '../api/presales'
import { recommendationApi } from '../api/recommendations'
import {
  fallbackMembers,
  fallbackPresales,
  fallbackRecommendations,
  fallbackRewards,
} from '../api/fallback'
import StatCard from '../components/StatCard.vue'
import { keepList } from '../utils/dataState'

const members = ref([...fallbackMembers])
const presales = ref([...fallbackPresales])
const rewards = ref([...fallbackRewards])
const recommendations = ref([...fallbackRecommendations])

const topMembers = computed(() => [...members.value].sort((a, b) => b.points - a.points).slice(0, 5))

onMounted(async () => {
  const [memberList, presaleList, rewardList, recommendationList] = await Promise.all([
    memberApi.list().catch(() => fallbackMembers),
    presaleApi.list().catch(() => fallbackPresales),
    pointApi.rewards().catch(() => fallbackRewards),
    recommendationApi.list().catch(() => fallbackRecommendations),
  ])
  members.value = keepList(memberList, members.value)
  presales.value = keepList(presaleList, presales.value)
  rewards.value = keepList(rewardList, rewards.value)
  recommendations.value = keepList(recommendationList, recommendations.value)
})
</script>
