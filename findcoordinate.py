import pyautogui
import time
pyautogui.FAILSAFE = True

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

while 0 == 0:
    print(currentMouseX, currentMouseY)
    currentMouseX, currentMouseY = pyautogui.position()
    time.sleep(1)

#firefox = 1169 1066
#private = 1160 809
#search = 1228 97
#compose = 120 262
#autotype 'to'
#subject = 1284 444
#body = 1443 539
#send = 1129 965
#exit out of private browser = 1888 36