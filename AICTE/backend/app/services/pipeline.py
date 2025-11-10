"""
Orchestrates the full pipeline: audio -> transcript -> intents -> score.
"""
import time
import tempfile
import os
from fastapi import UploadFile
from app.models.whisper_infer import WhisperTranscriber
from app.models.bert_intents import BERTIntentClassifier
from app.models.efficiency import EfficiencyScorer
from app.utils.logging import get_logger

logger = get_logger(__name__)


class TranscriptionPipeline:
    """Main pipeline for processing audio through transcription and analysis."""
    
    def __init__(self):
        self.transcriber = WhisperTranscriber()
        self.intent_classifier = BERTIntentClassifier()
        self.efficiency_scorer = EfficiencyScorer()
    
    async def process(self, audio_file: UploadFile) -> dict:
        """
        Process audio file through the complete pipeline.
        
        Args:
            audio_file: Uploaded audio file
            
        Returns:
            Dictionary with transcript, intents, and efficiency scores
        """
        start_time = time.time()
        
        try:
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                content = await audio_file.read()
                tmp_file.write(content)
                tmp_path = tmp_file.name
            
            try:
                # Step 1: Transcribe audio
                logger.info("Starting transcription pipeline")
                transcript = self.transcriber.transcribe(tmp_path)
                
                # Step 2: Classify intents
                intent_results = self.intent_classifier.classify(transcript)
                
                # Step 3: Calculate efficiency
                efficiency_results = self.efficiency_scorer.calculate_score(
                    transcript=transcript,
                    intents=intent_results["intents"],
                    top_intent=intent_results["top_intent"]
                )
                
                processing_time = time.time() - start_time
                
                return {
                    "transcript": transcript,
                    "intents": intent_results,
                    "efficiency": efficiency_results,
                    "processing_time": round(processing_time, 2)
                }
            
            finally:
                # Clean up temporary file
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)
                    logger.info(f"Cleaned up temporary file: {tmp_path}")
        
        except Exception as e:
            logger.error(f"Pipeline error: {str(e)}", exc_info=True)
            raise

