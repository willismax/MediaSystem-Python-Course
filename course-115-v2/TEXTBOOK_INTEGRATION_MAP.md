# 多媒體系統 V2｜現行課程主題與指定用書整合

現行課程以影像、聲音與短影音為主線。指定用書原本依影像處理章次與週次排列，V2 改依概念在多媒體系統中的作用重新編排。相同章節可以支援不同媒體，但跨媒體使用時必須重新確認資料單位、參數與限制。

## 重排原則

- 現行課程主題決定學習順序，指定用書提供概念與方法支援。
- 取樣、頻域、壓縮、可重現流程與安全可以跨影像、聲音及影片使用。
- 生成影像、語音合成、FFmpeg 與短影音敘事以 V2 週講義為主要教材。
- 影像偽裝與加密保留為安全延伸，不列入短影音專題的最低要求。

## 指定用書的新閱讀順序

| 閱讀單元 | 重排後內容 | 指定用書配套講義 | 接入現行課程的方式 |
|---|---|---|---|
| 1｜系統與工具 | 多媒體輸入、處理、輸出、Python 與可重現紀錄 | [CH01 數位媒體介紹](https://hackmd.io/a6IEdT8rRumRxrTDIRImRQ)、[Python 與 AI 協作](https://hackmd.io/rJDO25vqQbq_g5B6GeAKGg)、[可重複使用的處理流程](https://hackmd.io/-hhiSd8AQT-p3Js5fRm1-g) | 支援 W01、W03、W16 與 W18 的管線、環境及重跑紀錄。 |
| 2｜影像資料 | 取樣、量化、像素、色彩、矩陣、格式與壓縮 | [取樣、量化與影像格式](https://hackmd.io/LIgP3rEKQb61yaxJHCcStA)、[像素、色彩與矩陣](https://hackmd.io/v-yUNMzqSuSIXgKRL-O6ag)、[壓縮與壓縮痕跡](https://hackmd.io/hwMXI-0BRIq8nTbSX97p_g) | 直接支援 W02，並作為影片影格與輸出品質的先備概念。 |
| 3｜影像運算 | 卷積、邊緣、傅立葉轉換與頻率濾波 | [卷積、濾波與邊緣](https://hackmd.io/iQAy6_NqSdGzGIB31m_1jw)、[傅立葉轉換與頻譜](https://hackmd.io/kQLfdWczRDOHM3KghYyFiA)、[頻率濾波與比較](https://hackmd.io/M7EvMkgzRUiJ-OLGOPei5Q) | 直接支援 W03；頻域內容也支援 W10～W11 的聲音類比。 |
| 4｜生成與評估 | 參數紀錄、品質比較、資料風險與視覺安全 | [安全與效能評估](https://hackmd.io/46q9JgBgSDertq2fjnGfug)、[多媒體應用與視覺安全](https://hackmd.io/zV7psmnJTeKQt2DzFPvm8A) | 支援 W04～W08 的生成實驗設計、資料卡與作品說明；模型原理以 V2 講義為準。 |
| 5｜聲音與語音 | 取樣、頻譜、濾波、流程驗證與合成風險 | 取樣、傅立葉、頻率濾波、流程與安全章節 | 以跨媒體方式支援 W10～W12；音訊公式、API 與模型細節以 V2 講義為準。 |
| 6｜短影音與發布 | 影格壓縮、處理流程、效能、安全與成果展示 | 壓縮、流程、安全、[期末整合展示](https://hackmd.io/u6S09L95QsKOC9pSOJa5Iw)、[附錄與繳交模板](https://hackmd.io/aCrFmb1cRBi-M_Lmb9dXUA) | 支援 W13～W18 的輸出品質、素材紀錄、測試、README 與封存。 |
| 7｜安全延伸 | 有損式、無損式與加密影像偽裝 | [有損式影像偽裝](https://hackmd.io/s0gF1_7ySLeeDwwF30d8HA)、[無損式影像偽裝](https://hackmd.io/DACIlFaKTRiHCwGqspw0dQ)、[加密影像偽裝](https://hackmd.io/IQ2nAhcdS8uaF7g-CrWlAw) | 作為 W14、W16 或專題的選讀內容，不列入所有學生的必做路徑。 |

## 現行課程主題對照

| 現行課程主題 | 對應週次 | 指定用書整合內容 | Repo 其他學生教材 | 整合後的學習證據 |
|---|---|---|---|---|
| 多媒體資料與影像基礎 | W01～W03 | 系統、取樣、像素、卷積、頻域、格式與壓縮 | [`media/image`](../media/image/)、[`01.Intro-Python`](../01.Intro-Python/)、[`08.OpenCV-Mediapipe-DEMO`](../08.OpenCV-Mediapipe-DEMO/) | 媒體拆解圖、影像資訊表、控制變因濾鏡比較 |
| 生成影像與視覺敘事 | W04～W08 | 可重現流程、安全與效能評估 | [`11.AI`](../11.AI/)、[`09.Apps/OpenAI_Demo.ipynb`](../09.Apps/OpenAI_Demo.ipynb) | seed／參數紀錄、資料卡、影像故事組與技術說明 |
| 數位聲音與語音 | W10～W12 | 取樣、傅立葉、濾波、流程與安全的跨媒體類比 | [`media/audio`](../media/audio/)、[`media/ethics`](../media/ethics/) | 波形與頻譜比較、聲音重製、深偽證據分級 |
| 短影音與系統整合 | W13～W18 | 壓縮、可重現流程、安全、成果展示與附錄模板 | [`media/video`](../media/video/)、[`media/ethics`](../media/ethics/)、[`07.Pytest-DEMO`](../07.Pytest-DEMO/) | 分鏡、素材表、粗剪、測試結果、成品與 README |

## 內容邊界

指定用書中的影像公式不能直接替代音訊或影片公式。例如，影像的二維卷積與聲音的一維卷積共享局部加權概念，但軸的意義、邊界處理與評估方式不同。跨媒體類比用來建立概念橋梁，實作仍應回到各媒體講義與工具文件。

服務介面、免費額度、模型名稱及 GPU 可用性可能變動。教材保留原理、參數與驗證方法；使用服務前應查看官方文件。

## 來源版本

本整合表依 2026 年 8 月 9 日的「多媒體系統：數位影像處理與視覺安全」配套講義，以及 repo 內現行學生教材整理。
