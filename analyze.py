import csv
from pathlib import Path
import librosa

rows = []
for path in sorted(Path("tracks").glob("*.mp3")):
    y, sr = librosa.load(path)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    bpm = round(float(tempo[0]))
    print(path.name, bpm)
    rows.append([path.name, bpm])

with open("tracks.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["track", "bpm"])
    writer.writerows(rows)