#!/bin/bash
# Jupyter Notebook 快速啟動腳本 (Linux/macOS)
# 使用 uv 執行 Jupyter Notebook

TARGET_PATH=${1:-03.Request}

echo "📓 啟動 Jupyter Notebook"

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

# 進入指定目錄
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
FULL_PATH="$SCRIPT_DIR/../$TARGET_PATH"

if [ ! -d "$FULL_PATH" ]; then
    echo "❌ 找不到目錄: $FULL_PATH"
    echo "可用目錄:"
    echo "  - 01.Intro-Python"
    echo "  - 02.Gradio"
    echo "  - 03.Request"
    echo "  - 09.Apps"
    echo "  - 10.sql"
    echo "  - 11.AI"
    exit 1
fi

cd "$FULL_PATH"

echo "📂 當前目錄: $FULL_PATH"
echo "🚀 啟動 Jupyter Notebook..."
echo "按 Ctrl+C 停止服務"
echo ""

# 使用 uv 啟動 Jupyter Notebook
uv run --with jupyter --with notebook jupyter notebook
