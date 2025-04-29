# converts from .ogg to .mp3
import os
import subprocess

DIR_PATH = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

folders = ["animal-crossing", "wild-world", "new-leaf", "new-horizons", "aircheck", "live"]

for folder in folders:
    files = [f for f in os.listdir(f"{DIR_PATH}/../{folder}") if f.lower().endswith(".ogg")]
    for f in files:
        input = f"{DIR_PATH}/../{folder}/{f}"
        output = f"{DIR_PATH}/../{folder}/{f[:-4] + '.mp3'}"
        subprocess.run(["ffmpeg", "-n", "-i", input, output])
