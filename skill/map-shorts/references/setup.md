# Setup

Requirements: Python 3.10+, Node 18+, ffmpeg/ffprobe, Chrome or Chromium.

```bash
pip install numpy pillow edge-tts          # build + site tool
pip install pythainlp                      # Thai captions (optional)
pip install pyshp shapely                  # make_geo.py (optional)
npm i playwright-core && npx playwright install chromium   # run in the folder you work from; or pass --chrome <path>
```

Render speed
- With a GPU: `node scripts/render.mjs <clip>` (Chrome uses ANGLE/your GPU). Check the `renderer:` line it prints.
- Without: add `--swiftshader` (software, works anywhere, about 10x slower; fine for stills).
- Frames land in `<clip>/build/frames`; parallelise with `--from N --to M` in several processes.
- WSL: Chrome inside WSL only has software GL. Run Windows `node.exe` with Windows Chrome via `--chrome "C:\Program Files\Google\Chrome\Application\chrome.exe"` for the GPU.

Voices
- Draft (free, not for monetised videos): Edge TTS. Final: `export ELEVENLABS_API_KEY=...` and `"provider": "elevenlabs"` (or another licensed provider).
- Voice lines are cached in `<clip>/voice/` by text, so rebuilding after a camera edit costs nothing.
