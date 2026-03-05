import time
import pyautogui
pyautogui.FAILSAFE = True

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

time.sleep(10)
pyautogui.click(1695, 166)
time.sleep(2)
pyautogui.click(1303, 388)