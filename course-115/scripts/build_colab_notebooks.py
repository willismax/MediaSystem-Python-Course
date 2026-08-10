"""把 labs 中的教學腳本包裝為可上傳至 Colab 的單一程式碼 Notebook。"""

from __future__ import annotations
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"
OUT = ROOT / "colab"
FILES = {
    "W02_Image_Basics.ipynb": "w02_image_basics.py",
    "W03_Convolution.ipynb": "w03_convolution.py",
    "W04_Diffusion_Forward.ipynb": "w04_diffusion_forward.py",
    "W10_Audio_Spectrum.ipynb": "w10_audio_spectrum.py",
    "W11_Audio_Edit.ipynb": "w11_audio_edit.py",
    "W15_Make_Short.ipynb": "w15_make_short.py",
}


def notebook(title: str, script: str) -> dict:
    install = "!pip -q install Pillow numpy opencv-python-headless matplotlib librosa soundfile moviepy"
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"# {title}\n", "請先上傳講義指定的輸入素材，再依序執行。CPU 可完成；Colab GPU 非必要。\n"],
            },
            {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [install]},
            {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": script.splitlines(True)},
        ],
        "metadata": {
            "colab": {"provenance": []},
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for notebook_name, script_name in FILES.items():
        source = (LABS / script_name).read_text(encoding="utf-8")
        data = notebook(notebook_name.removesuffix(".ipynb").replace("_", " "), source)
        (OUT / notebook_name).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(notebook_name)


if __name__ == "__main__":
    main()

