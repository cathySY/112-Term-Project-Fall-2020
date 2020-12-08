#################################################
# TP2Code.py
#
# Your name: Yi Sijun Cathy
# Your andrew id: sijuncay
#################################################


#downloaded from CMU 15-112 website
import cs112_f20_week7_linter
import math, copy, random, string, calendar
from datetime import datetime
#from other TP files of mine
from Usefulwords import *
from EntryAnalysis import *
from wordcloud import *
from fileFunctions import *
#from perspective import *
#import perspective 
import EntryAnalysis
import Usefulwords

#downloaded from CMU 15-112 website
from cmu_112_graphics import *

# “Life moves pretty fast. If you don’t stop and look around 
#  once in a while, you could miss it.”
#                                             Ferris Bueller

#from 112 course notes 
#https://www.cs.cmu.edu/~112/notes/notes-graphics.html
#creates custom colors
def rgbString(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

#from 112 website: 
#https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html#creating2dLists
#makes 2d lists
def make2dList(rows, cols, string):
    emptyColor = string
    return [ ([emptyColor] * cols) for row in range(rows) ]


def appStarted(app):
    app.mode = 'main'
    app.dayNames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
                'Saturday', 'Sunday']
    app.skyColors = ['peachPuff','moccasin','papayaWhip','lemonChiffon','lightYellow','aliceBlue','lightCyan']
    app.sunColors = ['darkOrange', 'darkOrange', 'orange', 'orange', 'moccasin','lightGoldenrodYellow','lightCyan']
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
    app.textDict = {}
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
    app.cxSun, app.cySun, app.rSun = (app.width/2, app.height/2-3, app.width/10)
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
    app.cx1,app.cy1,app.cx2,app.cy2,app.cx3,app.cy3,app.cx4,app.cy4 = (
                        5520, #x
                        app.height/2+2.5,                       
                        1460, #x
                        app.height,
                        2300, #x
                        app.height,
                        5600, #x
                        app.height/2+2.5)
                        
    app.povLeft = app.width
    app.backPath = False
    app.frontPath = True
    app.theta = 0
    app.mainCentred = True
    app.timeLastSaved = ['Not saved yet']*7
    app.isPopUpBox = False
    app.areLinesMoving = False 
    app.buttonColor = 'cyan'
    app.dayChX1, app.dayChY1, app.dayChX2, app.dayChY2 = 597.5,400,797.5,600 #calculated values
    app.weekMainMood = ''
    app.xDiffTotal = 0
    app.xDiffTotalChanged = 0

def resetAll(app):
    app.mode = 'daily summary'
    app.dayNames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
                'Saturday', 'Sunday']
    app.weekDates = getWeek()
    #app.weekDates = createDayObjectsInWeek()
    app.currentDay = str(datetime.datetime.now().date())
    app.currentDayName = calendar.day_name[datetime.datetime.now().date().weekday()]
    app.index = app.weekDates.index(app.currentDay)
    #print(f'{app.currentDay}-text.txt')
    app.maxLineLength = 20
    app.fileContents = readFile(f'Entries/{app.currentDay}-text.txt')
    app.dayEntry = splitString(app,app.fileContents)
    app.letterPosition = [app.height/8*2 + 20]
    app.textY = (app.height/8)*2 - app.height/50
    app.lineY = (app.height/8)*2
    app.lineMoveCount = 0
    app.dLine = 5
    app.moveTextAndLine = False
    app.textDict = {}
    app.yearChartX, app.yearChartY = app.width/5, app.height/3
    #from CMU course notes about drawing a grid:
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
    #I modified the parameters
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
                        app.width/2 - 30,
                        app.height/2+2.5, 
                        app.width/5,
                        app.height, 
                        app.width - app.width/5, 
                        app.height,
                        app.width/2 + 30, 
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
    app.povLeft = app.width
    app.backPath = False
    app.theta = 0
    app.mainCentred = True
    app.timeLastSaved = ['Not saved yet']*7

#splits a long string into short strings of equal lengths
def splitString(app,string):
    string = string
    listOfStrings = []
    while len(string) >= app.maxLineLength:
        listOfStrings += [string[:app.maxLineLength]]
        string = string[app.maxLineLength:]
    listOfStrings += [string]
    return listOfStrings

#joins short strings into a long string
def listToString(app,list):
    lst = ''
    for string in list:
        lst += string
    return lst

def keyPressed(app, event):
    if event.key == 'Tab':
        resetAll(app)
    if app.mode == 'main':
        if event.key == 'Space':
            app.mode = 'weekly summary'
            getMostFrequentMood(app)

        #moving from one day to another    
        elif event.key == 'Up':
            app.areLinesMoving = True
            if (app.index >= 0) and (app.index <= len(app.weekDates)-2):
                app.index += 1
                app.currentDayName = app.dayNames[app.index]
                app.currentDay = app.weekDates[app.index]
                app.fileContents = readFile(f'Entries/{app.currentDay}-text.txt')
                app.dayEntry = splitString(app,app.fileContents)
                #sun gets bigger
                app.rSun += 20
        elif event.key == 'Down':
            if (app.index >= 1) and (app.index <= len(app.weekDates)-1):
                app.index -= 1
                app.currentDayName = app.dayNames[app.index]
                app.currentDay = app.weekDates[app.index]
                app.fileContents = readFile(f'Entries/{app.currentDay}-text.txt')
                app.dayEntry = splitString(app,app.fileContents)
                #sun gets smaller
                app.rSun += -20
    elif app.mode == 'day':
        if event.key == 'Right':
            app.mode = 'daily summary'
        #if current text string is too long/exceeds length of underline
        elif len(app.dayEntry[-1]) >= app.maxLineLength:
            #creates new empty string
            app.dayEntry += ['']
            app.moveTextAndLine = True
        elif event.key == 'Space':
            app.dayEntry[-1] += ' '
        elif event.key == 'Delete':
            #if entry is empty
            if app.dayEntry[0] == '':
                pass
            else:
                #if last string is empty, delete from second-last string
                if app.dayEntry[-1] == '':
                    app.dayEntry[-2] = app.dayEntry[-2][:-1]
                # if last string is not empty, delete from last string
                app.dayEntry[-1] = app.dayEntry[-1][:-1]
        elif event.key in string.printable:
            app.dayEntry[-1] += event.key
    elif app.mode == 'daily summary':
        if event.key == 'Left':
            app.mode = 'day'
    elif app.mode == 'weekly summary':
        if event.key == 'Enter':
            app.mode = 'main'

#replaces content in file with content written in entry using a long string
def saveFile(app):
    contents = listToString(app,app.dayEntry)
    writeFile(f'Entries/{app.currentDay}-text.txt',contents)

def timerFired(app):
    #moves text and line downwards at the same pace until a new line is reached
    if app.moveTextAndLine == True:
        app.lineY += app.dLine
        app.textY += app.dLine
        app.lineMoveCount += 1
    if app.lineMoveCount >= 40/app.dLine:
        app.moveTextAndLine = False
        app.lineMoveCount = 0
    if app.mode == 'year':
        #year chart expands when clicked
        if ((app.yearChartX <= app.width - 50) and
                (app.yearChartY <= app.height - 50)):
            app.yearChartX += 50
            app.yearChartY += 25
    if app.mode == 'main':
        #year chart shrinks when clicked
        if ((app.yearChartX >= app.width/5) and
                (app.yearChartY >= app.height/3)):
            app.yearChartX -= 50
            app.yearChartY -= 25
    if app.mode == 'main to day':
        x1, y1, x2, y2 = app.height/8, app.height/8, app.width - app.height/8, app.height - app.height/8
        if ((app.dayChX1 >= x1) and (app.dayChY1 >= y1)) and ((
                (app.dayChX2 <= x2) and (app.dayChY2 <= y2))):
            app.dayChX1 -= 38
            app.dayChY1 -= 26
            app.dayChX2 += 38
            app.dayChY2 += 10
        else:
            app.dayChX1, app.dayChY1, app.dayChX2, app.dayChY2 = 597.5,400,797.5,600
            app.mode = 'day'

      


def mouseDragged(app, event):
    app.dragging = True
    #how much the cursor is dragged in x-direction
    #can be positive or negative
    xdiff = (app.getX - event.x)
    app.theta -= xdiff/app.hTotalCircum * (math.pi*2)
    app.thetaMOD = app.theta % (2*math.pi)
    print("app.theta= ",app.theta)
    if (app.thetaMOD >= 0 and app.thetaMOD < math.pi/2): 
        app.cxSun -= xdiff
        app.cxSun %= app.hTotalCircum
        app.frontPath = True
        app.backPath = False
        app.x1 -= xdiff
        app.x4 -= xdiff
        app.x2 -= xdiff*1/4
        app.x3 -= xdiff*1/4
    elif (app.thetaMOD >= math.pi*3/2) and (app.thetaMOD < math.pi*2):
        app.cxSun -= xdiff
        app.cxSun %= app.hTotalCircum
        app.frontPath = True
        app.backPath = False
        app.x1 -= xdiff
        app.x4 -= xdiff
        app.x2 -= xdiff*1/4
        app.x3 -= xdiff*1/4
    #second quadrant 
    elif ((app.thetaMOD >= math.pi/2 and app.thetaMOD < math.pi*3/2)): 
        app.frontPath = False
        app.backPath = True
        if app.theta > 0:
            print("b = ", app.bx1,app.bx4)
            print(app.bx2, app.bx3)
            app.bx1 -= xdiff
            app.bx4 -= xdiff
            app.bx2 -= xdiff*1/4
            app.bx3 -= xdiff*1/4

        else:
            print(app.cx1,app.cx4)
            print(app.cx2, app.cx3)
            app.cx1 -= xdiff
            app.cx4 -= xdiff
            app.cx2 -= xdiff*1/4
            app.cx3 -= xdiff*1/4


def mouseReleased(app,event):
    app.dragging = False


def mouseMoved(app,event):
    x1,y1,x2,y2,x3,y3,x4,y4 = (app.x1,app.y1,app.x2,app.y2,app.x3,app.y3,app.x4,app.y4)
    grad1 = (y2-y1)/(x2+250-(x1+30))
    grad2 = (y3-y4)/(x3-250-(x4-30))
    lineX1 = (1/grad1)*(650-y1)+(x1+25)
    lineX2 = (1/grad2)*(650-y3)+(x3-250)
    if (lineX1 <= event.x <= lineX2) and (650 <= event.y <= app.height):
        app.isPopUpBox = True
    else:
        app.isPopUpBox = False

def mousePressed(app, event):
    if app.mode == 'splash':
        app.mode = 'main'
    app.getX = event.x
    app.getY = event.y
    margin = app.height/8
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    #x2-100,y1,x2,y1+100
    if app.mode == 'day':
        if (x2-100 < event.x < x2) and (y1 < event.y < y1+100):
            app.timeLastSaved[app.index] = app.currentDay + ' ' + str(datetime.datetime.now().time())[:5]
            app.mode = 'main'
            saveFile(app)
            app.mode = 'main'
    #elif app.mode == 'daily summary':
        #if (x2-100 < event.x < x2) and (y1 < event.y < y1+100):
            #app.mode = 'day'
    #DRAW YEAR CHART
    if app.mode == 'main':
        #if click on year chart
        if (50 < event.x < app.width/5) and (50 < event.y < app.height/3):
            app.mode = 'year'
    #canvas.create_rectangle(50, 50, app.width/5, app.height/3, fill = 'white')
        (row, col) = getCell(app, event.x, event.y)
    # select this (row, col) unless it is selected
        if (app.selection == (row, col)):
            app.selection = (-1, -1)
        else:
            app.selection = (row, col)
        x1,y1,x2,y2,x3,y3,x4,y4 = (app.x1,app.y1,app.x2,app.y2,app.x3,app.y3,app.x4,app.y4)
        grad1 = (y2-y1)/(x2+250-(x1+30))
        grad2 = (y3-y4)/(x3-250-(x4-30))
        lineX1 = (1/grad1)*(650-y1)+(x1+25)
        lineX2 = (1/grad2)*(650-y3)+(x3-250)
        #if user clicks the rectangle inside the trapezium
        if (lineX1 <= event.x <= lineX2) and (650 <= event.y <= app.height):
            app.mode = 'main to day'
            app.isPopUpBox = False
        if app.mainCentred == True:
            pass
    if app.mode == 'year':
        if (app.width/5 < event.x < app.width - 50) and (app.height/3 < event.y < app.height - 50):
            app.mode = 'main'
    if app.mode == 'weekly summary':
        margin = app.height/12
        x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
        if (x2-60 < event.x < x2) and (y1 < event.y < y1+60): 
            app.mode = 'main'


# draws the line under the text
def newLine(app, canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill = 'blue', width = 3)

#Day mode: zoom into an entry on a specific day
def drawDayMode(app, canvas):
    margin = app.height/8
    popupColor = 'blanchedAlmond'
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    #draw background
    canvas.create_rectangle(x1, y1, x2, y2, fill = 'white')
    newLine(app, canvas, margin*2, app.lineY, app.width - margin*2, app.lineY)
    #draw text
    lineSpacing = 40
    textX = app.width/2
    #draws text above current line
    for n in range(len(app.dayEntry[:-1])):
        textY = (app.height/8)*2 - app.height/50 + lineSpacing*n
        canvas.create_text(textX, textY, text = app.dayEntry[n], 
                                    font = 'Arial 20')
    #draws current line
    canvas.create_text(textX, app.textY, text = app.dayEntry[-1], 
                                font = 'Arial 20')
    drawDefaultDayText(app, canvas)


#draws the default text:
def drawDefaultDayText(app, canvas):
    textColor = 'black'
    margin = app.height/8
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    canvas.create_text(margin + 240, margin + 30, 
                            text = f"Entry date: {app.currentDayName}, {app.currentDay}", 
                            font = 'Arial 30 bold', fill = textColor)
    canvas.create_text(margin + 170, margin + 60, text = f'Time last saved: {app.timeLastSaved[app.index]}', 
                            font = 'Arial 20', fill = textColor)   

#Main mode: draw a sunset and a path leading to it
def drawMainMode(app, canvas):
    drawHorizonAndSun(app, canvas)
    if app.frontPath == True:
        drawPath(app, canvas)
    if app.backPath == True:
        if app.theta > 0:
            drawBackPath(app,canvas,app.bx1,app.by1,app.bx2,app.by2,app.bx3,
                            app.by3,app.bx4,app.by4) 
        else:
            drawBackPath(app,canvas,app.cx1,app.cy1,app.cx2,app.cy2,app.cx3,
                            app.cy3,app.cx4,app.cy4) 
    drawTrees(app, canvas)
    drawDailyButtons(app,canvas)
    drawYearChart(app, canvas)
    canvas.create_text(app.width-200,  30, 
                text = f"{app.currentDayName}, {app.currentDay}", 
                font = 'Krungthep 30 bold', fill = 'black')


            

def drawYearChart(app, canvas):
    #DRAW YEAR CHART
    canvas.create_rectangle(50, 50, app.yearChartX, app.yearChartY, 
                            fill = 'white')
    #Draw yearly calendar
    #grid code modified from: https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            fill = "white" if (app.selection == (row, col)) else "white"
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)

def drawHorizonAndSun(app, canvas):
    drawHorizon(app, canvas)
    if app.backPath == False:
        drawSun(app, canvas)

def drawHorizon(app, canvas):
    #DRAW SKY and LAND
    canvas.create_rectangle(0, 0, app.width, app.height/2, 
                                    fill = app.skyColors[app.index])
                                    #rgbString(255, 185, 30))
    canvas.create_rectangle(0, app.height/2, app.width, app.height, 
                                    fill = 'moccasin')    
    
    #DRAW HORIZON
    canvas.create_line(0, app.height/2, app.width, app.height/2, 
                        width = 5, fill = app.sunColors[app.index])

def drawSun(app, canvas):
    m1, m2 = app.width/160, app.width/35
    cx, cy, r = app.cxSun, app.cySun, app.rSun
    canvas.create_arc(cx-r-m2, cy-r-m2, cx+r+m2, cy+r+m2, start=0, 
                                extent=180, fill=app.sunColors[app.index], 
                                outline = app.sunColors[app.index])     
    canvas.create_arc(cx-r-m1, cy-r-m1, cx+r+m1, cy+r+m1, start=0, 
                                extent=180, fill='gold',
                                outline = 'gold')                       
    canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=0, 
                                extent=180, fill='orangeRed',
                                outline = 'orangeRed') 
    canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=10, 
                                extent=180-10*2, fill='orange', style='chord',
                                outline = 'orange') 
    canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=20, 
                                extent=180-20*2, fill='moccasin', style='chord',
                                outline = 'moccasin') 
    canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=30, 
                                extent=180-30*2, fill='lightYellow', style='chord',
                                outline = 'lightYellow')

def drawPath(app, canvas):
    x1,y1,x2,y2,x3,y3,x4,y4 = (app.x1,app.y1,app.x2,
                         app.y2,app.x3,app.y3,app.x4,app.y4)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, fill = 'peru')
    canvas.create_polygon(x1+15,y1,x2+60,y2,x3-60,y3,x4-15,y4, fill = 'pink')
    canvas.create_polygon(x1+25,y1,x2+80,y2,x3-80,y3,x4-25,y4, fill = 'peru')
    canvas.create_polygon(x1+30,y1,x2+250,y2,x3-250,y3,x4-30,y4, fill = 'lightBlue')
    #draw straight lines across
    if ((x3-80-(x4-25))) != 0:
        grad1 = (y2-y1)/(x2+80-(x1+25))
    if ((x3-80-(x4-25))) != 0:
        grad2 = (y3-y4)/(x3-80-(x4-25)) 
    for y in [650,520,450]:
        lineX1 = (1/grad1)*(y-y1)+(x1+25)
        lineX2 = (1/grad2)*(y-y3)+(x3-80)
        canvas.create_line(lineX1, y, lineX2, y, width = 5, fill = 'peru')
    #if mouse hovers over both, it changes color
    if app.isPopUpBox == True:
        grad1 = (y2-y1)/(x2+250-(x1+30))
        grad2 = (y3-y4)/(x3-250-(x4-30))
        lineX1 = (1/grad1)*(650-y1)+(x1+25)
        lineX2 = (1/grad1)*(app.height-y1)+(x1+25)
        lineX4 = (1/grad2)*(650-y3)+(x3-250)
        lineX3 = (1/grad2)*(app.height-y3)+(x3-250)
        canvas.create_polygon(lineX1-10, 640, lineX2-10, app.height, lineX3+10,
            app.height, lineX4+10, 640, fill = app.buttonColor)
        #draw popup rectangle
        #canvas.create_text(((lineX1-10+lineX4+10)/2-100+(lineX1-10+lineX4+10)/2+100)/2, 480, text = 'click for')
        #canvas.create_text(((lineX1-10+lineX4+10)/2-100+(lineX1-10+lineX4+10)/2+100)/2, 500, text = 'daily entry!')
        canvas.create_rectangle((lineX1-10+lineX4+10)/2-100,400,(lineX1-10+lineX4+10)/2+100,600, fill = 'white', outline = 'white')

def dayAnimation(app):
    pass

def drawBackPath(app,canvas,x1,y1,x2,y2,x3,y3,x4,y4):
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, fill = 'peru')
    canvas.create_polygon(x1+15,y1,x2+60,y2,x3-60,y3,x4-15,y4, fill = 'pink')
    canvas.create_polygon(x1+25,y1,x2+80,y2,x3-80,y3,x4-25,y4, fill = 'lightCoral')
    canvas.create_polygon(x1+30,y1,x2+250,y2,x3-250,y3,x4-30,y4, fill = 'lightBlue')
    #draw straight lines across
    grad1 = -2
    grad1 = -2
    
    if ((x3-80-(x4-25))) != 0:
        grad1 = (y2-y1)/(x2+80-(x1+25))
    if ((x3-80-(x4-25))) != 0:
        grad2 = (y3-y4)/(x3-80-(x4-25)) 
    for y in [650,520,450]:
        lineX1 = (1/grad1)*(y-y1)+(x1+25)
        lineX2 = (1/grad2)*(y-y3)+(x3-80)
        canvas.create_line(lineX1, y, lineX2, y, width = 5, fill = 'peru')

def drawDailyButtons(app,canvas):
    pass
    #x1,y1,x2,y2,x3,y3,x4,y4 = (app.x1*10/11,app.y1*5/3,app.x2+200,
                        # app.y2,app.x3-400,app.y3,app.x4*12/11,app.y4*5/3)
    #canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, fill = 'cyan',)

def drawSummaryCloseButton(app, canvas):
    margin = app.height/12
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    canvas.create_rectangle(x2-60,y1,x2,y1+60, fill = 'orange')

def drawCloseButton(app, canvas):
    margin = app.height/8
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    canvas.create_rectangle(x2-60,y1,x2,y1+60, fill = 'orange')

def drawTrees(app,canvas):
    #maybe use recursion to draw a cool design
    pass

#Year mode: year chart at corner of main mode expands to show 
#the progress made in the entire year
def drawYearMode(app, canvas):
    pass


#pointInGrid(app, x, y) and getCell(app, x, y) and getCellBounds(app, row, col)
# modified from: https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
def pointInGrid(app, x, y):
    # return True if (x, y) is inside the grid defined by app.
    return ((app.margin <= x <= app.width-app.margin) and
            (app.margin <= y <= app.height-app.margin))

def getCell(app, x, y):
    # aka "viewToModel"
    # return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
    if (not pointInGrid(app, x, y)):
        return (-1, -1)
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth  = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    row = int((y - app.margin) / cellHeight)
    col = int((x - app.margin) / cellWidth)

    return (row, col)

def getCellBounds(app, row, col):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.yearChartX - 2*app.margin
    gridHeight = app.yearChartY - 2*app.margin
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.margin + row * cellHeight
    y1 = app.margin + (row+1) * cellHeight
    return (x0, y0, x1, y1)

#draws bar chart for moods of each day
def drawBarChart(app,canvas):
    #draw background
    margin = app.height/12
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    canvas.create_rectangle(x1, y1, x2, y2, fill = 'white')
    #draw heading
    canvas.create_text(app.width/2, app.height/12 + 25, text = 'Weekly Summary', font = 'Krungthep 25')
    #draw bar chart
    moodDict = getMoodNumbersWeek(app)
    barX = 300
    for day in moodDict:
        moodNums = moodDict[day]
        sumOfNums = sum(moodNums)
        x0,x1 = barX, barX+80
        if sumOfNums > 0:
            happy, sad, angry = moodNums[0], moodNums[1], moodNums[2]
            fraction = 200/sumOfNums
            y0 = 200
            y1 = y0 + happy*fraction, 
            y2 = y0 + (happy+sad)*fraction, 
            y3 = y0 + (happy+sad+angry)*fraction
            canvas.create_rectangle(x0, y0, x1, y1, fill ='yellow', outline = 'white')
            canvas.create_rectangle(x1, y1, x0, y2, fill ='cornflowerBlue', outline = 'white')
            canvas.create_rectangle(x0, y2, x1, y3, fill ='crimson', outline = 'white')
        barX += ((800-80*7)/6 + 80)
        canvas.create_text((x1+x0)/2, y3 + 20, text = day[:3], font = 'Krungthep 20')

def getMostFrequentMood(app):
    summation = 0
    (happyN, sadN, angryN) = (0,0,0)
    moods = ['happy', 'sad', 'angry']
    moodDict = getMoodNumbersWeek(app)
    for day in moodDict:
        summation += sum(moodDict[day])
        happyN += moodDict[day][0]
        sadN += moodDict[day][1]
        angryN += moodDict[day][2]
    maxNum = max(happyN, sadN, angryN)
    for i in range(3):
        if ((happyN, sadN, angryN)[i] == maxNum) and (moods[i] not in app.weekMainMood):
            app.weekMainMood += moods[i]
            app.weekMainMood += ' '

def drawPiechart(app,canvas):
    summation = 0
    (happyN, sadN, angryN) = (0,0,0)
    moodDict = getMoodNumbersWeek(app)
    for day in moodDict:
        summation += sum(moodDict[day])
        happyN += moodDict[day][0]
        sadN += moodDict[day][1]
        angryN += moodDict[day][2]
    cx, cy, r = (400, 600, app.width/14)
    canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=0, 
                                extent=(happyN/summation)*360, fill='yellow', 
                                outline = 'white')     
    canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=(happyN/summation)*360, 
                                extent=(sadN/summation)*360, fill='blue',
                                outline = 'white')                       
    canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=((sadN+happyN)/summation)*360, 
                                extent=(angryN/summation)*360, fill='red',
                                outline = 'white') 

def drawWordSummary(app,canvas):
    count = 0
    time = 0
    for date in app.weekDates:
        if readFile(f'Entries/{date}-text.txt') != '':
            count += 1
    canvas.create_text(app.width-400,  550, 
                text = f"Number of journal entries = {count}/7", 
                font = 'Krungthep 30 bold', fill = 'black')
    canvas.create_text(app.width-400,  600, 
                text = f"Total time spent = ", 
                font = 'Krungthep 30 bold', fill = 'black')
    canvas.create_text(app.width-400,  650, 
                text = f"Main mood = {app.weekMainMood}", 
                font = 'Krungthep 30 bold', fill = 'black')

def drawSplashPage(app, canvas):
        canvas.create_text(app.width/2, 250, text='"Life moves pretty fast.', font='Krungthep 35')
        canvas.create_text(app.width/2, 300, text='If you don’t stop and look', font='Krungthep 25')
        canvas.create_text(app.width/2, 350, text='around once in a while,', font = 'Krungthep 25')
        canvas.create_text(app.width/2, 400, text=' you could miss it."', font='Krungthep 50')
        canvas.create_text(app.width/2, 450, text='Ferris Bueller', font='Krungthep 20')
        canvas.create_text(app.width/2, 550, text='Click anywhere to begin!', font='Arial 20')
        
        #credits
        canvas.create_text(app.width-300, app.height-20, text="All the Write Moves, by Cathy Yi (Fall'19 112 TP)", font='Arial 20')

def redrawAll(app, canvas):
    if app.mode == 'splash':
        drawSplashPage(app, canvas)
    elif app.mode == 'day':
        drawMainMode(app, canvas)
        drawDayMode(app, canvas)
        drawCloseButton(app, canvas)
    elif app.mode == 'main to day':
        drawMainMode(app, canvas)
        canvas.create_rectangle(app.dayChX1, app.dayChY1, app.dayChX2, app.dayChY2, fill = 'white')
    elif app.mode == 'daily summary':
        drawMainMode(app, canvas)
        drawWeeklySummary(app, canvas)
        drawCloseButton(app, canvas)
    elif app.mode == 'weekly summary':
        drawMainMode(app, canvas)
        drawBarChart(app,canvas)
        drawPiechart(app,canvas)
        drawWordSummary(app,canvas)
        drawSummaryCloseButton(app, canvas)
    elif app.mode == 'main':
        drawMainMode(app, canvas)
    elif app.mode == 'year' or app.mode == 'main':
        drawMainMode(app, canvas)
        drawYearMode(app, canvas)


runApp(width=1400, height=800)
