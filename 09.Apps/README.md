# 09. 實用應用程式

本章節收錄各種 Python 實用應用範例，包含 QR Code 產生器、OpenAI 應用示範等，可直接在 Google Colab 上執行。

## 📒 教材清單

| 教材 | 說明 | 開啟方式 |
|------|------|----------|
| [QRCode.ipynb](QRCode.ipynb) | QR Code 產生器 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/09.Apps/QRCode.ipynb) |
| [OpenAI_Demo.ipynb](OpenAI_Demo.ipynb) | OpenAI API 應用示範 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/09.Apps/OpenAI_Demo.ipynb) |

## 📁 檔案說明

| 檔案 | 說明 |
|------|------|
| `QRCode.ipynb` | QR Code 產生器，支援純黑白、彩色背景與 GIF 動態背景 |
| `QRCode.md` | QR Code 應用說明文件 |
| `OpenAI_Demo.ipynb` | OpenAI API 串接示範 |

## 🚀 快速開始

### 在 Google Colab 執行 (推薦)

直接點擊上方的 **Open in Colab** 徽章即可在 Colab 執行。

### QR Code 本機執行

```bash
# 使用 uv (推薦)
uv run --with qrcode --with pillow --with jupyter jupyter notebook QRCode.ipynb

# 或使用傳統方式
pip install qrcode pillow
jupyter notebook QRCode.ipynb
```

### OpenAI Demo 本機執行

> ⚠️ 需要自備 OpenAI API Key

```bash
# 使用 uv (推薦)
uv run --with openai --with jupyter jupyter notebook OpenAI_Demo.ipynb

# 或使用傳統方式
pip install openai
jupyter notebook OpenAI_Demo.ipynb
```

## 📚 學習重點

### QR Code
- 產生純黑白 QR Code
- 加入背景圖片製作彩色 QR Code
- 使用 GIF 動態背景

### OpenAI API
- OpenAI API 基本串接
- 文字生成應用
- 對話式 AI 範例

## 🔗 相關資源

- [qrcode PyPI](https://pypi.org/project/qrcode/)
- [OpenAI API 文件](https://platform.openai.com/docs/)
- [Pillow 文件](https://pillow.readthedocs.io/)
