#!/usr/bin/env python3

# auto2048.py - This program plays the GNOME 2048 game automatically by pressing the UP, RIGHT, DOWN, LEFT arrow keys in that order.

import pyautogui
import time


def main():
    time.sleep(3)                       # Give time to switch to the game window.
    while True:
        pyautogui.press("up")           # Press the 'up' arrow key.
        time.sleep(0.1)
        pyautogui.press("right")        # Press the 'right' arrow key.
        time.sleep(0.1)
        pyautogui.press("down")         # Press the 'down' arrow key.
        time.sleep(0.1)
        pyautogui.press("left")         # PRess the 'left' arrow key.
        time.sleep(0.1)


if __name__ == "__main__":
    main()
