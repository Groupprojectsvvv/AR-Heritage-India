@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
  where python >nul 2>nul
  if errorlevel 1 (echo Python 3 is required. Install it from https://www.python.org/downloads/ and enable PATH.& pause & exit /b 1)
  set "PYTHON=python"
) else (set "PYTHON=py -3")
if not exist ".venv\Scripts\python.exe" (
  echo Creating project virtual environment...
  %PYTHON% -m venv .venv
  if errorlevel 1 (echo Could not create virtual environment.& pause & exit /b 1)
)
echo Installing or updating project dependencies...
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (echo Dependency installation failed. Check your internet connection and Python installation.& pause & exit /b 1)
where cloudflared >nul 2>nul
if errorlevel 1 goto local_only

echo Starting the temporary HTTPS tunnel for phone AR preview...
echo Copy the https:// URL ending in trycloudflare.com from the Cloudflare window to your phone.
echo Keep both this window and the Cloudflare tunnel window open while testing.
start "AR Heritage India - HTTPS tunnel" cloudflared tunnel --url http://localhost:5000
timeout /t 3 /nobreak >nul
".venv\Scripts\python.exe" backend\launcher.py
echo The website server has stopped. Stop the tunnel with Ctrl+C in its window.
pause
exit /b 0

:local_only
echo cloudflared is not installed, so HTTPS AR preview will not start automatically.
echo Install the Windows cloudflared tool once from:
echo https://developers.cloudflare.com/tunnel/downloads/
echo Then run this file again. The local website can still run without cloudflared.
echo.
echo For local HTTP phone preview only, use the PHONE URL printed below on the same Wi-Fi.
echo Do not enter 127.0.0.1 on the phone; allow Python through Windows Firewall on Private networks if prompted.
".venv\Scripts\python.exe" backend\launcher.py
pause
