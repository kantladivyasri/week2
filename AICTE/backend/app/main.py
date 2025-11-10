"""
FastAPI application entry point with routes for audio transcription and analysis.
"""
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.services.pipeline import TranscriptionPipeline
from app.schemas.dto import TranscriptionResponse, ErrorResponse
from app.utils.audio import validate_audio_file
from app.config import settings

app = FastAPI(title="Air Traffic Transcriber & Analyzer")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pipeline = TranscriptionPipeline()


@app.get("/")
async def root():
    return {"message": "Air Traffic Transcriber & Analyzer API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(audio: UploadFile = File(...)):
    """
    Transcribe audio file and analyze for intents and efficiency.
    """
    try:
        # Validate audio file
        if not validate_audio_file(audio):
            raise HTTPException(status_code=400, detail="Invalid audio file format")
        
        # Process through pipeline
        result = await pipeline.process(audio)
        
        return TranscriptionResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT)

