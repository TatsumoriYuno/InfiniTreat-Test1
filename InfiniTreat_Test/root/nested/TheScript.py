import os
import sys
import cv2
import mss
import numpy
import keyboard
import pyautogui
from time import time, sleep, perf_counter
import pause

#Enter Now Postition
#pyautogui.moveTo(x=900, y=152)
#Chest Position
#pyautogui.moveTo(x=25, y=842)
#Finish Position
##pyautogui(x=803, y=789)
#Burger
#pyautogui(x=700, y=712)

def precise_delay(delay_amount):
    prv_t = perf_counter()
    
    while round((perf_counter() - prv_t) * 1000) / 1000 - 0.001 <= delay_amount:
        pass

print("Press 's' to start program.")
print("Once started press 'q' to quit and 'z' to loop.")
keyboard.wait('s')
pyautogui.press('x')


sct = mss.mss()
zero_txt = cv2.imread("TERNOW.PNG")

dimensions_counter = {'left': 850, 'top': 25, 'width': 250, 'height': 250}



while True:
    while True:
        scr = numpy.array(sct.grab(dimensions_counter))
        scr_remove = scr[:,:,:3]

        result = cv2.matchTemplate(scr_remove, zero_txt, cv2.TM_CCOEFF_NORMED)
        
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        #src = scr.copy()
        if max_val > .79:
            pyautogui.moveTo(x=937, y=279)
            pyautogui.click(button='left')
            precise_delay(.5)
            pyautogui.press('i')
            precise_delay(1.2)
            pyautogui.moveTo(x=780, y=834)
            pyautogui.click(button='left')
            precise_delay(.5)
            pyautogui.moveTo(x=656, y=735)
            pyautogui.click(button='left')
            precise_delay(7.32)
            pyautogui.moveTo(x=1268, y=836)
            pyautogui.click(button='left')
            precise_delay(3)
            pyautogui.keyDown('s')
            precise_delay(7.4)
            pyautogui.keyUp('s')
            pyautogui.press('x')
            max_val = 0
        
        cv2.imshow('P101 Timer', scr)
        cv2.waitKey(1)
    
        if keyboard.is_pressed('z'):
            pyautogui.press('x')
            break
        if keyboard.is_pressed('q'):
            break
    if keyboard.is_pressed('q'):
        break
print("Program closed with 'q' key.")
