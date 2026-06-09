export type StoreItem = {
  id: number
  name: string
  city: string | null
  is_active: boolean
}

export type StoreListData = {
  items: StoreItem[]
  total: number
  page: number
  page_size: number
  sort_by: string
  sort_order: string
}