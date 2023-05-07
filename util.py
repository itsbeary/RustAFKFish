from time import sleep
import pyautogui
import pytesseract
import cv2 
import numpy as np

xDefault = 720
yDefault = 603

x = 720
y = 603

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

def checkInventory():
     global x
     global xDefault
     global y
     pyautogui.press('e')
     sleep(0.5)
     pyautogui.leftClick(x, y)
     x = x + 90;
     if(x >= 1200):
          x = xDefault
          y = y + 90
     if(y >= 920):
         x = xDefault;
         y = yDefault;
         return False;
     else: 
          return True

#while True:
#     sleep(0.5)
#     if(checkInventory()):
#          print(read_item())
#     else:
#          print("finished")
#          exit()
          

     