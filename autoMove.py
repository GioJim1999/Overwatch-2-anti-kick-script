#ANTI KICK SCRIPT BY GIO

import pyautogui as pg
import time as t

pg.FAILSAFE = True

t.sleep(3)
while(True):
        pg.keyDown('w')
        t.sleep(0.5)
        pg.keyUp('w')
        pg.keyDown('s')
        t.sleep(0,5)
        pg.keyUp('s')
