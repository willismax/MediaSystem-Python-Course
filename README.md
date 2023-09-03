# NUTC-CSIE-MS

## 範例程式碼下載
- 安裝[Git Cli](https://git-scm.com/)
- 在終端機`git clone`專案  
  ```
  git clone MediaSystem-Python-Course
  cd MediaSystem-Python-Course
  ```
  
## 啟動虛擬環境 (2 選 1)
- 虛擬環境能讓開發套件單純化
### pipenv 虛擬環境+套件管理
  - pipenv(需先`pip install pipenv`，並在本機安裝對應的python版本)
    ```
    pipenv --python 3.10
    ```
    
  - 建立好資料夾要CD切換路徑
    ```
    cd NUTC-CSIE-MS
    ```
  
  - 在pipenv安裝相依套件
    以 requirements.txt 裝:
    ```
    pipenv install -r requirements.txt
    ```
    以 Pipfile 裝:
    ```
    pipenv sync
    ```

- 進入環境執行服務
    ```
    pipenv shell
    python app.py
    
    # 或未進入虛擬環境由本機執行
    pipenv run app.py
    ```
    
- 移除虛擬環境
    ```
    pipenv --rm
    ```

### 使用Python內建的虛擬機`venv`

- 建虛擬機venv
  ```
  python -m venv venv
  ```
- 啟動VM，windows為`venv\Scripts\activate`，如果已經在venv資料夾，應為`\Scripts\activate`；linux為`source openvino_env/bin/activate`
  ```
  # Windows
  venv\Scripts\activate
  
  # Linux
  source openvino_env/bin/activate
  ```
- 安裝相關套件
  ```
  pip install -r requirements.txt
  ```

## 相關專案摘要說明

### 01.Intro-Python
- 課程使用到的ipynb檔，在Colab執行

### 02.Gradio
- 可在Colab建立GUI，輔助課程使用

### 03.Selenium
- 需自行下載 webkit 等 Driver 測試，為進階爬蟲教學

### 04.Playwright
- 可錄製腳本抓html，再自己客製化

### 05.Flask
- 從基本網站服務到建立基本API

### 06.LINE-Bot-on-Fly
- 在 Fly.io 建立 LINE Bot ，服務以 Flask 框架實現，並包含 API 測試
- 在`config.py`填入相關tocken
- 服務包含:
  - LINE 訊息傳送 (需LINE Channel acess token、Channel secret、LINE user id)
  - LINE 文字與圖片訊息增加至 HackMD (需HackMD API、Imgure API)
  - LINE 文字訊息翻譯
  - LINE 文字訊息由 OpenAI 回應，並且記錄於 HhackMD (需OpenAI API) 

- 建立 Tasks API 測試:
  - [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/1745585-89afac06-ad51-4fc8-83c0-c26ccf8db7b9?action=collection%2Ffork&collection-url=entityId%3D1745585-89afac06-ad51-4fc8-83c0-c26ccf8db7b9%26entityType%3Dcollection%26workspaceId%3D9132735b-dff0-46b8-8852-839d022a2ac3)
  - Get, Post, Put, Delete測試

### 07.Pytest-DEMO
- 簡易的 pytest demo，寫好在終端機下`pytest`指令測試
- 另外也裝`pytest-cov`套件的話，`pytest --cov=./`可以測試覆蓋率Coverage
  ```
  pytest --cov=./ 
  或
  pytest --cov-report=html
  ```
### 08.OpenCV-Mediapipe-DEMO
- Mediapipe 簡易操作

## 注意事項
- 請配合課程使用，歡迎 issue 討論或發 PR (Pull Request)
- [如何發PR | W3HexSchool](https://w3c.hexschool.com/git/cc7d70b7)