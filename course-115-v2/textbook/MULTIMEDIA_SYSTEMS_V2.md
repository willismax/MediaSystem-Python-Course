# 多媒體系統教科書 V2｜從影像、聲音到短影音的完整學習路徑

> 本書整合《多媒體系統：AI 時代的實作之旅》與 [MediaSystem-Python-Course](https://github.com/willismax/MediaSystem-Python-Course) 的 V2 教材包，依四個教學模組重新編寫。沿著本書的順序閱讀與實作，即可完整走完 W01～W18 的學習路徑。

## 這本書怎麼用

多媒體作品看起來是創作，拆開來是一條資料管線：輸入是什麼、如何表示、經過哪些處理、如何判斷品質、輸出能否安全發布。本書把影像、聲音與短影音放進同一條管線思維，並全程示範如何與 AI 協作開發、如何留下可重現與可追溯的紀錄。

全書分四個模組，對應課程 W01～W18 的實施順序：

| 模組 | 主題 | 對應週次 | 主要成果 |
|---|---|---|---|
| A｜多媒體資料與影像基礎 | 媒體管線、AI 協作方法、取樣與量化、像素、色彩、格式、壓縮、卷積與頻域 | W01～W03 | 媒體拆解圖、影像參數實驗、控制變因濾鏡比較 |
| B｜生成影像與視覺敘事 | 擴散模型、潛在空間、提示控制、LoRA、影像一致性與生成倫理 | W04～W08 | 可重現提示實驗、影像故事組、期中技術說明 |
| C｜數位聲音與語音 | 波形、取樣率、FFT/STFT、聲音剪輯、語音合成、聲音深偽與證據判讀 | W10～W12 | 頻譜觀察、聲音重製、合成／真實聲音比較 |
| D｜短影音與系統整合 | 分鏡、時間軸、素材溯源、FFmpeg、編碼與容器、測試、發表與封存 | W13～W18 | 直式短影音、素材紀錄、測試證據與可重現專題包 |

W09 是期中整理與評量節點，不另立內容模組。

### 每章的固定結構

每一章都依「**問題 → 原理 → 小型實驗 → 創作 → 驗證**」前進：

1. **核心問題**：這章要回答什麼。
2. **概念**：用生活比喻與最少的數學講清楚原理。
3. **實作**：可在 CPU 執行的程式路徑，並示範與 AI 協作的方式。
4. **對應教材**：連到 repo 的週講義、labs、Colab 與模板。
5. **基礎練習與延伸挑戰**：第一次閱讀完成基礎練習；準備專題時回來做延伸挑戰。
6. **檢核題**：自我檢查是否真的理解。

### 學習方法：控制變因與可重現

本課程的實驗要求很簡單，但要求你每次都做到：**至少改變一個參數、觀察一個結果、提出一個解釋，並留下可重現紀錄**。每次實驗至少保留：

- 執行環境與套件版本。
- 輸入檔名、來源與授權。
- 關鍵參數與隨機種子（seed）。
- 輸出檔名與比較方式。
- 失敗案例、錯誤訊息與修正方法。
- AI 協作時的提示、採用內容與驗證方式。

一次同時更換模型、seed、尺寸與提示，結果就無法解釋。**修改單一變因並保留對比結果**，是全書所有實驗的共同守則。

### AI 使用政策

本課程**鼓勵**使用 AI 工具，但有三條規則：

1. **看得懂才能交**：繳交的每一行程式碼，你必須能解釋它在做什麼。
2. **標註 AI 參與**：作業附上 AI 協作紀錄——你問了什麼、AI 給了什麼、你修改了什麼。
3. **觀念檢核不使用 AI**：每週檢核題檢查你自己的理解。

AI 是放大器，放大的是你已有的理解；理解為零，放大後仍是零。

### 執行環境

所有基礎練習均提供 CPU 路徑。需要較多算力的生成或微調，先使用預先產生的結果理解參數，再視情況使用免費 Colab GPU。GPU 配額與商業服務**不是**完成本書的必要條件。

### 教材包資源

本書與 repo 的教材包搭配使用（連結均指向 [course-115-v2](https://github.com/willismax/MediaSystem-Python-Course/tree/main/course-115-v2)）：

| 類型 | 位置 | 用途 |
|---|---|---|
| 每週講義 | [`weeks/`](https://github.com/willismax/MediaSystem-Python-Course/tree/main/course-115-v2/weeks) | 概念、實驗、練習、繳交與檢核題 |
| CPU 實驗 | [`labs/`](https://github.com/willismax/MediaSystem-Python-Course/tree/main/course-115-v2/labs) | 影像、擴散、聲音與短影音程式 |
| Colab | [`colab/`](https://github.com/willismax/MediaSystem-Python-Course/tree/main/course-115-v2/colab) | 對應的瀏覽器 Notebook |
| 作業模板 | [`templates/`](https://github.com/willismax/MediaSystem-Python-Course/tree/main/course-115-v2/templates) | AI 使用、素材來源、同意紀錄與成果評量 |
| 延伸教材 | repo 根目錄 `01`～`11` 資料夾 | Python、Gradio、Flask、pytest、OpenCV 等延伸實作 |

### 完成四個模組後，你應能

1. 說明影像、聲音與影片的取樣、量化、壓縮及時間結構。
2. 使用 Python 與常見媒體工具完成基本處理，並保留可重現的輸入、參數與輸出。
3. 說明生成影像與語音合成的基本管線，不把服務介面當成模型原理。
4. 比較至少一組控制變因實驗，根據結果說明技術選擇與限制。
5. 以 FFmpeg 或 MoviePy 組合影像、聲音、字幕與影片，完成短影音作品。
6. 記錄素材來源、同意、AI 協作與後製過程，辨識可能造成誤認或侵害權利的發布風險。
7. 以架構圖、測試結果、失敗案例與 README 說明作品如何運作。

---

# 模組 A｜多媒體資料與影像基礎（W01～W03）

> 核心問題：一段媒體在電腦裡到底是什麼？我們如何檢查、處理並重現它？

本模組建立全書的三塊地基：**系統思維**（媒體是管線不是檔案集合）、**工作方法**（與 AI 協作、控制變因、可重現紀錄）、**資料表示**（取樣、量化、像素、卷積與頻域）。模組結束時，你要能交出媒體拆解圖、影像參數實驗與濾鏡比較。

---

## 第 1 章｜多媒體系統不是檔案集合

### 核心問題

什麼才算一個「多媒體系統」？（對應 [W01 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W01_課程啟動與多媒體系統.md)）

### 1.1 從一支短影音拆起

你在手機上看一支短影音時，背後發生了什麼：

1. **擷取**：創作者用鏡頭與麥克風錄下原始素材。
2. **處理**：剪輯軟體調色、上字幕、加背景音樂、轉場。
3. **壓縮與儲存**：影片被壓縮（否則一分鐘 4K 影片可能超過 5GB），存到雲端。
4. **傳輸**：伺服器依你的網速選擇適當畫質串流（自適應串流）。
5. **呈現與互動**：手機解碼、播放；你按讚、留言、拖動進度條，互動又回饋給系統。

![多媒體系統的五段管線](https://hackmd.io/_uploads/S1DALPj-Mg.png)

*圖 1-1｜多媒體系統的五段管線：每一段都是本書某幾章的主題，你的期末專題就是一條完整的小管線。*

把素材放在同一個資料夾，還不能稱為系統。系統至少要交代六件事：

1. 輸入從哪裡來，格式與使用權利是什麼。
2. 資料如何被讀取與檢查。
3. 處理步驟與參數如何排列。
4. 中間結果如何保存與命名。
5. 輸出如何驗證品質與限制。
6. 別人能否依文件重新執行。

基本管線可以寫成：

```text
輸入 → 檢查 → 轉換／生成 → 組合 → 驗證 → 輸出與紀錄
```

同一份素材可能在不同階段扮演不同角色：一張 PNG 可以是生成模型的參考圖、短影音中的畫面，也可以是系統測試時的固定輸入。清楚命名輸入、中間檔與輸出，比累積大量未整理素材更重要。

### 1.2 媒體的本質：一切都是數字

電腦不認識顏色、聲音或畫面，只認識數字。任何媒體要進入電腦，都必須先變成數字；任何處理，都是對數字的運算。

- 一張照片＝數百萬個「像素值」組成的數字陣列。
- 一段聲音＝每秒被「量」了四萬多次的氣壓數值序列。
- 一部影片＝每秒 24～60 張照片＋一條聲音，再加上聰明的壓縮。

學多媒體，就是學「怎麼用程式操作這些數字」——第 3 章正式處理「類比 → 數位」的轉換原理。

### 1.3 你的第一支多媒體程式

建好環境（Python 3.11+、虛擬環境、`pip install pillow`；完整安裝指引見附錄 A），建立 `week01_hello.py`：

```python
"""我的第一支多媒體程式 — 生成一張漸層色卡"""
from PIL import Image

width, height = 800, 400
img = Image.new("RGB", (width, height))

# 逐一設定每個像素的顏色，做出由藍到橘的水平漸層
for x in range(width):
    ratio = x / width            # 0.0（最左）到 1.0（最右）
    r = int(255 * ratio)
    g = int(120 * ratio)
    b = int(255 * (1 - ratio))
    for y in range(height):
        img.putpixel((x, y), (r, g, b))

img.save("my_first_gradient.png")
print("完成！請打開 my_first_gradient.png。")
```

這張漸層圖的每一個像素，都是你的程式算出來的——你剛剛親手「無中生有」了一張影像。第 4 章會用 NumPy 把這支程式加速一百倍。

### 1.4 可重現紀錄：從第一天開始

每次實驗至少保留：執行環境與套件版本、輸入檔名與來源授權、關鍵參數與隨機種子、輸出檔名與比較方式、失敗案例與修正方法、AI 協作的提示與驗證方式。

使用 repo 提供的模板：[AI 使用紀錄](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/templates/ai-usage.md)、[素材紀錄表 ASSET_LOG.csv](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/templates/ASSET_LOG.csv)。

### 對應教材

- [W01｜課程啟動與多媒體系統](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W01_課程啟動與多媒體系統.md)
- [01.Intro-Python 延伸教材](https://github.com/willismax/MediaSystem-Python-Course/tree/main/01.Intro-Python)

### 基礎練習

1. 選一支 15～30 秒短影音，畫出「影像、聲音、文字、處理與輸出」的關係圖。不要只列軟體名稱，要指出每一步接收什麼資料、產生什麼資料。
2. 修改漸層程式，做出由你的學號末三碼決定的配色漸層，存檔為 `gradient_學號.png`。

### 檢核題

- 「把素材放在同一個資料夾」與「一個多媒體系統」差在哪六件事？
- 你的漸層程式中，哪一行決定了漸層的方向？

---

## 第 2 章｜與 AI 協作的開發方法

### 核心問題

AI 能直接生成程式碼，為什麼還要學原理？「會用 AI」到底是什麼能力？

### 2.1 開發哲學三句話

1. **AI 負責「打字」，你負責「思考」**：語法細節交給 AI，問題拆解、方案選擇、結果驗證留給自己。
2. **每一行都要能解釋**：這是本課程的鐵律。
3. **先讓它動，再讓它好**：用 AI 快速做出能跑的版本，再逐步理解、重構、優化。

理解原理的人，使用 AI 的效率是不理解的人的數倍——而且只有理解的人能判斷 AI 什麼時候在「一本正經地胡說八道」。AI 生成的程式碼可能語法正確但邏輯錯誤、用了過時的函式庫、在邊界條件出錯、或效能極差。

### 2.2 CGRF：有效提示的四要素

把 AI 當成「能力很強但完全不了解你的工程師」。一個有效的程式提示包含四要素：

| 要素 | 說明 | 範例片段 |
|---|---|---|
| **C**ontext 背景 | 你是誰、用什麼工具、程度如何 | 「我是 Python 初學者，Windows + Python 3.12，用 Pillow」 |
| **G**oal 目標 | 要做什麼，輸入輸出是什麼 | 「讀取資料夾中所有 .jpg，每張縮成寬 800px」 |
| **R**estrictions 限制 | 不要什麼、邊界條件 | 「保持長寬比；原檔不可覆蓋；壞檔要跳過並警告」 |
| **F**ormat 格式 | 輸出形式 | 「逐行加中文註解；先解釋思路再給程式碼」 |

實務上，好的 AI 協作是多輪對話：CGRF 拿到初版 → 把錯誤訊息完整貼回去 → 要求改進 → 任何看不懂的地方立刻問。

### 2.3 三道防線：驗證 AI 程式碼

AI 生成的程式碼「看起來對」和「真的對」之間有一道鴻溝。對每段 AI 程式碼執行三道防線：

![CGRF 與三道防線](https://hackmd.io/_uploads/HJnR5ws-zg.png)

*圖 2-1｜與 AI 協作的兩個核心工具：CGRF 負責「問得清楚」，三道防線負責「驗得確實」。*

1. **閱讀理解（看）**：逐行讀過，看不懂的行先問 AI、再查文件。通不過防線一的程式碼，不准進入你的作業。
2. **預測執行（想）**：執行前先寫下你預測的結果，執行後比對。預測錯誤的地方，就是你理解有漏洞的地方——這是最高效的學習訊號。
3. **邊界測試（踹）**：空資料夾會怎樣？檔名有中文或空格會怎樣？給它一張 1×1 的圖、一個副檔名是 .jpg 的文字檔會怎樣？AI 特別容易在邊界條件出錯，因為提示裡通常沒提到。

關於「vibe coding」（完全用自然語言指揮 AI、幾乎不看程式碼）：原型期可以 vibe，**交付前必須收斂回理解**。三道防線就是收斂的工具。

### 2.4 實作：AI 結對開發「批次縮圖工具」

情境：把活動的 300 張照片縮小放上網站。

1. 用 CGRF 提示取得初版（讀取 `photos/` 所有圖檔、等比例縮成寬 800px、存到 `photos_small/`、壞檔跳過並警告）。
2. 執行三道防線：逐行讀懂（`os.listdir`？`Image.thumbnail` 和 `resize` 差在哪？）；預測輸出再執行；放一個假的 .jpg 文字檔、清空資料夾、放中文檔名試踹。
3. 自己定義一個新功能（印出節省空間統計、命令列參數、浮水印），練習寫規格 → AI 起草 → 你驗證。
4. `git init` 並 commit——從本週起養成版本紀錄習慣。

### 對應教材

- [01.Intro-Python](https://github.com/willismax/MediaSystem-Python-Course/tree/main/01.Intro-Python)、[07.Pytest-DEMO](https://github.com/willismax/MediaSystem-Python-Course/tree/main/07.Pytest-DEMO)
- 附錄 C｜AI 協作提示範本

### 基礎練習

1. 完成批次縮圖工具，繳交程式、三道防線紀錄（預測 vs 實際、踹出了什麼）、AI 協作紀錄。
2. 故意請 AI 寫一個含 bug 的程式（「寫一個計算平均值的函式，偷埋一個不易發現的 bug」），用三道防線把 bug 揪出來。

### 檢核題

- CGRF 四要素各是什麼？少了 R（限制）最常出什麼問題？
- 三道防線中，哪一道最能抓到「邊界條件錯誤」？

---

## 第 3 章｜取樣、量化與媒體資料

### 核心問題

真實世界是連續的，電腦是離散的——連續訊號如何變成數字？損失了什麼？（對應 [W02 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W02_數位影像與像素.md)）

### 3.1 取樣與量化

把連續訊號變成離散數字，需要兩個步驟：

1. **取樣（sampling）**：沿著時間或空間軸，每隔固定間隔量一次——決定「量多密」。
2. **量化（quantization）**：把每次量到的值，用有限位元數的整數記錄——決定「量多準」。

比喻：用一疊照片記錄一場舞蹈。取樣＝每秒拍幾張（拍太少，動作跳格）；量化＝每張照片的畫質（太低，細節糊掉）。

![取樣與量化](https://hackmd.io/_uploads/BJIh3vs-Gl.png)

*圖 3-1｜類比 → 數位的兩個步驟：取樣在時間軸上「挑點」，量化把每個點的值「對齊格線」——對不齊的部分就是量化誤差。*

影像在**空間**上取樣，形成寬 × 高的像素網格；聲音在**時間**上取樣，形成依序排列的振幅數值；影片在時間上取樣畫面，每一格內又包含空間取樣。

**Nyquist 取樣定理**：取樣頻率必須至少是訊號最高頻率的兩倍，才能完整重建訊號。取樣不足時，高頻變化被誤認成較低頻的圖樣，稱為**混疊（aliasing）**——影片裡車輪倒轉、細條紋衣服的摩爾紋，都是混疊。

![混疊](https://hackmd.io/_uploads/BydT2PiZMl.png)

*圖 3-2｜混疊的視覺證據：9 Hz 的訊號用 10 Hz 取樣（不足 2 倍），取樣點連起來「長得像」1 Hz——訊號偽裝成了更低的頻率。*人耳可聽頻率約 20 Hz～20 kHz，所以 CD 取樣率是 44,100 Hz——比 20 kHz 的兩倍多一點，是 Nyquist 定理的直接應用。

**位元深度（bit depth）**：每個樣本用幾個位元記錄。

| 位元深度 | 可表示階數 | 用途 |
|---|---|---|
| 1 bit | 2 | 黑白傳真 |
| 8 bit | 256 | 影像單一色板 |
| 16 bit | 65,536 | CD 音質音訊 |
| 24 bit | 約 1,678 萬 | 專業錄音、「全彩」影像（8bit × 3 色板） |

量化必然產生**量化誤差**：位元深度越低誤差越大——聽起來是雜訊，看起來是色帶（banding，天空漸層出現一圈圈色階）。

### 3.2 算一算：未壓縮媒體有多大？

未壓縮影像的理論資料量：

```text
寬 × 高 × 通道數 × 每通道位元數 ÷ 8
```

三個必算範例：

```text
一張 4000×3000 全彩照片：4000 × 3000 × 3 bytes ≈ 34.3 MB
一分鐘 CD 音質立體聲：44100 × 2 bytes × 2 聲道 × 60 秒 ≈ 20.2 MB
一分鐘 1080p30 未壓縮視訊：1920 × 1080 × 3 × 30 × 60 ≈ 11.2 GB
```

最後一個數字值得盯著看三秒：未壓縮一分鐘 Full HD 要 11 GB，但手機裡一分鐘影片只有 60～150 MB——差距約一百倍，就是壓縮技術的功勞（模組 D 拆解它）。

理論資料量不等於磁碟上的檔案大小——實際檔案還受檔案標頭、metadata 與壓縮方式影響。公式的價值不在背誦，而在**檢查結果是否合理**。

> 單位提醒：1 byte = 8 bits。檔案大小用 bytes（MB），網路速度用 bits（Mbps）。「100 Mbps 的網路」每秒實際只能傳約 12.5 MB。

### 3.3 編碼與檔案格式

| 格式 | 類型 | 壓縮 | 一句話本質 |
|---|---|---|---|
| BMP | 影像 | 無壓縮 | 像素值直接攤平，巨大但單純 |
| PNG | 影像 | 無損 | 像 zip 一樣壓縮像素，解開後一模一樣；支援透明 |
| JPEG | 影像 | 有損 | 丟掉人眼不敏感的細節換 10 倍壓縮；反覆存檔會越來越糊 |
| GIF | 影像 | 無損但限 256 色 | 靠「只能用 256 色」變小；支援簡單動畫 |
| WAV | 音訊 | 通常無壓縮 | 取樣值直接存 |
| MP3 / AAC | 音訊 | 有損 | 利用心理聲學丟掉你聽不到的成分 |
| MP4 | 視訊容器 | — | 是「容器」：視訊軌（H.264 等）與音訊軌（AAC）各自編碼 |

**無損 vs 有損**是本章最重要的分類。實務判斷：**編輯過程用無損，最終發布用有損**——每次有損存檔都再丟一次資訊。

**魔術數字（magic number）**：每種格式開頭幾個位元組是檔案的身分證。PNG 開頭是 `89 50 4E 47`，JPEG 是 `FF D8 FF`。把 .png 改名成 .jpg 不會改變檔案本質：

```python
with open("photo.png", "rb") as f:
    header = f.read(8)
print(header.hex())   # 89504e470d0a1a0a
```

### 3.4 實作：親手數位化一個聲音

不需要麥克風，用 NumPy 從零合成聲波，「聽見」取樣率與位元深度的影響（此實驗同時是模組 C 的先修）：

```python
"""取樣與量化實驗"""
import numpy as np
import wave

def make_tone(freq=440, seconds=2.0, sample_rate=44100, bit_depth=16):
    """合成正弦波並存成 WAV 檔"""
    # 取樣：在時間軸上每 1/sample_rate 秒取一點
    t = np.linspace(0, seconds, int(sample_rate * seconds), endpoint=False)
    signal = np.sin(2 * np.pi * freq * t)          # 值域 -1.0 ~ 1.0

    # 量化：把 -1.0~1.0 對應到整數階
    levels = 2 ** (bit_depth - 1) - 1              # 16bit → 32767 階
    quantized = (signal * levels).astype(np.int16)

    filename = f"tone_{freq}Hz_{sample_rate}sr_{bit_depth}bit.wav"
    with wave.open(filename, "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sample_rate)
        w.writeframes(quantized.tobytes())
    return filename

print(make_tone())
```

**破壞性實驗一（聽見 Nyquist）**：對 440 Hz 的音，用 44100 / 8000 / 1000 / 500 Hz 取樣率各生成一次。440 Hz 依 Nyquist 需要至少 880 Hz 取樣率——`sample_rate=500` 時你聽到的不是 440 Hz，而是一個錯誤的更低頻率：混疊發生了。

**破壞性實驗二（聽見量化誤差）**：把 16 bit 訊號劣化到 8 / 4 / 2 bit（`(q >> shift) << shift`），4 bit 以下會聽到明顯的「沙沙」雜訊——那就是量化誤差的聲音。

### 對應教材

- [W02｜數位影像與像素](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W02_數位影像與像素.md)
- [影像基礎 CPU 實驗](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/labs/w02_image_basics.py)、[Colab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/colab/W02_Image_Basics.ipynb)
- [media/image 數位影像教材](https://github.com/willismax/MediaSystem-Python-Course/tree/main/media/image)

### 基礎練習

1. 讀取同一張圖片的寬、高、模式與檔案大小，另存成 PNG 與 JPEG，比較檔案大小與畫面差異，說明「像素尺寸不變」為什麼不代表「檔案大小不變」。
2. 完成兩個破壞性實驗，各附 100 字聽感紀錄。
3. 你的手機相機是 5000 萬像素：一張未壓縮全彩照片多大？實拍檔案約 4 MB，壓縮比是多少？

### 延伸挑戰

- 合成 C 大三和弦（261.63、329.63、392.00 Hz）。三個 sin 相加後值域變成 ±3，直接量化會削波（clipping）——先正規化再量化。
- 寫一支 `file_detective.py`：讀取檔案前 12 bytes 比對魔術數字，識破「偽裝副檔名」的檔案。

### 檢核題

- 取樣與量化各決定了什麼？各自的失真長什麼樣（看的、聽的各一例）？
- CD 取樣率為什麼是 44,100 Hz 而不是 20,000 Hz？

---

## 第 4 章｜數位影像：像素、色彩與矩陣運算

### 核心問題

一張圖片在電腦裡是什麼？「調亮」「濾鏡」在數學上是什麼操作？

### 4.1 影像的解剖學

點陣圖影像是像素的矩形網格。「解析度 1920×1080」表示橫向 1920 格、縱向 1080 格。每個像素記錄顏色值：

- **灰階**：每像素 1 個數字（0=黑，255=白）。
- **RGB**：每像素 3 個數字（紅、綠、藍各 0–255）。
- **RGBA**：再加 1 個 Alpha（透明度）。

所以一張 RGB 影像在程式裡是一個**高 × 寬 × 3** 的三維陣列。本章要建立的心智模型：

> 所有影像處理，本質上都是對這個陣列的數學運算。調亮＝整個陣列加一個數；對比＝乘一個數；濾鏡＝對鄰近像素加權平均；去背＝把某些位置的 Alpha 設為 0。

兩個新手陷阱：

- **座標原點在左上角**，y 軸向下——與數學課相反。
- **螢幕用加法混色**（紅+綠=黃，三色全開=白），與顏料的減法混色（CMYK，印刷用）相反。

**HSV 色彩模型**：RGB 適合機器，HSV 適合人——H 色相（什麼顏色）、S 飽和度（多濃）、V 明度（多亮）。「把照片調鮮豔」在 RGB 裡難描述，在 HSV 裡就是「S 調高」。許多濾鏡的實作是：RGB → HSV → 調整 → 轉回 RGB。

### 4.2 Pillow 核心操作

```python
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

img = Image.open("photo.jpg")
print(img.size, img.mode)              # (寬, 高), 'RGB'

small = img.resize((800, 600))         # 強制縮放（可能變形）
img.thumbnail((800, 800))              # 等比縮放（就地修改，不放大）
crop = img.crop((100, 50, 500, 350))   # 裁切 (左, 上, 右, 下)
rot = img.rotate(90, expand=True)      # 旋轉（expand 避免裁角）
gray = img.convert("L")                # 轉灰階

bright = ImageEnhance.Brightness(img).enhance(1.3)
blur = img.filter(ImageFilter.GaussianBlur(5))

img.save("out.jpg", quality=85)        # JPEG 可指定品質
```

繪圖與文字（中文字型是高頻卡關點——Windows 用 `C:/Windows/Fonts/msjh.ttc`，macOS 用 `PingFang.ttc`，給絕對路徑最穩）：

```python
draw = ImageDraw.Draw(img)
draw.rectangle([50, 50, 300, 120], fill=(0, 0, 0, 180))
font = ImageFont.truetype("msjh.ttc", 48)
draw.text((60, 60), "迎新晚會", font=font, fill="white")
```

### 4.3 NumPy 視角：影像就是矩陣

Pillow 與 NumPy 無縫互轉，而 NumPy 把「逐像素迴圈」變成「一行陣列運算」，速度差距可達百倍：

```python
import numpy as np
from PIL import Image

arr = np.array(Image.open("photo.jpg"))   # shape: (高, 寬, 3), dtype: uint8

# 調亮 40 —— 注意 uint8 溢位！
brighter = np.clip(arr.astype(np.int16) + 40, 0, 255).astype(np.uint8)

negative = 255 - arr                       # 負片
gray = (0.299*arr[:,:,0] + 0.587*arr[:,:,1] + 0.114*arr[:,:,2]).astype(np.uint8)
```

**uint8 溢位是本章最重要的陷阱**：8 位元無號整數超過 255 會「繞回」從 0 重算（200+100=44），亮部變成詭異暗色。標準解法：先轉大型別運算 → `np.clip` 裁回 0–255 → 轉回 `uint8`。**AI 生成的影像程式碼經常忘記這件事**——三道防線的重點檢查項。

灰階公式的 0.299/0.587/0.114 不是隨便定的：人眼對綠色最敏感，所以綠色權重最高。

第 1 章的漸層程式，NumPy 版只要四行：

```python
x = np.linspace(0, 1, 800)
grad = np.zeros((400, 800, 3), dtype=np.uint8)
grad[:, :, 0] = (255 * x)          # 廣播到每一列
grad[:, :, 2] = (255 * (1 - x))
Image.fromarray(grad).save("gradient_fast.png")
```

親自計時比較兩版——「向量化」的威力在處理視訊（每秒 30 張影像）時是生死攸關。

### 4.4 實作：活動海報批次生成器

情境：給一張底圖＋一份 CSV 活動清單，自動生成全部海報。先寫虛擬碼（**會拆解的人指揮 AI，不會拆解的人被 AI 的輸出牽著走**）：

```python
# 1. 用 csv 模組讀入 events.csv → list of dict
# 2. 對每一筆活動：
#    a. 開啟 template.jpg，轉成 RGBA
#    b. 在下方 1/3 疊一條半透明黑色色帶
#    c. 在色帶上畫標題（大字）、日期＋地點（小字）
#    d. 轉回 RGB，存成 posters/海報_{title}.jpg
# 3. 印出「共生成 N 張海報」
```

把骨架與 4.2 的 API 速覽交給 AI 實作。三道防線驗收重點：半透明色帶是否真的半透明（AI 常直接畫不透明矩形）？中文字型路徑對不對？標題 30 個字會不會爆版面？

常見錯誤速查：

| 症狀 | 解法 |
|---|---|
| `cannot write mode RGBA as JPEG` | JPEG 不支援透明，存檔前 `convert("RGB")` |
| 中文變豆腐字 □□□ | 字型不含中文，改用 msjh.ttc / PingFang.ttc |
| 亮度調整後顏色詭異 | uint8 溢位，回 4.3 節 |
| 圖很大時程式很慢 | 還在用 putpixel？改 NumPy |

### 對應教材

- [W02｜數位影像與像素](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W02_數位影像與像素.md)、[labs/w02_image_basics.py](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/labs/w02_image_basics.py)

### 基礎練習

1. 完成海報生成器，繳交程式、3 張輸出海報、AI 協作紀錄。
2. 寫出 `negative()`、`brightness(delta)`、`channel_swap()` 三個 NumPy 函式，各附效果圖。
3. 用自己的話解釋灰階公式為什麼不是各 1/3。

### 延伸挑戰

- 九宮格切圖器：把正方形照片切成 9 張、順序符合 IG 排版。邊長不能被 3 整除時你怎麼處理？說明決策。
- 用 HSV 實作「只保留紅色」（《辛德勒的名單》效果）。紅色色相跨越 0°，小心處理「兩頭」。

### 檢核題

- uint8 溢位的後果是什麼？標準解法的三個步驟？
- JPEG 與 PNG 的選用時機？

---

## 第 5 章｜卷積、濾波與頻域

### 核心問題

濾鏡為什麼能找出邊緣？「模糊」「銳化」在數學上差在哪？（對應 [W03 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W03_卷積與影像處理.md)）

### 5.1 卷積：濾鏡的數學心臟

第 4 章的處理（調亮、負片）都是「一個像素自己變」；模糊、銳化、邊緣偵測需要「看鄰居」——這就是**卷積**：

> 拿一個小矩陣（**核，kernel**，常見 3×3），罩在影像每個像素上，把「核的權重 × 對應像素值」加總，作為該像素的新值。整張圖掃一遍。

二維卷積的數學表示：

$$
y(i,j)=\sum_m\sum_n x(i-m,j-n)\,k(m,n)
$$

三個經典核，三種效果：

```text
模糊（平均核）         銳化                邊緣偵測（Laplacian）
1/9 [1 1 1]          [ 0 -1  0]          [ 0  1  0]
    [1 1 1]          [-1  5 -1]          [ 1 -4  1]
    [1 1 1]          [ 0 -1  0]          [ 0  1  0]
```

- **模糊**：新值＝周圍 9 格的平均 → 差異被抹平。
- **銳化**：自己 ×5、扣掉四鄰 → 與鄰居的差異被放大。
- **邊緣**：平坦區（自己≈鄰居）輸出趨近 0（黑），邊緣處輸出大（亮）→ 只剩輪廓。

注意關係：**銳化＝原圖＋邊緣**。「美顏濾鏡」的基本款是：模糊（磨皮）後再把邊緣加回來一點（保留五官立體感）。你每天用的濾鏡，核心就是這幾個 3×3 矩陣的排列組合。

一個理解性的檢查：為什麼銳化核的元素總和是 1，而邊緣核的總和是 0？（想想「平坦區域」分別應該輸出什麼。）

用 NumPy 親手寫一次卷積（只為理解，實務用 OpenCV 的優化版）：

```python
import numpy as np

def convolve_gray(img, kernel):
    """最直白的卷積實作：雙層迴圈版（慢，但每一步看得見）"""
    h, w = img.shape
    kh, kw = kernel.shape
    pad = kh // 2
    padded = np.pad(img, pad, mode="edge")   # 邊界用複製法補
    out = np.zeros_like(img, dtype=np.float64)
    for y in range(h):
        for x in range(w):
            region = padded[y:y+kh, x:x+kw]
            out[y, x] = np.sum(region * kernel)
    return np.clip(out, 0, 255).astype(np.uint8)
```

實作時還要決定**邊界填補、輸出大小、通道處理與數值範圍**。函式庫可以完成計算，但不能替代這些選擇。

### 5.2 OpenCV 快速上手

```python
import cv2

img = cv2.imread("photo.jpg")        # 注意：讀進來是 BGR，不是 RGB！
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur  = cv2.GaussianBlur(img, (15, 15), 0)   # 核尺寸須為奇數
edges = cv2.Canny(gray, 80, 160)             # Canny 邊緣偵測（兩個閾值）
cv2.imwrite("edges.jpg", edges)
```

> **BGR 陷阱**：OpenCV 因歷史因素用 BGR 排列。直接丟給 matplotlib 顯示，藍色和紅色會互換（人臉變藍）。這是 AI 生成 OpenCV 程式碼的高頻錯誤。另外：Windows 路徑含中文時 `imread` 會**靜默回傳 None**——記得檢查 `img is None`。

`cv2.Canny` 比單一 Laplacian 核強得多，它是一條小型管線：高斯去噪 → Sobel 梯度 → 非極大值抑制 → 雙閾值滯後連接。閾值調低 → 細節多但雜訊多；調高 → 乾淨但漏邊。**參數沒有標準答案，動手調出感覺。**

### 5.3 空間域與頻域

空間域直接處理像素位置；頻域把影像拆成不同變化速度的成分。低頻對應緩慢變化（大面積明暗），高頻常包含邊緣、細節與雜訊。傅立葉轉換提供另一種觀察方式——但「高頻等於雜訊」並不成立，重要輪廓也在高頻。

這個「把訊號拆成頻率成分」的視角，在模組 C 的聲音處理（FFT/STFT）會再次出現：影像的二維卷積與聲音的一維卷積共享「局部加權」概念，但**軸的意義、邊界處理與評估方式不同**。跨媒體類比用來建立概念橋梁，實作仍應回到各媒體的工具文件。

### 5.4 實作：控制變因濾鏡比較

對同一張影像套用模糊、銳化與邊緣核。**每次只改一個卷積核**，保留輸出與觀察，說明哪些差異來自核權重、哪些可能來自邊界處理。

延伸：人臉偵測與馬賽克（詳見 [08.OpenCV-Mediapipe-DEMO](https://github.com/willismax/MediaSystem-Python-Course/tree/main/08.OpenCV-Mediapipe-DEMO)）。馬賽克的原理＝縮小再放大（最近鄰插值，故意保留方塊感）：

```python
def mosaic(region, block=12):
    h, w = region.shape[:2]
    small = cv2.resize(region, (max(1, w//block), max(1, h//block)),
                       interpolation=cv2.INTER_LINEAR)
    return cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
```

`img[y:y+h, x:x+w]` 這種 NumPy 切片可直接取出（並改寫）影像子區域——OpenCV 影像就是 NumPy 陣列，第 4 章的所有技巧在此通用。

**參數掃描實驗**（所有調參工作的原型）：固定一張照片，系統性地掃參數並記錄成表，結論用一句話寫下「最佳組合是什麼、為什麼」。

### 對應教材

- [W03｜卷積與影像處理](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W03_卷積與影像處理.md)
- [卷積 CPU 實驗](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/labs/w03_convolution.py)、[Colab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/colab/W03_Convolution.ipynb)
- [08.OpenCV-Mediapipe-DEMO](https://github.com/willismax/MediaSystem-Python-Course/tree/main/08.OpenCV-Mediapipe-DEMO)

### 基礎練習

1. 用手寫卷積函式對同一張灰階圖套用三個經典核，輸出三張結果並標註哪張是哪個核。
2. 完成控制變因濾鏡比較實驗，使用附錄 B 的實驗證據模板記錄。

### 延伸挑戰

- 素描濾鏡：灰階 → 反相 → 高斯模糊 → 顏色閃避混合（`result = gray*255/(255-blur)`，注意除零）。
- 把手寫卷積與 `cv2.filter2D` 做速度對比（同一張 1080p 灰階圖），回報倍率，再問 AI 為什麼 OpenCV 快這麼多。

### 檢核題

- 卷積的「核」是什麼？模糊核與邊緣核在權重設計上差在哪？
- BGR 陷阱會造成什麼可見症狀？

---

## 模組 A 總結與學習證據

完成本模組後，你應該手上有：

- [ ] 一張媒體拆解圖（短影音的五段管線分析）
- [ ] 影像參數實驗（PNG/JPEG 比較、資料量計算）
- [ ] 取樣／量化破壞性實驗的聽感與圖形紀錄
- [ ] 控制變因濾鏡比較（附實驗證據模板）
- [ ] 每份作業的 AI 協作紀錄

這些證據將在 W08 期中技術說明與期末專題包中再次使用——不要丟。

---

# 模組 B｜生成影像與視覺敘事（W04～W08）

> 核心問題：AI 如何從雜訊生成影像？我們如何控制它、微調它，並誠實地說明作品背後的技術選擇？

模組 A 處理的是「已經存在的媒體」；本模組開始，你可以憑文字召喚出不存在的影像。但本模組的重點不是「按下生成鍵」，而是**理解生成管線、設計可重現的實驗、建立一致的視覺敘事，並為作品負責**。模組結束時（W08 期中），你要交出可重現的提示實驗、3～6 張影像故事組與期中技術說明。

---

## 第 6 章｜擴散模型如何學習去噪

### 核心問題

AI 如何從雜訊生成圖片？（對應 [W04 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W04_擴散模型原理.md)）

### 6.1 直覺版：從雲裡看出形狀

人人都能在雲裡「看出」一隻狗——擴散模型就是一個被訓練到極致的「看雲術士」，而且你可以用文字指定它看出什麼。

主流圖像生成（Stable Diffusion、DALL·E、Midjourney 等）多基於**擴散模型（diffusion model）**：

- **訓練時（學「加噪的逆操作」）**：拿大量影像，逐步加雜訊直到變成純雜訊，讓神經網路學習每一步的「去噪」——給它一張帶噪的圖，它要估計「噪是哪些」。
- **生成時（從噪到圖）**：從一張純隨機雜訊出發，讓網路一步步去噪（常見 20～50 步）。文字提示透過注意力機制全程「引導」去噪方向。

![擴散模型去噪過程](https://hackmd.io/_uploads/Hy-fvrn-Ge.png)

*圖 6-1｜擴散生成：從 100% 雜訊出發逐步去噪；文字提示全程引導去噪方向，同提示＋同種子會得到同一張圖。*

### 6.2 原理版：前向與反向過程

前向過程把雜訊逐步加入影像，常見表示為：

$$
q(x_t\mid x_0)=\mathcal{N}\!\left(\sqrt{\bar{\alpha}_t}\,x_0,\;(1-\bar{\alpha}_t)I\right)
$$

$x_0$ 是原始資料，$x_t$ 是第 $t$ 步的帶噪資料，$\bar{\alpha}_t$ 控制保留多少原始訊號。模型（常用 U-Net 結構）在不同**時間步（timestep）**估計雜訊；生成時從雜訊開始反覆執行反向步驟。

這個式子描述加噪分布，不代表只靠公式就能完成高品質生成——工程上還有雜訊排程、取樣器、條件機制等大量設計。**不要把服務介面當成模型原理**：會按網頁按鈕不等於理解管線。

### 6.3 為什麼先做前向實驗

完整模型訓練需要大量算力，但**前向加噪可以用 NumPy 在 CPU 執行**。觀察不同時間步的影像，有助於理解時間步、雜訊排程與可辨識資訊之間的關係——這也是本課程「CPU 路徑優先」哲學的示範：先理解機制，再談算力。

### 實作：前向擴散模擬

固定原圖與隨機種子，只改變時間步或雜訊強度，排出一組漸進結果。指出從哪個階段開始，原圖的主要結構已難以辨識。

### 對應教材

- [W04｜擴散模型原理](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W04_擴散模型原理.md)
- [前向擴散 CPU 實驗](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/labs/w04_diffusion_forward.py)、[Colab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/colab/W04_Diffusion_Forward.ipynb)

### 檢核題

- 擴散模型「訓練時」與「生成時」各在做什麼？
- 為什麼固定 seed 之後，同提示、同模型會得到同一張圖？

---

## 第 7 章｜潛在空間、提示控制與可重現比較

### 核心問題

文字如何控制生成影像？如何做一個「能下結論」的生成實驗？（對應 [W05 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W05_潛在擴散與提示控制.md)）

### 7.1 潛在擴散：先壓縮再去噪

高解析度影像包含大量像素。**潛在擴散（latent diffusion）**先用編碼器（VAE）把影像壓到較小的潛在表示，在潛在空間進行去噪，再由解碼器還原影像。這能大幅降低運算量——但潛在表示不是一般圖片壓縮檔，也不能直接解讀為單一視覺概念。

文字條件通常先經過文字編碼器，再透過**交叉注意力（cross-attention）**影響去噪過程。提示只是條件的一部分；**模型版本、seed、步數、取樣器、尺寸與引導強度都會影響結果**。

### 7.2 兩個關鍵參數

- **種子（seed）**：初始雜訊的隨機數。**同提示＋同種子＋同模型＝同圖**。要微調一張滿意的圖，固定種子改提示；要多樣性，換種子。
- **引導強度（guidance scale / CFG）**：模型「多聽話」。分類器自由引導以條件與無條件預測的差值調整文字條件強度：

$$
\hat{\epsilon}=\epsilon_{uncond}+s\,(\epsilon_{cond}-\epsilon_{uncond})
$$

$s$ 太低 → 圖漂亮但沒在理你的提示；太高 → 嚴格遵循但過飽和、僵硬，可能出現視覺瑕疵。常用 5～9，**較大不保證較好**。

### 7.3 圖像提示工程

有效圖像提示的常見結構：**主體＋風格＋構圖/視角＋光線/氛圍＋品質詞**：

> `a corgi wearing a graduation cap`（主體）`, flat illustration style`（風格）`, centered composition, plain background`（構圖）`, soft pastel colors`（氛圍）

實戰經驗：

- **具體勝於華麗**：「golden retriever puppy sitting on a red skateboard」遠勝「a super amazing beautiful dog」。
- **負面提示**清單化排除不要的：`blurry, extra fingers, watermark, text`。
- **風格詞彙是巨大的槓桿**：watercolor / pixel art / isometric 3D / vintage poster——同一主體換風格詞，等於換一個畫師。
- **文字渲染是弱項**：多數模型畫不好圖中文字（尤其中文）。海報文字的正解：**AI 生成留白底圖＋Pillow 疊字**——模組 A 第 4 章的技術立刻有了新用途。

### 7.4 公平比較：生成實驗的科學

要判斷某個提示或參數是否有效，至少應固定其他主要條件。一次同時更換模型、seed、尺寸與提示，結果就難以解釋。

標準實驗設計——**四格比較，只改變一個變因**：

1. 固定提示、生成 4 個不同 seed（看多樣性）。
2. 固定 seed、掃 4 個 guidance scale（看服從度與瑕疵的權衡）。
3. 固定其他一切、A/B 兩版提示（看措辭的槓桿）。

保留提示、seed、步數與輸出，寫下觀察與限制。**若使用線上服務而無法固定完整參數，也要明確記錄這項限制**——「無法控制」本身就是重要的實驗資訊。

### 7.5 批次生成的工程習慣

呼叫生成 API 時的三個標配（AI 起草的 API 程式常漏掉後兩個）：

```python
import os, requests

API_KEY = os.environ["IMAGE_API_KEY"]     # 金鑰走環境變數，絕不寫死、絕不 commit
r = requests.post(ENDPOINT, json=payload,
                  headers={"Authorization": f"Bearer {API_KEY}"},
                  timeout=120)             # 沒設 timeout 的請求是潛在的永久卡死
r.raise_for_status()                       # 非 2xx 及早報錯
```

批次生產線再加兩個機制——**快取**（同提示不重複扣費：用提示的雜湊值當快取檔名）與**節流**（`time.sleep` 控制請求頻率，避免觸發速率限制）。這兩個機制在期末專題可照搬。

### 對應教材

- [W05｜潛在擴散與提示控制](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W05_潛在擴散與提示控制.md)
- [11.AI 延伸教材](https://github.com/willismax/MediaSystem-Python-Course/tree/main/11.AI)、[09.Apps/OpenAI_Demo.ipynb](https://github.com/willismax/MediaSystem-Python-Course/blob/main/09.Apps/OpenAI_Demo.ipynb)

### 基礎練習

1. 設計一個四格比較，只改變一個變因。保留提示、seed、步數與輸出，用附錄 B 模板寫下觀察與限制。
2. 記錄一份「提示版本史」：同一目標圖的提示如何逐輪修改、每輪圖變了什麼。

### 檢核題

- 潛在擴散為什麼比像素空間擴散省算力？代價是什麼？
- 你的實驗裡有哪些變因其實無法控制？你怎麼記錄它們？

---

## 第 8 章｜LoRA、資料品質與影像一致性

### 核心問題

影像微調改變了什麼？如何讓一組影像「像同一個世界的」？（對應 [W06 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W06_LoRA與影像微調.md)）

### 8.1 微調不是「把參考圖放進提示」

微調（fine-tuning）會根據資料**更新模型參數或附加參數**。LoRA（Low-Rank Adaptation）將權重更新近似為兩個較小矩陣的乘積：

$$
\Delta W = BA
$$

當秩 $r$ 遠小於原權重維度時，需要訓練與保存的參數大幅減少。這降低了微調成本，但**不會自動解決資料偏差、授權或過擬合**。DreamBooth 等方法的核心概念相同：用少量資料讓模型學會特定主體或風格。

### 8.2 資料卡：微調前必須回答的問題

- 圖片從哪裡來，是否有使用權利？
- 主體、背景、角度與光線是否過度單一？（過擬合的溫床）
- 標註文字是否描述真正需要學習的特徵？
- 訓練與比較資料是否分開？
- 哪些輸出表示模型只是「記住」訓練圖？

**實際訓練不是理解 LoRA 的必要條件。**設備有限時，先比較預先產生的結果，練習辨識資料與參數造成的差異——這正是資料卡訓練的目的。

### 8.3 從單張到影像系列

短影音需要一組能共同工作的影像。先建立**風格規格**——角色、色彩、構圖、光線與畫面比例——再生成或處理素材。風格統一的實戰技巧：**固定風格描述字串，只替換主體**：

```python
STYLE = ("flat vector illustration, navy and coral color palette, "
         "clean composition, plain light background, no text")
prompt = f"{subject}, {STYLE}"
```

單張看起來漂亮，不代表放進時間軸後能形成一致敘事。這是模組 D 的伏筆：影像故事組是短影音的素材前身。

### 對應教材

- [W06｜LoRA 與影像微調](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W06_LoRA與影像微調.md)
- [W07｜生成影像工作室](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W07_生成影像工作室.md)

### 基礎練習

規劃一份微調資料卡，或使用既有模型完成 3～6 張影像故事組的風格規格書。

### 檢核題

- LoRA 的「低秩」省下了什麼？沒有省下什麼（哪些問題仍在）？
- 資料卡五個問題中，哪一個直接對應「過擬合」風險？

---

## 第 9 章｜影像故事組、生成倫理與技術說明

### 核心問題

如何做出一致而可信的影像系列，並說明作品背後的技術選擇？（對應 [W07](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W07_生成影像工作室.md)、[W08 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W08_期中影像展與技術答辯.md)）

### 9.1 生成影像工作室：完整工作流

1. **風格規格**：第 8 章的規格書落地——角色設定、色彩限制、構圖規則、畫面比例（為模組 D 的直式短影音預留 9:16 或 3:4）。
2. **批次生成**：提示模板＋快取＋節流（第 7 章）。
3. **生成後處理**：置中裁切統一尺寸 → 疊色帶 → Pillow 上字（中文字型路徑！）——模組 A 的海報生成器直接重用。**上週的作業是這週的函式庫。**
4. **版本與來源**：每張成品記錄提示、seed、模型版本、後製步驟，寫入素材紀錄表。

### 9.2 生成式媒體的倫理：這不是選修

本課程把倫理放在技術同一章，因為**你現在就擁有了製造以假亂真影像的能力**。三個你必須能回答的問題：

**1. 版權：生成的圖是誰的？**
各國法律仍在演變。多處司法實務傾向：純 AI 生成、無足夠人類創作參與的圖像不受著作權保護；台灣現行著作權法也以「人類精神創作」為要件。模型用受版權保護的圖訓練是否侵權，多起訴訟進行中。課程立場：作業中使用生成圖**必須標註**「AI 生成＋所用工具」；商用前必須查當下平台條款與法律現狀。

**2. 深偽：技術中性，使用不中性。**
把真人的臉合成到其未同意的影像中，在多數司法區已構成犯罪。本課程紅線：**不生成可辨識之真實人物的影像，不生成試圖以假亂真的新聞性內容。**

**3. 訓練資料：你的作品餵了誰？**
創作者的風格可被一句「in the style of ___」召喚——這公平嗎？沒有標準答案，但有兩個可操作的習慣：尊重平台的 opt-out 機制；在「致敬風格」與「冒充作者」之間自覺劃線。

交件前的倫理檢查清單：

- [ ] 成品標註了「AI 生成（工具名）＋後製：本人」？
- [ ] 提示中沒有真實人物名、在世藝術家名？
- [ ] 沒有試圖讓成品冒充攝影紀實？

### 9.3 期中技術說明：讓選擇可以被檢驗

W08 的期中影像展不只展示成品，還要**技術答辯**。作品說明至少包含：

- **控制變因實驗**：至少一組「只改一個參數」的比較與結論。
- **失敗案例**：哪些生成結果被淘汰、為什麼——失敗案例是你「有判斷力」的證據。
- **後製方式**：哪些部分是生成的、哪些是後製的。
- **素材來源**：提示、seed、模型版本、參考素材的授權。

口頭說明的檢驗標準：隨機指作品中任一張圖，你能否說出它的提示、參數與淘汰同伴？

### 對應教材

- [W07｜生成影像工作室](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W07_生成影像工作室.md)
- [W08｜期中影像展與技術答辯](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W08_期中影像展與技術答辯.md)
- [media/ethics 媒體倫理教材](https://github.com/willismax/MediaSystem-Python-Course/tree/main/media/ethics)

### 基礎練習

完成 3～6 張影像故事組：風格規格書、每張的提示/seed/版本紀錄、至少一組控制變因比較、失敗案例、倫理檢查清單。

### 延伸挑戰

- 研究平台的 image-to-image 或 inpainting 功能，把自己拍的照片轉成指定風格，附前後對照與參數紀錄。
- 立場短文 300 字：「學校設計類作業應該／不應該允許 AI 生成圖像」，至少引用本章一個事實、回應一個反方論點。

### 檢核題

- 「可重現」對生成作品來說具體指哪些紀錄？
- 課程的兩條生成紅線是什麼？為什麼「對方口頭同意」仍不足夠？

---

## 模組 B 總結與學習證據（W08 期中檢核）

- [ ] 前向擴散漸進實驗（時間步 × 可辨識度）
- [ ] 四格控制變因比較 × 至少一組（附錄 B 模板）
- [ ] 提示版本史
- [ ] 微調資料卡或風格規格書
- [ ] 3～6 張影像故事組＋完整參數紀錄
- [ ] 失敗案例集
- [ ] 倫理檢查清單
- [ ] 期中技術說明（口頭答辯準備）

W09 為期中整理與評量節點：依課程公告完成評量，把以上證據整理成資料夾——它們就是期末專題包的第一批素材。

---

# 模組 C｜數位聲音與語音（W10～W12）

> 核心問題：聲音如何變成可以運算的數字？剪輯時實際改變了什麼？語音合成如何生成，深偽又如何判讀？

模組 A 第 3 章你已經用 NumPy 合成過正弦波、聽過混疊與量化誤差——本模組把那次實驗展開成完整的聲音處理能力：波形與頻譜的判讀、剪輯的訊號原理、語音合成與辨識的管線，以及聲音深偽的證據判讀。模組結束時，你要交出頻譜觀察、聲音重製練習與合成／真實聲音比較。

---

## 第 10 章｜聲音的取樣、波形與頻譜

### 核心問題

聲音如何變成可以運算的數字？如何「看見」聲音？（對應 [W10 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W10_數位聲音與頻譜.md)）

### 10.1 從物理到數字：聲音的三層描述

| 物理層 | 感知層 | 數位層 |
|---|---|---|
| 頻率（Hz，每秒振動次數） | 音高（440 Hz＝標準 A） | 樣本序列的波動快慢 |
| 振幅（壓力變化大小) | 音量 | 樣本數值的大小 |
| 波形形狀（泛音組成） | 音色（為何鋼琴≠小提琴） | 諧波的相對強度 |

**音色**值得多說一句：鋼琴和小提琴拉同一個 A，都以 440 Hz 為**基頻**，但同時疊著 880、1320、1760 Hz……等**泛音**，兩者泛音比例不同——這就是你能分辨樂器的原因。模組 A 合成的純正弦波之所以聽起來「像電話按鍵般無機」，正是因為它沒有任何泛音。

**分貝（dB）**：人耳對音量的感知是對數的。+6 dB ≈ 振幅加倍，-∞ dB＝靜音。音訊工具的音量操作直接用 dB。

數位聲音是一串依時間排列的振幅數值。取樣率 $f_s$ 表示每秒記錄幾次，位元深度表示每次振幅可用多少離散值。要避免理想條件下的混疊，取樣率應高於訊號最高頻率的兩倍（Nyquist，模組 A 第 3 章）；實際系統還要考慮濾波器與硬體限制。

### 10.2 三種視角：波形、FFT、STFT

- **波形**（振幅 × 時間）：適合觀察時間位置、振幅與靜音。
- **FFT**（快速傅立葉轉換）：把整段訊號拆成頻率成分，適合觀察「整段包含哪些頻率」。
- **STFT**（短時傅立葉轉換）：把聲音切成短窗逐窗做 FFT，可以看見**頻率如何隨時間變化**——結果畫成圖就是**頻譜圖（spectrogram）**。

STFT 的核心權衡：**窗長較大 → 頻率解析度較細、時間定位較粗；窗長較小 → 相反**。沒有免費的午餐。

頻譜圖判讀指南（本章的觀念高峰）：

- 水平亮線＝持續的音高（基頻與泛音是一組平行線）。
- 垂直亮紋＝打擊／爆裂聲（瞬間、全頻率）。
- 人聲的「條紋族」在 100–4000 Hz；嘶聲（s、sh）是高頻雲霧。
- 純音是水平線、滑音是斜線。

### 10.3 用 librosa 看見聲音

```python
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

y, sr = librosa.load("recording.m4a", sr=22050)   # y: -1~1 的 float 陣列

# 波形圖
plt.figure(figsize=(12, 3))
librosa.display.waveshow(y, sr=sr)
plt.savefig("waveform.png", dpi=150); plt.close()

# 頻譜圖：聲音的「樂譜照片」，x=時間, y=頻率, 顏色=能量
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
plt.figure(figsize=(12, 4))
librosa.display.specshow(D, sr=sr, x_axis="time", y_axis="hz")
plt.colorbar(format="%+2.0f dB"); plt.ylim(0, 8000)
plt.savefig("spectrogram.png", dpi=150); plt.close()
```

對著自己錄音的頻譜圖，找出你說的某個字——這個練習會讓「聲音＝數據」從口號變成體感。

### 對應教材

- [W10｜數位聲音與頻譜](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W10_數位聲音與頻譜.md)
- [聲音頻譜 CPU 實驗](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/labs/w10_audio_spectrum.py)、[Colab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/colab/W10_Audio_Spectrum.ipynb)
- [media/audio 數位音訊教材](https://github.com/willismax/MediaSystem-Python-Course/tree/main/media/audio)

### 基礎練習

1. 產生或讀取兩段頻率不同的聲音，繪出波形與頻譜。改變取樣率或 STFT 參數，說明圖形差異——不要只貼結果。
2. 對三種聲音（說話、唱歌或樂器、拍手）各生成頻譜圖，用判讀指南各寫兩句觀察。

### 檢核題

- 波形、FFT、STFT 各適合回答什麼問題？
- STFT 窗長的權衡是什麼？

---

## 第 11 章｜聲音剪輯與訊號處理

### 核心問題

剪輯聲音時實際改變了什麼？（對應 [W11 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W11_聲音剪輯與訊號處理.md)）

### 11.1 每個操作都是訊號運算

裁切、淡入淡出、正規化、濾波、變速與變調都會改變數位訊號。處理順序沒有通用答案，但**應能說明每一步解決什麼問題**：

- 先裁掉無用片段可減少後續運算。
- 正規化前若存在尖峰，整段音量可能仍然偏小。
- 三個訊號相加後值域超過 ±1 → 削波（clipping）→ 先正規化再輸出。

### 11.2 pydub：音訊界的 Pillow

pydub 把音訊變成可以「切片、相加」的物件（需要 FFmpeg 處理 MP3/M4A 等格式）：

```python
from pydub import AudioSegment

audio = AudioSegment.from_file("recording.m4a")
print(len(audio))                  # 長度（毫秒）

clip = audio[5000:15000]           # 切片：第 5 秒到第 15 秒（單位毫秒！）
louder = clip + 6                  # 音量 +6 dB
combo = clip + louder              # 串接！AudioSegment + AudioSegment 是接起來
faded = combo.fade_in(2000).fade_out(3000)
mixed = clip.overlay(bgm - 12)     # 疊軌：人聲疊上調小 12dB 的背景音樂

faded.export("result.mp3", format="mp3", bitrate="192k")
```

> **多載陷阱**：`audio + 6` 是調音量、`audio + audio2` 是串接——同一個 `+` 兩種行為，取決於右邊是數字還是音訊。AI 生成程式時偶爾混用，讀碼時多看一眼。

**靜音偵測**——注意 `silence_thresh` 用「相對於整體平均音量」而非絕對值，使程式適應不同錄音（值得學起來的設計手法）：

```python
from pydub.silence import detect_nonsilent

spans = detect_nonsilent(
    audio,
    min_silence_len=800,               # 連續安靜超過 0.8 秒才算靜音段
    silence_thresh=audio.dBFS - 14)    # 比整體平均低 14dB 視為安靜
```

**正規化**：

```python
def normalize_to(audio, target_dbfs=-16.0):
    """把平均音量調到 target_dbfs"""
    return audio.apply_gain(target_dbfs - audio.dBFS)
```

一個理解性的問題：為什麼正規化要在「移除靜音之後」做？（提示：`audio.dBFS` 是平均值，靜音會拉低平均。）

### 11.3 實作：聲音重製練習（Podcast 自動剪輯器）

情境：你的錄音有大量長停頓。工具目標：**移除長靜音（保留自然短停頓）→ 整體正規化 → 加片頭片尾 → 輸出 MP3**。

```text
1. 載入錄音
2. detect_nonsilent 找出非靜音區段
3. 把各區段取出，中間用 300ms 靜音接起來（完全不留停頓會喘不過氣！）
4. 正規化到 -16 dBFS 左右
5. 片頭 fade_out + 正文 + 片尾 fade_in
6. 匯出 MP3，印出：原長度、新長度、移除秒數
```

三道防線重點：

- **想**：處理前先目測波形圖預測「會移除幾秒」，再比對程式輸出。
- **踹**：輸入一段全程沒有靜音的音檔 → 崩潰還是優雅處理？全靜音呢？
- **聽**：**用耳朵全程聽過一次輸出**——數字正確不等於聽感自然。`min_silence_len` 調太短會把呼吸剪掉，聽起來像機關槍；這個參數的手感只能用耳朵建立。

常見錯誤速查：

| 症狀 | 解法 |
|---|---|
| `Couldn't find ffmpeg` | FFmpeg 沒裝或不在 PATH（附錄 A），裝完重開終端機 |
| 輸出忽大忽小 | 對「每個區段」分別正規化了——應對「整段」正規化一次 |
| `detect_nonsilent` 什麼都沒偵測到 | 印出 `audio.dBFS` 看實際音量，調整相對閾值 |

### 11.4 變速與變調

`librosa.effects.time_stretch`（變速不變調）與 `librosa.effects.pitch_shift`（變調不變速）。為什麼變調後語速沒變？關鍵字「phase vocoder」——在 STFT 域分別處理頻率與時間，正是第 10 章頻譜視角的應用。

### 對應教材

- [W11｜聲音剪輯與訊號處理](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W11_聲音剪輯與訊號處理.md)
- [聲音剪輯 CPU 實驗](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/labs/w11_audio_edit.py)、[Colab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/colab/W11_Audio_Edit.ipynb)

### 基礎練習

1. 對同一段聲音做裁切、淡入淡出與正規化，保留處理前後波形及聆聽紀錄。
2. 完成 Podcast 剪輯器，繳交程式、前後音檔、前後波形對照圖、移除秒數統計。

### 延伸挑戰

- 自動混音 DJ：偵測兩首歌的 BPM，把第二首變速到與第一首相同再 crossfade。
- 變聲器初探：把錄音升高／降低 4 個半音，聽「花栗鼠」和「大叔」效果。

### 檢核題

- 為什麼正規化的順序（先去靜音再正規化）重要？
- 「數字正確不等於聽感自然」——舉一個本章的具體例子。

---

## 第 12 章｜語音合成、辨識與深偽風險

### 核心問題

聲音深偽如何生成，又如何判讀風險？（對應 [W12 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W12_語音合成與深偽辨識.md)）

### 12.1 語音合成（TTS）管線

老一代 TTS（拼接合成）把預錄音素黏起來，聽得出機器感；現代**神經 TTS** 直接從文字生成聲學表示再還原成波形，自然度已跨過「不仔細聽分不出」的門檻。常見管線：

```text
文字 → 文字分析 → 聲學模型 → 梅爾頻譜（中間表示）→ vocoder → 波形
```

- **梅爾頻譜（mel-spectrogram）**：依人耳感知刻度壓縮的頻譜，是常見的中間表示——第 10 章的頻譜知識直接派上用場。
- **speaker embedding**：把「說話者是誰」壓成向量，作為合成條件。
- **voice conversion**：保留語言內容、改變聲音特徵。

不同系統實作不同，**不能把這些元件視為固定配方**。入門實作（edge-tts，免金鑰）：

```python
import asyncio, edge_tts

async def speak(text, out="speech.mp3", voice="zh-TW-HsiaoChenNeural"):
    await edge_tts.Communicate(text, voice).save(out)

asyncio.run(speak("大家好，歡迎收看本週的多媒體系統課程。"))
```

選平台的試金石：中英夾雜（「我們用 Python 做 demo」）念得自然嗎？

### 12.2 語音辨識（STT）：Whisper

Whisper 開源後，高品質語音辨識變成「一行 pip install」，且**可完全在本機執行**（隱私敏感素材的首選）：

```python
import whisper

model = whisper.load_model("small")        # tiny/base/small/medium/large
result = model.transcribe("lecture.m4a", language="zh")

print(result["text"])                      # 全文
for seg in result["segments"]:             # 分段 + 時間戳：字幕的原料！
    print(f"[{seg['start']:7.2f} → {seg['end']:7.2f}] {seg['text']}")
```

工程權衡（又是三角習題）：tiny 最快但勉強可用，small 日常夠用（課程預設），large 最好但最慢。**先用 tiny 把流程跑通，再換 small/medium 出正式結果。**

中文輸出傾向簡體：可用 `initial_prompt="以下是繁體中文。"` 引導，或用 OpenCC 後處理。

**品質指標 WER（字錯誤率）**：（替換＋插入＋刪除）÷ 參考字數。親手算一次自己錄音的 WER——對「AI 輸出需要驗證」這件事，沒有比親手數錯字更深刻的體驗。這個流程與業界評測 AI 系統的方法本質相同。

### 12.3 聲音深偽：生成與判讀

語音克隆技術用幾秒鐘樣本就能合成「你」說任何話的音檔，詐騙集團已實際用它假冒家人聲音。

**判讀原則：聽起來像某人，不等於可以證明是某人。**辨識深偽時，單靠主觀聽感或單一偵測器都不夠。較可靠的做法是同時檢查多類證據，把判斷依據分成三類：

1. **可觀察訊號**：頻譜異常、呼吸與口水聲缺失、韻律過於平整、背景噪音斷裂。
2. **來源證據**：檔案來源、上傳者、metadata、原始脈絡是否可追溯。
3. **仍不確定**：明確列出無法判斷的部分——誠實的「不確定」比武斷的結論更有價值。

### 12.4 安全界線

- 只使用**自己的聲音**、取得明確同意的素材或完全合成角色。
- 不得仿冒未同意者；課程作業中**即使對方口頭同意也不做他人聲音克隆**（同意的舉證與範圍界定超出課堂能處理的程度）。
- 不得把合成內容包裝成真實錄音；生成與後製過程要留下**揭露紀錄**。
- 防詐實務：接到「家人」的緊急匯款電話——掛斷，用原號碼回撥。把這個知識帶回家，是本章的隱藏作業。

### 對應教材

- [W12｜語音合成與深偽辨識](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W12_語音合成與深偽辨識.md)
- [media/ethics 媒體倫理教材](https://github.com/willismax/MediaSystem-Python-Course/tree/main/media/ethics)

### 基礎練習

1. 用 TTS 生成同一段文字的三種聲音／語速版本，讓兩位同學盲測「哪個最自然」，回報結果。
2. 選一段合成或真實聲音，將判斷依據分成「可觀察訊號」「來源證據」「仍不確定」三類，完成比較與揭露卡。

### 延伸挑戰

- 用 Whisper 轉寫 1 分鐘自己的錄音，人工聽寫「正確答案」，手算 WER；換 tiny 模型重跑，比較 WER 與耗時。
- 完成「合成聲音＋自己聲音」的頻譜對照圖，標出你觀察到的差異。

### 檢核題

- TTS 管線中，梅爾頻譜扮演什麼角色？
- 深偽判讀的三類證據是什麼？為什麼「單一偵測器」不夠？

---

## 模組 C 總結與學習證據

- [ ] 波形與頻譜比較（不同取樣率／STFT 參數）
- [ ] 聲音重製練習（前後波形對照＋聆聽紀錄）
- [ ] 合成／真實聲音比較與揭露卡（三類證據分級）
- [ ] WER 體檢報告（延伸）

這些能力在模組 D 直接復用：旁白 TTS、字幕轉寫（Whisper）、配樂處理（pydub）都是短影音管線的組件。

---

# 模組 D｜短影音與系統整合（W13～W18）

> 核心問題：如何把腳本、素材、聲音、字幕、編碼、測試與發布紀錄，組成一個可重現的作品——一個真正的「系統」？

前三個模組給了你所有零件：影像處理與生成（A、B）、聲音處理與合成（C）。本模組把零件組成完整管線：**分鏡 → 素材包 → 合成 → 測試 → 發表 → 封存**。成品是一支 720×1280 直式短影音，但真正的交付物是**整個可重現的專題包**。

---

## 第 13 章｜影片的時間結構、編碼與容器

### 核心問題

影片如何被合成與壓縮？（對應 [W13](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W13_短影音腳本與數位影片.md)、[W15 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W15_FFmpeg與短影音合成.md)）

### 13.1 三個關鍵參數

影片是依時間顯示的畫面序列，通常還包含聲音、字幕與 metadata。

- **影格率（fps）**：每秒顯示幾格。24 fps 是電影感的由來，30 fps 一般視訊，60 fps 適合運動；低於約 12 fps 人眼開始覺得卡。
- **解析度**：每格畫面的像素尺寸。注意 4K 的像素數是 Full HD 的 **4 倍**——處理時間與檔案大小大致同倍率放大。
- **位元率（bitrate）**：每秒配置多少資料量。**同一解析度下，位元率才是畫質的真正決定者**：1080p 給 1 Mbps 糊成一團，給 8 Mbps 就相當清晰。串流平台的「自動畫質」切的就是位元率階梯。

三者關係：`檔案大小 ≈ 位元率 × 時長`。模組 A 算過：未壓縮 1080p30 約需 1.5 Gbps，實用位元率約 5–10 Mbps——**壓縮率高達 200 倍**。怎麼辦到的？

### 13.2 視訊壓縮的兩大支柱

**支柱一：幀內壓縮（intra-frame）**——每一格自己就是一張影像，用類似 JPEG 的方式壓縮（DCT 轉換 → 量化 → 熵編碼；「丟資訊」發生在量化那一步，quality 參數控制量化表的兇狠程度）。

**支柱二：幀間壓縮（inter-frame）**——視訊壓縮的殺手鐧。關鍵洞察：**相鄰影格幾乎一樣**。主播報新聞 1 秒 30 格，變的只有嘴型——何必存 30 次？編碼器把影格分成三種：

- **I-frame（關鍵格）**：完整影像，獨立可解。
- **P-frame（預測格）**：只存「和前面那格差在哪」＋物件移動向量。
- **B-frame（雙向格）**：參考前後兩格做插值，更省。

**GOP（Group of Pictures）**描述一組相關影格的安排方式。實務佐證：拖動進度條時「先糊一下才清楚」，是解碼器跳到附近 I-frame 再往後推算的痕跡；快速剪輯、雪花、紙花的畫面容易糊，因為幀間壓縮失效、位元率不夠分。

用 I/P/B 概念解釋兩件事（檢核題等級）：(a) 為什麼靜止場景的監視器錄影壓縮率特別高？(b) 為什麼剪輯軟體精確剪切時常要重新編碼？

### 13.3 編碼器與容器

- **編碼器（codec）**：壓縮演算法。H.264（最通用）、H.265/HEVC（省一半但吃算力）、VP9/AV1（開放授權）。
- **容器（container）**：打包視訊軌＋音訊軌＋字幕軌的「盒子」。MP4、MKV、MOV。

「.mp4 打不開」的真相通常是：**播放器認得盒子，但不認得裡面的編碼**。副檔名只能提示容器，不能說明內部編碼。本課程的安全牌：**MP4 容器＋H.264 視訊＋AAC 音訊**——相容性之王。

用 `ffprobe` 讀取真相：

```bash
ffprobe -v error -show_format -show_streams input.mp4
```

### 對應教材

- [W13｜短影音腳本與數位影片](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W13_短影音腳本與數位影片.md)
- [media/video 數位視訊教材](https://github.com/willismax/MediaSystem-Python-Course/tree/main/media/video)

### 基礎練習

用 `ffprobe` 讀取一支影片的容器、視訊編碼、音訊編碼、解析度、影格率、時長與位元率。轉出另一個版本，**只改一個輸出參數**，比較品質與檔案大小。

### 檢核題

- fps、解析度、位元率各決定什麼？哪一個才是「畫質的真正決定者」？
- I/P/B frame 各存什麼？

---

## 第 14 章｜從腳本、分鏡到素材包

### 核心問題

短影音如何形成可理解的時間敘事？如何建立可追溯的素材庫？（對應 [W13](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W13_短影音腳本與數位影片.md)、[W14 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W14_生成內容與素材溯源.md)）

### 14.1 15～30 秒也需要結構

先決定**觀眾要理解什麼**，再把時間分配給開場、主要訊息與收束。每個鏡頭記錄：畫面、旁白、字幕、音效、時間與轉場——避免進入剪輯後才發現資訊超出時間。

分鏡表的檢驗標準：**讓另一位同學只看分鏡與素材表，能否判斷每個鏡頭要用哪些檔案？**

規格決策先於程式：「直式 9:16 還是橫式 16:9？」「直幅照片置中裁切還是加模糊邊？」——**AI 可以替你寫程式，不能替你做產品決定。先決定，再下提示。**

### 14.2 素材包是輸入契約

素材包不只是檔案集合。每個素材至少要有：

- 唯一檔名與媒體類型。
- 來源、作者與取得日期。
- 授權或同意狀態。
- 是否由 AI 生成或修改。
- 生成工具、提示與主要參數。
- 預定用途與後製紀錄。

**來源不明的素材不應進入最終時間軸。**若授權需要標示姓名或連結，在作品說明或片尾保留。使用 repo 模板：[ASSET_LOG.csv](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/templates/ASSET_LOG.csv)、[同意紀錄 CONSENT_RECORD.md](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/templates/CONSENT_RECORD.md)。

素材溯源（provenance）不是行政作業，是系統的一部分：模組 B 的影像故事組（提示＋seed＋版本）、模組 C 的旁白（TTS 揭露）與配樂（授權），在這裡匯流成一份可檢驗的素材表。

### 對應教材

- [W14｜生成內容與素材溯源](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W14_生成內容與素材溯源.md)

### 基礎練習

完成四格或六格分鏡，建立對應素材表。交換檢查：同學只看分鏡與素材表，能否指出每個鏡頭的檔案？

### 檢核題

- 素材包的六項最低欄位是什麼？
- 為什麼「來源不明的素材不應進入最終時間軸」？

---

## 第 15 章｜短影音合成：FFmpeg 與 MoviePy

### 核心問題

如何把影像、聲音、字幕放到同一條時間軸，輸出符合規格的成品？（對應 [W15 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W15_FFmpeg與短影音合成.md)）

### 15.1 合成前先統一規格

開始合成前，先統一：畫面比例、解析度（本課程：720×1280 直式）、影格率、聲音取樣率與檔名。**格式不一致時，錯誤常在輸出階段才出現。**

混合橫直幅素材的真實難點——置中裁切的參考做法：

```python
from PIL import Image

def fit_portrait(path, out_path, target=(720, 1280)):
    """等比縮放後置中裁切到 720x1280"""
    img = Image.open(path)
    tw, th = target
    scale = max(tw / img.width, th / img.height)   # 取 max：確保鋪滿
    img = img.resize((round(img.width*scale), round(img.height*scale)))
    left, top = (img.width - tw)//2, (img.height - th)//2
    img.crop((left, top, left+tw, top+th)).save(out_path)
```

為什麼 `scale` 取 `max` 不取 `min`？動手畫個圖想清楚——面試等級的小問題。

### 15.2 兩套工具的分工

- **OpenCV**：逐格讀取與分析（`while cap.read()` 迴圈是萬用骨架——模組 A 的任何影像技術放進迴圈就升級成視訊版）。注意 `VideoWriter` 寫出的 mp4 **不含音訊**。
- **MoviePy**：剪輯成品（底層呼叫 FFmpeg）。
- **FFmpeg 命令列**：轉碼、封裝、批次處理與 `ffprobe` 檢驗。

**規則：逐格分析用 OpenCV，剪輯成品用 MoviePy，檢驗與轉碼用 FFmpeg。**

MoviePy 合成範例：

```python
from moviepy import VideoFileClip, ImageClip, AudioFileClip, \
                    TextClip, CompositeVideoClip, concatenate_videoclips

clip = VideoFileClip("clip.mp4").subclipped(2, 8)
photo = ImageClip("scene01.png", duration=4)          # 照片變 4 秒片段

txt = (TextClip(text="第一幕", font="msjh.ttc", font_size=64,
                color="white", stroke_color="black", stroke_width=2)
       .with_duration(4).with_position(("center", "bottom")))

scene = CompositeVideoClip([photo, txt])              # 疊圖層
final = concatenate_videoclips([scene, clip], method="compose")
final = final.with_audio(AudioFileClip("bgm.mp3").subclipped(0, final.duration))

final.write_videofile("output.mp4", fps=30, codec="libx264", audio_codec="aac")
```

> **版本注意（AI 知識會過期的最佳實證）**：MoviePy 2.x 改了大量 API（`subclipped`/`resized`/`with_*`，匯入不再有 `.editor`）。網路舊教學與 AI 訓練資料多為 1.x 寫法。**若 AI 給的程式報 `AttributeError` 或 `ImportError`，先查版本**（`pip show moviepy`），並在提示中明確說「我用 MoviePy 2.x」。官方文件才是真相。

### 15.3 自動上字幕：模組 C 的直接應用

把 Whisper 的分段時間戳變成字幕，是 STT＋視訊的經典整合：

```text
input.mp4 ─→ [抽出音軌] ─→ [Whisper 轉寫] ─→ segments(文字+時間戳)
                                                  │
input.mp4 ─→ [MoviePy 載入] ────┐                 ▼
                                ├──→ [逐段疊字幕] ←─ SRT 檔（順手輸出，通用格式）
                                ▼
                           output.mp4
```

![字幕機管線](https://hackmd.io/_uploads/rJGiDH3Wfx.png)

*圖 15-1｜自動上字幕機的資料流：上排是「聲音 → 文字＋時間戳」，下排是「原影片＋字幕 → 成品」；SRT 檔是順手輸出的通用格式。*

SRT 是通用字幕格式，規則簡單——產生器自己寫只要 15 行（秒數 → `HH:MM:SS,mmm` 的換算是基本功，**這 15 行不用 AI**；寫完再請 AI review 邊界情況：毫秒補零了嗎？）。

字幕燒錄的驗收清單：中文字型路徑正確？亮背景上看得清楚（描邊或半透明底）？過長句子會爆版面（需斷行）？時間戳對得上（抽查 3 個點）？

### 15.4 輸出參數實驗

同一支影片用三組參數輸出，記錄檔案大小、轉檔時間與目測畫質：

| preset | bitrate | 檔案大小 | 轉檔時間 | 目測畫質 |
|---|---|---|---|---|
| ultrafast | 預設 | ? | ? | ? |
| medium | 預設 | ? | ? | ? |
| medium | 2M | ? | ? | ? |

結論一句話：速度、大小、畫質，你犧牲了誰？——**壓縮率沒有免費的午餐**，這個三角習題每個多媒體工程師天天在解。

開發習慣：**測試輸出一律低解析度＋短片段，最後才出正式版**（快速迭代迴圈）。轉檔極慢是正常的，視訊是重運算。

### 對應教材

- [W15｜FFmpeg 與短影音合成](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W15_FFmpeg與短影音合成.md)
- [短影音合成 CPU 實驗](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/labs/w15_make_short.py)、[Colab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/colab/W15_Make_Short.ipynb)

### 基礎練習

1. 依分鏡與素材包完成 720×1280 粗剪版（rough cut）。
2. 完成輸出參數實驗表與一句話結論。

### 延伸挑戰

- Ken Burns 效果：每張照片在 3 秒內從 100% 緩慢放大到 110%（MoviePy 的 `resized` 接受 `lambda t: ...` 函式——動畫的核心模式）。
- 全自動報告影片產生器「大滿貫」：講稿 txt → TTS 念稿 → 生成插圖輪播 → 自動上字幕 → 成品。這條管線就是市面上「AI 影片工具」的基本架構，而你手上已有全部零件。

### 檢核題

- OpenCV、MoviePy、FFmpeg 三者的分工原則？
- 為什麼「測試輸出用低解析度短片段」是重要的工程習慣？

---

## 第 16 章｜系統整合、測試與錯誤處理

### 核心問題

作品是否已經成為一個系統？（對應 [W16 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W16_進度小報告與系統測試.md)）

### 16.1 三類測試

1. **正常路徑**：所有必要素材存在，能產生符合規格的成品。
2. **邊界條件**：極短素材、不同尺寸、空白字幕或接近上限的檔案仍能合理處理。
3. **錯誤路徑**：檔案遺失、格式不支援或參數錯誤時，系統提供**可理解的訊息**，而不是只留下失敗輸出。

測試不只看程式有沒有結束。還要檢查：影像是否變形、字幕是否超出畫面、聲音是否削波、同步是否偏移、輸出能否在常見播放器開啟。

![系統化除錯](https://hackmd.io/_uploads/SJ-DdHnbMl.png)

*圖 16-2｜系統化除錯：重現 → 定位 → 假設 → 驗證 → 修正，每一步都留下紀錄——與 AI 協作除錯時，這份紀錄就是最好的提示。*

每個測試案例記錄四件事：**輸入、預期結果、實際結果、修正狀態。**

### 16.2 多媒體輸出無法 `==` 比對，怎麼測？

多媒體程式的輸出（影像、音檔、影片）每次可能有微小差異，不能直接 `assert output == expected`。三個策略：

1. **測性質，不測內容**（最常用）：輸出檔案存在？解析度是 720×1280？時長在預期範圍？含音訊軌？
2. **測統計特徵**：輸出影像的平均亮度在合理區間？音訊的 dBFS 接近目標值？
3. **黃金樣本（golden file）**：固定輸入與參數，比對輸出與已驗證過的樣本的相似度（允許誤差）。

pytest 延伸教材見 [07.Pytest-DEMO](https://github.com/willismax/MediaSystem-Python-Course/tree/main/07.Pytest-DEMO)。

### 16.3 管線整合與風險清單

W16 的進度小報告要求三樣東西：

- **Rough cut**：能從頭播到尾的粗剪版（醜沒關係，要完整）。
- **架構圖**：資料從輸入到輸出經過哪些步驟、每步的工具與參數。
- **風險清單**：哪些步驟可能失敗、失敗時怎麼辦、哪些還沒測。

MVP 心法：**使用者能從「輸入」走到「產出」的最短路徑，每一步都真的在動——即使每一步都很醜。**先走通最短路徑，再迭代加深。

![MVP 縱切片](https://hackmd.io/_uploads/SJRNur2WMx.png)

*圖 16-1｜MVP 是縱切片：先讓輸入到產出的整條路走通，再逐段加深——不是把某一段做到完美才前進。*「最後一刻還在加功能」是專案的第一死因；發表前一週應**功能凍結**，只修 bug、寫文件。

### 對應教材

- [W16｜進度小報告與系統測試](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W16_進度小報告與系統測試.md)
- [07.Pytest-DEMO](https://github.com/willismax/MediaSystem-Python-Course/tree/main/07.Pytest-DEMO)

### 基礎練習

為作品列出一個正常案例、一個邊界案例與一個錯誤案例。每個案例記錄輸入、預期結果、實際結果與修正狀態。

### 檢核題

- 三類測試各回答什麼問題？
- 「測性質不測內容」適合多媒體輸出的原因是什麼？

---

## 第 17 章｜發表、封存與可重現的專題包

### 核心問題

如何讓技術說明可以被檢驗？如何把成果整理成可重現的專題？（對應 [W17](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W17_期末成果發表A.md)、[W18 週講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W18_期末成果發表B與封存.md)）

### 17.1 發表：不只展示成品

工程界的殘酷真相：沒有人會讀你的程式碼來理解你做了什麼——他們讀你的 README、看你的 demo、聽你的三分鐘。發表時要說明：**問題、輸入、處理管線、關鍵參數、比較證據、失敗案例、授權與限制。**

口頭答辯的檢驗標準與期中相同：隨機指作品任一部分，你能否說出它的來源、參數與技術選擇？

### 17.2 專題包最低內容

```text
project/
├─ README.md
├─ AI_USAGE.md
├─ assets/            ← 素材（含 asset-log 對應）
├─ src/ 或 notebooks/
├─ outputs/
├─ tests/ 或 test-results/
└─ asset-log.csv
```

README 至少包含：環境、安裝、執行方式、輸入、參數、輸出、限制與來源。程式無法公開時，也要保留足以重現流程的步驟與參數。

### 17.3 發布前檢查

- [ ] 影像、聲音與影片是否取得必要授權或同意。
- [ ] 是否含有可識別個資、位置或未同意者。
- [ ] 生成與合成內容是否清楚揭露。
- [ ] 音量、字幕、畫面比例與播放相容性是否通過檢查。
- [ ] 專題包能否在另一個環境依 README 重跑。

### 17.4 封存與重現測試

最後一個練習，也是全書的驗收：**把專題複製到新的資料夾或環境，只依 README 執行一次。**記錄無法重現的步驟，補齊缺少的檔案、套件版本與參數。

能被別人重跑的作品，才是系統；只能在你電腦上跑的作品，是奇蹟。

### 對應教材

- [W17｜期末成果發表 A](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W17_期末成果發表A.md)、[W18｜發表 B 與封存](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W18_期末成果發表B與封存.md)
- [成果評量規準 FINAL_RUBRIC.md](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/templates/FINAL_RUBRIC.md)

### 檢核題

- 專題包的七個最低組成是什麼？
- 「重現測試」怎麼做？它驗證了系統的哪個性質？

---

## 模組 D 總結與學習證據（期末檢核）

- [ ] 15～30 秒分鏡與腳本（W13）
- [ ] 專題素材包＋素材紀錄表＋同意紀錄（W14）
- [ ] 720×1280 粗剪版＋輸出參數實驗（W15）
- [ ] 架構圖、三類測試案例、風險清單（W16）
- [ ] 完整作品＋口頭答辯（W17）
- [ ] 可重現專題包：README、AI_USAGE、asset-log、重現測試紀錄（W18）

---

# 附錄

## 附錄 A｜開發環境與工具

### 基本環境

1. **Python 3.11+**：Windows 安裝時務必勾選「Add Python to PATH」；macOS 建議 `brew install python`。
2. **VS Code**＋Python 擴充套件。
3. **Git**：`git config --global user.name / user.email` 設定身分。
4. **虛擬環境**（每個專案獨立的工具箱）：

```bash
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install pillow numpy matplotlib
```

也可以用更現代的 `uv`（速度更快、環境與依賴管理合一）。

5. **FFmpeg**（模組 C、D 必備）：Windows `winget install ffmpeg`，macOS `brew install ffmpeg`。裝完**重開終端機**。

### 各模組套件速查

| 模組 | 套件 |
|---|---|
| A | `pillow numpy matplotlib opencv-python` |
| B | `requests pillow`（+ 各平台生成 API 或本機 Stable Diffusion） |
| C | `pydub librosa soundfile openai-whisper edge-tts` |
| D | `moviepy opencv-python`（+ FFmpeg/ffprobe） |

### 工具與用途

| 工具 | 適合處理的工作 |
|---|---|
| Pillow | 影像讀寫、尺寸、色彩與基本轉換 |
| NumPy | 陣列、卷積、取樣與數值實驗 |
| OpenCV | 影像與影片處理、濾鏡及視覺分析 |
| librosa | 聲音載入、頻譜、STFT 與音訊特徵 |
| pydub | 聲音剪輯、串接、音量與格式轉換 |
| MoviePy | 以 Python 組合畫面、聲音與字幕 |
| FFmpeg／ffprobe | 轉碼、封裝、媒體資訊與批次處理 |
| Whisper | 語音辨識與字幕時間戳 |
| Jupyter／Colab | 保存程式、說明、參數、圖表與結果 |
| Git | 保存版本與比較修改；不提交金鑰與敏感素材 |

### 常見卡關急救

| 症狀 | 解法 |
|---|---|
| `python` 不是內部或外部命令 | 安裝時沒勾 Add to PATH，重跑安裝器選 Modify 補勾 |
| PowerShell 無法載入指令碼 | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| `ModuleNotFoundError` | 忘了啟用虛擬環境，或裝錯環境 |
| `Couldn't find ffmpeg` | 沒裝或不在 PATH；裝完重開終端機 |
| matplotlib 圖空白 | 一律 `plt.savefig()` 存檔再開圖，最穩 |

卡關超過 15 分鐘的標準流程：**完整複製錯誤訊息 → 貼給 AI → 附上「我用 Windows/macOS、Python 版本 X」**。描述環境是新手最常漏掉、卻最關鍵的資訊。

### 金鑰安全鐵律

金鑰不寫進程式碼、不 commit 進 Git，一律放環境變數或 `.env`（並把 `.env` 加入 `.gitignore`）。歷史上無數金鑰是在「不小心 push 上 GitHub」時洩漏的——有自動爬蟲在掃。

---

## 附錄 B｜實驗證據模板

每一個控制變因實驗都用這個模板記錄：

```markdown
## 問題
我要比較什麼？

## 固定條件
輸入、環境、模型或工具版本、未改變的參數。

## 改變的變因
這次只改哪一項？

## 結果
輸出、數值、圖表或聆聽／觀看紀錄。

## 解釋
結果支持什麼判斷？還有哪些其他可能原因？

## 限制
哪些條件無法控制、哪些結果尚不能推論？

## 來源與 AI 協作
素材、引用、提示、採用內容與驗證方式。
```

---

## 附錄 C｜AI 協作提示範本

### CGRF 起手式

```text
【背景】我是 Python 初學者，環境是 <OS> + Python <版本>，使用 <函式庫>。
【目標】請寫一個程式：<輸入> → <處理> → <輸出>。
【限制】<邊界條件、不要什麼、錯誤處理要求>。
【格式】請逐行加中文註解，先解釋思路再給程式碼。
```

### 解釋程式碼

```text
請先用一句話總結這段程式在做什麼，再逐行解釋，最後指出一個潛在問題。
<貼上程式碼>
```

### 除錯

```text
執行後出現這個錯誤：
<完整 traceback>
我的環境是 <OS>、Python <版本>、<函式庫> <版本>。我已嘗試 <做過的事>。
```

### Code review

```text
請 code review 這段程式：有什麼 bug 風險、命名問題、可讀性問題？
特別檢查：uint8 溢位、BGR/RGB 順序、timeout 與錯誤處理、邊界條件。
```

### AI 協作報告固定格式

```markdown
## AI 協作報告
1. 工具：我使用的 AI 工具與用途分工
2. 三個最有價值的提示：原文＋為什麼有效
3. 一次 AI 的錯誤：它錯在哪、我怎麼發現的（三道防線哪一道抓到的）
4. 比例自估：AI 起草 vs 我撰寫 vs 我修改，各約多少
5. 反思：重來一次，我會怎麼改變與 AI 的分工
```

---

## 附錄 D｜週次 × 章節 × 教材對照表

| 週次 | 模組 | 本書章節 | 核心問題 | repo 教材 |
|---:|---|---|---|---|
| W01 | A | 第 1、2 章 | 什麼才算一個多媒體系統？ | [W01 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W01_課程啟動與多媒體系統.md) |
| W02 | A | 第 3、4 章 | 一張圖片在電腦裡是什麼？ | [W02 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W02_數位影像與像素.md)、[lab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/labs/w02_image_basics.py)、[Colab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/colab/W02_Image_Basics.ipynb) |
| W03 | A | 第 5 章 | 濾鏡為什麼能找出邊緣？ | [W03 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W03_卷積與影像處理.md)、[lab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/labs/w03_convolution.py)、[Colab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/colab/W03_Convolution.ipynb) |
| W04 | B | 第 6 章 | AI 如何從雜訊生成圖片？ | [W04 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W04_擴散模型原理.md)、[lab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/labs/w04_diffusion_forward.py)、[Colab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/colab/W04_Diffusion_Forward.ipynb) |
| W05 | B | 第 7 章 | 文字如何控制生成影像？ | [W05 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W05_潛在擴散與提示控制.md) |
| W06 | B | 第 8 章 | 影像微調改變了什麼？ | [W06 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W06_LoRA與影像微調.md) |
| W07 | B | 第 9 章 | 如何做出一致而可信的影像系列？ | [W07 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W07_生成影像工作室.md) |
| W08 | B | 第 9 章 | 如何說明作品背後的技術選擇？ | [W08 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W08_期中影像展與技術答辯.md) |
| W09 | 節點 | — | 期中整理與評量 | 依課程公告 |
| W10 | C | 第 10 章 | 聲音如何變成可以運算的數字？ | [W10 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W10_數位聲音與頻譜.md)、[lab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/labs/w10_audio_spectrum.py)、[Colab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/colab/W10_Audio_Spectrum.ipynb) |
| W11 | C | 第 11 章 | 剪輯聲音時實際改變了什麼？ | [W11 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W11_聲音剪輯與訊號處理.md)、[lab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/labs/w11_audio_edit.py)、[Colab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/colab/W11_Audio_Edit.ipynb) |
| W12 | C | 第 12 章 | 聲音深偽如何生成與判讀？ | [W12 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W12_語音合成與深偽辨識.md) |
| W13 | D | 第 13、14 章 | 短影音如何形成時間敘事？ | [W13 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W13_短影音腳本與數位影片.md) |
| W14 | D | 第 14 章 | 如何建立可追溯的素材庫？ | [W14 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W14_生成內容與素材溯源.md) |
| W15 | D | 第 15 章 | 影片如何被合成與壓縮？ | [W15 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W15_FFmpeg與短影音合成.md)、[lab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/labs/w15_make_short.py)、[Colab](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/colab/W15_Make_Short.ipynb) |
| W16 | D | 第 16 章 | 作品是否已經成為一個系統？ | [W16 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W16_進度小報告與系統測試.md) |
| W17 | D | 第 17 章 | 如何讓技術說明可以被檢驗？ | [W17 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W17_期末成果發表A.md) |
| W18 | D | 第 17 章 | 如何把成果整理成可重現的專題？ | [W18 講義](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/weeks/W18_期末成果發表B與封存.md) |

## 附錄 E｜主要來源與邊界說明

- 課程論文與官方文件整理於 [references.md](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/references.md)。
- 指定用書《多媒體系統：AI 時代的實作之旅》各章與 V2 的接入方式，見 [指定用書整合表](https://github.com/willismax/MediaSystem-Python-Course/blob/main/course-115-v2/TEXTBOOK_INTEGRATION_MAP.md)。
- **內容邊界**：影像公式不能直接替代音訊或影片公式。影像的二維卷積與聲音的一維卷積共享局部加權概念，但軸的意義、邊界處理與評估方式不同——跨媒體類比用來建立概念橋梁，實作仍應回到各媒體講義與工具文件。
- 模型服務、免費額度、模型名稱與 GPU 可用性可能變動。本書保留原理、參數與驗證方法；使用服務前應查看官方文件。
