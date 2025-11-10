"""
Whisper model for audio transcription (pretrained).
"""
import whisper
from app.config import settings
from app.utils.logging import get_logger

logger = get_logger(__name__)


class WhisperTranscriber:
    """Whisper-based audio transcription model."""
    
    def __init__(self):
        self.model = None
        self.model_id = settings.WHISPER_MODEL_ID
        self.device = settings.DEVICE
    
    def load_model(self):
        """Load the Whisper model."""
        if self.model is None:
            logger.info(f"Loading Whisper model: {self.model_id}")
            self.model = whisper.load_model(self.model_id, device=self.device)
            logger.info("Whisper model loaded successfully")
        return self.model
    
    def transcribe(self, audio_path: str) -> str:
        """
        Transcribe audio file to text.
        
        Args:
            audio_path: Path to audio file
            
        Returns:
            Transcribed text
        """
        model = self.load_model()
        logger.info(f"Transcribing audio: {audio_path}")
        
        result = model.transcribe(audio_path)
        transcript = result["text"].strip()
        
        logger.info(f"Transcription completed: {len(transcript)} characters")
        return transcript

