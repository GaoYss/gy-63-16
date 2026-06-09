<template>
  <div class="page-stack">
    <section class="stats-grid">
      <StatCard label="活动数量" :value="presales.length" hint="当前预售批次" :icon="CalendarClock" />
      <StatCard label="总名额" :value="totalQuota" hint="可预约库存" :icon="Package" />
      <StatCard label="已预约" :value="totalReserved" hint="会员预订份数" :icon="ShoppingBag" />
      <StatCard label="订单数" :value="orders.length" hint="预售订单" :icon="ClipboardList" />
    </section>

  <div class="content-grid two-columns">
    <section class="panel">
      <div class="panel-header">
        <h2>预售活动</h2>
      </div>
      <div class="card-grid">
        <article v-for="presale in presales" :key="presale.id" class="presale-card">
          <div>
            <strong>{{ presale.title }}</strong>
            <span>{{ presale.start_date }} 至 {{ presale.end_date }}</span>
          </div>
          <div class="price-row">
            <b>￥{{ presale.price }}</b>
            <span>原价 ￥{{ presale.original_price }}</span>
          </div>
          <div class="progress-track">
            <div :style="{ width: `${(presale.reserved / presale.quota) * 100}%` }"></div>
          </div>
          <small>已预约 {{ presale.reserved }} / {{ presale.quota }}，{{ presale.pickup_date }} 提货</small>
          <button class="secondary-button" @click="reserve(presale.id)">预约一份</button>
        </article>
      </div>
      <div class="order-list">
        <h3>预约订单</h3>
        <article v-for="order in orders" :key="order.id" class="compact-card">
          <div>
            <strong>订单 #{{ order.id }}</strong>
            <span>{{ memberName(order.member_id) }} · {{ presaleName(order.presale_id) }}</span>
          </div>
          <b>￥{{ order.amount }} / {{ order.quantity }}份</b>
        </article>
        <EmptyState v-if="!orders.length" text="暂无预约订单" />
      </div>
    </section>

    <section class="panel">
      <div class="panel-header">
        <h2>新增预售</h2>
      </div>
      <MessageBanner :message="message" :type="messageType" />
      <form class="form-stack" @submit.prevent="submit">
        <label>活动标题<input v-model="form.title" required /></label>
        <label>水果名称<input v-model="form.fruit_name" required /></label>
        <div class="form-row">
          <label>预售价<input v-model.number="form.price" min="0" step="0.1" type="number" /></label>
          <label>原价<input v-model.number="form.original_price" min="0" step="0.1" type="number" /></label>
        </div>
        <div class="form-row">
          <label>开始日期<input v-model="form.start_date" type="date" /></label>
          <label>结束日期<input v-model="form.end_date" type="date" /></label>
        </div>
        <label>提货日期<input v-model="form.pickup_date" type="date" /></label>
        <label>名额<input v-model.number="form.quota" min="1" type="number" /></label>
        <button class="primary-button" type="submit">发布活动</button>
      </form>
    </section>
  </div>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from 'vue'
import { CalendarClock, ClipboardList, Package, ShoppingBag } from 'lucide-vue-next'

import { fallbackMembers, fallbackPresales } from '../api/fallback'
import { memberApi } from '../api/members'
import { presaleApi } from '../api/presales'
import EmptyState from '../components/EmptyState.vue'
import MessageBanner from '../components/MessageBanner.vue'
import StatCard from '../components/StatCard.vue'
import { keepList } from '../utils/dataState'

const presales = ref([...fallbackPresales])
const members = ref([...fallbackMembers])
const orders = ref([])
const message = ref('')
const messageType = ref('success')
const form = reactive({
  title: '',
  fruit_name: '',
  price: 39.9,
  original_price: 49.9,
  start_date: '2026-06-01',
  end_date: '2026-06-15',
  pickup_date: '2026-06-18',
  quota: 100,
  reserved: 0,
})

const totalQuota = computed(() => presales.value.reduce((sum, item) => sum + item.quota, 0))
const totalReserved = computed(() => presales.value.reduce((sum, item) => sum + item.reserved, 0))

async function loadData() {
  const [presaleList, memberList, orderList] = await Promise.all([
    presaleApi.list().catch(() => fallbackPresales),
    memberApi.list().catch(() => fallbackMembers),
    presaleApi.orders().catch(() => []),
  ])
  presales.value = keepList(presaleList, presales.value)
  members.value = keepList(memberList, members.value)
  orders.value = Array.isArray(orderList) ? orderList : orders.value
}

async function submit() {
  try {
    await presaleApi.create({ ...form })
    Object.assign(form, {
      title: '',
      fruit_name: '',
      price: 39.9,
      original_price: 49.9,
      start_date: '2026-06-01',
      end_date: '2026-06-15',
      pickup_date: '2026-06-18',
      quota: 100,
      reserved: 0,
    })
    message.value = '预售活动已发布'
    messageType.value = 'success'
    await loadData()
  } catch (error) {
    message.value = error.message
    messageType.value = 'error'
  }
}

async function reserve(presaleId) {
  try {
    await presaleApi.reserve({ member_id: members.value[0]?.id || 1, presale_id: presaleId, quantity: 1 })
    message.value = '预约成功'
    messageType.value = 'success'
    await loadData()
  } catch (error) {
    message.value = error.message
    messageType.value = 'error'
  }
}

function memberName(memberId) {
  return members.value.find((member) => member.id === memberId)?.name || `会员${memberId}`
}

function presaleName(presaleId) {
  return presales.value.find((presale) => presale.id === presaleId)?.title || `活动${presaleId}`
}

onMounted(loadData)
</script>
