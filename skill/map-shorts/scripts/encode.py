#!/usr/bin/env python3
"""map-shorts encode: clip/build/frames/%04d.jpg + build/voice.m4a -> clip/build/<name>-<tag>.mp4 (1080x1920, H.264, AAC).
Usage: encode.py <clip_dir> [tag]"""
import json, subprocess, sys
from pathlib import Path

clip = Path(sys.argv[1]).resolve(); tag = sys.argv[2] if len(sys.argv) > 2 else "v1"
fps = json.loads((clip / "build/meta.json").read_text())["fps"]
out = clip / "build" / f"{clip.name}-{tag}.mp4"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(fps), "-i", str(clip / "build/frames/%04d.jpg"), "-i", str(clip / "build/voice.m4a"),
                "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-b:v", "9M", "-maxrate", "14M", "-bufsize", "18M", "-preset", "medium",
                "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", "-shortest", str(out)], check=True)
print(out)
