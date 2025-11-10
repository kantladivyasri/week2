"""
Pydantic models for request/response DTOs.
"""
from pydantic import BaseModel
from typing import Dict, List, Optional


class IntentScores(BaseModel):
    """Intent classification scores."""
    top_intent: str
    intents: Dict[str, float]


class EfficiencyMetrics(BaseModel):
    """Efficiency scoring metrics."""
    overall_score: float
    intent_score: float
    clarity_score: float
    urgency_score: float
    status: str
    word_count: int
    char_count: int


class TranscriptionResponse(BaseModel):
    """Response model for transcription endpoint."""
    transcript: str
    intents: IntentScores
    efficiency: EfficiencyMetrics
    processing_time: Optional[float] = None


class ErrorResponse(BaseModel):
    """Error response model."""
    error: str
    detail: Optional[str] = None

