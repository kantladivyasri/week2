/**
 * Axios client wrapper for backend API calls.
 */
import axios from 'axios'
import { TranscriptionResponse } from '../types/api'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 60000, // 60 seconds for audio processing
})

export const transcribeAudio = async (audioFile: File): Promise<TranscriptionResponse> => {
  const formData = new FormData()
  formData.append('audio', audioFile)

  // Don't set Content-Type header - let browser set it with boundary for FormData
  const response = await apiClient.post<TranscriptionResponse>('/transcribe', formData)
  return response.data
}

export const healthCheck = async (): Promise<{ status: string }> => {
  const response = await apiClient.get('/health', {
    timeout: 5000, // 5 seconds timeout for health checks
  })
  return response.data
}

export default apiClient

