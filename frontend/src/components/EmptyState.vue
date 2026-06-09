<template>
  <div class="empty-state">
    <component :is="icon" size="28" />
    <p>{{ text }}</p>
  </div>
</template>

<script setup>
import { Inbox } from 'lucide-vue-next'

defineProps({
  text: { type: String, default: '暂无数据' },
  icon: { type: [Object, Function], default: Inbox },
})
</script>
