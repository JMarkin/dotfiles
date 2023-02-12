#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyautogui
import Quartz
import time

pyautogui.FAILSAFE=False

def click(x, y):
    print("press")
    cur_pos = pyautogui.position() 
    pyautogui.click(x, y)
    pyautogui.press('command', presses=2, interval=0.1)
    pyautogui.click(cur_pos.x, cur_pos.y)


def run():
    while 1:
        windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListExcludeDesktopElements|Quartz.kCGWindowListOptionOnScreenOnly,Quartz.kCGNullWindowID)
        rdp =next(filter(lambda x: x["kCGWindowOwnerName"] == "Microsoft Remote Desktop", windows))
        x,y = rdp["kCGWindowBounds"]["X"],rdp["kCGWindowBounds"]["Y"]
        x+=100
        y+=100
        click(x, y)
        time.sleep(5*60)


if __name__ == "__main__":
    run()
