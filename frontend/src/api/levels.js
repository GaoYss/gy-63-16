import { http } from './http'

export const levelApi = {
  list: () => http.get('/levels'),
  create: (payload) => http.post('/levels', payload),
}
