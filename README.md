# Air Traffic Transcriber & Analyzer

A full-stack application for transcribing air traffic control audio and analyzing communication efficiency using AI models.

## Features

- Audio transcription using Whisper
- Intent classification using BERT
- Efficiency scoring for air traffic communications
- Modern web interface

## Setup

### Prerequisites

**Windows Users:**
1. Install FFmpeg (required for Whisper):
   - Download from: https://ffmpeg.org/download.html
   - Or use chocolatey: `choco install ffmpeg`
   - Or use winget: `winget install ffmpeg`
   - Add FFmpeg to your PATH environment variable

2. Python Version:
   - **Recommended:** Python 3.10, 3.11, or 3.12
   - **Python 3.13:** Supported but may have compatibility issues with some packages
   - **Minimum:** Python 3.8

### Backend

**Option 1: Using install script (Recommended for Windows)**

From the project root:
```bash
cd backend
.\install.bat
```

Or if already in the `backend` directory:
```bash
.\install.bat
```

**Note:** In PowerShell, use `.\install.bat` (with `.\` prefix). In CMD, you can use just `install.bat`.

**Option 2: Manual installation**

1. Create virtual environment:
```bash
cd backend
python -m venv venv
venv\Scripts\activate
```

2. Upgrade pip and build tools:
```bash
python -m pip install --upgrade pip setuptools wheel
```

3. Install NumPy first (to get pre-built wheel):
```bash
pip install "numpy>=1.26.0" --only-binary=numpy
```

4. Install PyTorch (CPU version with pre-built wheels):
```bash
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
```

5. Install remaining dependencies:
```bash
pip install -r requirements.txt
```

   **Troubleshooting:**
   - If `openai-whisper` installation fails, try:
     ```bash
     pip install git+https://github.com/openai/whisper.git
     ```
   - If NumPy build fails, ensure you're using a pre-built wheel:
     ```bash
     pip install "numpy>=1.26.0" --only-binary=numpy
     ```
   - **Python 3.13 users:** Some packages may not have wheels yet. Consider using Python 3.11 or 3.12 for better compatibility.

6. Configure environment:
   - Copy `.env.example` to `.env` (or create manually)
   - Edit `.env` with your settings

7. Run the server:
```bash
# In PowerShell:
.\start.bat

# In CMD:
start.bat

# Or manually:
uvicorn app.main:app --reload
```

### Frontend

1. Install dependencies:
```bash
cd frontend
npm install
```

   **Or use the install script:**
   ```bash
   cd frontend
   .\install.bat
   ```

2. Configure environment:
   - Create `frontend/.env.local` file with:
     ```
     VITE_API_BASE_URL=http://localhost:8000
     ```

3. Run the development server:
```bash
npm run dev
```

**Troubleshooting Frontend Issues:**

- **Path errors with `&` in folder name:** The ampersand in "AI&GREEN" can cause issues. Solutions:
  1. Use quotes around paths: `cd "C:\Users\Makkena\Desktop\AI&GREEN\frontend"`
  2. Use the install script: `.\install.bat`
  3. Consider renaming the project folder to remove special characters (e.g., "AI-GREEN")
  
- **Module not found errors:** Try cleaning and reinstalling:
  ```bash
  rmdir /s /q node_modules
  del package-lock.json
  npm install
  ```

## Project Structure

- `backend/` - FastAPI application with AI models
- `frontend/` - React/TypeScript web interface

