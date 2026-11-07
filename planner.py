import csv

CAMELOT = {
    "Abm": "1A", "Ebm": "2A", "Bbm": "3A", "Fm": "4A",
    "Cm": "5A", "Gm": "6A", "Dm": "7A", "Am": "8A",
    "Em": "9A", "Bm": "10A", "Gbm": "11A", "Dbm": "12A",
    "B": "1B", "Gb": "2B", "Db": "3B", "Ab": "4B",
    "Eb": "5B", "Bb": "6B", "F": "7B", "C": "8B",
    "G": "9B", "D": "10B", "A": "11B", "E": "12B",
}

def compatible(key1, key2):
    code1 = CAMELOT[key1]
    code2 = CAMELOT[key2]

    num1, letter1 = int(code1[:-1]), code1[-1]
    num2, letter2 = int(code2[:-1]), code2[-1]

    # Rule 1: same code
    if code1 == code2:
        return True

    # Rule 2: same letter, numbers one apart (12 and 1 count as neighbors)
    if letter1 == letter2 and abs(num1 - num2) in (1,11):
        return True

    # Rule 3: same number, different letter
    if num1 == num2:
        return True

    return False

def bpm_close(bpm1,bpm2):
    if abs(bpm1 - bpm2) / bpm1 <= 0.06:
        return True

    doubledBpm = bpm1 * 2
    doubledBpm2 = bpm2 * 2

    if abs(doubledBpm - bpm2) / doubledBpm <= 0.06:
        return True

    if abs(doubledBpm2 - bpm1) / doubledBpm2 <= 0.06:
        return True

    return False

def load_Tracks(path = "tracks.csv"):
    tracks = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            tracks.append({
                "title": row["track"],
                "bpm": float(row["bpm"]),
                "key": row["key"],
            })
    return tracks

def build_Set(tracks, start):
    current = start
    playlist = [current]
    remaining = [t for t in tracks if t is not start]

    while True:
        next_track = None
        for track in remaining:
            if compatible(current["key"], track["key"]) and bpm_close(current["bpm"], track["bpm"]):
                next_track = track
                break

        if next_track is None:
            break

        playlist.append(next_track)
        remaining.remove(next_track)
        current = next_track

    return playlist

tracks = load_Tracks()
best = []

for start in tracks:
    playlist = build_Set(tracks, start)
    
    if len(playlist) > len(best):
        best = playlist

playlist = build_Set(load_Tracks(),start)

for track in best:
    print(track["bpm"], CAMELOT[track["key"]], track["title"])
print(len(best), "tracks in the set")