# Video Liker

A small Python script that double-clicks the video under your mouse to like it, once or
on a loop, for TikTok, Instagram Reels or YouTube Shorts in the browser. It only clicks
where you point, so it works without logging in through any API.

## Run

```bash
pip install -r requirements.txt
python video_liker.py                          # like once after a 5 s countdown
python video_liker.py --likes 20 --every 8 --next   # like 20 videos, scrolling to the next each time
```

Move the mouse to any screen corner to stop it at once.

Use it on your own account and within each platform's rules: heavy automated liking can
get an account rate limited.
