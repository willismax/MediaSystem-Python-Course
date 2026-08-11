"""W03：使用 NumPy 實作灰階 3×3 卷積。"""

from pathlib import Path
import numpy as np
from PIL import Image


KERNELS = {
    "blur": np.ones((3, 3), dtype=np.float32) / 9,
    "sharpen": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32),
    "edge": np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], np.float32),
}


def convolve_gray(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """以 edge padding 計算 3×3 卷積，輸出截斷到 0–255。"""
    padded = np.pad(image.astype(np.float32), 1, mode="edge")
    output = np.zeros_like(image, dtype=np.float32)
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            window = padded[row : row + 3, col : col + 3]
            output[row, col] = np.sum(window * kernel)
    return np.clip(output, 0, 255).astype(np.uint8)


def main() -> None:
    source = Path("input.jpg")
    output_dir = Path("output_w03")
    output_dir.mkdir(exist_ok=True)
    if not source.exists():
        raise FileNotFoundError("請把測試圖片命名為 input.jpg。")

    # 縮小可讓純 Python 迴圈在一般 CPU 上快速完成。
    image = Image.open(source).convert("L")
    image.thumbnail((640, 640))
    gray = np.asarray(image)
    for name, kernel in KERNELS.items():
        result = convolve_gray(gray, kernel)
        Image.fromarray(result).save(output_dir / f"{name}.png")
        print(name, kernel.tolist())


if __name__ == "__main__":
    main()

