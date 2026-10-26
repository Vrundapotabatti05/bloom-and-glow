@echo off
title Bloom & Glow - Gift Shop (Next.js)
echo.
echo  Starting Bloom and Glow Gift Shop (Next.js)...
echo  Browser will open at http://localhost:3000
echo  Close this window to stop.
echo.
set PATH=C:\Program Files\nodejs;%PATH%
cd /d "%~dp0"
if not exist node_modules (
  echo Installing dependencies...
  call npm install
)
start "" http://localhost:3000
call npm run dev
pause