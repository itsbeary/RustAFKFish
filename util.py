from time import sleep
import pyautogui
import pytesseract
import cv2 
import numpy as np


def press_button():
    pyautogui.keyDown('a')
    pyautogui.keyDown('s')
    sleep(2)
    pyautogui.keyUp('a')
    pyautogui.keyUp('s')

def read_item():
        x, y, width, height = 675, 115, 200, 40
        screenshot = pyautogui.screenshot(region=(x, y, width, height))

        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        

        pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Beary\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
        text = pytesseract.image_to_string(screenshot ,lang='eng', config='--psm 12 --oem 1')
        return text

def gainedItem():
    return pyautogui.pixelMatchesColor(1812, 763, (88, 101, 66), tolerance=10)

