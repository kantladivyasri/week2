"""
Audio helper functions for validation and processing.
"""
import os
from fastapi import UploadFile
from app.utils.logging import get_logger

logger = get_logger(__name__)

ALLOWED_AUDIO_FORMATS = {".wav", ".mp3", ".m4a", ".flac", ".ogg"}


def validate_audio_file(audio_file: UploadFile) -> bool:
    """
    Validate uploaded audio file format.
    
    Args:
        audio_file: Uploaded file object
        
    Returns:
        True if valid, False otherwise
    """
    if not audio_file.filename:
        logger.warning("Audio file has no filename")
        return False
    
    # Check file extension
    file_ext = os.path.splitext(audio_file.filename)[1].lower()
    if file_ext not in ALLOWED_AUDIO_FORMATS:
        logger.warning(f"Invalid audio format: {file_ext}")
        return False
    
    # Check content type if available
    if audio_file.content_type:
        valid_types = {
            "audio/wav", "audio/wave",
            "audio/mpeg", "audio/mp3",
            "audio/mp4", "audio/m4a",
            "audio/flac",
            "audio/ogg"
        }
        if audio_file.content_type not in valid_types:
            logger.warning(f"Invalid content type: {audio_file.content_type}")
            return False
    
    logger.info(f"Audio file validated: {audio_file.filename}")
    return True


def check_ffmpeg() -> bool:
    """
    Check if ffmpeg is available in the system.
    
    Returns:
        True if ffmpeg is available, False otherwise
    """
    import subprocess
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            check=True
        )
        logger.info("ffmpeg is available")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        logger.warning("ffmpeg is not available")
        return False

