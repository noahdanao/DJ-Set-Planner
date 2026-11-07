# DJ Set Planner

A Python tool that helps DJs plan sets. It scans a music folder, reads
each track's BPM and key from the metadata that DJ software like Serato
saves inside the file, and falls back to audio analysis for tracks that
haven't been analyzed. Results are saved to a CSV file.

## Status
- [x] BPM and key from Serato metadata
- [x] Audio-based BPM detection as a fallback (librosa)
- [x] Harmonic mixing rules (Camelot wheel)
- [x] Tempo matching, including half-time tracks
- [x] Automatic set ordering
- [ ] Longer sets by trying every starting track
- [ ] Web interface

## Usage
    pip install librosa mutagen
    python analyze.py
    python planner.py

Set `MUSIC_DIR` at the top of `analyze.py` to your music folder.
`analyze.py` saves each track's BPM and key to `tracks.csv`, and
`planner.py` builds an ordered set from that file.

## How it works
Two tracks can follow each other when:
- **Keys are compatible** on the Camelot wheel: the same key, a neighboring
  number with the same letter (12 and 1 count as neighbors), or the same
  number with the other letter.
- **Tempos are within 6%**, or within 6% once one track is doubled, so
  half-time tracks (like jersey club tagged at 70 BPM) can still match.

The planner starts from one track and repeatedly picks the next track that
passes both checks. Because it takes the first match it finds, it can stop
before using every song, which is the next thing to improve.
