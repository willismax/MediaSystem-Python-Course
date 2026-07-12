# 02. Gradio — 互動式 AI 介面

本章節介紹如何使用 [Gradio](https://www.gradio.app/) 快速建立機器學習模型的互動式網頁介面，無需前端開發經驗，適合在 Google Colab 環境中直接執行。

## 📒 教材清單

| 教材 | 說明 | 開啟方式 |
|------|------|----------|
| [gradio_demo.ipynb](gradio_demo.ipynb) | Gradio 互動介面入門示範 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/02.Gradio/gradio_demo.ipynb) |

## 🚀 快速開始

### 在 Google Colab 執行 (推薦)

直接點擊上方的 **Open in Colab** 徽章即可在 Colab 執行，無需本機環境設定。

### 本機執行

```bash
# 使用 uv (推薦)
uv run --with gradio --with jupyter jupyter notebook gradio_demo.ipynb

# 或使用傳統方式
pip install gradio
jupyter notebook gradio_demo.ipynb
```

## 📚 學習重點

- Gradio 基本元件 (Textbox、Image、Audio 等)
- 建立簡易 AI 互動介面
- 在 Colab 分享 Gradio 公開連結
- 結合機器學習模型進行示範

## 🔗 相關資源

- [Gradio 官方文件](https://www.gradio.app/docs/)
- [Gradio GitHub](https://github.com/gradio-app/gradio)
