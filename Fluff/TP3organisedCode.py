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

def appStarted(app):
    app.dayNames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
                'Saturday', 'Sunday']
    app.weekDates = getWeek()
    app.currentDay = str(datetime.datetime.now().date())
    app.currentDayName = calendar.day_name[datetime.datetime.now().date().weekday()]
    app.index = app.weekDates.index(app.currentDay)
    app.maxLineLength = 100
    app.fileContents = readFile(f'Entries/{app.currentDay}-text.txt')
    app.dayEntry = splitString(app,app.fileContents)
    app.letterPosition = [app.height/8*2 + 20]
    app.textY = (app.height/8)*2 - app.height/50
    app.lineY = (app.height/8)*2
    app.lineMoveCount = 0
    app.dLine = 5
    app.moveTextAndLine = False
    app.yearChartX, app.yearChartY = app.width/5, app.height/3
    app.rows = 3
    app.cols = 4
    app.margin = 100 # margin around grid
    app.selection = (-1, -1) # (row, col) of selection, (-1,-1) for none
    ### Circle
    app.hDistCovered = 0
    app.hR, app.hFrameCircum = app.height/2, app.width
    app.hTotalCircum = 2*math.pi*app.hR*10
    app.hTotalArea = math.pi * (app.hR)**2
    ###
    app.cxSun, app.cySun, app.rSun = (app.width/2, 
                                app.height/2, app.width/10)
    app.dMove = 150
    app.dragging = False
    app.getX = 0
    app.getY = 0
    app.x1,app.y1,app.x2,app.y2,app.x3,app.y3,app.x4,app.y4 = (
                        app.width/2 - 40,
                        app.height/2+2.5, 
                        app.width/5,
                        app.height, 
                        app.width - app.width/5, 
                        app.height,
                        app.width/2 + 40, 
                        app.height/2+2.5)
    app.bx1,app.by1,app.bx2,app.by2,app.bx3,app.by3,app.bx4,app.by4 = (
                        -app.width*3, #x
                        app.height/2+2.5, 
                        -900, #x
                        app.height, 
                        -900  + app.width*3/5, #x
                        app.height,
                        -app.width*3 + 80, #x
                        app.height/2+2.5)
    app.backPath = False
    app.theta = 0
    app.mainCentred = True
    app.timeLastSaved = ['Not saved yet']*7

def resetAll(app):
        app.dayNames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
                    'Saturday', 'Sunday']
        app.weekDates = getWeek()
        app.currentDay = str(datetime.datetime.now().date())
        app.currentDayName = calendar.day_name[datetime.datetime.now().date().weekday()]
        app.index = app.weekDates.index(app.currentDay)
        app.yearChartX, app.yearChartY = app.width/5, app.height/3
        app.rows = 3
        app.cols = 4
        app.margin = 100 # margin around grid
        app.selection = (-1, -1) # (row, col) of selection, (-1,-1) for none
        ### Circle
        app.hDistCovered = 0
        app.hR, app.hFrameCircum = app.height/2, app.width
        app.hTotalCircum = 2*math.pi*app.hR*10
        app.hTotalArea = math.pi * (app.hR)**2
        ###
        app.cxSun, app.cySun, app.rSun = (app.width/2, 
                                    app.height/2, app.width/10)
        app.dMove = 150
        app.dragging = False
        app.getX = 0
        app.getY = 0
        app.x1,app.y1,app.x2,app.y2,app.x3,app.y3,app.x4,app.y4 = (
                            app.width/2 - 40,
                            app.height/2+2.5, 
                            app.width/5,
                            app.height, 
                            app.width - app.width/5, 
                            app.height,
                            app.width/2 + 40, 
                            app.height/2+2.5)
        app.bx1,app.by1,app.bx2,app.by2,app.bx3,app.by3,app.bx4,app.by4 = (
                            -app.width*3, #x
                            app.height/2+2.5, 
                            -900, #x
                            app.height, 
                            -900  + app.width*3/5, #x
                            app.height,
                            -app.width*3 + 80, #x
                            app.height/2+2.5)
        app.backPath = False
        app.theta = 0
        app.mainCentred = True

def splitString(app,string):
    string = string
    listOfStrings = []
    while len(string) >= app.maxLineLength:
        listOfStrings += [string[:app.maxLineLength]]
        string = string[app.maxLineLength:]
    listOfStrings += [string]
    return listOfStrings

def listToString(app,list):
    lst = ''
    for string in list:
        lst += string
    return lst


#modes learnt from: https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html#subclassingApp

class SplashScreenMode(Mode):
    def redrawAll(mode, canvas):
        #quote from the movie 'Ferris Bueller's Day Off'
        canvas.create_text(mode.width/2, 250, text='"Life moves pretty fast.', font='Krungthep 35')
        canvas.create_text(mode.width/2, 300, text='If you don’t stop and look', font='Krungthep 25')
        canvas.create_text(mode.width/2, 350, text='around once in a while,', font = 'Krungthep 25')
        canvas.create_text(mode.width/2, 400, text='you could miss it."', font='Krungthep 50')

    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.gameMode)

class MainMode(Mode):
    def keyPressed(app, event):
        if event.key == 'Tab':
            resetAll(app)
        elif event.key == 'd':
            mode.app.setActiveMode(mode.app.dayMode)
        elif event.key == 'Space':
            mode.app.setActiveMode(mode.app.weekSummaryMode)
        elif event.key == 'Up':
            if (app.index >= 0) and (app.index <= len(app.weekDates)-2):
                app.index += 1
                app.currentDayName = app.dayNames[app.index]
                app.currentDay = app.weekDates[app.index]
                app.fileContents = readFile(f'Entries/{app.currentDay}-text.txt')
                app.dayEntry = splitString(app,app.fileContents)
                app.rSun += 20
        elif event.key == 'Down':
            if (app.index >= 1) and (app.index <= len(app.weekDates)-1):
                app.index -= 1
                app.currentDayName = app.dayNames[app.index]
                app.currentDay = app.weekDates[app.index]
                app.fileContents = readFile(f'Entries/{app.currentDay}-text.txt')
                app.dayEntry = splitString(app,app.fileContents)
                #sun gets bigger
                app.rSun += -20

    def redrawAll(app, canvas):
        pass

class dayMode(Mode):
    #writes the entries as user types
    if event.key == 'Enter':
        app.timeLastSaved[app.index] = app.currentDay + ' ' + str(datetime.datetime.now().time())[:5]
        app.mode = 'main'
        saveFile(app)
    #if current text string is too long/exceeds length of line
    if len(app.dayEntry[-1]) >= app.maxLineLength:
        #creates new empty string
        app.dayEntry += ['']
        app.moveTextAndLine = True
    if event.key == 'Space':
        if len(app.dayEntry) >= 2:
            if len(app.dayEntry[-2]) < app.maxLineLength:
                app.dayEntry[-2] += ' '
            else:
                app.dayEntry[-1] += ' '
        else:
            app.dayEntry[-1] += ' '
    elif event.key == 'Delete':
        if app.dayEntry[0] == '':
            pass
        else:
            if app.dayEntry[-1] == '':
                app.dayEntry[-2] = app.dayEntry[-2][:-1]
            app.dayEntry[-1] = app.dayEntry[-1][:-1]
    elif event.key in string.printable:
        if len(app.dayEntry) >= 2:
            if len(app.dayEntry[-2]) < app.maxLineLength:
                app.dayEntry[-2] += event.key
            else:
                app.dayEntry[-1] += event.key
        else: 
            app.dayEntry[-1] += event.key
        
class daySummaryMode(Mode):
    def 

class MyModalApp(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        #app.gameMode = GameMode()
        #app.helpMode = HelpMode()
        app.setActiveMode(app.splashScreenMode)
        #app.timerDelay = 50

app = MyModalApp(width=1400, height=800)

        '''
    if app.mode == 'year':
        #year chart expands when clicked
        if ((app.yearChartX <= app.width - 50) and
                (app.yearChartY <= app.height - 50)):
            app.yearChartX += 50
            app.yearChartY += 25
            '''
