<template>
  <div class="page-stack">
    <section class="stats-grid">
      <StatCard label="可兑换商品" :value="rewards.length" hint="库存权益" :icon="Gift" />
      <StatCard label="当前会员积分" :value="currentMember?.points || 0" hint="兑换前余额" :icon="WalletCards" />
      <StatCard label="积分流水" :value="records.length" hint="筛选会员记录" :icon="ListChecks" />
      <StatCard label="总库存" :value="totalStock" hint="剩余兑换份数" :icon="PackageCheck" />
    </section>

  <div class="content-grid two-columns">
    <section class="panel">
      <div class="panel-header">
        <h2>兑换商品</h2>
        <select v-model.number="selectedMemberId" @change="loadRecords">
          <option v-for="member in members" :key="member.id" :value="member.id">
            {{ member.name }} · {{ member.points }}分
          </option>
        </select>
      </div>
      <div class="card-grid">
        <article v-for="reward in rewards" :key="reward.id" class="reward-card">
          <div>
            <strong>{{ reward.title }}</strong>
            <span>{{ reward.description }}</span>
          </div>
          <div class="reward-meta">
            <b>{{ reward.points_cost }} 分</b>
            <span>库存 {{ reward.stock }}</span>
          </div>
          <button class="secondary-button" @click="redeem(reward.id)">兑换</button>
        </article>
      </div>
    </section>

    <section class="panel">
      <div class="panel-header">
        <h2>积分记录</h2>
      </div>
      <MessageBanner :message="message" :type="messageType" />
      <form class="inline-form" @submit.prevent="adjust">
        <input v-model.number="adjustForm.change" type="number" placeholder="积分变动，如 100" />
        <input v-model="adjustForm.note" placeholder="原因，如 购买水果" />
        <button class="primary-button" type="submit">记一笔</button>
      </form>
      <div class="timeline">
        <article v-for="record in records" :key="record.id" class="timeline-item">
          <div>
            <strong>{{ record.note }}</strong>
            <span>{{ record.created_at }}</span>
          </div>
          <b :class="{ negative: record.change < 0 }">{{ record.change > 0 ? '+' : '' }}{{ record.change }}</b>
        </article>
      </div>
    </section>
  </div>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from 'vue'
import { Gift, ListChecks, PackageCheck, WalletCards } from 'lucide-vue-next'

import { fallbackMembers, fallbackRecords, fallbackRewards } from '../api/fallback'
import { memberApi } from '../api/members'
import { pointApi } from '../api/points'
import MessageBanner from '../components/MessageBanner.vue'
import StatCard from '../components/StatCard.vue'
import { keepList } from '../utils/dataState'

const rewards = ref([...fallbackRewards])
const members = ref([...fallbackMembers])
const records = ref([...fallbackRecords])
const selectedMemberId = ref(1)
const message = ref('')
const messageType = ref('success')
const adjustForm = reactive({ change: 100, note: '购买水果获得积分' })

const currentMember = computed(() => members.value.find((member) => member.id === selectedMemberId.value))
const totalStock = computed(() => rewards.value.reduce((sum, reward) => sum + reward.stock, 0))

async function loadRecords() {
  const recordList = await pointApi.records(selectedMemberId.value).catch(() => fallbackRecords)
  records.value = keepList(recordList, records.value)
}

async function loadData() {
  const [rewardList, memberList] = await Promise.all([
    pointApi.rewards().catch(() => fallbackRewards),
    memberApi.list().catch(() => fallbackMembers),
  ])
  rewards.value = keepList(rewardList, rewards.value)
  members.value = keepList(memberList, members.value)
  selectedMemberId.value = memberList[0]?.id || 1
  await loadRecords()
}

async function redeem(rewardId) {
  try {
    await pointApi.redeem({ member_id: selectedMemberId.value, reward_id: rewardId })
    message.value = '兑换成功'
    messageType.value = 'success'
    await loadData()
  } catch (error) {
    message.value = error.message
    messageType.value = 'error'
  }
}

async function adjust() {
  try {
    await pointApi.adjust({
      member_id: selectedMemberId.value,
      change: adjustForm.change,
      note: adjustForm.note,
    })
    message.value = '积分记录已保存'
    messageType.value = 'success'
    await loadData()
  } catch (error) {
    message.value = error.message
    messageType.value = 'error'
  }
}

onMounted(loadData)
</script>
