"""
BERT model for intent classification (pretrained).
"""
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from app.config import settings
from app.utils.logging import get_logger

logger = get_logger(__name__)


class BERTIntentClassifier:
    """BERT-based intent classification model."""
    
    def __init__(self):
        self.tokenizer = None
        self.model = None
        self.model_id = settings.BERT_MODEL_ID
        self.device = settings.DEVICE
        
        # Common air traffic control intents
        self.intent_labels = [
            "clearance",
            "instruction",
            "request",
            "confirmation",
            "warning",
            "emergency",
            "routine"
        ]
    
    def load_model(self):
        """Load the BERT model and tokenizer."""
        if self.model is None:
            logger.info(f"Loading BERT model: {self.model_id}")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
            self.model = AutoModelForSequenceClassification.from_pretrained(
                self.model_id,
                num_labels=len(self.intent_labels)
            )
            self.model.to(self.device)
            self.model.eval()
            logger.info("BERT model loaded successfully")
        return self.model, self.tokenizer
    
    def classify(self, text: str) -> dict:
        """
        Classify intents in the transcribed text.
        
        Args:
            text: Transcribed text to analyze
            
        Returns:
            Dictionary with intent classifications and scores
        """
        model, tokenizer = self.load_model()
        logger.info(f"Classifying intents for text: {text[:50]}...")
        
        # Tokenize input
        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=512,
            padding=True
        ).to(self.device)
        
        # Get predictions
        with torch.no_grad():
            outputs = model(**inputs)
            predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        
        # Map to intent labels
        scores = predictions[0].cpu().numpy()
        intent_scores = {
            self.intent_labels[i]: float(scores[i])
            for i in range(len(self.intent_labels))
        }
        
        # Get top intent
        top_intent_idx = scores.argmax()
        top_intent = self.intent_labels[top_intent_idx]
        
        logger.info(f"Top intent: {top_intent} (score: {scores[top_intent_idx]:.3f})")
        
        return {
            "top_intent": top_intent,
            "intents": intent_scores
        }

