import { createRouter, createWebHistory } from 'vue-router'

import DashboardView from '../views/DashboardView.vue'
import LevelsView from '../views/LevelsView.vue'
import MembersView from '../views/MembersView.vue'
import PointsView from '../views/PointsView.vue'
import PresalesView from '../views/PresalesView.vue'
import RecommendationsView from '../views/RecommendationsView.vue'

const routes = [
  { path: '/', name: 'dashboard', component: DashboardView },
  { path: '/members', name: 'members', component: MembersView },
  { path: '/levels', name: 'levels', component: LevelsView },
  { path: '/points', name: 'points', component: PointsView },
  { path: '/presales', name: 'presales', component: PresalesView },
  { path: '/recommendations', name: 'recommendations', component: RecommendationsView },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
