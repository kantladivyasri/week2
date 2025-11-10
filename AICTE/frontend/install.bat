@echo off
REM Windows batch script to install frontend dependencies

echo Installing Frontend Dependencies...

REM Remove existing node_modules if corrupted
if exist "node_modules\" (
    echo Cleaning existing node_modules...
    rmdir /s /q node_modules
)

REM Remove package-lock.json
if exist "package-lock.json" (
    del package-lock.json
)

REM Install dependencies
echo Installing dependencies...
call npm install

echo.
echo Installation complete!
echo.
echo To start the dev server, run:
echo   npm run dev
echo.
echo NOTE: If you encounter path issues due to the '&' in folder name,
echo consider renaming the project folder to remove special characters.

pause

