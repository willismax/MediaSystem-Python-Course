# 11. AI 與大型語言模型 (LLM)

本章節介紹如何透過 Python 串接 AI 與大型語言模型 (LLM) API，以 Google Gemini 為主要示範，適合想要快速上手生成式 AI 應用的學習者。

## 📒 教材清單

| 教材 | 說明 | 開啟方式 |
|------|------|----------|
| [動手串接_LLM_API_入門教學(Gemini_).ipynb](動手串接_LLM_API_入門教學(Gemini_).ipynb) | Gemini API 入門教學 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/11.AI/動手串接_LLM_API_入門教學(Gemini_).ipynb) |
| [在_Colab_終端機使用_Gemini_CLI.ipynb](在_Colab_終端機使用_Gemini_CLI.ipynb) | 在 Colab 使用 Gemini CLI | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/11.AI/在_Colab_終端機使用_Gemini_CLI.ipynb) |
| [gemini_cli_colab_tutorial.ipynb](gemini_cli_colab_tutorial.ipynb) | Gemini CLI 完整教學 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/11.AI/gemini_cli_colab_tutorial.ipynb) |

## 🚀 快速開始

### 在 Google Colab 執行 (推薦)

直接點擊上方的 **Open in Colab** 徽章即可在 Colab 執行。

> ⚠️ 需要自備 Google AI Studio API Key，可前往 [Google AI Studio](https://aistudio.google.com/) 免費申請。

### 本機執行

```bash
# 使用 uv (推薦)
uv run --with google-generativeai --with jupyter jupyter notebook

# 或使用傳統方式
pip install google-generativeai
jupyter notebook
```

### 設定 API Key

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
```

在 Colab 中建議使用 Secrets 功能儲存 API Key：

```python
from google.colab import userdata
api_key = userdata.get('GOOGLE_API_KEY')
```

## 📚 學習重點

- Google Gemini API 申請與設定
- 基本文字生成 (Text Generation)
- 多輪對話 (Multi-turn Chat)
- 使用 Gemini CLI 於終端機互動
- 結合 Python 建立 AI 應用

## 🔗 相關資源

- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API 官方文件](https://ai.google.dev/docs)
- [google-generativeai PyPI](https://pypi.org/project/google-generativeai/)
- [Gemini CLI GitHub](https://github.com/google-gemini/gemini-cli)
