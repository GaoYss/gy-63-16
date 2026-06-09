import { http } from './http'

export const pointApi = {
  rewards: () => http.get('/points/rewards'),
  records: (memberId) => http.get(memberId ? `/points/records?member_id=${memberId}` : '/points/records'),
  redeem: (payload) => http.post('/points/redeem', payload),
  adjust: (payload) => http.post('/points/adjust', payload),
}
