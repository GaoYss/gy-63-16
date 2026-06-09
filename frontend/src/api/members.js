import { http } from './http'

export const memberApi = {
  list: () => http.get('/members'),
  create: (payload) => http.post('/members', payload),
  update: (id, payload) => http.patch(`/members/${id}`, payload),
}
