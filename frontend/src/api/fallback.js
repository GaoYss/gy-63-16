export const fallbackLevels = [
  {
    id: 1,
    name: '普通会员',
    min_points: 0,
    discount: 1,
    benefits: ['积分累计', '新品提醒'],
  },
  {
    id: 2,
    name: '银卡会员',
    min_points: 500,
    discount: 0.95,
    benefits: ['95折优惠', '生日双倍积分'],
  },
  {
    id: 3,
    name: '金卡会员',
    min_points: 1500,
    discount: 0.9,
    benefits: ['9折优惠', '预售优先购', '专属推荐'],
  },
]

export const fallbackMembers = [
  {
    id: 1,
    name: '李明',
    phone: '13800000001',
    level_id: 2,
    points: 860,
    favorite_categories: ['柑橘', '莓果'],
    level: fallbackLevels[1],
  },
  {
    id: 2,
    name: '王芳',
    phone: '13800000002',
    level_id: 3,
    points: 2100,
    favorite_categories: ['热带水果', '礼盒'],
    level: fallbackLevels[2],
  },
]

export const fallbackRewards = [
  {
    id: 1,
    title: '10元水果券',
    points_cost: 300,
    stock: 24,
    description: '满39元可用，适合日常补货。',
  },
  {
    id: 2,
    title: '精品蓝莓一盒',
    points_cost: 680,
    stock: 10,
    description: '125g装，门店自提。',
  },
  {
    id: 3,
    title: '当季果篮升级',
    points_cost: 1200,
    stock: 8,
    description: '果篮增加进口奇异果和车厘子。',
  },
]

export const fallbackRecords = [
  {
    id: 1,
    member_id: 1,
    change: 120,
    type: 'earn',
    note: '购买当季水果',
    created_at: '2026-06-01 10:00',
  },
  {
    id: 2,
    member_id: 2,
    change: -300,
    type: 'redeem',
    note: '兑换10元水果券',
    created_at: '2026-06-01 11:30',
  },
]

export const fallbackPresales = [
  {
    id: 1,
    title: '云南高山蓝莓预售',
    fruit_name: '高山蓝莓',
    price: 39.9,
    original_price: 49.9,
    start_date: '2026-06-01',
    end_date: '2026-06-15',
    pickup_date: '2026-06-18',
    quota: 200,
    reserved: 68,
    remaining: 132,
  },
  {
    id: 2,
    title: '海南贵妃芒礼盒',
    fruit_name: '贵妃芒',
    price: 88,
    original_price: 108,
    start_date: '2026-06-05',
    end_date: '2026-06-20',
    pickup_date: '2026-06-23',
    quota: 120,
    reserved: 35,
    remaining: 85,
  },
]

export const fallbackRecommendations = [
  {
    id: 1,
    name: '阳光玫瑰葡萄',
    category: '葡萄',
    freshness_score: 98,
    origin: '云南',
    price: 29.9,
    tags: ['高甜', '无籽', '冷链到店'],
    reason: '新鲜度高，适合作为今日主推',
  },
  {
    id: 2,
    name: '佳沛金奇异果',
    category: '进口水果',
    freshness_score: 95,
    origin: '新西兰',
    price: 8.8,
    tags: ['维C', '早餐', '会员热购'],
    reason: '到店批次稳定，适合搭配早餐场景推荐',
  },
  {
    id: 3,
    name: '泰国金枕榴莲',
    category: '热带水果',
    freshness_score: 92,
    origin: '泰国',
    price: 42,
    tags: ['香甜', '预售同款', '高客单'],
    reason: '适合热带水果偏好会员',
  },
  {
    id: 4,
    name: '四川爱媛橙',
    category: '柑橘',
    freshness_score: 96,
    origin: '四川',
    price: 16.9,
    tags: ['多汁', '家庭装', '复购高'],
    reason: '到店批次新鲜度高，可提升复购',
  },
]
