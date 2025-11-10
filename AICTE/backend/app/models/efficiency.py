"""
Efficiency scoring logic for air traffic communications.
"""
from typing import Dict, List
from app.config import settings
from app.utils.logging import get_logger

logger = get_logger(__name__)


class EfficiencyScorer:
    """Calculate efficiency scores for air traffic communications."""
    
    def __init__(self):
        self.threshold = settings.EFFICIENCY_THRESHOLD
    
    def calculate_score(
        self,
        transcript: str,
        intents: Dict[str, float],
        top_intent: str
    ) -> Dict[str, float]:
        """
        Calculate efficiency score based on transcript and intents.
        
        Args:
            transcript: Transcribed text
            intents: Intent classification scores
            top_intent: Primary intent detected
            
        Returns:
            Dictionary with efficiency metrics and overall score
        """
        logger.info("Calculating efficiency score")
        
        # Base metrics
        word_count = len(transcript.split())
        char_count = len(transcript)
        
        # Intent-based scoring
        intent_score = self._score_by_intent(intents, top_intent)
        
        # Clarity scoring (based on length and structure)
        clarity_score = self._score_clarity(transcript, word_count)
        
        # Urgency scoring (emergency/warning intents)
        urgency_score = self._score_urgency(intents)
        
        # Overall efficiency (weighted combination)
        overall_score = (
            intent_score * 0.4 +
            clarity_score * 0.4 +
            urgency_score * 0.2
        )
        
        # Determine status
        status = "efficient" if overall_score >= self.threshold else "needs_improvement"
        
        result = {
            "overall_score": round(overall_score, 3),
            "intent_score": round(intent_score, 3),
            "clarity_score": round(clarity_score, 3),
            "urgency_score": round(urgency_score, 3),
            "status": status,
            "word_count": word_count,
            "char_count": char_count
        }
        
        logger.info(f"Efficiency score calculated: {overall_score:.3f} ({status})")
        return result
    
    def _score_by_intent(self, intents: Dict[str, float], top_intent: str) -> float:
        """Score based on intent clarity and relevance."""
        # Higher scores for clear, actionable intents
        high_value_intents = ["clearance", "instruction", "confirmation"]
        medium_value_intents = ["request", "routine"]
        
        if top_intent in high_value_intents:
            return min(1.0, intents.get(top_intent, 0.5) + 0.2)
        elif top_intent in medium_value_intents:
            return intents.get(top_intent, 0.5)
        else:
            return intents.get(top_intent, 0.3)
    
    def _score_clarity(self, transcript: str, word_count: int) -> float:
        """Score based on transcript clarity and conciseness."""
        # Optimal length range (not too short, not too verbose)
        if 10 <= word_count <= 50:
            return 0.9
        elif 5 <= word_count < 10 or 50 < word_count <= 100:
            return 0.7
        elif word_count < 5:
            return 0.5
        else:
            return 0.4  # Too verbose
    
    def _score_urgency(self, intents: Dict[str, float]) -> float:
        """Score based on urgency indicators."""
        emergency_score = intents.get("emergency", 0.0)
        warning_score = intents.get("warning", 0.0)
        
        if emergency_score > 0.5:
            return 1.0  # High urgency handled well
        elif warning_score > 0.5:
            return 0.8
        else:
            return 0.6  # Routine communication

