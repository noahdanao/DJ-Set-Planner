# DJ Set Planner

A Python tool that helps DJs plan sets. It scans a folder of tracks,
detects each song's tempo (BPM), and saves the results to a CSV file.

## Status
- [x] BPM detection for a folder of MP3s
- [ ] Key detection
- [ ] Transition scoring and automatic set ordering
- [ ] Web interface

## Usage
    pip install librosa
    python analyze.py

Put your MP3s in a `tracks/` folder first. Results are saved to `tracks.csv`.
