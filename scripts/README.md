# MediaSystem Python Course - Quick Launch Scripts
# 本資料夾包含各種快速啟動腳本

## PowerShell 腳本使用方式

### run-flask.ps1
快速啟動 Flask 專案

```powershell
.\scripts\run-flask.ps1
```

### run-jupyter.ps1
在指定目錄啟動 Jupyter Notebook

```powershell
# 預設在 03.Request 目錄
.\scripts\run-jupyter.ps1

# 指定其他目錄
.\scripts\run-jupyter.ps1 -Path "11.AI"
```

### setup-uv.ps1
安裝 uv 工具

```powershell
.\scripts\setup-uv.ps1
```

## 注意事項

如果遇到 PowerShell 執行政策錯誤，請以管理員身份執行：

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

或是直接使用 uv 指令：

```bash
uv run app.py
uv run --with jupyter jupyter notebook
```
