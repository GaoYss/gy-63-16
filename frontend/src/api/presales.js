import { http } from './http'

export const presaleApi = {
  list: () => http.get('/presales'),
  create: (payload) => http.post('/presales', payload),
  reserve: (payload) => http.post('/presales/orders', payload),
  orders: () => http.get('/presales/orders'),
}
