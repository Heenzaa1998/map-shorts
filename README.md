# map-shorts (beta)

An open-source agent skill (Claude Code / any agent that reads `SKILL.md`) that makes **vertical map-explainer Shorts**: one continuous 3D camera shot from a NASA globe to real satellite terrain, with narration, word-synced captions, glass cards, counters and map overlays. You describe the video in a `spec.json`; the scripts voice it, time everything to the spoken words, render it in headless Chrome and encode an MP4. No stock footage, no editor.

The skill also carries the *method*: how to pick topics that hold viewers, script rules, pacing, QA and honesty rules (`skill/map-shorts/references/method.md`).

## Install
```bash
cp -r skill/map-shorts ~/.claude/skills/        # Claude Code
pip install -r requirements.txt
npm install && npx playwright install chromium
```
Then ask your agent: *"Make a map-shorts clip about why Lake Baikal is so deep."*

## Check your setup
```bash
python3 skill/map-shorts/scripts/check_setup.py .
```

## Try the example by hand
```bash
python3 skill/map-shorts/scripts/make_site.py examples/fuji --name region --box 26 44 126 146 --zimg 8 --zter 7 --grid 512
python3 skill/map-shorts/scripts/make_site.py examples/fuji --box 34.9 36.0 138.0 139.4 --zimg 12 --zter 11
python3 skill/map-shorts/scripts/build.py examples/fuji
node skill/map-shorts/scripts/render.mjs examples/fuji --times 3,8,15      # stills first
node skill/map-shorts/scripts/render.mjs examples/fuji && python3 skill/map-shorts/scripts/encode.py examples/fuji
```
Software rendering (`--swiftshader`) is slow (~0.5 fps); a GPU is about 10x faster.

## Known limitations (beta)
- Tested on Linux (WSL) with software rendering. Not yet tested on Windows or macOS, or with a GPU; please report issues.
- The ElevenLabs voice path has not been tested end to end in this release.
- Without a GPU a 30 s clip takes about 20-30 minutes to render.
- The free Edge voice is for drafts; it is robotic in Thai and not licensed for monetised videos.
- Country/province outlines look soft in close-ups; beacons can look like flat bars from some angles.
- Camera framing needs a few rounds of stills per clip; it is not one-click.

## Privacy and safety
- Edge TTS sends your script text to Microsoft's speech service; ElevenLabs sends it to ElevenLabs with your key (read from `ELEVENLABS_API_KEY`, never stored). `make_site.py` / `make_geo.py` download map tiles and Natural Earth files from EOX, AWS and Natural Earth.
- `render.mjs` serves only the clip and template folders on 127.0.0.1 to a headless Chrome and does not disable the browser sandbox.
- Treat a `spec.json` from someone else as code (see SKILL.md).

## What is not included
Music, sound effects, avatars, brand assets and cloned voices. Bring your own (CC0 sounds are fine). Narration: Edge TTS for free drafts only (not licensed for monetised videos), ElevenLabs with your own key (`ELEVENLABS_API_KEY`) for finals. Details in `skill/map-shorts/references/licenses.md`.

## License
Code and docs MIT. Bundled data keep their own licenses, see `NOTICE.md`. Videos you make must carry the imagery and terrain credits (the build adds a credit line; the description needs the full text, see licenses.md). This is not legal advice.
