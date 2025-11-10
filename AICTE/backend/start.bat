@echo off
REM Windows batch script to start the FastAPI server

echo Starting Air Traffic Transcriber & Analyzer Backend...

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip and build tools
echo Upgrading pip and build tools...
python -m pip install --upgrade pip setuptools wheel

REM Install NumPy first (to get pre-built wheel)
echo Installing NumPy...
pip install "numpy>=1.26.0" --only-binary=numpy

REM Install/update dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Start the server
echo Starting server...
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

pause

