#!/usr/bin/env python3
"""map-shorts setup check: run once before the first clip. Prints what is missing and how to fix it; changes nothing.
Usage: check_setup.py [project_dir]   (project_dir = where you will run render.mjs, default: current folder)"""
import importlib.util, json, os, shutil, subprocess, sys
from pathlib import Path

proj = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve(); here = Path(__file__).resolve().parent
ok = True


def line(good, what, fix=""):
    global ok
    ok &= good or fix.startswith("(optional)")
    print(("  OK   " if good else "  --   ") + what + ("" if good else f"\n         fix: {fix}"))


print("map-shorts setup check\n")
line(sys.version_info >= (3, 10), f"Python {sys.version.split()[0]} (3.10+)", "install Python 3.10 or newer")
for mod, pkg, opt in [("numpy", "numpy", 0), ("PIL", "pillow", 0), ("edge_tts", "edge-tts", 0),
                      ("pythainlp", "pythainlp", 1), ("shapefile", "pyshp", 1), ("shapely", "shapely", 1)]:
    line(importlib.util.find_spec(mod) is not None, f"python package {pkg}", ("(optional) " if opt else "") + f"pip install {pkg}")
for tool in ("ffmpeg", "ffprobe", "node"):
    line(shutil.which(tool) is not None, tool, f"install {tool} and put it on PATH")
pw = any((d / "node_modules/playwright-core").exists() for d in [proj, *proj.parents, here, *here.parents])
line(pw, "node package playwright-core", f"cd {proj} && npm i playwright-core && npx playwright install chromium")
line(bool(os.environ.get("ELEVENLABS_API_KEY")), "ELEVENLABS_API_KEY set (final-quality voice)",
     "(optional) only needed for the final voice; the free Edge voice is for drafts, not monetised videos")
for f in ("template/data/blue-marble.jpg", "template/data/ne10_countries.geojson", "template/vendor/three.min.js", "template/fonts/Kanit-Bold.ttf"):
    line((here.parent / f).exists(), f"skill file {f}", "re-download the skill: a file is missing")
print("\n" + ("Ready. Next: ask the agent for a clip, or try examples/fuji from the repository." if ok else "Fix the -- lines above, then run this again."))
sys.exit(0 if ok else 1)
