#!/bin/bash
# Flask 快速啟動腳本 (Linux/macOS)
# 使用 uv 執行 Flask 應用

FLASK_APP=${1:-flask01}

echo "🚀 啟動 Flask 應用: $FLASK_APP"

# 檢查 uv 是否已安裝
if ! command -v uv &> /dev/null; then
    echo "❌ 未找到 uv，正在安裝..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    
    if [ $? -ne 0 ]; then
        echo "❌ uv 安裝失敗"
        exit 1
    fi
    
    echo "✅ uv 安裝成功"
    # 重新載入 PATH
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# 進入 Flask 目錄
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
FLASK_PATH="$SCRIPT_DIR/../05.Flask/$FLASK_APP"

if [ ! -d "$FLASK_PATH" ]; then
    echo "❌ 找不到 Flask 應用: $FLASK_PATH"
    exit 1
fi

cd "$FLASK_PATH"

echo "📂 當前目錄: $FLASK_PATH"

# 檢查是否存在 requirements.txt
if [ -f "requirements.txt" ]; then
    echo "📦 安裝依賴..."
    uv venv
    uv pip install -r requirements.txt
fi

# 啟動 Flask 應用
echo "🌐 啟動 Flask 服務..."
echo "按 Ctrl+C 停止服務"
echo ""

uv run app.py
