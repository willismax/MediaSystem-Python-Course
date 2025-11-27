# Flask 快速啟動腳本
# 使用 uv 執行 Flask 應用

param(
    [string]$FlaskApp = "flask01"
)

Write-Host "🚀 啟動 Flask 應用: $FlaskApp" -ForegroundColor Green

# 檢查 uv 是否已安裝
if (!(Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "❌ 未找到 uv，正在安裝..." -ForegroundColor Yellow
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ uv 安裝失敗" -ForegroundColor Red
        exit 1
    }
    
    Write-Host "✅ uv 安裝成功" -ForegroundColor Green
}

# 進入 Flask 目錄
$FlaskPath = Join-Path $PSScriptRoot "..\05.Flask\$FlaskApp"

if (!(Test-Path $FlaskPath)) {
    Write-Host "❌ 找不到 Flask 應用: $FlaskPath" -ForegroundColor Red
    exit 1
}

Set-Location $FlaskPath

Write-Host "📂 當前目錄: $FlaskPath" -ForegroundColor Cyan

# 檢查是否存在 requirements.txt
if (Test-Path "requirements.txt") {
    Write-Host "📦 安裝依賴..." -ForegroundColor Yellow
    uv venv
    uv pip install -r requirements.txt
}

# 啟動 Flask 應用
Write-Host "🌐 啟動 Flask 服務..." -ForegroundColor Green
Write-Host "按 Ctrl+C 停止服務" -ForegroundColor Yellow
Write-Host ""

uv run app.py
