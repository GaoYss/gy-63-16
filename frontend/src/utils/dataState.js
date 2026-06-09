export function keepList(next, current) {
  return Array.isArray(next) && next.length > 0 ? next : current
}
