# uv 安裝腳本
# 自動檢測並安裝 uv 套件管理工具

Write-Host "🔧 uv 安裝與設定" -ForegroundColor Green
Write-Host ""

# 檢查 uv 是否已安裝
if (Get-Command uv -ErrorAction SilentlyContinue) {
    $uvVersion = uv --version
    Write-Host "✅ uv 已安裝: $uvVersion" -ForegroundColor Green
    
    $response = Read-Host "是否要更新 uv? (y/N)"
    if ($response -ne 'y' -and $response -ne 'Y') {
        Write-Host "跳過更新" -ForegroundColor Yellow
        exit 0
    }
}

Write-Host "📥 正在下載並安裝 uv..." -ForegroundColor Cyan

try {
    # 下載並執行 uv 安裝腳本
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "✅ uv 安裝成功！" -ForegroundColor Green
        Write-Host ""
        Write-Host "接下來可以使用以下指令：" -ForegroundColor Cyan
        Write-Host "  uv --version              # 查看版本" -ForegroundColor White
        Write-Host "  uv venv                   # 建立虛擬環境" -ForegroundColor White
        Write-Host "  uv pip install package    # 安裝套件" -ForegroundColor White
        Write-Host "  uv run script.py          # 執行腳本" -ForegroundColor White
        Write-Host ""
        Write-Host "快速啟動腳本：" -ForegroundColor Cyan
        Write-Host "  .\scripts\run-flask.ps1   # 啟動 Flask" -ForegroundColor White
        Write-Host "  .\scripts\run-jupyter.ps1 # 啟動 Jupyter" -ForegroundColor White
        Write-Host ""
        
        # 驗證安裝
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
        
        if (Get-Command uv -ErrorAction SilentlyContinue) {
            $version = uv --version
            Write-Host "已安裝版本: $version" -ForegroundColor Green
        } else {
            Write-Host "⚠️  請重新開啟終端機以使用 uv" -ForegroundColor Yellow
        }
    } else {
        Write-Host "❌ 安裝失敗" -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "❌ 安裝過程中發生錯誤: $_" -ForegroundColor Red
    exit 1
}
