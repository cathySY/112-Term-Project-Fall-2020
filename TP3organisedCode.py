#################################################
# TP3Code.py
#
# Your name: Yi Sijun Cathy
# Your andrew id: sijuncay
#################################################


#downloaded from CMU 15-112 website
import cs112_f20_week7_linter
import math, copy, random, string, calendar
from datetime import datetime
#from my local files
from Usefulwords import *
from EntryAnalysis import *
from fileFunctions import *
#downloaded from CMU 15-112 website
from cmu_112_graphics import *

''' add this quote as a splash page after TP2? '''
# “Life moves pretty fast. If you don’t stop and look around 
#  once in a while, you could miss it.”
#                                             Ferris Bueller

#rgbString(r, g, b) copied from: https://www.cs.cmu.edu/~112/notes/notes-graphics.html
#creates custom colors
def rgbString(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

#make2dList(rows, cols, string) copied from 112 website: https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html#creating2dLists
def make2dList(rows, cols, string):
    emptyColor = string
    return [ ([emptyColor] * cols) for row in range(rows) ]

#learnt from from: https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html#subclassingApp
class SplashScreenMode(Mode):
    def redrawAll(mode, canvas):
        #quote from the movie 'Ferris Bueller's Day Off'
        canvas.create_text(mode.width/2, 250, text='"Life moves pretty fast.', font='Krungthep 35')
        canvas.create_text(mode.width/2, 300, text='If you don’t stop and look', font='Krungthep 25')
        canvas.create_text(mode.width/2, 350, text='around once in a while,', font = 'Krungthep 25')
        canvas.create_text(mode.width/2, 400, text='you could miss it."', font='Krungthep 50')

    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.gameMode)

class MyModalApp(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        #app.gameMode = GameMode()
        #app.helpMode = HelpMode()
        app.setActiveMode(app.splashScreenMode)
        #app.timerDelay = 50

app = MyModalApp(width=1400, height=800)