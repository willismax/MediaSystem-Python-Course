"""W04：依 DDPM 的封閉形式模擬前向加噪；不需 GPU 或模型權重。"""

from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw


def to_uint8(array: np.ndarray) -> np.ndarray:
    return np.clip(array * 255, 0, 255).astype(np.uint8)


def main() -> None:
    source = Path("input.jpg")
    if not source.exists():
        raise FileNotFoundError("請把測試圖片命名為 input.jpg。")

    image = Image.open(source).convert("RGB").resize((320, 320))
    x0 = np.asarray(image, dtype=np.float32) / 255.0
    rng = np.random.default_rng(42)
    epsilon = rng.normal(0, 1, x0.shape).astype(np.float32)
    alpha_bars = (1.0, 0.95, 0.70, 0.30, 0.05)
    panels: list[Image.Image] = []

    for alpha_bar in alpha_bars:
        xt = np.sqrt(alpha_bar) * x0 + np.sqrt(1 - alpha_bar) * epsilon
        panel = Image.fromarray(to_uint8(xt))
        canvas = Image.new("RGB", (320, 350), "white")
        canvas.paste(panel, (0, 30))
        ImageDraw.Draw(canvas).text((8, 8), f"alpha_bar={alpha_bar:.2f}", fill="black")
        panels.append(canvas)

    montage = Image.new("RGB", (320 * len(panels), 350), "white")
    for index, panel in enumerate(panels):
        montage.paste(panel, (index * 320, 0))
    montage.save("w04_forward_diffusion.png")
    print("已輸出 w04_forward_diffusion.png；固定 seed=42。")


if __name__ == "__main__":
    main()

