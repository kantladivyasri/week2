@echo off
REM Windows batch script to install dependencies with proper order

echo Installing Air Traffic Transcriber & Analyzer Backend Dependencies...

REM Check Python version
python --version
echo.
echo NOTE: Python 3.10-3.12 recommended for best compatibility
echo Python 3.13 may have compatibility issues with some packages
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip and build tools first (critical for Python 3.13)
echo Upgrading pip and build tools...
python -m pip install --upgrade pip setuptools wheel

REM Install NumPy first (use latest version for Python 3.13 compatibility)
echo Installing NumPy...
pip install "numpy>=1.26.0" --only-binary=numpy

REM Install PyTorch (has pre-built wheels)
echo Installing PyTorch...
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu

REM Install core FastAPI dependencies
echo Installing FastAPI dependencies...
pip install fastapi uvicorn[standard] python-multipart
pip install pydantic pydantic-settings

REM Install transformers
echo Installing transformers...
pip install transformers

REM Try to install openai-whisper (may need alternative method)
echo Installing Whisper...
pip install openai-whisper
if errorlevel 1 (
    echo Whisper installation failed, trying alternative method...
    pip install git+https://github.com/openai/whisper.git
)

REM Install audio processing
echo Installing audio processing tools...
pip install ffmpeg-python

echo.
echo Installation complete!
echo.
echo To start the server, run: start.bat
echo Or manually: uvicorn app.main:app --reload

pause

