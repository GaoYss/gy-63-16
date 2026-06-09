import { http } from './http'

export const recommendationApi = {
  list: (memberId) => http.get(memberId ? `/recommendations?member_id=${memberId}` : '/recommendations'),
}
