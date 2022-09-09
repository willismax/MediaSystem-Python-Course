
# 電腦視覺DEMO



## OpenCV + MediaPipe
- 建議使用pipenv虛擬環境，本案例採python 3.8，相依外部套件可透過`pipenv sync`將`Pipfile.lock`內鎖定的相依套件進行安裝。

    ```
    pipenv --python 3.8
    pipenv sync
    ```

- pipenv相關命令:
    ```
    pipenv shell  #進入虛擬環境
    exit #離開虛擬環境
    pipenv --rm  #移除虛擬環境
    ```


- 執行程式: 
  `pipenv shell` 進入虛擬環境後，選擇自己想執行的程式開啟，開啟後按`esc`或`q`離開。

    ```
    python app-hands.py  #手部辨識
    python app-holistic.py  #肢體辨識
    python app-pose.py  #姿態辨識
    ```



## 參考:
- https://google.github.io/mediapipe/
- [【python】OpenCV + MediaPipe 手部追蹤 ｜ MediaPipe 教學 ｜ 影像辨識 ｜ 電腦視覺 ｜ AI 人工智慧](https://www.youtube.com/watch?v=x4eeX7WJIuA)
