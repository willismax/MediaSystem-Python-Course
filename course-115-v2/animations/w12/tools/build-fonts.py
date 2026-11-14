#!/usr/bin/env python3
"""把三支動畫用到的中文字，從 Noto Sans CJK TC 裁成小型 woff2（500 / 900 兩個字重）。

改過任何 .html 的文字後重跑一次：
    python3 tools/build-fonts.py
需要：pip install fonttools brotli，以及系統字型 fonts-noto-cjk
（Ubuntu: sudo apt install fonts-noto-cjk fonts-noto-cjk-extra）。
"""
import glob
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CLIPS = sorted(d for d in glob.glob(os.path.join(ROOT, "w12-*")) if os.path.isdir(d))

SOURCES = {
    "500": ["/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc"],
    "900": ["/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc"],
}
TC_INDEX = 3  # 0 JP, 1 KR, 2 SC, 3 TC, 4 HK

chars = set()
files = []
for d in CLIPS:
    files += glob.glob(os.path.join(d, "*.html")) + glob.glob(os.path.join(d, "assets", "*.js"))
for path in files:
    with open(path, encoding="utf-8") as f:
        chars.update(f.read())
# 基本 ASCII 與常用全形標點一律收錄，避免臨時改字時缺字
chars.update(chr(c) for c in range(0x20, 0x7F))
chars.update("，。、：；！？（）「」『』／＋－＝×÷→←↑↓≈≤≥±−…・·％～✓✗①②③④⑤")
text = "".join(sorted(c for c in chars if c.isprintable()))

import shutil
tmp = os.path.join(HERE, ".fonts-tmp")
os.makedirs(tmp, exist_ok=True)
for weight, cands in SOURCES.items():
    src = next((p for p in cands if os.path.exists(p)), None)
    if not src:
        sys.exit(f"找不到 {cands}，請先安裝 fonts-noto-cjk")
    name = f"NotoSansTC-{weight}-subset.woff2"
    out = os.path.join(tmp, name)
    subprocess.run(
        [
            "pyftsubset", src, f"--font-number={TC_INDEX}", f"--text={text}",
            "--flavor=woff2", "--layout-features=*", f"--output-file={out}",
        ],
        check=True,
    )
    for d in CLIPS:  # 三個專案各放一份（HyperFrames 的資產路徑必須在專案內的 assets/）
        os.makedirs(os.path.join(d, "assets", "fonts"), exist_ok=True)
        shutil.copy(out, os.path.join(d, "assets", "fonts", name))
    print(f"{name}  {os.path.getsize(out) // 1024} KB -> {len(CLIPS)} 個專案")
shutil.rmtree(tmp)
print(f"{len(text)} 個字元")
