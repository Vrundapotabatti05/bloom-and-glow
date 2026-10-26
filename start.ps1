Write-Host "============================================" -ForegroundColor Magenta
Write-Host "    BLOOM & GLOW - Gift Shop (Next.js)" -ForegroundColor Magenta
Write-Host "============================================" -ForegroundColor Magenta
Write-Host ""

$env:Path = "C:\Program Files\nodejs;" + $env:Path
Set-Location $PSScriptRoot

if (-not (Test-Path "node_modules")) {
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    npm install
}

Write-Host "Starting website..." -ForegroundColor Green
Write-Host "Browser will open at http://localhost:3000" -ForegroundColor Cyan
Write-Host "Close this window to stop the server." -ForegroundColor Yellow
Write-Host ""

Start-Process "http://localhost:3000"
npm run dev