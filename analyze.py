import csv
from pathlib import Path

import librosa
from mutagen.id3 import ID3

MUSIC_DIR = Path.home() / "Downloads" / "serrato files"


def read_tags(path):
    """Return the (bpm, key) saved inside the file, or None for missing values."""
    bpm, key = None, None
    try:
        tags = ID3(path)
    except Exception:
        return bpm, key
    if "TBPM" in tags:
        try:
            bpm = float(tags["TBPM"].text[0])
        except ValueError:
            pass
    if "TKEY" in tags:
        key = str(tags["TKEY"].text[0])
    return bpm, key


def detect_bpm(path):
    """Estimate BPM from the audio when the file has no saved value."""
    y, sr = librosa.load(path)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    bpm = float(tempo[0])
    return bpm * 2 if bpm < 80 else bpm


rows = []
for path in sorted(MUSIC_DIR.glob("*.mp3")):
    bpm, key = read_tags(path)
    source = "tag"
    if bpm is None:
        bpm = detect_bpm(path)
        source = "librosa"
    bpm = round(bpm, 1)
    print(path.stem, bpm, key, source)
    rows.append([path.stem, bpm, key or "", source])

with open("tracks.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["track", "bpm", "key", "source"])
    writer.writerows(rows)