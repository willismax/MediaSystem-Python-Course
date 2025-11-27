# Jupyter Notebook 快速啟動腳本
# 使用 uv 執行 Jupyter Notebook

param(
    [string]$Path = "03.Request"
)

Write-Host "📓 啟動 Jupyter Notebook" -ForegroundColor Green

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

# 進入指定目錄
$TargetPath = Join-Path $PSScriptRoot "..\$Path"

if (!(Test-Path $TargetPath)) {
    Write-Host "❌ 找不到目錄: $TargetPath" -ForegroundColor Red
    Write-Host "可用目錄:" -ForegroundColor Yellow
    Write-Host "  - 01.Intro-Python" -ForegroundColor Cyan
    Write-Host "  - 02.Gradio" -ForegroundColor Cyan
    Write-Host "  - 03.Request" -ForegroundColor Cyan
    Write-Host "  - 09.Apps" -ForegroundColor Cyan
    Write-Host "  - 10.sql" -ForegroundColor Cyan
    Write-Host "  - 11.AI" -ForegroundColor Cyan
    exit 1
}

Set-Location $TargetPath

Write-Host "📂 當前目錄: $TargetPath" -ForegroundColor Cyan
Write-Host "🚀 啟動 Jupyter Notebook..." -ForegroundColor Green
Write-Host "按 Ctrl+C 停止服務" -ForegroundColor Yellow
Write-Host ""

# 使用 uv 啟動 Jupyter Notebook
uv run --with jupyter --with notebook jupyter notebook
