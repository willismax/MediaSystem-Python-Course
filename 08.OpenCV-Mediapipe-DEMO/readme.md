
# 電腦視覺DEMO



## OpenCV + MediaPipe
- 建議使用pipenv虛擬環境，本案例採python 3.10以上，相依外部套件可透過`pipenv install`安裝所需套件。

    ```
    pipenv --python 3.10
    pipenv install
    ```

- pipenv相關命令:
    ```
    pipenv shell  #進入虛擬環境
    exit #離開虛擬環境
    pipenv --rm  #移除虛擬環境
    ```


- 執行程式: 
  `pipenv shell` 進入虛擬環境後，選擇自己想執行的程式開啟，開啟後按`ESC`或`q`離開。

    ```bash
    python app-hands.py  #手部辨識
    python app-holistic.py  #肢體辨識
    python app-pose.py  #姿態辨識
    python handle-hand-demo.py  #手勢辨識(愛心/中指)
    ```

- 注意事項:
  - 程式預設使用編號0的攝影機(通常是主要攝影機)
  - 如果有多個攝影機，可以在程式碼中修改`cv2.VideoCapture(0)`的數字
  - 執行時需要允許程式存取攝影機權限



## 參考:
- https://google.github.io/mediapipe/
- [【python】OpenCV + MediaPipe 手部追蹤 ｜ MediaPipe 教學 ｜ 影像辨識 ｜ 電腦視覺 ｜ AI 人工智慧](https://www.youtube.com/watch?v=x4eeX7WJIuA)
