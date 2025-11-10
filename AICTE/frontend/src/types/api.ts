/**
 * TypeScript types matching backend DTOs.
 */

export interface IntentScores {
  top_intent: string
  intents: Record<string, number>
}

export interface EfficiencyMetrics {
  overall_score: number
  intent_score: number
  clarity_score: number
  urgency_score: number
  status: string
  word_count: number
  char_count: number
}

export interface TranscriptionResponse {
  transcript: string
  intents: IntentScores
  efficiency: EfficiencyMetrics
  processing_time?: number
}

