import librosa

y, sr = librosa.load("song.mp3")
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
print("BPM:", tempo)