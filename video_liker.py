"""Auto-liker: double-clicks the spot under your mouse, for liking short videos.

Point the mouse at the video before the countdown ends. Moving the mouse to a screen
corner stops it (pyautogui's failsafe), as does Ctrl+C.
"""

import argparse
import time

import pyautogui


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--delay", type=float, default=5, help="seconds before the first like (default 5)")
    parser.add_argument("--likes", type=int, default=1, help="how many videos to like (default 1)")
    parser.add_argument("--every", type=float, default=10, help="seconds between likes (default 10)")
    parser.add_argument("--next", action="store_true", help="press the Down arrow after each like to go to the next video")
    args = parser.parse_args()

    print(f"Move your mouse over the video. Starting in {args.delay:g} s...")
    time.sleep(args.delay)
    x, y = pyautogui.position()
    print(f"Liking at x={x}, y={y}. Move the mouse to a screen corner to stop.")
    try:
        for n in range(1, args.likes + 1):
            pyautogui.doubleClick(x, y)  # double-tap likes on TikTok, Instagram and YouTube Shorts web
            print(f"Liked {n}/{args.likes}")
            if n < args.likes:
                if args.next:
                    pyautogui.press("down")
                time.sleep(args.every)
    except (KeyboardInterrupt, pyautogui.FailSafeException):
        print("Stopped.")


if __name__ == "__main__":
    main()
