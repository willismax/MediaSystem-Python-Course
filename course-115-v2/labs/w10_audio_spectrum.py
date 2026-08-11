"""W10：繪製波形與 STFT 頻譜。"""

from pathlib import Path
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    source = Path("input.wav")
    if not source.exists():
        raise FileNotFoundError("請把 3–5 秒 WAV 命名為 input.wav。")

    y, sr = librosa.load(source, sr=None, mono=True)
    n_fft, hop_length = 1024, 256
    stft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
    db = librosa.amplitude_to_db(np.abs(stft), ref=np.max)
    print(f"取樣率：{sr} Hz｜樣本數：{len(y)}｜秒數：{len(y) / sr:.3f}")

    fig, axes = plt.subplots(2, 1, figsize=(12, 7), constrained_layout=True)
    librosa.display.waveshow(y, sr=sr, ax=axes[0])
    axes[0].set(title="Waveform", xlabel="Time (s)", ylabel="Amplitude")
    image = librosa.display.specshow(
        db, sr=sr, hop_length=hop_length, x_axis="time", y_axis="hz", ax=axes[1]
    )
    axes[1].set(title=f"STFT｜n_fft={n_fft}, hop={hop_length}")
    fig.colorbar(image, ax=axes[1], format="%+2.0f dB")
    fig.savefig("w10_waveform_stft.png", dpi=160)


if __name__ == "__main__":
    main()

