"""將 PowerPoint 匯出的 Slide*.PNG 組成每週一張縮圖總覽。"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1] / "slides" / "previews"
SOURCE = ROOT / "exported"
OUTPUT = ROOT / "montages"


def natural_key(path: Path) -> int:
    digits = "".join(ch for ch in path.stem if ch.isdigit())
    return int(digits or 0)


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    font = ImageFont.load_default()
    for deck in sorted(path for path in SOURCE.iterdir() if path.is_dir()):
        slides = sorted(list(deck.glob("Slide*.PNG")) + list(deck.glob("投影片*.PNG")), key=natural_key)
        if not slides:
            slides = sorted(deck.glob("*.PNG"), key=natural_key)
        if not slides:
            continue
        columns, thumb_width = 3, 480
        opened = [Image.open(slide).convert("RGB") for slide in slides]
        thumb_height = round(thumb_width * opened[0].height / opened[0].width)
        rows = (len(opened) + columns - 1) // columns
        sheet = Image.new("RGB", (columns * thumb_width, rows * (thumb_height + 28)), "#0b0e14")
        draw = ImageDraw.Draw(sheet)
        for index, image in enumerate(opened):
            image.thumbnail((thumb_width, thumb_height))
            x = (index % columns) * thumb_width
            y = (index // columns) * (thumb_height + 28)
            sheet.paste(image, (x, y))
            draw.text((x + 8, y + thumb_height + 6), f"Slide {index + 1}", fill="white", font=font)
        output = OUTPUT / f"{deck.name}.jpg"
        sheet.save(output, quality=88)
        print(output)


if __name__ == "__main__":
    main()

