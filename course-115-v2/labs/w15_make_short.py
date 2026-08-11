"""W15：用 MoviePy 將圖片、旁白與字幕合成直式短影音。"""

from pathlib import Path
from moviepy import AudioFileClip, ImageClip, TextClip, CompositeVideoClip, concatenate_videoclips


WIDTH, HEIGHT, FPS = 720, 1280, 30


def fit_vertical(path: Path, seconds: float) -> ImageClip:
    clip = ImageClip(str(path)).with_duration(seconds)
    scale = min(WIDTH / clip.w, HEIGHT / clip.h)
    return clip.resized(scale).with_position(("center", "center"))


def main() -> None:
    images = sorted(Path("image").glob("*.png")) + sorted(Path("image").glob("*.jpg"))
    audio_path = Path("audio/narration.wav")
    if not images or not audio_path.exists():
        raise FileNotFoundError("需要 image/ 內的圖片，以及 audio/narration.wav。")

    audio = AudioFileClip(str(audio_path))
    seconds = audio.duration / len(images)
    scenes = []
    for index, path in enumerate(images, start=1):
        background = ImageClip(color=(18, 20, 28), size=(WIDTH, HEIGHT)).with_duration(seconds)
        image = fit_vertical(path, seconds)
        label = TextClip(
            text=f"Scene {index}", font_size=42, color="white", method="caption", size=(620, None)
        ).with_duration(seconds).with_position(("center", 1080))
        scenes.append(CompositeVideoClip([background, image, label], size=(WIDTH, HEIGHT)))

    video = concatenate_videoclips(scenes, method="compose").with_audio(audio)
    Path("output").mkdir(exist_ok=True)
    video.write_videofile(
        "output/rough_cut.mp4", fps=FPS, codec="libx264", audio_codec="aac", preset="medium"
    )
    video.close()
    audio.close()


if __name__ == "__main__":
    main()

