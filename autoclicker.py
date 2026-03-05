import pyautogui
import time
pyautogui.FAILSAFE = True

def click():
    clicktime = 1
    repeat = 0
    repeat2input = input("How many times should the program click?")
    clicktimeinput = input("How long should the program pause between clicking?")
    clicktime = int(clicktimeinput)
    if repeat2input == "infinite":
        repeat2input = "100000000000000000000"
    if clicktimeinput == "0":
        clicktime = float(0.05)
    repeat2 = int(repeat2input)
    while repeat <= repeat2:
        time.sleep(clicktime)
        pyautogui.click()
        repeat = repeat + 1



click()