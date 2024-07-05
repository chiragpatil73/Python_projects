import pyautogui as pt
import time as ti


name=input('enter the your name:')
ti.sleep(3)
pt.hotkey('win')
pt.typewrite('paint')
ti.sleep(2)
pt.press('enter')
ti.sleep(2)
pt.click(455,123)
ti.sleep(2)
pt.moveTo(470,471)
pt.click(475,480)
ti.sleep(2)
pt.typewrite(name)

