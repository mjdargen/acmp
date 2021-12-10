# converts from .ogg to .mp3
import os
import subprocess

folders = ['animal-crossing', 'wild-world',
           'new-leaf', 'new-horizons', 'aircheck', 'live']

for folder in folders:
    files = [f for f in os.listdir(
        f'../{folder}') if f.lower().endswith(".ogg")]
    for f in files:
        input = f"../{folder}/{f}"
        output = f"../{folder}/{f[:-4] + '.mp3'}"
        subprocess.run(['ffmpeg', '-n', '-i', input, output])
