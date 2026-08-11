"""W02：觀察像素、格式與 JPEG 品質。CPU 可執行。"""

from pathlib import Path
from PIL import Image


def main() -> None:
    source = Path("input.jpg")
    output = Path("output_w02")
    output.mkdir(exist_ok=True)
    if not source.exists():
        raise FileNotFoundError("請把測試圖片命名為 input.jpg，放在目前資料夾。")

    image = Image.open(source)
    rgb = image.convert("RGB")
    print(f"格式：{image.format}｜模式：{image.mode}｜尺寸：{image.size}")
    print(f"左上角 RGB：{rgb.getpixel((0, 0))}")

    rgb.save(output / "image.png")
    for quality in (95, 70, 40):
        rgb.save(output / f"image_q{quality}.jpg", quality=quality, optimize=True)

    for path in sorted(output.iterdir()):
        print(f"{path.name:18s} {path.stat().st_size / 1024:8.1f} KiB")


if __name__ == "__main__":
    main()

