import {
  fallbackLevels,
  fallbackMembers,
  fallbackPresales,
  fallbackRecommendations,
  fallbackRecords,
  fallbackRewards,
} from './fallback'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api'

const fallbackGetters = [
  { test: (path) => path === '/levels', data: () => fallbackLevels },
  { test: (path) => path === '/members', data: () => fallbackMembers },
  { test: (path) => path === '/points/rewards', data: () => fallbackRewards },
  { test: (path) => path.startsWith('/points/records'), data: () => fallbackRecords },
  { test: (path) => path === '/presales', data: () => fallbackPresales },
  { test: (path) => path === '/presales/orders', data: () => [] },
  { test: (path) => path.startsWith('/recommendations'), data: () => fallbackRecommendations },
]

function fallbackFor(path) {
  return fallbackGetters.find((entry) => entry.test(path))?.data()
}

async function request(path, options = {}) {
  const method = options.method || 'GET'
  const attempts = method === 'GET' ? 2 : 1

  for (let attempt = 0; attempt < attempts; attempt += 1) {
    try {
      return await requestOnce(path, options)
    } catch (error) {
      if (attempt < attempts - 1) {
        await new Promise((resolve) => window.setTimeout(resolve, 300))
        continue
      }

      const fallback = method === 'GET' ? fallbackFor(path) : undefined
      if (fallback) {
        console.warn(`接口暂不可用，已使用示例数据: ${path}`)
        return fallback
      }
      throw error
    }
  }
}

async function requestOnce(path, options = {}) {
  const controller = new AbortController()
  const timeout = window.setTimeout(() => controller.abort(), 6000)

  try {
    const response = await fetch(`${API_BASE_URL}${path}`, {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: controller.signal,
      ...options,
    })

    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: '请求失败' }))
      throw new Error(error.detail || '请求失败')
    }

    return response.json()
  } finally {
    window.clearTimeout(timeout)
  }
}

export const http = {
  get: (path) => request(path),
  post: (path, body) => request(path, { method: 'POST', body: JSON.stringify(body) }),
  patch: (path, body) => request(path, { method: 'PATCH', body: JSON.stringify(body) }),
}
