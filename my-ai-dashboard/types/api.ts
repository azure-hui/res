export type ApiResponse<T> = {
  code: string
  message: string
  data: T
  request_id: string
  timestamp: string
}

export type ApiErrorResponse = {
  code: string
  message: string
  data: null
  request_id?: string
  timestamp?: string
}