---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.15.1
  kernelspec:
    display_name: Python 3
    name: python3
---

<!-- #region id="view-in-github" colab_type="text" -->
<a href="https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/09.Apps/QRCode.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
<!-- #endregion -->

<!-- #region id="nTnP3h-lf9YW" -->
# QRCode 產生器
- 以下為 Python 程式，您只需要登入 Google 帳號即可使用
- 若您需要留存此筆記本，請複製到雲端硬碟
- 檔案製作完請在左側資料欄下載，該檔案 Colab 關閉後即消失喔
<!-- #endregion -->

```python id="hp-U8QMhTd2O" cellView="form"
#@title 0. 輸入 URL 連結或文字
url = 'https://willismax.github.io/my-site/' #@param {type:"string"}
```

```python id="1nxfS5FXxjcB" cellView="form" colab={"base_uri": "https://localhost:8080/", "height": 76} outputId="92400bad-56c1-4011-9fe8-231efb7f5f56"
#@title 1. (選用)上傳圖片(JPG, PNG, BMP, GIF)
from google.colab import files
picture = files.upload()
pic = [ k for k,v in picture.items()][0]
# https://drive.google.com/file/d/11C1lG26NR0xIzxKCak6VGGxb3G_1pf6P/view?usp=sharing
```

```python id="3fPbn6ie2Sc5" cellView="form" colab={"base_uri": "https://localhost:8080/"} outputId="bb344a03-f039-41d3-8d57-a1cfa7d35274"
#@title 2-1. 製作單純無背景的 QR Code
try:
    from MyQR import myqr
except:
    !pip install -qU MyQr
    from MyQR import myqr

myqr.run( words = url, level = 'L', colorized = False, save_name = './純黑白qrcode.jpg' )
```

<!-- #region id="wAFzUpllNKlC" -->
---

<!-- #endregion -->

<!-- #region id="psXI5oUPWETu" -->
### 製作有背景的 QR Code
- 將生成彩色、黑白 QRCode 各1張
- 如果底圖是 GIF 檔，底圖會動起來


<!-- #endregion -->

<!-- #region id="jrvaHvD467zL" -->
> GIF 梗圖可至 [Tensor](https://tenor.com/zh-TW/) 尋找
<!-- #endregion -->

```python id="ICwXgoATTGLg" cellView="form" colab={"base_uri": "https://localhost:8080/"} outputId="f8ddb14b-056b-4786-e011-16fccc105b25"
#安裝 MyQR 模組
try:
    from MyQR import myqr
except:
    !pip install -qU MyQr
    from MyQR import myqr


#@title 2-2. 製作 QR Code (黑白底圖)


# 黑白圖片的QR Code
try:
  myqr.run(
    words = url,
    picture = pic,
    version = 20, # QR Code的邊長，越大圖案越清楚
    level = 'H', # 糾錯水平，預設是H(最高)
    colorized = False, # 背景圖片是否用彩色，預設是False(黑白)
    save_name = './qrcode-wb.png' # 儲存檔案名稱
    )
except:
  myqr.run(
    words = url,
    picture = pic,
    version = 20, # QR Code的邊長，越大圖案越清楚
    level = 'H', # 糾錯水平，預設是H(最高)
    colorized = False, # 背景圖片是否用彩色，預設是False(黑白)
    save_name = './qrcode-wb.gif' # 儲存檔案名稱
    )


```

```python colab={"base_uri": "https://localhost:8080/"} id="G3TeW7FUyIzi" outputId="ea102a14-416c-4009-a659-61b99fa0d463" cellView="form"
#安裝 MyQR 模組
try:
    from MyQR import myqr
except:
    !pip install -qU MyQr
    from MyQR import myqr

#@title 2-3. 製作 QR Code (彩色底圖)

# 2-3. 彩色圖片的QR Code
try:
  myqr.run(
    words = url,
    picture = pic,
    version = 10,
    level = 'H',
    colorized = True, # 背景圖片是否用彩色，True為彩色
    save_name = './qrcode-color.png'
    )
except:
  myqr.run(
    words = url,
    picture = pic,
    version = 10, # QR Code的邊長，越大圖案越清楚
    level = 'H', # 糾錯水平，預設是H(最高)
    colorized = True, # 背景圖片是否用彩色，預設是False(黑白)
    save_name = './qrcode-color.gif' # 儲存檔案名稱
    )
```

<!-- #region id="-mXpHd-q0NzK" -->
## 下載QRCode
- 點選介面左邊的資料夾，點兩下可以顯示檔案，右鍵可以下載檔案
<!-- #endregion -->
