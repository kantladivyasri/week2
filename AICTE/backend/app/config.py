"""
Configuration settings loaded from environment variables.
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings."""
    
    # Model Configuration
    WHISPER_MODEL_ID: str = "openai/whisper-base"
    BERT_MODEL_ID: str = "bert-base-uncased"
    DEVICE: str = "cpu"  # "cpu" or "cuda"
    
    # Efficiency Thresholds
    EFFICIENCY_THRESHOLD: float = 0.7
    
    # API Configuration
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

