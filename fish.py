import time
import pyautogui
from util import *
import win32api
import win32con

def refish():
    print("refish")
    time.sleep(3.5)
    cast()

def cast():
    print("fishing")
    time.sleep(0.75)
    pyautogui.mouseDown(button='right')
    time.sleep(1.5)
    pyautogui.click(button='left')
    pyautogui.mouseUp(button='right')
    time.sleep(20)
    print("start reeling")
    for i in range(0, 100):
        if(not gainedItem()):
            reel()
        else:
            print('fish is caught')
            time.sleep(0.1)
            pyautogui.press('1')
            time.sleep(0.8)
            pyautogui.press('1')
            time.sleep(0.1)
            refish()
            return;


def reel():
    time.sleep(2.5)
    press_button()
    print("stopped reel")


def repairRod():
    time.sleep(2)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1900, 0, 0, 0)
    time.sleep(0.4)
    pyautogui.press('e')
    time.sleep(0.2)
    pyautogui.moveTo(714, 968)
    time.sleep(0.2)
    pyautogui.dragTo(1305, 764, 0.2, button='left')
    time.sleep(0.2)
    pyautogui.leftClick(1585, 822)
    time.sleep(0.2)
    pyautogui.moveTo(1305, 764)
    time.sleep(0.2)
    pyautogui.dragTo(714, 968, 0.2, button='left')
    time.sleep(0.2)
    pyautogui.press('esc')
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1900, 0, 0, 0)
    time.sleep(0.2)
    pyautogui.press('1')

repairRod()