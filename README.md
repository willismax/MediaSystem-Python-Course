# NUTC-CSIE-MS

- 範例程式碼下載(需先安裝git)

    ```
    git clone https://github.com/willismax/NUTC-CSIE-MS.git
    cd NUTC-CSIE-MS
    ```

- 啟動虛擬環境pipenv(需先`pip install pipenv`，並在本機安裝對應的python版本)
    ```
    pipenv --python 3.9.9
    ```

- 安裝相依套件﹑YES!!

    ```
    pipenv install -r requirements.txt
    ```
    如已經有Pipfile.lock檔，可執行:
    ```
    pipenv sync
    ```

- 執行服務
    ```
    # 開啟虛擬環境並進入環境執行
    pipenv shell
    python app.py
    
    # 或未進入虛擬環境由本機執行
    pipenv run app.py
    ```
    
- 移除虛擬環境
    ```
    pipenv --rm
    ```

## LINE-BOT-DEMO

- 提醒:
    - 請配合LINE MESSAGE API填入資訊於`config.py`
        ```
        CHANNEL_ACCESS_TOKEN = ''
        CHANNEL_SERET = ''
        ```

## flask-api-DEMO

> 以開放資料台灣電影院票房統計示範

- 依前述方式執行
    ```
    #進入目錄
    cd flask-api

    #開虛擬環境
    pipenv --python 3.10

    #同步安裝Pipfile.lock對應檔案
    pipenv sync 

    #進入虛擬環境
    pipenv shell 
    
    #執行程式
    python app.py 
    ```
- 執行`app.py`後可以觀察的網址
    - v1
        - http://localhost:5000
        - http://localhost:5000/api/all
        - http://localhost:5000/api/美國
        - http://localhost:5000/api/尚氣與十環傳奇
    - v2
        - http://localhost:5000/api/v2/GET/all
        - http://localhost:5000/api/v2/GET/country/美國
        - http://localhost:5000/api/v2/GET/movie/期末考

- 執行`bike.py`後可以觀察的網址
    - 請觀察Http Response Headers
        - http://localhost:5000
        - http://localhost:5000/df
        - http://localhost:5000/df2json
        - http://localhost:5000/json
        - http://localhost:5000/jsonify

## about GitHub
- 遠端 git push 需要設定個人PAT，push 時輸入git帳號，輸入git密碼時貼上PAT，參閱https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
- 另外如果是linux，可能push時需要管理者權限，使用sudo git push
