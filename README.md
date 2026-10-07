# DJ Set Planner

A Python tool that helps DJs plan sets. It scans a music folder, reads
each track's BPM and key from the metadata that DJ software like Serato
saves inside the file, and falls back to audio analysis for tracks that
haven't been analyzed. Results are saved to a CSV file.

## Status
- [x] BPM and key from Serato metadata
- [x] Audio-based BPM detection as a fallback (librosa)
- [ ] Harmonic mixing rules (Camelot wheel)
- [ ] Transition scoring and automatic set ordering
- [ ] Web interface

## Usage
    pip install librosa mutagen
    python analyze.py

Set `MUSIC_DIR` at the top of `analyze.py` to your music folder.
Results are saved to `tracks.csv` with each track's BPM, key, and
where the values came from.
