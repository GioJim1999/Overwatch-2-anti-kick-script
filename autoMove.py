#anti kick script run it alt tab to game you have 3 seconds
#let it run if you want it to stop free your mouse and move to the top left of the screen
#By: Gio
import pyautogui as pg
import time as t

pg.FAILSAFE = True

t.sleep(3)
while(True):
        pg.keyDown('w')
        t.sleep(0.5)
        pg.keyUp('w')
        pg.keyDown('s')
        t.sleep(0.5)
        pg.keyUp('s')
