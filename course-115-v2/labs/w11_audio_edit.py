"""W11：使用 librosa／soundfile 完成裁切、淡入淡出與峰值正規化。"""

from pathlib import Path
import librosa
import numpy as np
import soundfile as sf


def main() -> None:
    source = Path("input.wav")
    if not source.exists():
        raise FileNotFoundError("請把旁白 WAV 命名為 input.wav。")

    y, sr = librosa.load(source, sr=None, mono=True)
    start, end = int(1.0 * sr), min(int(9.0 * sr), len(y))
    clip = y[start:end].copy()
    if clip.size == 0:
        raise ValueError("音檔太短，無法取出 1–9 秒範圍。")

    peak = np.max(np.abs(clip))
    if peak > 0:
        clip = 0.9 * clip / peak

    fade_samples = min(int(0.15 * sr), len(clip) // 2)
    clip[:fade_samples] *= np.linspace(0, 1, fade_samples)
    clip[-fade_samples:] *= np.linspace(1, 0, fade_samples)
    sf.write("w11_narration_edit.wav", clip, sr, subtype="PCM_16")
    print(f"輸出 {len(clip) / sr:.2f} 秒｜取樣率 {sr} Hz｜峰值 {np.max(np.abs(clip)):.3f}")


if __name__ == "__main__":
    main()

